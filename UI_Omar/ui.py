# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Equalizer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1080, 850)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.OriginalSignalGroupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OriginalSignalGroupbox.setFont(font)
        self.OriginalSignalGroupbox.setObjectName("OriginalSignalGroupbox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.OriginalSignalGroupbox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.OriginalSignalViewer = QtWidgets.QGraphicsView(self.OriginalSignalGroupbox)
        self.OriginalSignalViewer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OriginalSignalViewer.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.OriginalSignalViewer.setObjectName("OriginalSignalViewer")
        self.gridLayout_4.addWidget(self.OriginalSignalViewer, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.OriginalSignalGroupbox, 0, 0, 1, 1)
        self.SpectrogramGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SpectrogramGroupBox.setFont(font)
        self.SpectrogramGroupBox.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.SpectrogramGroupBox.setObjectName("SpectrogramGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SpectrogramGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SignalBeforeEditiing_2 = QtWidgets.QGraphicsView(self.SpectrogramGroupBox)
        self.SignalBeforeEditiing_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SignalBeforeEditiing_2.setStyleSheet("background-color:rgb(0,0,0)")
        self.SignalBeforeEditiing_2.setObjectName("SignalBeforeEditiing_2")
        self.verticalLayout.addWidget(self.SignalBeforeEditiing_2)
        self.gridLayout.addWidget(self.SpectrogramGroupBox, 0, 1, 3, 1)
        self.EditedSignalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.EditedSignalGroupBox.setFont(font)
        self.EditedSignalGroupBox.setObjectName("EditedSignalGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.EditedSignalGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.EditedSignalViewer = QtWidgets.QGraphicsView(self.EditedSignalGroupBox)
        self.EditedSignalViewer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditedSignalViewer.setStyleSheet("background-color:rgb(0,0,0)")
        self.EditedSignalViewer.setObjectName("EditedSignalViewer")
        self.gridLayout_5.addWidget(self.EditedSignalViewer, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.EditedSignalGroupBox, 2, 0, 1, 1)
        self.SignalEditorGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SignalEditorGroupBox.setFont(font)
        self.SignalEditorGroupBox.setObjectName("SignalEditorGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.SignalEditorGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Slider1 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider1.setMinimum(1)
        self.Slider1.setMaximum(10)
        self.Slider1.setOrientation(QtCore.Qt.Vertical)
        self.Slider1.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider1.setTickInterval(1)
        self.Slider1.setObjectName("Slider1")
        self.gridLayout_3.addWidget(self.Slider1, 0, 2, 1, 1)
        self.Slider3 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider3.setMinimum(1)
        self.Slider3.setMaximum(10)
        self.Slider3.setPageStep(10)
        self.Slider3.setOrientation(QtCore.Qt.Vertical)
        self.Slider3.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider3.setTickInterval(1)
        self.Slider3.setObjectName("Slider3")
        self.gridLayout_3.addWidget(self.Slider3, 0, 1, 1, 1)
        self.Slider2 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider2.setToolTip("")
        self.Slider2.setMinimum(1)
        self.Slider2.setMaximum(10)
        self.Slider2.setOrientation(QtCore.Qt.Vertical)
        self.Slider2.setInvertedAppearance(False)
        self.Slider2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider2.setTickInterval(1)
        self.Slider2.setObjectName("Slider2")
        self.gridLayout_3.addWidget(self.Slider2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.SignalEditorGroupBox, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Equalizer"))
        self.OriginalSignalGroupbox.setTitle(_translate("MainWindow", "Signal Before Editing"))
        self.SpectrogramGroupBox.setTitle(_translate("MainWindow", "Spectrogram"))
        self.EditedSignalGroupBox.setTitle(_translate("MainWindow", "Signal After Editing"))
        self.SignalEditorGroupBox.setTitle(_translate("MainWindow", "Signal Editor"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

