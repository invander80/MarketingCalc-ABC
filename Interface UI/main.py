import json
import random
from ui.main.ui_main import *

with open("jsonFiles/sheet.json", "r") as jsonFile:
    data = json.load(jsonFile)


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qannimation = QAnimation(self)

        #self.submitBtn.clicked.connect(self.calcValue)
        self.setShadow(self.frame_4, "#4cfeff")

        self.lst = []

    def setShadow(self, widget, color):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(color)
        widget.setGraphicsEffect(shadow)

    """def calcValue(self):
        self.lst.append(float(self.amountEdit.text()) * float(self.priceEdit.text()))
        print(self.lst)"""


class QAnimation(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.timer = QTimer()
        self.timer.timeout.connect(self.animateBackground)
        self.timer.timeout.connect(self.animateToolBar)
        self.timer.timeout.connect(self.animateNavBar)
        self.timer.start(30)

        self.bgCount = 0
        self.up = 0
        self.down = 300

        self.navCounter = 0

        self.toolBegin = 0
        self.toolEnd = 100

    def animateNavBar(self):
        if self.navCounter >= 360:
            self.navCounter = 0
        self.navCounter += 3
        self.changeNavBar(self.navCounter)

    def changeNavBar(self, value):
        navSheet = data["NavBar"].replace("{0}", str(-value))
        self.parent.navBg.setStyleSheet(navSheet)

    def animateBackground(self):
        if self.bgCount >= 300:
            self.bgCount = 0
        self.bgCount += 1
        self.changeStyle(self.bgCount)

    def changeStyle(self, value):
        progress = value / 100.0
        stop1 = str(progress)
        if self.up < 300:
            bgSheet = data["Background"].replace("{0}", stop1).replace("{1}", "-0.2").replace("{2}", "1.0")
            self.parent.navLoad.setStyleSheet(bgSheet)
            self.up += 1
        elif self.up == 300:
            if self.down > 0:
                bgSheet = data["Background"].replace("{0}", stop1).replace("{1}", "1.2").replace("{2}", "1.0")
                self.parent.navLoad.setStyleSheet(bgSheet)
                self.down -= 1
            else:
                self.up = 0
                self.down = 300

    def animateToolBar(self):
        if self.toolBegin < 100:
            self.toolBegin += 1
            self.changeStyle2(self.toolBegin)
        elif self.toolBegin == 100:
            if self.toolEnd > 0:
                self.toolEnd -= 1
                self.changeStyle2(self.toolEnd)
            else:
                self.toolBegin = 0
                self.toolEnd = 100

    def changeStyle2(self, value):
        progress = value / 100.0
        stop2 = str(progress+1.0)
        stop3 = str(progress-1.0)
        toolSheet = data["ToolBar"].replace("{1}", stop2).replace("{2}", stop3)
        editLines = data["Edit"].replace("{1}", stop2).replace("{2}", stop3)
        self.parent.toolBar.setStyleSheet(toolSheet)
        self.parent.amountEdit.setStyleSheet(editLines)
        self.parent.priceEdit.setStyleSheet(editLines)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()


