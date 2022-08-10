
"""
MAP Client Plugin - Generated from MAP Client v0.17.0
"""

__version__ = '0.1.2'
__author__ = 'Hugh Sorby'
__stepname__ = 'Convert Data to Zinc'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.convertdatatozincstep'

# import class that derives itself from the step mountpoint.
from mapclientplugins.convertdatatozincstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc