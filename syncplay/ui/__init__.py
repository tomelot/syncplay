import os

try:
    from syncplay.ui.gui import MainWindow as GraphicalUI
except ImportError:
    pass
from syncplay.ui.consoleUI import ConsoleUI


def getUi(graphical=True, passedBar=None):
    if graphical:
        ui = GraphicalUI(passedBar=passedBar)
    else:
        ui = ConsoleUI()
        ui.setDaemon(True)
        ui.start()
    return ui
