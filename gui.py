# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python32\project\1\Gui.ui'
#
# Created: Fri Sep  7 11:42:05 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 362)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/ir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.canvas = QtGui.QWidget(MainWindow)
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.frame = QtGui.QFrame(self.canvas)
        self.frame.setGeometry(QtCore.QRect(10, 10, 491, 341))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.mainFram = QtGui.QTabWidget(self.frame)
        self.mainFram.setGeometry(QtCore.QRect(0, 0, 481, 311))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.mainFram.setFont(font)
        self.mainFram.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mainFram.setTabPosition(QtGui.QTabWidget.North)
        self.mainFram.setTabShape(QtGui.QTabWidget.Triangular)
        self.mainFram.setObjectName(_fromUtf8("mainFram"))
        self.IP = QtGui.QWidget()
        self.IP.setObjectName(_fromUtf8("IP"))
        self.toolBoxIP = QtGui.QToolBox(self.IP)
        self.toolBoxIP.setGeometry(QtCore.QRect(20, 10, 431, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBoxIP.setFont(font)
        self.toolBoxIP.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBoxIP.setFrameShape(QtGui.QFrame.VLine)
        self.toolBoxIP.setObjectName(_fromUtf8("toolBoxIP"))
        self.rangeIP = QtGui.QWidget()
        self.rangeIP.setGeometry(QtCore.QRect(0, 0, 429, 149))
        self.rangeIP.setObjectName(_fromUtf8("rangeIP"))
        self.frame_7 = QtGui.QFrame(self.rangeIP)
        self.frame_7.setGeometry(QtCore.QRect(20, 0, 381, 151))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.scanIp1 = QtGui.QPushButton(self.frame_7)
        self.scanIp1.setGeometry(QtCore.QRect(110, 100, 91, 41))
        self.scanIp1.setObjectName(_fromUtf8("scanIp1"))
        self.startLineEditIP = QtGui.QLineEdit(self.frame_7)
        self.startLineEditIP.setGeometry(QtCore.QRect(140, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startLineEditIP.setFont(font)
        self.startLineEditIP.setObjectName(_fromUtf8("startLineEditIP"))
        self.endLineEditIP = QtGui.QLineEdit(self.frame_7)
        self.endLineEditIP.setGeometry(QtCore.QRect(140, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endLineEditIP.setFont(font)
        self.endLineEditIP.setObjectName(_fromUtf8("endLineEditIP"))
        self.startLabelIp = QtGui.QLabel(self.frame_7)
        self.startLabelIp.setGeometry(QtCore.QRect(10, 10, 51, 31))
        self.startLabelIp.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startLabelIp.setFont(font)
        self.startLabelIp.setObjectName(_fromUtf8("startLabelIp"))
        self.endLabelIp = QtGui.QLabel(self.frame_7)
        self.endLabelIp.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.endLabelIp.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endLabelIp.setFont(font)
        self.endLabelIp.setObjectName(_fromUtf8("endLabelIp"))
        self.line_3 = QtGui.QFrame(self.frame_7)
        self.line_3.setGeometry(QtCore.QRect(40, 50, 118, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.frame_7)
        self.line_4.setGeometry(QtCore.QRect(70, 20, 3, 61))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/default-ip.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBoxIP.addItem(self.rangeIP, icon1, _fromUtf8(""))
        self.hostIP = QtGui.QWidget()
        self.hostIP.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.hostIP.setObjectName(_fromUtf8("hostIP"))
        self.frame_9 = QtGui.QFrame(self.hostIP)
        self.frame_9.setGeometry(QtCore.QRect(20, 10, 381, 131))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.scanIP2 = QtGui.QPushButton(self.frame_9)
        self.scanIP2.setGeometry(QtCore.QRect(110, 70, 91, 41))
        self.scanIP2.setObjectName(_fromUtf8("scanIP2"))
        self.hostName = QtGui.QLineEdit(self.frame_9)
        self.hostName.setGeometry(QtCore.QRect(160, 20, 171, 31))
        self.hostName.setObjectName(_fromUtf8("hostName"))
        self.hostLabel = QtGui.QLabel(self.frame_9)
        self.hostLabel.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.hostLabel.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hostLabel.setFont(font)
        self.hostLabel.setObjectName(_fromUtf8("hostLabel"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/what_is_my_ip_address.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBoxIP.addItem(self.hostIP, icon2, _fromUtf8(""))
        self.MyIPAddress = QtGui.QWidget()
        self.MyIPAddress.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.MyIPAddress.setObjectName(_fromUtf8("MyIPAddress"))
        self.frame_8 = QtGui.QFrame(self.MyIPAddress)
        self.frame_8.setGeometry(QtCore.QRect(20, 0, 371, 151))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setMidLineWidth(-3)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.scanPCIP = QtGui.QPushButton(self.frame_8)
        self.scanPCIP.setGeometry(QtCore.QRect(30, 90, 91, 41))
        self.scanPCIP.setObjectName(_fromUtf8("scanPCIP"))
        self.label = QtGui.QLabel(self.frame_8)
        self.label.setGeometry(QtCore.QRect(0, 30, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.myIPLineEdit = QtGui.QLineEdit(self.frame_8)
        self.myIPLineEdit.setGeometry(QtCore.QRect(160, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.myIPLineEdit.setFont(font)
        self.myIPLineEdit.setObjectName(_fromUtf8("myIPLineEdit"))
        self.toolBoxIP.addItem(self.MyIPAddress, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/e4d0af18af30a4aeb70e0ccb0078d4cb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainFram.addTab(self.IP, icon3, _fromUtf8(""))
        self.Port = QtGui.QWidget()
        self.Port.setObjectName(_fromUtf8("Port"))
        self.frame_3 = QtGui.QFrame(self.Port)
        self.frame_3.setGeometry(QtCore.QRect(260, 20, 161, 241))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 131, 241))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.table = QtGui.QTableView(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table.setFont(font)
        self.table.setObjectName(_fromUtf8("table"))
        self.horizontalLayout.addWidget(self.table)
        self.frame_2 = QtGui.QFrame(self.Port)
        self.frame_2.setGeometry(QtCore.QRect(10, 90, 211, 181))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.scanPort = QtGui.QPushButton(self.frame_2)
        self.scanPort.setGeometry(QtCore.QRect(50, 130, 91, 41))
        self.scanPort.setObjectName(_fromUtf8("scanPort"))
        self.startPort = QtGui.QSpinBox(self.frame_2)
        self.startPort.setGeometry(QtCore.QRect(110, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startPort.setFont(font)
        self.startPort.setObjectName(_fromUtf8("startPort"))
        self.endPort = QtGui.QSpinBox(self.frame_2)
        self.endPort.setGeometry(QtCore.QRect(110, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endPort.setFont(font)
        self.endPort.setMaximum(65535)
        self.endPort.setProperty("value", 65535)
        self.endPort.setObjectName(_fromUtf8("endPort"))
        self.startLabelPort = QtGui.QLabel(self.frame_2)
        self.startLabelPort.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.startLabelPort.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startLabelPort.setFont(font)
        self.startLabelPort.setObjectName(_fromUtf8("startLabelPort"))
        self.endLabelPort = QtGui.QLabel(self.frame_2)
        self.endLabelPort.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.endLabelPort.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endLabelPort.setFont(font)
        self.endLabelPort.setObjectName(_fromUtf8("endLabelPort"))
        self.line = QtGui.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(80, 30, 3, 61))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(30, 60, 118, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.frame_10 = QtGui.QFrame(self.Port)
        self.frame_10.setGeometry(QtCore.QRect(10, 10, 221, 81))
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.IP_PortScaner = QtGui.QLineEdit(self.frame_10)
        self.IP_PortScaner.setGeometry(QtCore.QRect(70, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IP_PortScaner.setFont(font)
        self.IP_PortScaner.setObjectName(_fromUtf8("IP_PortScaner"))
        self.hostLabel_3 = QtGui.QLabel(self.frame_10)
        self.hostLabel_3.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.hostLabel_3.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hostLabel_3.setFont(font)
        self.hostLabel_3.setObjectName(_fromUtf8("hostLabel_3"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/d3a1cd1e79201295ffde6c5d6f680d7f.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainFram.addTab(self.Port, icon4, _fromUtf8(""))
        self.PC = QtGui.QWidget()
        self.PC.setObjectName(_fromUtf8("PC"))
        self.frame_11 = QtGui.QFrame(self.PC)
        self.frame_11.setGeometry(QtCore.QRect(40, 20, 391, 231))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setMidLineWidth(-3)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.scanIPLocation = QtGui.QPushButton(self.frame_11)
        self.scanIPLocation.setGeometry(QtCore.QRect(30, 90, 91, 41))
        self.scanIPLocation.setObjectName(_fromUtf8("scanIPLocation"))
        self.label_2 = QtGui.QLabel(self.frame_11)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.IPLocation = QtGui.QLineEdit(self.frame_11)
        self.IPLocation.setGeometry(QtCore.QRect(160, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IPLocation.setFont(font)
        self.IPLocation.setObjectName(_fromUtf8("IPLocation"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/113f15629c5bb690c359ae540cec01fd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainFram.addTab(self.PC, icon5, _fromUtf8(""))
        self.Trace = QtGui.QWidget()
        self.Trace.setObjectName(_fromUtf8("Trace"))
        self.frame_6 = QtGui.QFrame(self.Trace)
        self.frame_6.setGeometry(QtCore.QRect(20, 30, 441, 191))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.traceButton = QtGui.QPushButton(self.frame_6)
        self.traceButton.setGeometry(QtCore.QRect(180, 90, 91, 41))
        self.traceButton.setObjectName(_fromUtf8("traceButton"))
        self.addressIPTrace = QtGui.QLineEdit(self.frame_6)
        self.addressIPTrace.setEnabled(True)
        self.addressIPTrace.setGeometry(QtCore.QRect(260, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addressIPTrace.setFont(font)
        self.addressIPTrace.setAutoFillBackground(False)
        self.addressIPTrace.setObjectName(_fromUtf8("addressIPTrace"))
        self.hostLabel_2 = QtGui.QLabel(self.frame_6)
        self.hostLabel_2.setGeometry(QtCore.QRect(10, 40, 241, 31))
        self.hostLabel_2.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hostLabel_2.setFont(font)
        self.hostLabel_2.setMouseTracking(False)
        self.hostLabel_2.setWordWrap(False)
        self.hostLabel_2.setObjectName(_fromUtf8("hostLabel_2"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/whois_ip.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainFram.addTab(self.Trace, icon6, _fromUtf8(""))
        self.TransferFile = QtGui.QWidget()
        self.TransferFile.setObjectName(_fromUtf8("TransferFile"))
        self.toolBoxFtp = QtGui.QToolBox(self.TransferFile)
        self.toolBoxFtp.setGeometry(QtCore.QRect(20, 20, 431, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBoxFtp.setFont(font)
        self.toolBoxFtp.setFrameShape(QtGui.QFrame.VLine)
        self.toolBoxFtp.setObjectName(_fromUtf8("toolBoxFtp"))
        self.uploadFile = QtGui.QWidget()
        self.uploadFile.setGeometry(QtCore.QRect(0, 0, 429, 179))
        self.uploadFile.setObjectName(_fromUtf8("uploadFile"))
        self.frame_5 = QtGui.QFrame(self.uploadFile)
        self.frame_5.setEnabled(True)
        self.frame_5.setGeometry(QtCore.QRect(40, 0, 361, 181))
        self.frame_5.setAcceptDrops(False)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.upload = QtGui.QPushButton(self.frame_5)
        self.upload.setGeometry(QtCore.QRect(80, 110, 91, 41))
        self.upload.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.upload.setObjectName(_fromUtf8("upload"))
        self.chooseFileUpload = QtGui.QPushButton(self.frame_5)
        self.chooseFileUpload.setEnabled(True)
        self.chooseFileUpload.setGeometry(QtCore.QRect(40, 50, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chooseFileUpload.setFont(font)
        self.chooseFileUpload.setObjectName(_fromUtf8("chooseFileUpload"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/designer-tab-order-tool.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBoxFtp.addItem(self.uploadFile, icon7, _fromUtf8(""))
        self.downloadFile = QtGui.QWidget()
        self.downloadFile.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.downloadFile.setObjectName(_fromUtf8("downloadFile"))
        self.frame_4 = QtGui.QFrame(self.downloadFile)
        self.frame_4.setGeometry(QtCore.QRect(10, 0, 371, 171))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.download = QtGui.QPushButton(self.frame_4)
        self.download.setGeometry(QtCore.QRect(120, 100, 91, 41))
        self.download.setObjectName(_fromUtf8("download"))
        self.addressFile = QtGui.QLineEdit(self.frame_4)
        self.addressFile.setGeometry(QtCore.QRect(180, 40, 171, 31))
        self.addressFile.setText(_fromUtf8(""))
        self.addressFile.setObjectName(_fromUtf8("addressFile"))
        self.hostLabel_4 = QtGui.QLabel(self.frame_4)
        self.hostLabel_4.setGeometry(QtCore.QRect(20, 40, 141, 31))
        self.hostLabel_4.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hostLabel_4.setFont(font)
        self.hostLabel_4.setMouseTracking(False)
        self.hostLabel_4.setWordWrap(False)
        self.hostLabel_4.setObjectName(_fromUtf8("hostLabel_4"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/tux.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBoxFtp.addItem(self.downloadFile, icon8, _fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/avatar32.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainFram.addTab(self.TransferFile, icon9, _fromUtf8(""))
        MainWindow.setCentralWidget(self.canvas)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.File = QtGui.QMenu(self.menubar)
        self.File.setObjectName(_fromUtf8("File"))
        self.menu_IP_Scanning = QtGui.QMenu(self.File)
        self.menu_IP_Scanning.setObjectName(_fromUtf8("menu_IP_Scanning"))
        self.Transfer = QtGui.QMenu(self.menubar)
        self.Transfer.setObjectName(_fromUtf8("Transfer"))
        self.HelpMenu = QtGui.QMenu(self.menubar)
        self.HelpMenu.setObjectName(_fromUtf8("HelpMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.Port_Scanning = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/Ico_alpha_SearchIndex_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Port_Scanning.setIcon(icon10)
        self.Port_Scanning.setObjectName(_fromUtf8("Port_Scanning"))
        self.IP_Computer = QtGui.QAction(MainWindow)
        self.IP_Computer.setIcon(icon1)
        self.IP_Computer.setObjectName(_fromUtf8("IP_Computer"))
        self.Exit = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/o_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon11)
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.Download = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Download.setIcon(icon12)
        self.Download.setObjectName(_fromUtf8("Download"))
        self.Upload = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Upload.setIcon(icon13)
        self.Upload.setObjectName(_fromUtf8("Upload"))
        self.Help = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Help.setIcon(icon14)
        self.Help.setObjectName(_fromUtf8("Help"))
        self.Contact = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/email.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Contact.setIcon(icon15)
        self.Contact.setObjectName(_fromUtf8("Contact"))
        self.actionRange_IP = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/3-0.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRange_IP.setIcon(icon16)
        self.actionRange_IP.setObjectName(_fromUtf8("actionRange_IP"))
        self.actionHost_Name = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/smalllogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHost_Name.setIcon(icon17)
        self.actionHost_Name.setObjectName(_fromUtf8("actionHost_Name"))
        self.action_Trace = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/new.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Trace.setIcon(icon18)
        self.action_Trace.setObjectName(_fromUtf8("action_Trace"))
        self.actionMy_IP_address = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/hide_my_ip_address.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMy_IP_address.setIcon(icon19)
        self.actionMy_IP_address.setObjectName(_fromUtf8("actionMy_IP_address"))
        self.menu_IP_Scanning.addAction(self.actionRange_IP)
        self.menu_IP_Scanning.addSeparator()
        self.menu_IP_Scanning.addAction(self.actionHost_Name)
        self.menu_IP_Scanning.addAction(self.actionMy_IP_address)
        self.File.addAction(self.menu_IP_Scanning.menuAction())
        self.File.addAction(self.Port_Scanning)
        self.File.addSeparator()
        self.File.addAction(self.action_Trace)
        self.File.addAction(self.IP_Computer)
        self.File.addSeparator()
        self.File.addAction(self.Exit)
        self.File.addSeparator()
        self.Transfer.addAction(self.Download)
        self.Transfer.addSeparator()
        self.Transfer.addAction(self.Upload)
        self.HelpMenu.addAction(self.Help)
        self.HelpMenu.addSeparator()
        self.HelpMenu.addAction(self.Contact)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Transfer.menuAction())
        self.menubar.addAction(self.HelpMenu.menuAction())
        self.startLabelIp.setBuddy(self.startLineEditIP)
        self.endLabelIp.setBuddy(self.endLineEditIP)
        self.hostLabel.setBuddy(self.hostName)
        self.startLabelPort.setBuddy(self.startPort)
        self.endLabelPort.setBuddy(self.endPort)
        self.hostLabel_3.setBuddy(self.hostName)
        self.hostLabel_2.setBuddy(self.hostName)
        self.hostLabel_4.setBuddy(self.hostName)

        self.retranslateUi(MainWindow)
        self.mainFram.setCurrentIndex(2)
        self.toolBoxIP.setCurrentIndex(0)
        self.toolBoxFtp.setCurrentIndex(0)
        self.toolBoxFtp.layout().setSpacing(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Scanner", None, QtGui.QApplication.UnicodeUTF8))
        self.scanIp1.setToolTip(QtGui.QApplication.translate("MainWindow", "Scanning your IP range", None, QtGui.QApplication.UnicodeUTF8))
        self.scanIp1.setText(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.startLineEditIP.setText(QtGui.QApplication.translate("MainWindow", "0.0.0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.endLineEditIP.setText(QtGui.QApplication.translate("MainWindow", "255.255.255.255", None, QtGui.QApplication.UnicodeUTF8))
        self.startLabelIp.setText(QtGui.QApplication.translate("MainWindow", "Start IP", None, QtGui.QApplication.UnicodeUTF8))
        self.endLabelIp.setText(QtGui.QApplication.translate("MainWindow", "End IP", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxIP.setItemText(self.toolBoxIP.indexOf(self.rangeIP), QtGui.QApplication.translate("MainWindow", "Scan a range IP", None, QtGui.QApplication.UnicodeUTF8))
        self.scanIP2.setToolTip(QtGui.QApplication.translate("MainWindow", "Detect IP address", None, QtGui.QApplication.UnicodeUTF8))
        self.scanIP2.setStatusTip(QtGui.QApplication.translate("MainWindow", "Detect IP", None, QtGui.QApplication.UnicodeUTF8))
        self.scanIP2.setText(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.hostName.setText(QtGui.QApplication.translate("MainWindow", "Enter your Host Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLabel.setText(QtGui.QApplication.translate("MainWindow", "Enter host to scan: ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxIP.setItemText(self.toolBoxIP.indexOf(self.hostIP), QtGui.QApplication.translate("MainWindow", "Detect the IP of Host name", None, QtGui.QApplication.UnicodeUTF8))
        self.scanPCIP.setToolTip(QtGui.QApplication.translate("MainWindow", "IP Scanning", None, QtGui.QApplication.UnicodeUTF8))
        self.scanPCIP.setText(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "   Press Scan to detect your Computer IP Address: ", None, QtGui.QApplication.UnicodeUTF8))
        self.myIPLineEdit.setText(QtGui.QApplication.translate("MainWindow", "  My address  IP is: ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxIP.setItemText(self.toolBoxIP.indexOf(self.MyIPAddress), QtGui.QApplication.translate("MainWindow", "Detect  my IP address", None, QtGui.QApplication.UnicodeUTF8))
        self.mainFram.setTabText(self.mainFram.indexOf(self.IP), QtGui.QApplication.translate("MainWindow", "IP Scanner", None, QtGui.QApplication.UnicodeUTF8))
        self.scanPort.setToolTip(QtGui.QApplication.translate("MainWindow", "Port Scanning", None, QtGui.QApplication.UnicodeUTF8))
        self.scanPort.setText(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.startLabelPort.setText(QtGui.QApplication.translate("MainWindow", "Start Port", None, QtGui.QApplication.UnicodeUTF8))
        self.endLabelPort.setText(QtGui.QApplication.translate("MainWindow", "End  Port", None, QtGui.QApplication.UnicodeUTF8))
        self.IP_PortScaner.setText(QtGui.QApplication.translate("MainWindow", "Enter your IP: ", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLabel_3.setText(QtGui.QApplication.translate("MainWindow", "Enter IP: ", None, QtGui.QApplication.UnicodeUTF8))
        self.mainFram.setTabText(self.mainFram.indexOf(self.Port), QtGui.QApplication.translate("MainWindow", "Port Scanner", None, QtGui.QApplication.UnicodeUTF8))
        self.scanIPLocation.setToolTip(QtGui.QApplication.translate("MainWindow", "IP Scanning", None, QtGui.QApplication.UnicodeUTF8))
        self.scanIPLocation.setText(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "   Press Scan to detect  location IP Address: ", None, QtGui.QApplication.UnicodeUTF8))
        self.IPLocation.setText(QtGui.QApplication.translate("MainWindow", "  Enter IP address : ", None, QtGui.QApplication.UnicodeUTF8))
        self.mainFram.setTabText(self.mainFram.indexOf(self.PC), QtGui.QApplication.translate("MainWindow", "  IP Location", None, QtGui.QApplication.UnicodeUTF8))
        self.traceButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Trace IP", None, QtGui.QApplication.UnicodeUTF8))
        self.traceButton.setText(QtGui.QApplication.translate("MainWindow", "Track", None, QtGui.QApplication.UnicodeUTF8))
        self.addressIPTrace.setText(QtGui.QApplication.translate("MainWindow", "Track IP , Host or webSite: ", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Press Track to Track IP , Host or webSite: ", None, QtGui.QApplication.UnicodeUTF8))
        self.mainFram.setTabText(self.mainFram.indexOf(self.Trace), QtGui.QApplication.translate("MainWindow", "Track ", None, QtGui.QApplication.UnicodeUTF8))
        self.upload.setToolTip(QtGui.QApplication.translate("MainWindow", "Upload File", None, QtGui.QApplication.UnicodeUTF8))
        self.upload.setText(QtGui.QApplication.translate("MainWindow", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseFileUpload.setToolTip(QtGui.QApplication.translate("MainWindow", "Choose your File", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseFileUpload.setText(QtGui.QApplication.translate("MainWindow", "Choose File For Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxFtp.setItemText(self.toolBoxFtp.indexOf(self.uploadFile), QtGui.QApplication.translate("MainWindow", "Upload file against Target", None, QtGui.QApplication.UnicodeUTF8))
        self.download.setToolTip(QtGui.QApplication.translate("MainWindow", "Download File", None, QtGui.QApplication.UnicodeUTF8))
        self.download.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLabel_4.setText(QtGui.QApplication.translate("MainWindow", "Enter location file name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxFtp.setItemText(self.toolBoxFtp.indexOf(self.downloadFile), QtGui.QApplication.translate("MainWindow", "Download file from Target", None, QtGui.QApplication.UnicodeUTF8))
        self.mainFram.setTabText(self.mainFram.indexOf(self.TransferFile), QtGui.QApplication.translate("MainWindow", "File Transfer", None, QtGui.QApplication.UnicodeUTF8))
        self.File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_IP_Scanning.setTitle(QtGui.QApplication.translate("MainWindow", "&IP Scanning", None, QtGui.QApplication.UnicodeUTF8))
        self.Transfer.setTitle(QtGui.QApplication.translate("MainWindow", "&Transfer", None, QtGui.QApplication.UnicodeUTF8))
        self.HelpMenu.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.Port_Scanning.setText(QtGui.QApplication.translate("MainWindow", "&Port Scanning", None, QtGui.QApplication.UnicodeUTF8))
        self.Port_Scanning.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.IP_Computer.setText(QtGui.QApplication.translate("MainWindow", "&Computer IP", None, QtGui.QApplication.UnicodeUTF8))
        self.IP_Computer.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.Exit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.Download.setText(QtGui.QApplication.translate("MainWindow", "&Download", None, QtGui.QApplication.UnicodeUTF8))
        self.Download.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.Upload.setText(QtGui.QApplication.translate("MainWindow", "&Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.Upload.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.Help.setText(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.Help.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.Contact.setText(QtGui.QApplication.translate("MainWindow", "&Contact", None, QtGui.QApplication.UnicodeUTF8))
        self.Contact.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRange_IP.setText(QtGui.QApplication.translate("MainWindow", "&Range IP", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRange_IP.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHost_Name.setText(QtGui.QApplication.translate("MainWindow", "&Host Name", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Trace.setText(QtGui.QApplication.translate("MainWindow", "&Trace", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Trace.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMy_IP_address.setText(QtGui.QApplication.translate("MainWindow", "My IP address", None, QtGui.QApplication.UnicodeUTF8))
