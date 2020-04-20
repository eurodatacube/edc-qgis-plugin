# -*- coding: utf-8 -*-


import os.path
from sys import version_info

if version_info[0] >= 3:
    from PyQt5.QtWidgets import QDockWidget
    from PyQt5.uic import loadUiType
    from PyQt5.QtCore import pyqtSignal
else:
    from PyQt4.QtGui import QDockWidget
    from PyQt4.uic import loadUiType
    from PyQt4.QtCore import pyqtSignal

FORM_CLASS, _ = loadUiType(os.path.join(os.path.dirname(__file__),
                                        'EDC_OGC_dockwidget_base.ui'))


class EDC_OGC_DockWidget(QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(EDC_OGC_DockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        # temporary hide the download tab
        self.downloadTab.setVisible(False)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

