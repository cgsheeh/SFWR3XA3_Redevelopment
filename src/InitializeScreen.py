__author__ = 'connor'



import pyforms

from pyforms import BaseWidget
from pyforms.Controls import ControlImage


class InitializeWindow(BaseWidget):
    def __init__(self):
        super(InitializeWindow, self).__init__("Welcome to RedevBazaar")
        self.logo = ControlImage('images/logo.png')
