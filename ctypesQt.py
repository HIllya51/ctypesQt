import os,ctypes
from ctypes import c_void_p,c_wchar_p,c_size_t,pointer,sizeof,POINTER,c_int,c_char_p,c_bool,cast
from config import QTBIN_DIR,QTPLUGIN_DIR

Qt5Core=ctypes.CDLL(os.path.join(QTBIN_DIR,'Qt5Core'))
Qt5Widgets=ctypes.CDLL(os.path.join(QTBIN_DIR,'Qt5Widgets'))
Qt5Gui=ctypes.CDLL(os.path.join(QTBIN_DIR,'Qt5Gui'))

QCoreApplication_addLibraryPath=Qt5Core.__getattr__('?addLibraryPath@QCoreApplication@@SAXAEBVQString@@@Z')
QApplication_ctor=Qt5Widgets.__getattr__('??0QApplication@@QEAA@AEAHPEAPEADH@Z')
QFont_ctor=Qt5Gui.__getattr__('??0QFont@@QEAA@AEBVQString@@HH_N@Z')
QFont_dtor=Qt5Gui.__getattr__('??1QFont@@QEAA@XZ')
QApplication_setFont=Qt5Widgets.__getattr__('?setFont@QApplication@@SAXAEBVQFont@@PEBD@Z')
QApplication_exec=Qt5Widgets.__getattr__('?exec@QApplication@@SAHXZ')
QApplication_dtor=Qt5Widgets.__getattr__('??1QApplication@@UEAA@XZ')
QApplication_processEvents=Qt5Core.__getattr__('?processEvents@QCoreApplication@@SAXV?$QFlags@W4ProcessEventsFlag@QEventLoop@@@@@Z')

# QString_fromStdWString=Qt5Core.__getattr__('?fromStdWString@QString@@SA?AV1@AEBV?$basic_string@_WU?$char_traits@_W@std@@V?$allocator@_W@2@@std@@@Z')
# QString_fromUtf16=Qt5Core.__getattr__("?fromUtf16@QString@@SA?AV1@PEB_SH@Z") 
# QString_fromUtf8=Qt5Core.__getattr__("?fromUtf8@QString@@SA?AV1@PEBDH@Z")
QString_fromWCharArray=Qt5Core.__getattr__("?fromWCharArray@QString@@SA?AV1@PEB_WH@Z") 
QString_dtor=Qt5Core.__getattr__('??1QString@@QEAA@XZ')

class PTR(c_char_p*sizeof(c_void_p)):
    pass
class QString(PTR):
    def __init__(self,s:str) -> None:
        QString_fromWCharArray(self,s,len(s))
    def __del__(self) -> None:
        QString_dtor(self)
QString_fromWCharArray.argtypes=QString,c_wchar_p,c_size_t
QString_dtor.argtypes=QString,

class QFont(PTR):
    def __init__(self, family,pointSize=-1,weight=-1,italic=False) -> None:
        QFont_ctor(self,QString(family),pointSize,weight,italic)
    def __del__(self):
        QFont_dtor(self)
QFont_ctor.argtypes=QFont,QString,c_int,c_int,c_bool
QFont_dtor.argtypes=QFont,
class QApplication(PTR):
        
    @staticmethod
    def addLibraryPath(path:str):
        qs=QString(path)
        QCoreApplication_addLibraryPath(qs)
    def __init__(self) -> None:
        _=c_int(0)
        QApplication_ctor(self,pointer(_),None,331266)
    def __del__(self):
        QApplication_dtor(self)
    @staticmethod
    def exec():
        QApplication_exec()
    @staticmethod
    def processEvents(_=0):
        QApplication_processEvents(_)
    @staticmethod
    def setFont(font:QFont):
        QApplication_setFont(font,None)
QApplication_ctor.argtypes=QApplication,POINTER(c_int),POINTER(c_char_p),c_int
QApplication_dtor.argtypes=QApplication,
QApplication_processEvents.argtypes=c_int,
QApplication_setFont.argtypes=QFont,c_char_p


QWidget_ctor=Qt5Widgets.__getattr__('??0QWidget@@QEAA@PEAV0@V?$QFlags@W4WindowType@Qt@@@@@Z')
QWidget_dtor=Qt5Widgets.__getattr__('??1QWidget@@UEAA@XZ')
QWidget_show=Qt5Widgets.__getattr__('?show@QWidget@@QEAAXXZ')
class WindowFlags(c_int):
    pass
class QWidget(PTR):
    def __init__(self,parent=None,flags=0) -> None:
        QWidget_ctor(self,parent,flags)
    def __del__(self):
        QWidget_dtor(self)
    def show(self):
        QWidget_show(self)

QWidget_ctor.argtypes=QWidget,c_void_p,WindowFlags
QWidget_dtor.argtypes=QWidget,
QWidget_show.argtypes=QWidget,

QPushButton_ctor=Qt5Widgets.__getattr__('??0QPushButton@@QEAA@PEAVQWidget@@@Z')
QPushButton_dtor=Qt5Widgets.__getattr__('??1QPushButton@@UEAA@XZ')
QPushButton_ctor_text=Qt5Widgets.__getattr__('??0QPushButton@@QEAA@AEBVQString@@PEAVQWidget@@@Z')
class QPushButton(PTR):
    def __init__(self, parent=None,text=None) -> None:
        if(text):
            QPushButton_ctor_text(self,QString(text),parent)
        else:
            QPushButton_ctor(self,parent)
        self.p=parent   #保持parent的引用，否则会先析构parent
    def __del__(self):
        QPushButton_dtor(self)
QPushButton_ctor.argtypes=QPushButton,c_void_p
QPushButton_dtor.argtypes=QPushButton,
QPushButton_ctor_text.argtypes=QPushButton,QString,c_void_p