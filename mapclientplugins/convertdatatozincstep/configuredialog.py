from PySide2 import QtWidgets
from mapclientplugins.convertdatatozincstep.ui_configuredialog import Ui_ConfigureDialog

from opencmiss.importer import main

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


def _display_parameter(name, importer_parameters):
    display = ""
    names = []
    if name in importer_parameters:
        names.append(importer_parameters[name])
    elif name + "s" in importer_parameters:
        names.extend(importer_parameters[name + "s"])

    if len(names):
        display += "\n"
        display += f"## {name}"
        display += "s" if len(names) > 1 else ""
        display += "\n"
        for index, n in enumerate(names):
            if "mimetype" in n:
                display += f"{index + 1}. {n['mimetype']}\n"

    return display


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._ui.comboBoxInputData.insertItems(0, ["--"] + main.available_importers())

        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEditIdentifier.textChanged.connect(self.validate)
        self._ui.comboBoxInputData.currentTextChanged.connect(self._input_data_changed)

    def _input_data_changed(self, text):
        if text == "--":
            self._ui.textEditInputData.clear()
        else:
            importer_parameters = main.import_parameters(text)

            display_importer_parameters = f"# {importer_parameters['title']}\n"
            display_importer_parameters += importer_parameters["description"]
            display_importer_parameters += _display_parameter("input", importer_parameters)
            display_importer_parameters += _display_parameter("output", importer_parameters)

            self._ui.textEditInputData.setMarkdown(display_importer_parameters)

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(
                self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEditIdentifier.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEditIdentifier.text())
        if valid:
            self._ui.lineEditIdentifier.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEditIdentifier.setStyleSheet(INVALID_STYLE_SHEET)

        valid_importer = self._ui.comboBoxInputData.currentText() != "--"

        return valid and valid_importer

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEditIdentifier.text()
        config = {'identifier': self._ui.lineEditIdentifier.text(), 'Input data': self._ui.comboBoxInputData.currentText()}
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEditIdentifier.setText(config['identifier'])
        self._ui.comboBoxInputData.setCurrentText(config['Input data'])
