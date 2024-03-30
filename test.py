import config
config.QTBIN_DIR='./bin'
config.QTPLUGIN_DIR='./bin/plugins'
from ctypesQt import QApplication,QFont,QWidget,QPushButton
QApplication.addLibraryPath(config.QTPLUGIN_DIR)

app=QApplication()
app.setFont(QFont("MS Shell Dlg 2", 10))

qw=QWidget()
qpush=QPushButton(qw)

qw.show()
app.exec()