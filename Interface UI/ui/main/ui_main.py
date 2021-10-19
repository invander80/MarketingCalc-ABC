# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainINhlhJ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images.img

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1356, 862)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.border = QFrame(Form)
        self.border.setObjectName(u"border")
        self.border.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.border.setFrameShape(QFrame.StyledPanel)
        self.border.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.border)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.statusBar = QFrame(self.border)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 50))
        self.statusBar.setMaximumSize(QSize(16777215, 50))
        self.statusBar.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.statusBar.setFrameShape(QFrame.StyledPanel)
        self.statusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.statusLayout_3 = QGridLayout()
        self.statusLayout_3.setObjectName(u"statusLayout_3")
        self.statusContainer_3 = QFrame(self.statusBar)
        self.statusContainer_3.setObjectName(u"statusContainer_3")
        self.statusContainer_3.setMinimumSize(QSize(100, 40))
        self.statusContainer_3.setMaximumSize(QSize(16777215, 40))
        self.statusContainer_3.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border-radius:10px;")
        self.statusContainer_3.setFrameShape(QFrame.StyledPanel)
        self.statusContainer_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.statusContainer_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 2, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.statusLayout_3.addWidget(self.statusContainer_3, 0, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.statusLayout_3)


        self.gridLayout.addWidget(self.statusBar, 2, 0, 1, 1)

        self.mainContainer = QFrame(self.border)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setStyleSheet(u"border-image:none;\n"
"background:none;")
        self.mainContainer.setFrameShape(QFrame.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.mainContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.navLoad = QFrame(self.mainContainer)
        self.navLoad.setObjectName(u"navLoad")
        self.navLoad.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.349304 rgba(0, 0, 0, 205), stop:0.477589 rgba(76, 254, 255, 205), stop:0.520866 rgba(76, 242, 255, 205), stop:0.700155 rgba(0, 0, 0, 205));")
        self.navLoad.setFrameShape(QFrame.StyledPanel)
        self.navLoad.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.navLoad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(self.navLoad)
        self.background.setObjectName(u"background")
        self.background.setStyleSheet(u"border-image: url(:/bg/bg/honeycomb-wallpaper-hd-1920x1080-166094.png);")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.background)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.background)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border-image:none;\n"
"background:none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setVerticalSpacing(11)
        self.gridLayout_14.setContentsMargins(10, 10, 10, 10)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(400, 160))
        self.frame_4.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border-radius:20px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setMaximumSize(QSize(50, 50))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-radius:25px;")

        self.gridLayout_12.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-radius:25px;")

        self.gridLayout_12.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.navBg = QFrame(self.frame_4)
        self.navBg.setObjectName(u"navBg")
        self.navBg.setMinimumSize(QSize(480, 140))
        self.navBg.setMaximumSize(QSize(480, 140))
        self.navBg.setStyleSheet(u"border-radius:20px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:137.5, stop:0.03 rgba(124, 242, 255, 205), stop:0.118333 rgba(30, 25, 8, 0));")
        self.navBg.setFrameShape(QFrame.StyledPanel)
        self.navBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.navBg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_5 = QFrame(self.navBg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(460, 120))
        self.frame_5.setMaximumSize(QSize(460, 120))
        self.frame_5.setStyleSheet(u"background-color: rgb(22, 22, 22);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.amountEdit = QLineEdit(self.frame_5)
        self.amountEdit.setObjectName(u"amountEdit")
        self.amountEdit.setMinimumSize(QSize(100, 0))
        self.amountEdit.setMaximumSize(QSize(100, 16777215))
        self.amountEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei\";\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0.379, y1:0, x2:0.669, y2:0, stop:0.112 rgba(0, 0, 0, 0), stop:0.466049 rgba(0, 251, 255, 155), stop:0.604956 rgba(0, 251, 255, 155), stop:0.874 rgba(0, 0, 0, 0));\n"
"border-radius:0px;")

        self.gridLayout_15.addWidget(self.amountEdit, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei\";")

        self.gridLayout_15.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei\";")

        self.gridLayout_15.addWidget(self.label_9, 0, 0, 1, 1)

        self.submitBtn = QPushButton(self.frame_5)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setMinimumSize(QSize(50, 35))
        self.submitBtn.setMaximumSize(QSize(50, 35))
        self.submitBtn.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-radius:10px;")

        self.gridLayout_15.addWidget(self.submitBtn, 0, 4, 1, 1)

        self.priceEdit = QLineEdit(self.frame_5)
        self.priceEdit.setObjectName(u"priceEdit")
        self.priceEdit.setMinimumSize(QSize(100, 0))
        self.priceEdit.setMaximumSize(QSize(100, 16777215))
        self.priceEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei\";\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0.379, y1:0, x2:0.669, y2:0, stop:0.112 rgba(0, 0, 0, 0), stop:0.466049 rgba(0, 251, 255, 155), stop:0.604956 rgba(0, 251, 255, 155), stop:0.874 rgba(0, 0, 0, 0));\n"
