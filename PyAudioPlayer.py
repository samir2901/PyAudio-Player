from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtMultimedia
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 400)
        MainWindow.setMinimumSize(QtCore.QSize(482,380))
        MainWindow.setMaximumSize(QtCore.QSize(482, 380))
        icon = QtGui.QIcon.fromTheme(":/logo/multimedia-audio-player-icon.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("* {\n"
"    background: #191919;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -7px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #191919;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 32px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 32px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #353535;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border-width: 0px 1px 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-width: 1px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background:#353535;\n"
"    border: 1px solid #5A5A5A;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    position: absolute;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    left: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    top: 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: top left;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"}\n"
"\n"
"QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QAbstractButton:pressed {\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    show-decoration-selected: 1;\n"
"    selection-background-color: #3D7848;\n"
"    selection-color: #DDDDDD;\n"
"    alternate-background-color: #353535;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #191919;\n"
"    border: 1px solid #5A5A5A;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QHeaderView::section:selected, QHeaderView::section::checked {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #5A5A5A;\n"
"}\n"
"\n"
"QTabBar {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 1px;\n"
"    background-color: #3D7848;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #353535;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.playBtn = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn.setGeometry(QtCore.QRect(30, 190, 91, 31))
        self.playBtn.setObjectName("playBtn")
        self.playBtn.clicked.connect(self.play)


        self.pauseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn.setGeometry(QtCore.QRect(200, 190, 91, 31))
        self.pauseBtn.setObjectName("pauseBtn")
        self.pauseBtn.clicked.connect(self.pause)

        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(370, 190, 91, 31))
        self.stopBtn.setObjectName("stopBtn")
        self.stopBtn.clicked.connect(self.stop)


        self.currentPlaying = QtWidgets.QLabel(self.centralwidget)
        self.currentPlaying.setGeometry(QtCore.QRect(30, 20, 421, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.currentPlaying.setFont(font)
        self.currentPlaying.setAlignment(QtCore.Qt.AlignCenter)
        self.currentPlaying.setObjectName("currentPlaying")


        self.developLabel = QtWidgets.QLabel(self.centralwidget)
        self.developLabel.setGeometry(QtCore.QRect(290, 310, 121, 21))
        self.developLabel.setObjectName("developLabel")



        self.thunderLogo = QtWidgets.QLabel(self.centralwidget)
        self.thunderLogo.setGeometry(QtCore.QRect(410, 300, 51, 31))
        self.thunderLogo.setText("")
        self.thunderLogo.setPixmap(QtGui.QPixmap(":/image/thunder_logo.png"))
        self.thunderLogo.setScaledContents(True)
        self.thunderLogo.setObjectName("thunderLogo")


        self.volumeBar = QtWidgets.QSlider(self.centralwidget)
        self.volumeBar.setGeometry(QtCore.QRect(320, 260, 141, 20))
        self.volumeBar.setMinimum(0)
        self.volumeBar.setMaximum(100)
        self.volumeBar.setOrientation(QtCore.Qt.Horizontal)
        self.volumeBar.setObjectName("volumeBar")
        self.volumeBar.valueChanged.connect(self.changeVolume)


        self.volumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(260, 260, 47, 13))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setObjectName("volumeLabel")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)        
        self.actionOpen_Media = QtWidgets.QAction(MainWindow)
        self.actionOpen_Media.setObjectName("actionOpen_Media")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_Media)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionExit.triggered.connect(self.closeApp)
        self.actionOpen_Media.triggered.connect(self.getAudioFile)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyAudio Player"))
        self.playBtn.setText(_translate("MainWindow", "Play"))
        self.pauseBtn.setText(_translate("MainWindow", "Pause"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.currentPlaying.setText(_translate("MainWindow", "No File is Selected"))
        self.developLabel.setText(_translate("MainWindow", "Developed by thunder"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Media.setText(_translate("MainWindow", "Open Audio "))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.player =QtMultimedia.QMediaPlayer()
        self.player.setVolume(20)
        self.volumeBar.setValue(20)


    def getAudioFile(self):
        global currentAudio
        global filename
        filter = "Audio Files (*.mp3)"
        f = QtWidgets.QFileDialog.getOpenFileName(None,"Open File",".",filter)
        filename = f[0]
        #print(filename)
        #print("File is opened")        
        try:
            self.url = QtCore.QUrl.fromLocalFile(filename)
            self.content = QtMultimedia.QMediaContent(self.url)
            self.player.setMedia(self.content)
            currentAudio = filename
            currentText = os.path.basename(currentAudio)
            self.currentPlaying.setText(currentText)
            self.player.play()
        except:
            self.currentPlaying.setText(currentText)
            
    
    def closeApp(self):
        #print("Exit is Pressed")
        sys.exit()

    def changeVolume(self, event):
        #print(event)
        self.player.setVolume(event)

    def play(self):    
        global currentText    
        try:           
            currentAudio = filename
            currentText = os.path.basename(currentAudio)
            self.currentPlaying.setText(currentText)
            self.player.play()
            #print("Play Button is Pressed")   
        except:            
            print("No File Selected")     

    def pause(self):
        self.player.pause()
        #print("Pause is pressed")

    def stop(self):
        self.currentPlaying.setText("Stopped!!")
        self.player.stop()
        #print("Stop is pressed")

    
import images_rc


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
