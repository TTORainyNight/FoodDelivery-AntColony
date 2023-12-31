from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os
from xml.etree.ElementTree import C14NWriterTarget
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1085, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Q1 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Q1.setGeometry(QtCore.QRect(90, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Q1.setFont(font)
        self.Q1.setObjectName("Q1")
        self.P1 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.P1.setGeometry(QtCore.QRect(280, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.P1.setFont(font)
        self.P1.setObjectName("P1")
        self.Q2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Q2.setGeometry(QtCore.QRect(90, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Q2.setFont(font)
        self.Q2.setObjectName("Q2")
        self.P3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.P3.setGeometry(QtCore.QRect(280, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.P3.setFont(font)
        self.P3.setObjectName("P3")
        self.Q3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Q3.setGeometry(QtCore.QRect(90, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Q3.setFont(font)
        self.Q3.setObjectName("Q3")
        self.C4 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.C4.setGeometry(QtCore.QRect(470, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.C4.setFont(font)
        self.C4.setObjectName("C4")
        self.C3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(470, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.C3.setFont(font)
        self.C3.setObjectName("C3")
        self.P2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.P2.setGeometry(QtCore.QRect(280, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.P2.setFont(font)
        self.P2.setObjectName("P2")
        self.L1 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(470, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L1.setFont(font)
        self.L1.setObjectName("L1")
        self.Q4 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Q4.setGeometry(QtCore.QRect(90, 340, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Q4.setFont(font)
        self.Q4.setObjectName("Q4")
        self.P4 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.P4.setGeometry(QtCore.QRect(280, 340, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.P4.setFont(font)
        self.P4.setObjectName("P4")
        self.L2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(470, 340, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L2.setFont(font)
        self.L2.setObjectName("L2")
        self.Q5 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Q5.setGeometry(QtCore.QRect(90, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Q5.setFont(font)
        self.Q5.setObjectName("Q5")
        self.C1 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(280, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.C1.setFont(font)
        self.C1.setObjectName("C1")
        self.L3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(470, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L3.setFont(font)
        self.L3.setObjectName("L3")
        self.Q6 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Q6.setGeometry(QtCore.QRect(90, 500, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Q6.setFont(font)
        self.Q6.setObjectName("Q6")
        self.C2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(280, 500, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.C2.setFont(font)
        self.C2.setObjectName("C2")
        self.L4 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.L4.setGeometry(QtCore.QRect(470, 500, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L4.setFont(font)
        self.L4.setObjectName("L4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 340, 61, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 420, 61, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 500, 61, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 100, 61, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 180, 61, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 260, 61, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(220, 340, 61, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(220, 420, 61, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(220, 500, 61, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(400, 100, 71, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(410, 180, 61, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(410, 270, 61, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(410, 340, 61, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(410, 420, 61, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(410, 500, 61, 31))
        self.label_18.setObjectName("label_18")
        self.StartButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(220, 570, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.StartButton.clicked.connect(self.Start_Button_Clicked)
        self.RestButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RestButton.setGeometry(QtCore.QRect(620, 570, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RestButton.setFont(font)
        self.RestButton.setObjectName("RestButton")
        self.RestButton.clicked.connect(self.Rest_Button_Clicked)
        self.RestLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.RestLabel.setGeometry(QtCore.QRect(600, 100, 441, 441))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.RestLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.RestLabel.setFont(font)
        self.RestLabel.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.RestLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.RestLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.RestLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.RestLabel.setWordWrap(True)
        self.RestLabel.setObjectName("RestLabel")
        self.label_19 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(0, -20, 1161, 731))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("back.jpg"))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(800, 640, 181, 21))
        self.label_20.setObjectName("label_20")
        self.label_19.raise_()
        self.Q1.raise_()
        self.P1.raise_()
        self.Q2.raise_()
        self.P3.raise_()
        self.Q3.raise_()
        self.C4.raise_()
        self.C3.raise_()
        self.P2.raise_()
        self.L1.raise_()
        self.Q4.raise_()
        self.P4.raise_()
        self.L2.raise_()
        self.Q5.raise_()
        self.C1.raise_()
        self.L3.raise_()
        self.Q6.raise_()
        self.C2.raise_()
        self.L4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.StartButton.raise_()
        self.RestButton.raise_()
        self.RestLabel.raise_()
        self.label_20.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1085, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #“规划”按钮单击事件
    def Start_Button_Clicked(self):
        #数据初始化
        if os.path.exists('OutPut.txt'):
            os.remove('OutPut.txt')   #删除输出文件
        self.RestLabel.setText(self.RestLabel.text() + f"<html><head/><body><p><span style=\" font-size:16pt;\">成功，正在规划路径，请等待……</span></p></body></html>")
        q1=0
        q2=0
        q3=0
        q4=0
        q5=0
        q6=0
        l1=0
        l2=0
        l3=0
        l4=0
        c1=0
        c2=0
        c3=0
        c4=0
        p1=0
        p2=0
        p3=0
        p4=0
        #数据保存
        q1 = self.Q1.toPlainText()
        q2 = self.Q2.toPlainText()
        q3 = self.Q3.toPlainText()
        q4 = self.Q4.toPlainText()
        q5 = self.Q5.toPlainText()
        q6 = self.Q6.toPlainText()
        l1 = self.L1.toPlainText()
        l2 = self.L2.toPlainText()
        l3 = self.L3.toPlainText()
        l4 = self.L4.toPlainText()
        c1 = self.C1.toPlainText()
        c2 = self.C2.toPlainText()
        c3 = self.C3.toPlainText()
        c4 = self.C4.toPlainText()
        p1 = self.P1.toPlainText()
        p2 = self.P2.toPlainText()
        p3 = self.P3.toPlainText()
        p4 = self.P4.toPlainText()
        df = pd.DataFrame({'启智园': [q1,q2,q3,q4,q5,q6,l1,l2,l3,l4,'I`m tired'], '崇实园': [c1,c2,c3,c4,p1,p2,p3,p4,'GUIsocomplex','TutuQiang','9958']})
        df.to_excel('Inmeal.xlsx', index=False)
        os.system('start wmzh.exe')

    #“检测”按钮单击事件
    def Rest_Button_Clicked(self):
        if not os.path.exists('OutPut.txt'):
            self.RestLabel.setText(self.RestLabel.text() + f"<html><head/><body><p><span style=\" font-size:16pt;\">蚁群算法正在执行，请等待……</span></p></body></html>")
        else:
            with open('OutPut.txt', 'r', encoding='utf-8') as f:
                content = f.read()
                content = content.replace(' ', '&nbsp;')
                content = content.replace('\n', '<br>')
                content = content.replace('[', '')
                content = content.replace(']', '')
                content = content.replace(',', '->')
                self.RestLabel.setWordWrap(True)
                self.RestLabel.setText(f"<html><head/><body><p><span style=\" font-size:13pt;\">{content}</span></p></body></html>")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "启智1、2"))
        self.label_2.setText(_translate("MainWindow", "启智3、4"))
        self.label_3.setText(_translate("MainWindow", "启智5、6"))
        self.label_4.setText(_translate("MainWindow", "启智7、8"))
        self.label_5.setText(_translate("MainWindow", "启智9、10"))
        self.label_6.setText(_translate("MainWindow", "  职技楼"))
        self.label_7.setText(_translate("MainWindow", "诚朴1、2"))
        self.label_8.setText(_translate("MainWindow", "诚朴园3"))
        self.label_9.setText(_translate("MainWindow", "诚朴4、5"))
        self.label_10.setText(_translate("MainWindow", "诚朴园6"))
        self.label_11.setText(_translate("MainWindow", "崇实7、8"))
        self.label_12.setText(_translate("MainWindow", "崇实园9"))
        self.label_13.setText(_translate("MainWindow", "崇实10、11"))
        self.label_14.setText(_translate("MainWindow", "崇实园12"))
        self.label_15.setText(_translate("MainWindow", "理科群1"))
        self.label_16.setText(_translate("MainWindow", "理科群2"))
        self.label_17.setText(_translate("MainWindow", "理科群3"))
        self.label_18.setText(_translate("MainWindow", " 文科楼"))
        self.StartButton.setText(_translate("MainWindow", "规划"))
        self.RestButton.setText(_translate("MainWindow", "检测结果"))
        self.RestLabel.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">欢迎来到蚁群算法校园外卖小车路径规划!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">请君洗耳，听吾之言：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    师大学子，中燃人学习为业。缘蚁群，忘路之远近。忽逢桃花林，夹岸数百步，中无杂树，芳草鲜美，落英缤纷。有令硕、雨诺、玉涵、启柯之美，远离人间，未闻犬吠、鸡鸣之声，但见群鸟自飞，人迹罕至。忽见英杰，称之李强。复行数十步，豁然开朗。土地平旷，屋舍俨然，有良田美池桑竹之属。</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "放个防伪标签，这是我们小组→"))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())