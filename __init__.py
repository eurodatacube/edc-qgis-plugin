# -*- coding: utf-8 -*-

# noinspection PyPep8Naming
# pylint: disable=invalid-name


def classFactory(iface):
    """Load EDC_OGC class from file EDC_OGC.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .EDC_OGC import EDC_OGC
    return EDC_OGC(iface)
