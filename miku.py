import sys
import os
import random
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtWidgets, QtGui

class MyMikuPet(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        quit = QAction("退出", self, triggered=os._exit)
        quit.setIcon(QIcon("img/icon.png"))
        addPet = QAction("添加一个Miku", self, triggered = addOnePet)
        addPet.setIcon(QIcon("img/icon.png"))
        removePet = QAction("移除一个Miku", self, triggered = delOnePet)
        removePet.setIcon(QIcon("img/icon.png"))
        about = QAction("About", self, triggered=aboutInfo)
        about.setIcon(QIcon("img/icon.png"))
        self.pet = myPet()
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(addPet)
        self.trayIconMenu.addAction(removePet)
        self.trayIconMenu.addAction(about)
        self.trayIconMenu.addAction(quit)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("img/icon.png"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()

def addOnePet():
    pets.append(myPet())

def delOnePet():
    if len(pets)==0:
        return
    del pets[len(pets)-1]

def aboutInfo():
    webbrowser.open_new_tab("https://github.com/luxingwen/desktop-pet-miku")

class myPet(QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.repaint()
        self.img = QLabel(self)
        self.actionDatas = []
        self.initData()
        self.index = 0
        self.setPic("shime1.png")
        self.resize(128, 128)
        self.show()
        self.runing = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.actionRun)
        self.timer.start(500)
        self.randomPos()

    def getImgs(self, pics):
        listPic = []
        for item in pics:
            img = QImage()
            img.load('img/'+item)
            listPic.append(img)
        return listPic

    def initData(self):
        imgs = self.getImgs(["shime1b.png", "shime2b.png", "shime1b.png", "shime3b"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime11.png", "shime15.png", "shime16.png", "shime17.png", "shime16.png", "shime17.png", "shime16.png", "shime17.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime54.png", "shime55.png", "shime26.png", "shime27.png", "shime28.png", "shime29.png","shime26.png", "shime27.png", "shime28.png", "shime29.png","shime26.png", "shime27.png", "shime28.png", "shime29.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime31.png", "shime32.png", "shime31.png", "shime33.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime18.png", "shime19.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime34b.png", "shime35b.png", "shime34b.png", "shime36b.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime14.png", "shime14.png", "shime52.png", "shime13.png", "shime13.png", "shime13.png", "shime52.png", "shime14.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime42.png", "shime43.png", "shime44.png", "shime45.png", "shime46.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime1.png", "shime38.png", "shime39.png", "shime40.png", "shime41.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime25.png", "shime25.png", "shime53.png", "shime24.png", "shime24.png", "shime24.png", "shime53.png", "shime25.png"])
        self.actionDatas.append(imgs)
        imgs = self.getImgs(["shime20.png", "shime21.png", "shime20.png", "shime21.png", "shime20.png"])
        self.actionDatas.append(imgs)

    def actionRun(self):
        if not self.runing:
            self.action = random.randint(0, len(self.actionDatas)-1)
            self.index = 0
            self.runing = True
        self.runFunc(self.actionDatas[self.action])

    def setPic(self, pic):
        img = QImage()
        img.load('img/'+pic)
        self.img.setPixmap(QPixmap.fromImage(img))

    def runFunc(self, imgs):
        if self.index >= len(imgs):
            self.index = 0
            self.runing = False
        self.img.setPixmap(QPixmap.fromImage(imgs[self.index]))
        self.index += 1

    def randomPos(self):
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move(int((screen.width()-size.width())*random.random()), int((screen.height()-size.height())*random.random()))

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__ == "__main__":
    global pets
    pets=[]
    app = QApplication(sys.argv)
    w = MyMikuPet()
    sys.exit(app.exec_())
