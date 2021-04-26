# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from display_imgAndcomp import DisplayImgComp

class Ui_MainWindow(DisplayImgComp):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PNG/editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Img1GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.Img1GroupBox.setFont(font)
        self.Img1GroupBox.setObjectName("Img1GroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.Img1GroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.Image1ComboBox = QtWidgets.QComboBox(self.Img1GroupBox)
        self.Image1ComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Image1ComboBox.setObjectName("Image1ComboBox")
        self.Image1ComboBox.addItem("")
        self.Image1ComboBox.addItem("")
        self.Image1ComboBox.addItem("")
        self.Image1ComboBox.addItem("")
        self.gridLayout.addWidget(self.Image1ComboBox, 0, 1, 1, 1)
        self.Image1ViewerA = QtWidgets.QLabel(self.Img1GroupBox)
        self.Image1ViewerA.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Image1ViewerA.setObjectName("Image1ViewerA")
        self.gridLayout.addWidget(self.Image1ViewerA, 1, 0, 1, 1)
        # Display Img 1
        pixmap = QtGui.QPixmap(self.path1)
        pixmap = pixmap.scaled(355, 300, QtCore.Qt.KeepAspectRatio)
        self.Image1ViewerA.setPixmap(pixmap)
        #---------------------------------------------------------------
        self.Image1ViewerB = QtWidgets.QLabel(self.Img1GroupBox)
        self.Image1ViewerB.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Image1ViewerB.setObjectName("Image1ViewerB")
        self.gridLayout.addWidget(self.Image1ViewerB, 1, 1, 1, 1)
        
        ##############################################################
        self.gridLayout_5.addWidget(self.Img1GroupBox, 0, 0, 1, 1)
        self.MixerGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.MixerGroupBox.setFont(font)
        self.MixerGroupBox.setObjectName("MixerGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MixerGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OutputLabel = QtWidgets.QLabel(self.MixerGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setObjectName("OutputLabel")
        self.gridLayout_2.addWidget(self.OutputLabel, 0, 2, 1, 1)
        self.OutputCombobox = QtWidgets.QComboBox(self.MixerGroupBox)
        self.OutputCombobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OutputCombobox.setObjectName("OutputCombobox")
        self.OutputCombobox.addItem("")
        self.OutputCombobox.addItem("")
        self.gridLayout_2.addWidget(self.OutputCombobox, 0, 3, 1, 1)
        self.Component1Label = QtWidgets.QLabel(self.MixerGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Component1Label.setFont(font)
        self.Component1Label.setObjectName("Component1Label")
        self.gridLayout_2.addWidget(self.Component1Label, 1, 0, 1, 1)
        self.Component1ComboBox1 = QtWidgets.QComboBox(self.MixerGroupBox)
        self.Component1ComboBox1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Component1ComboBox1.setObjectName("Component1ComboBox1")
        self.Component1ComboBox1.addItem("")
        self.Component1ComboBox1.addItem("")
        self.gridLayout_2.addWidget(self.Component1ComboBox1, 1, 1, 1, 1)
        self.Component1ProgressBar = QtWidgets.QProgressBar(self.MixerGroupBox)
        self.Component1ProgressBar.setProperty("value", 50)
        self.Component1ProgressBar.setObjectName("Component1ProgressBar")
        self.gridLayout_2.addWidget(self.Component1ProgressBar, 1, 2, 1, 2)
        self.Component1ComboBox2 = QtWidgets.QComboBox(self.MixerGroupBox)
        self.Component1ComboBox2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Component1ComboBox2.setObjectName("Component1ComboBox2")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.gridLayout_2.addWidget(self.Component1ComboBox2, 2, 1, 1, 3)
        self.Component2Label = QtWidgets.QLabel(self.MixerGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Component2Label.setFont(font)
        self.Component2Label.setObjectName("Component2Label")
        self.gridLayout_2.addWidget(self.Component2Label, 3, 0, 1, 1)
        self.Component2ComboBox1 = QtWidgets.QComboBox(self.MixerGroupBox)
        self.Component2ComboBox1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Component2ComboBox1.setObjectName("Component2ComboBox1")
        self.Component2ComboBox1.addItem("")
        self.Component2ComboBox1.addItem("")
        self.gridLayout_2.addWidget(self.Component2ComboBox1, 3, 1, 1, 1)
        self.Component2ProgressBar = QtWidgets.QProgressBar(self.MixerGroupBox)
        self.Component2ProgressBar.setProperty("value", 50)
        self.Component2ProgressBar.setObjectName("Component2ProgressBar")
        self.gridLayout_2.addWidget(self.Component2ProgressBar, 3, 2, 1, 2)
        self.Component2ComboBox2 = QtWidgets.QComboBox(self.MixerGroupBox)
        self.Component2ComboBox2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Component2ComboBox2.setObjectName("Component2ComboBox2")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.gridLayout_2.addWidget(self.Component2ComboBox2, 4, 1, 1, 3)
        self.gridLayout_5.addWidget(self.MixerGroupBox, 0, 1, 1, 1)
        self.Img2Groupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.Img2Groupbox.setFont(font)
        self.Img2Groupbox.setObjectName("Img2Groupbox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Img2Groupbox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Image2ComboBox = QtWidgets.QComboBox(self.Img2Groupbox)
        self.Image2ComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Image2ComboBox.setObjectName("Image2ComboBox")
        self.Image2ComboBox.addItem("")
        self.Image2ComboBox.addItem("")
        self.Image2ComboBox.addItem("")
        self.Image2ComboBox.addItem("")
        self.gridLayout_3.addWidget(self.Image2ComboBox, 0, 1, 1, 1)
        self.Image2ViewerA = QtWidgets.QLabel(self.Img2Groupbox)
        self.Image2ViewerA.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Image2ViewerA.setObjectName("Image2ViewerA")
        self.gridLayout_3.addWidget(self.Image2ViewerA, 1, 0, 1, 1)
        # Display Img 2
        pixmap_img2 = QtGui.QPixmap(self.path2)
        pixmap_img2 = pixmap_img2.scaled(355, 300, QtCore.Qt.KeepAspectRatio)
        self.Image2ViewerA.setPixmap(pixmap_img2)
        #---------------------------------------------------------------
        ########################################################
        self.Image2ViewerB = QtWidgets.QLabel(self.Img2Groupbox)
        self.Image2ViewerB.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Image2ViewerB.setObjectName("Image2ViewerB")
        self.gridLayout_3.addWidget(self.Image2ViewerB, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.Img2Groupbox, 1, 0, 1, 1)
        self.OutputGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.OutputGroupBox.setFont(font)
        self.OutputGroupBox.setObjectName("OutputGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.OutputGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.viewer1 = QtWidgets.QLabel(self.OutputGroupBox)
        self.viewer1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.viewer1.setObjectName("viewer1")
        self.gridLayout_4.addWidget(self.viewer1, 0, 0, 1, 1)
        self.viewer2 = QtWidgets.QLabel(self.OutputGroupBox)
        self.viewer2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.viewer2.setObjectName("viewer2")
        self.gridLayout_4.addWidget(self.viewer2, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.OutputGroupBox, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1450, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Img1GroupBox.setTitle(_translate("MainWindow", "Image 1"))
        self.Image1ComboBox.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Image1ComboBox.setItemText(1, _translate("MainWindow", "Phase"))
        self.Image1ComboBox.setItemText(2, _translate("MainWindow", "Real"))
        self.Image1ComboBox.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.MixerGroupBox.setTitle(_translate("MainWindow", "Mixer"))
        self.OutputLabel.setText(_translate("MainWindow", "Output to:"))
        self.OutputCombobox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.OutputCombobox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.Component1Label.setText(_translate("MainWindow", "Component 1:"))
        self.Component1ComboBox1.setItemText(0, _translate("MainWindow", "Image 1"))
        self.Component1ComboBox1.setItemText(1, _translate("MainWindow", "Image 2"))
        self.Component1ComboBox2.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Component1ComboBox2.setItemText(1, _translate("MainWindow", "Phase"))
        self.Component1ComboBox2.setItemText(2, _translate("MainWindow", "Real"))
        self.Component1ComboBox2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.Component1ComboBox2.setItemText(4, _translate("MainWindow", "Uni Magnitude"))
        self.Component1ComboBox2.setItemText(5, _translate("MainWindow", "Uni Phase"))
        self.Component2Label.setText(_translate("MainWindow", "Component 2:"))
        self.Component2ComboBox1.setItemText(0, _translate("MainWindow", "Image 1"))
        self.Component2ComboBox1.setItemText(1, _translate("MainWindow", "Image 2"))
        self.Component2ComboBox2.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Component2ComboBox2.setItemText(1, _translate("MainWindow", "Phase"))
        self.Component2ComboBox2.setItemText(2, _translate("MainWindow", "Real"))
        self.Component2ComboBox2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.Component2ComboBox2.setItemText(4, _translate("MainWindow", "Uni Magnitude"))
        self.Component2ComboBox2.setItemText(5, _translate("MainWindow", "Uni Phase"))
        self.Img2Groupbox.setTitle(_translate("MainWindow", "Image 2"))
        ###################################################################
        # index of img2 combobox start from 4 to 7 to be unique
        ###################################################################
        self.Image2ComboBox.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Image2ComboBox.setItemText(1, _translate("MainWindow", "Phase"))
        self.Image2ComboBox.setItemText(2, _translate("MainWindow", "Real"))
        self.Image2ComboBox.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.OutputGroupBox.setTitle(_translate("MainWindow", "Output"))
        ###################################################
        # linking is here 
        # for Image1 and 2 components
        ####################################################
        self.Image1ComboBox.currentIndexChanged.connect(self.Update_img_component)
        self.Image2ComboBox.currentIndexChanged.connect(self.Update_img_component)

    def Update_img_component(self, component_indx):
        pixmap_img1_comp = QtGui.QPixmap(self.path3)
        pixmap_img1_comp = pixmap_img1_comp.scaled(355, 300, QtCore.Qt.KeepAspectRatio)

        if component_indx == 0: # magnitude
            self.get_img_magnitude()
            self.Image1ViewerB.setPixmap(pixmap_img1_comp)
            self.Image1ViewerB.show()

        elif component_indx == 1: # phase
            pass
        elif component_indx == 2: # reals
            self.get_img_reals()
            self.Image1ViewerB.setPixmap(pixmap_img1_comp)
            self.Image1ViewerB.show()
        elif component_indx == 3: # imaginary
            self.get_img_imgnary()
            self.Image1ViewerB.setPixmap(pixmap_img1_comp)
            self.Image1ViewerB.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

