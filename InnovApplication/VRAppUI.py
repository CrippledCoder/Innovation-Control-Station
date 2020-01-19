import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel, QSpacerItem, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5 import QtWidgets, Qt, QtCore
from PyQt5.QtCore import *
import time


class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Texan VR"
        self.width = 1500
        self.height = 1000

        grid_layout = QGridLayout()  # outermost layout
        self.setLayout(grid_layout)

        # halves
        rightLayout = QGridLayout()
        rightBottomLayout = QGridLayout()
        rightTopLayoutOuter = QVBoxLayout()
        rightTopTopLayout = QHBoxLayout()
        rightTopBottomLayout = QHBoxLayout()

        # Label Maker
        leftLabel = QLabel("")
        rightTopSqLabel = QLabel("Squadron")
        rightTopFlightLabel = QLabel("Flight")

        # Button Maker
        topLeftButton = QPushButton("Free Fly")
        topRightButton = QPushButton("Missions")
        bottomLeftButton = QPushButton("Custom")
        bottomRightButton = QPushButton("Admin")

        # Combo Container Maker
        # Squadron
        comboSquadron = QComboBox(self)
        comboSquadron.addItem("37th FTS")
        comboSquadron.addItem("41st FTS")

        # Flight
        comboFlight = QComboBox(self)
        comboFlight.addItem("A Flight")
        comboFlight.addItem("B Flight")
        comboFlight.addItem("C Flight")
        comboFlight.addItem("D Flight")
        comboFlight.addItem("F Flight")
        comboFlight.addItem("V Flight")
        comboFlight.addItem("W Flight")
        comboFlight.addItem("X Flight")
        comboFlight.addItem("Y Flight")
        comboFlight.addItem("Z Flight")

        # stylesheet area
        buttonStyle = '''QPushButton {
                                        box-shadow: 3px 4px 0px 0px #1564ad;
                                        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.05 #79bbff, stop:1 #378de5);
                                        border-radius:5px;
                                        border:1px solid #337bc4;
                                        display:inline-block;
                                        cursor:pointer;
                                        color:#ffffff;
                                        font-family:Arial;
                                        font-size:40px;
                                        font-weight:bold;
                                        padding:12px 44px;
                                        text-decoration:none;
                                        text-shadow:0px 1px 0px #528ecc;
                                        height: 80px;
                                        }
                            QPushButton:hover {
                                        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.05 #378de5, stop:1 #79bbff);
                                        background-color:#378de5;
                                        }
                             QPushButton:active {
                                            position:relative;
                                            top:1px;
                                        }
                                        '''
        topLeftButton.setStyleSheet(buttonStyle)
        topRightButton.setStyleSheet(buttonStyle)
        bottomLeftButton.setStyleSheet(buttonStyle)
        bottomRightButton.setStyleSheet(buttonStyle)

        leftLabel.setText('''<p>
                                <font size="15"><b>Welcome to Texan VR <br>Control Center!</b></font>
                             </p>
                             <br>
                             <p>
                             <font size="4">
                                <br>
                                <i>Free Fly:</i>  Starts at 13R at Columbus
                                <br>
                                <br>
                                <i>Missions:</i> Select a pre-planned mission
                                <br>
                                <br>
                                <i>Custom:</i> Select the parameters that fit your training
                                <br>
                                <br>
                                <i>Admin:</i> For VR Admin use
                            </font>
                             </p>
                            ''')
        rightTopSqLabel.setStyleSheet("font-weight: bold;")
        rightTopFlightLabel.setStyleSheet("font-weight: bold;")
        self.setStyleSheet("background-color: #72A0C1;")  # widget background

        # Alignments set
        leftLabel.setAlignment(Qt.AlignCenter)
        rightTopSqLabel.setAlignment(Qt.AlignRight)
        rightTopFlightLabel.setAlignment(Qt.AlignRight)

        # Item Organizing
        grid_layout.addWidget(leftLabel, 0, 0)
        grid_layout.addLayout(rightLayout, 0, 1)

        # upper right quadrant
        rightLayout.addLayout(rightTopLayoutOuter, 0, 0)  # used a vertical layout
        rightTopLayoutOuter.addItem(self.vSpacer(200))
        rightTopLayoutOuter.addLayout(rightTopTopLayout)
        rightTopLayoutOuter.addLayout(rightTopBottomLayout)
        rightTopTopLayout.addWidget(rightTopSqLabel)
        rightTopTopLayout.addWidget(comboSquadron)
        rightTopTopLayout.addItem(self.hSpacer(200))
        rightTopBottomLayout.addWidget(rightTopFlightLabel)
        rightTopBottomLayout.addWidget(comboFlight)
        rightTopBottomLayout.addItem(self.hSpacer(200))

        # space out the right
        rightLayout.addItem(self.vSpacer(200), 1, 0)

        # bottom right quadrant
        rightLayout.addLayout(rightBottomLayout, 2, 0)  # big grid
        rightBottomLayout.addWidget(topLeftButton, 0, 0)
        rightBottomLayout.addWidget(topRightButton, 0, 1)
        rightBottomLayout.addWidget(bottomLeftButton, 1, 0)
        rightBottomLayout.addWidget(bottomRightButton, 1, 1)

        grid_layout.setRowStretch(1,0)
        # example if a spacer is needed
        # grid_layout.addItem(self.vSpacer(100), 3, 0)

        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

    def vSpacer(self, size):
        return QSpacerItem(0, size, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

    def hSpacer(self, size):
        return QSpacerItem(size, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
