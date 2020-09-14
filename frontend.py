from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import downloader
WHITE=QtGui.QColor(255,255,255)
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Youtube Downloader")
        self.resize(800,600)


        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.text_label()
        self.text_edit()
        self.hvid()
        self.lvid()
        self.audio()

        self.show()


    def text_label(self):

        self.label = QtWidgets.QLabel("Enter link here:",self)
        self.label.setGeometry(30, 50, 161, 31)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)


    def text_edit(self):

        self.lineEdit = QtWidgets.QTextEdit(self)
        self.lineEdit.setGeometry(230, 30, 501, 61)
        self.lineEdit.setObjectName("lineEdit")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.lineEdit.setFont(font)

    def hvid(self):
        self.highQuality = QtWidgets.QPushButton("Download in High Quality",self)
        self.highQuality.setGeometry(230, 150, 251, 61)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.highQuality.setFont(font)
        self.highQuality.clicked.connect( lambda:fend("mp4",'high') )

    def lvid(self):
        self.lowQuality= QtWidgets.QPushButton("Download in Low Quality",self)
        self.lowQuality.setGeometry(230, 230, 251, 61)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.lowQuality.setFont(font)
        self.lowQuality.clicked.connect( lambda:fend("mp4",'low') )

    def audio(self):
        self.audioButton=QtWidgets.QPushButton( " Download Audio " , self )
        self.audioButton.setGeometry(230,320,251,61)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.audioButton.setFont(font)

        self.audioButton.clicked.connect( lambda:fend("mp3", 'low' ) )

    def fend(self,format,quality):
        vlink=self.lineEdit.toPlainText()
        fname=QtWidgets.QFileDialog.getOpenFileName(self,'Open Folder', 'c:\\')
        downloader.videosearch(vlink,format,fname,quality)

app=QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

dark_palette = QtGui.QPalette()

dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.WindowText, WHITE)
dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ToolTipBase,WHITE)
dark_palette.setColor(QtGui.QPalette.ToolTipText,WHITE)
dark_palette.setColor(QtGui.QPalette.Text, WHITE)
dark_palette.setColor(QtGui.QPalette.Button, QtCore.Qt.blue)
dark_palette.setColor(QtGui.QPalette.ButtonText,WHITE)
dark_palette.setColor(QtGui.QPalette.BrightText,QtGui.QColor(255,0,0))
dark_palette.setColor(QtGui.QPalette.Link,QtGui.QColor(42, 130, 218))
dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(0,0,0))

app.setPalette(dark_palette)

app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
window=Ui_MainWindow()
sys.exit(app.exec_())
