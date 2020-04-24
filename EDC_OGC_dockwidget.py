# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
# Project: Euro Data Cube <http://eurodatacube.com>
# 
#
#-------------------------------------------------------------------------------
# Copyright (C) 2020 EOX IT Services GmbH <office@eox.at>
#
# This program is free software; you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation; either version 2 of the License, or     
# (at your option) any later version.  
# 
# This code was developed based on SentinelHub plugin by Sinergise ltd.
#     Original SentinelHub plugin : <https://github.com/sinergise/qgis_sentinel_hub/tree/master/SentinelHub>.
#     copyright            : (C) 2017 by Sentinel Hub, Sinergise ltd.
#     email                : info@sentinel-hub.com 
#-------------------------------------------------------------------------------

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


    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

