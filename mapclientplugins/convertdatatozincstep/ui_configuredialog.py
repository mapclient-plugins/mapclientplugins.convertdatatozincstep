# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(623, 443)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.labelIdentifier = QLabel(self.configGroupBox)
        self.labelIdentifier.setObjectName(u"labelIdentifier")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelIdentifier)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditIdentifier)

        self.labelInputData = QLabel(self.configGroupBox)
        self.labelInputData.setObjectName(u"labelInputData")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelInputData)

        self.comboBoxInputData = QComboBox(self.configGroupBox)
        self.comboBoxInputData.setObjectName(u"comboBoxInputData")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxInputData)

        self.textEditInputData = QTextEdit(self.configGroupBox)
        self.textEditInputData.setObjectName(u"textEditInputData")
        self.textEditInputData.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.textEditInputData)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Convert Data to Zinc", None))
        self.configGroupBox.setTitle("")
        self.labelIdentifier.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.labelInputData.setText(QCoreApplication.translate("ConfigureDialog", u"Input data:  ", None))
    # retranslateUi