"border-radius:0px;")

        self.gridLayout_15.addWidget(self.priceEdit, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-radius:10px;")

        self.gridLayout_15.addWidget(self.pushButton, 1, 0, 1, 5)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.gridLayout_12.addWidget(self.navBg, 0, 1, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_12)


        self.gridLayout_14.addWidget(self.frame_4, 1, 1, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_2, 1, 6, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableWidget_2 = QTableWidget(self.frame_3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"background:rgba(0,0,0,0);\n"
"}")

        self.gridLayout_11.addWidget(self.tableWidget_2, 0, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_11, 0, 0, 1, 7)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.donutLayout = QGridLayout()
        self.donutLayout.setObjectName(u"donutLayout")

        self.verticalLayout_2.addLayout(self.donutLayout)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.background)


        self.gridLayout_2.addWidget(self.navLoad, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.mainContainer, 1, 0, 1, 1)

        self.toolBar = QFrame(self.border)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMinimumSize(QSize(0, 50))
        self.toolBar.setMaximumSize(QSize(16777215, 50))
        self.toolBar.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0.379, y1:0, x2:0.669, y2:0, stop:0.112 rgba(0, 0, 0, 0), stop:0.466049 rgba(0, 251, 255, 155), stop:0.604956 rgba(0, 251, 255, 155), stop:0.874 rgba(0, 0, 0, 0));")
        self.toolBar.setFrameShape(QFrame.StyledPanel)
        self.toolBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.toolBar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(2)
        self.gridLayout_4.setVerticalSpacing(0)
        self.frame = QFrame(self.toolBar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setMaximumSize(QSize(150, 16777215))
        self.frame.setStyleSheet(u"background:none;\n"
"border-bottom:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(50, 40))
        self.minimizeBtn.setMaximumSize(QSize(50, 40))
        self.minimizeBtn.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border-radius:10px;")

        self.gridLayout_7.addWidget(self.minimizeBtn, 0, 0, 1, 1)

        self.restoreBtn = QPushButton(self.frame)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setMinimumSize(QSize(50, 40))
        self.restoreBtn.setMaximumSize(QSize(50, 40))
        self.restoreBtn.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border-radius:10px;")

        self.gridLayout_7.addWidget(self.restoreBtn, 0, 1, 1, 1)

        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(50, 40))
        self.exitBtn.setMaximumSize(QSize(50, 40))
        self.exitBtn.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border-radius:10px;")

        self.gridLayout_7.addWidget(self.exitBtn, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 1, 1, 1)

        self.logoContainer = QFrame(self.toolBar)
        self.logoContainer.setObjectName(u"logoContainer")
        self.logoContainer.setMinimumSize(QSize(0, 40))
        self.logoContainer.setMaximumSize(QSize(16777215, 40))
        self.logoContainer.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border-radius:10px;\n"
"border-bottom:none;")
        self.logoContainer.setFrameShape(QFrame.StyledPanel)
        self.logoContainer.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.logoContainer, 0, 0, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_4)


        self.gridLayout.addWidget(self.toolBar, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.border)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"EK-Preis(\u20ac):", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Menge:", None))
        self.submitBtn.setText("")
        self.pushButton.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.exitBtn.setText("")
    # retranslateUi

