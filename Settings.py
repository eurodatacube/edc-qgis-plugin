# -*- coding: utf-8 -*-
"""
This script contains parameters and settings for Euro Data Cube services
"""

# Locations where QGIS will save values
service_url_location = "Euro Data Cube/service_base_url"
download_folder_location = "Euro Data Cube/download_folder"

service_types = ['WMS', 'WMTS']

# Main request parameters
parameters = {
    'title': '',
    'layers': '',
    'time': '',
    'crs': 'EPSG:3857'
}

# WMS parameters - the first 3 parameters are required for qgis layer
parameters_wms = {
    'IgnoreGetFeatureInfoUrl': '1',
    'IgnoreGetMapUrl': '1',
    'contextualWMSLegend': '0',
    'service': 'WMS',
    'styles': '',
    'request': 'GetMap',
    'format': 'image/png',
    'transparent': 'true',
    'version': '1.3.0',
}

# WFS parameters
parameters_wfs = {
    'service': 'WFS',
    'version': '2.0.0',
    'request': 'GetFeature',
    'typenames': 'S2.TILE',
    'maxfeatures': '100',
    'outputformat': 'application/json',
}

# WCS parameters
parameters_wcs = {
    'service': 'wcs',
    'request': 'GetCoverage',
    'format': 'image/png',
    'showLogo': 'false',
    'transparent': 'false',
    'version': '1.1.1',
    'resx': '10',
    'resy': '10'
}

# WMTS parameters
parameters_wmts = {
    'IgnoreGetFeatureInfoUrl': '1',
    'IgnoreGetMapUrl': '1',
    'contextualWMSLegend': '0',
    'service': 'WMTS',
    'styles': '',
    'request': 'GetTile',
    'format': 'image/png',
    'transparent': 'true',
    'tileMatrixSet': 'PopularWebMercator512'
}

# data_source_props = {'S2L1C': {'url': services_base_url,
#                                'wfs_name': 'S2.TILE',
#                                'pretty_name': 'Sentinel-2 L1C'},
#                      'S2L2A': {'url': services_base_url,
#                                'wfs_name': 'DSS2',
#                                'pretty_name': 'Sentinel-2 L2A'},
#                      'S1GRD': {'url': services_base_url,
#                                'wfs_name': 'DSS3',
#                                'pretty_name': 'Sentinel-1'},
#                      'L8L1C': {'url': uswest_base_url,
#                                'wfs_name': 'DSS6',
#                                'pretty_name': 'Landsat 8'},
#                      'MODIS': {'url': uswest_base_url,
#                                'wfs_name': 'DSS5',
#                                'pretty_name': 'MODIS'},
#                      'DEM': {'url': uswest_base_url,
#                              'wfs_name': 'DSS4',
#                              'pretty_name': 'DEM'}}

# values for UI selections
priorities = [('mostRecent', 'Most recent'),
              ('leastRecent', 'Least recent'),
              ('leastCC', 'Least cloud coverage')]

atmfilter_list = ['NONE', 'DOS1', 'ATMCOR']  # Not yet implemented
cloud_correction = ['NONE', 'REPLACE']  # Not yet implemented

image_formats = [('image/png', 'PNG'),
                 ('image/jpeg', 'JPEG'),
                 ('image/tiff;depth=8', '8-bit TIFF'),
                 ('image/tiff;depth=16', '16-bit TIFF'),
                 ('image/tiff;depth=32f', '32-bit float TIFF')]

max_cloud_cover_image_size = 1000000
