
# For Development

to setup locally:
- clone the repository
- in the QGIS plugin directory create a folder and name  `Euro Data Cube` ( in **linux** plugins dir resides in ` ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`)
- copy all the files into the `Euro data cube` folder
- sometimes you have to re-compile the resources:
```
 pyrcc5 -o resources.py resources.qrc
```
- in **QGIS** got to `plugins -> Manage and install plugins -> installed` and enable the **Euro Data Cube**

## Prerequisites
- for compiling Qt [pyrcc5](http://manpages.ubuntu.com/manpages/trusty/man1/pyrcc5.1.html)


