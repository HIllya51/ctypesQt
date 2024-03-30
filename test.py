import config
config.QTBIN_DIR='./bin'
config.QTPLUGIN_DIR='./bin/plugins'
from ctypesQt import QApplication,QFont,QWidget
QApplication.addLibraryPath(config.QTPLUGIN_DIR)

app=QApplication()
app.setFont(QFont("MS Shell Dlg 2", 10))

qw=QWidget()
qw.show()

app.exec()