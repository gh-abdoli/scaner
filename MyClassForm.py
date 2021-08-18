import sys, re
import os
from PyQt4 import QtCore, QtGui
from gui import *
from Location import *

import socket

listPortHigh = []
listPortLow = []

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent = None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(parent)
    self.initGui()

  def initGui(self):
    self.connect(self.ui.chooseFileUpload, QtCore.SIGNAL("clicked()"), self.fileDialogUpload )
    self.connect(self.ui.scanIPLocation, QtCore.SIGNAL("clicked()"), self.locate )
    self.connect(self.ui.scanIP2, QtCore.SIGNAL("clicked()"), self.ipHostName)
    self.connect(self.ui.scanPort, QtCore.SIGNAL("clicked()"), self.portScaner)
    self.connect(self.ui.scanIp1, QtCore.SIGNAL("clicked()"), self.ipScanner)
    self.connect(self.ui.download, QtCore.SIGNAL("clicked()"), self.download)
    self.connect(self.ui.upload, QtCore.SIGNAL("clicked()"), self.upload)
    self.connect(self.ui.traceButton, QtCore.SIGNAL("clicked()"), self.trace)
    self.connect(self.ui.Exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
    self.connect(self.ui.scanPCIP, QtCore.SIGNAL("clicked()"), self.myIP)
    

  def exit(self):
    sys.exit()

  def locate(self):
    
    Form = QtGui.QMainWindow()
    locate = Map()
    locate.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
       
       

  def getIP(self):

    ip = self.ui.IPLocation.text()    
    host = ''
    
    return None   
    

  def fileDialogUpload(self):
    fd = QtGui.QFileDialog(self)
    plik = fd.getOpenFileName()
    self.ui.chooseFileUpload.setText(plik)
 
 
  def ScanHigh(self, TargetIP, start, end):

    #global listPortHigh = []
        
    for i in range(start, end):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = s.connect_ex((TargetIP, i))

      if(result == 0):
        listPortHigh.append(result)
      
      s.close()
      
    return listPortHigh

  def ScanLow(self, TargetIP, start, end):

    #global listPortLow = []

    for i in range(start, end):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = s.connect_ex((TargetIP, i))

      if(result == 0):
        
        listPortLow.append(result)
        
      s.close()
      
    return listPortLow
     
      
  def portScaner(self):

    import threading

    listPort = []

    IP = self.ui.IP_PortScaner.text()
    #IP = '127.0.0.1'
    startPort = int(self.ui.startPort.text())
    endPort = int(self.ui.endPort.text())

    mid = int((startPort + endPort) / 2)

    #self.ui.table.clear()

    threading.Thread(target = self.ScanLow, args=(IP, startPort, mid)).start()
    threading.Thread(target = self.ScanHigh, args=(IP, mid + 1, endPort)).start()

    listPort = listPortLow + listPortHigh

    for row in range(startPort, endPort):
      item = QtGui.QTableWidgetItem()
      if row in listPort:
        self.ui.table.setItem(row, ' OPEN ', item)
      else:
        self.ui.table.setItem(row, ' CLOSED ', item)

    
  def closeEvent(self, event):
    reply = QtGui.QMessageBox.question(self, 'Message',
                                       "Are you sure to quit?", QtGui.QMessageBox.Yes,
                                       QtGui.QMessageBox.No)
    if reply == QtGui.QMessageBox.Yes:
      event.accept()
    else:
      event.ignore()

  def ipScanner(self):

    startIP = self.ui.startLineEditIP.text()
    endIP = self.ui.endLineEditIP.text()

    ipRange = []

    for i in range(int(startIP.split('.')[0]), int(endIP.split('.')[0])):
      for j in range(int(startIP.split('.')[1]), int(endIP.split('.')[1])):
        for x in range(int(startIP.split('.')[2]), int(endIP.split('.')[2])):
          for y in range(int(startIP.split('.')[3]), int(endIP.split('.')[3])):
            ipRange.append(str(i)+ ''.join('.') + str(j) + ''.join('.') + str(x)+ ''.join('.') + str(y))

    try:
      for i in ipRange:
        file = os.popen('ping ' + i)
        line = file.read()
        match = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',line)
        ipText = match.group(0)
        f.close()
      return ipText
    except :
      print("Err in GetIP Func: not found")

  def ipHostName(self):

    
      hostName = self.ui.hostName.text()
      ip = socket.gethostbyname(hostName)
      if ip == None :
        reply = QtGui.QMessageBox.question(self, 'Error Message',
                                           "Invalid Host Name...?" + "\n Do you have work? ", QtGui.QMessageBox.Yes,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
          event.accept()
        else:
          event.ignore()
      else:
        pass

  def download(self):

    import urllib.request

    url = self.ui.addressFile.text()
    webFile = urllib.request.urlopen(url)
    localFile = open(os.path.split()[-1], 'wb')
    #os.system('wget %s -a log.log' % url)
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()

  def upload(self):

    import ftplib

    path = self.ui.chooseFileUpload.text()
    
    for root, dirs, files in os.walk(path):
      for fname in files:
        full_fname = os.path.join(root, fname)
        ftplib.FTP.storebinary('STOR remote/dir' + fname, open(full_fname, 'rb'))

    

  def trace(self):

    import urllib.request
    import urllib.parse

    addressIP = self.ui.addressIPTrace.text()
    #method is 'post'
    params = urllib.parse.urlencode({"QRY" : addressIP})
    params = params.encode('utf-8')
    f = urllib.request.urlopen('http://www.ip-adress.com/ip_tracer/' , params)
    localFile = open(os.path.split()[-1], 'wb')
    localFile.write(f.read().decode('utf-8') )
    f.close()
    localFile.close()

    return

  def myIP(self):

    ip = socket.gethostbyname(socket.gethostname())
    self.ui.myIPLineEdit.setText(ip)
  
    
    
      

  
