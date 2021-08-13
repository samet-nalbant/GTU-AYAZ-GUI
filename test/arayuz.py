# Bu arayüz, GTU AYAZ takımı tarafından teknofest yarışması için geliştirilmiştir.
from PyQt5 import QtCore, QtGui, QtWidgets
from dronekit import connect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import subprocess as sp
import sys
import glob

class flag:
    x =0
    arm = False
class Ui_StackedWidget(object):
    # Bu fonksiyon StackedWidget oluşturmak için gerekli diğer fonksiyonların çağrıldığı fonksiyondur.İçerisinde StackedWidget oluşturulur ve arayüz ve menü olmak üzere 2 ayrı sayfa açılır.
    def setupUi(self, StackedWidget): 
        StackedWidget.setObjectName("GTU AYAZ YER ISTASYONU")
        StackedWidget.resize(1920, 1080)
        self.setFixedSize(1920, 1080)
        self.menuOlustur(StackedWidget)
        self.panelOlustur()
        self.konumAyarla()
        self.pushButton.clicked.connect(self.baglan)
        StackedWidget.addWidget(self.arayuz)
        self.retranslateUi(StackedWidget)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)
    # Bu fonksiyounun içerisinde menü sayfası için gerekli objeler oluşturulmuştur.
    def menuOlustur(self,StackedWidget):
        self.menu = QtWidgets.QWidget()
        self.menu.setObjectName("menu")
        self.label = QtWidgets.QLabel(self.menu)
        self.label.setGeometry(QtCore.QRect(710, 299, 500, 500))
        self.label.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../source/ayazlogo.png"))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.menu)
        self.comboBox.setGeometry(QtCore.QRect(1620, 20, 101, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.menu)
        self.comboBox_2.setGeometry(QtCore.QRect(1740, 20, 101, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.menu)
        self.pushButton.setGeometry(QtCore.QRect(840, 730, 231, 81))
        self.pushButton.setStyleSheet("font: 75 25pt \"Purisa\";\n"
"font-weight: bold;")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.menu)
        self.label_2.setGeometry(QtCore.QRect(220, 870, 311, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../source/gtulogo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.menu)
        self.label_3.setGeometry(QtCore.QRect(1210, 790, 581, 331))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../source/huklogo.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.menu)
        self.label_4.setGeometry(QtCore.QRect(400, 110, 1081, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../source/ayaz.png"))
        self.label_4.setObjectName("label_4")
        self.listeDoldur()
        StackedWidget.addWidget(self.menu)
    # Bu fonksiyon menüde bulunan bağlantı hızı seçeneği ve bağlantı portu için gerekli olan listeleri doldurur. Aktif olan portları listelemek için ubuntu terminalinde ls/dev/tty*S olan koumutu subprocess kütüphanesinde bulunan getotput fonksiyonuyla elde edilip doldurulmuştur.
    def listeDoldur(self):
        output = sp.getoutput("ls /dev/ttyS*") # aktif olan port listesini döndürür.
        x = output.split("\n") # String halinde alınan portları parçalar.
        self.comboBox.addItems(x) # Elde edilen portları bağlantılar listesine ekler.
        output = sp.getoutput("ls /dev/ttyA*") # aktif olan port listesini döndürür.
        x = output.split("\n") # String halinde alınan portları parçalar.
        y = x[0].split(" ") # Elde edilen portları bağlantılar listesine ekler.
        if(len(y) <= 1):
            self.comboBox.addItems(x)
        self.comboBox_2.addItems(["2400","4800","9600","19200","38400","57600","11520"]) # bağlantı hızı seçeneklerini listeye ekler
        self.comboBox_2.setCurrentIndex(5)
    # Bu fonksiyonda uçuş göstergeleri için gerekli olan objeler oluşturulmuştur.
    def panelOlustur(self):
        self.arayuz = QtWidgets.QWidget()
        self.arayuz.setObjectName("arayuz")
        self.label_5 = QtWidgets.QLabel(self.arayuz)
        self.label_5.setGeometry(QtCore.QRect(579, 0, 761, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../source/ucus kontrol.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.arayuz = QtWidgets.QWidget()
        self.arayuz.setObjectName("arayuz")
        self.text = QtWidgets.QLabel(self.arayuz)
        self.text.setGeometry(QtCore.QRect(550, 15, 761, 81))
        self.text.setScaledContents(True)
        self.text.setText("")
        self.text.setPixmap(QtGui.QPixmap("../source/ucus kontrol.png"))
        self.text.setObjectName("text")
        self.irtifa = QtWidgets.QLabel(self.arayuz)
        self.irtifa.setGeometry(QtCore.QRect(220, 90, 400, 400))
        self.irtifa.setText("")
        self.irtifa.setPixmap(QtGui.QPixmap("../source/altitude.png"))
        self.irtifa.setObjectName("irtifa")
        self.hava_hizi = QtWidgets.QLabel(self.arayuz)
        self.hava_hizi.setGeometry(QtCore.QRect(690, 90, 400, 400))
        self.hava_hizi.setText("")
        self.hava_hizi.setPixmap(QtGui.QPixmap("../source/airspeed.png"))
        self.hava_hizi.setObjectName("hava_hizi")
        self.pusula = QtWidgets.QLabel(self.arayuz)
        self.pusula.setGeometry(QtCore.QRect(1160, 90, 400, 400))
        self.pusula.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.pusula.setText("")
        self.pusula.setPixmap(QtGui.QPixmap("../source/compass.png"))
        self.pusula.setObjectName("pusula")
        self.pusula.setAlignment(QtCore.Qt.AlignCenter)
        self.pusula_pixmap = QPixmap("../source/compass.png")
        self.donus_kor = QtWidgets.QLabel(self.arayuz)
        self.donus_kor.setGeometry(QtCore.QRect(220, 560, 400, 400))
        self.donus_kor.setText("")
        self.donus_kor.setPixmap(QtGui.QPixmap("../source/Turn CoordinatorOut.png"))
        self.donus_kor.setObjectName("donus_kor")
        self.dikey_hiz = QtWidgets.QLabel(self.arayuz)
        self.dikey_hiz.setGeometry(QtCore.QRect(690, 560, 400, 400))
        self.dikey_hiz.setText("")
        self.dikey_hiz.setPixmap(QtGui.QPixmap("../source/verticalspeed.png"))
        self.dikey_hiz.setObjectName("dikey_hiz")
        self.durum_dis = QtWidgets.QLabel(self.arayuz)
        self.durum_dis.setGeometry(QtCore.QRect(1090, 490, 540, 540))
        self.durum_dis.setStyleSheet("background-color: rgba(204, 0, 0, 0);\n"
"background-color: rgba(204, 0, 0, 0);")
        self.durum_dis.setText("")
        self.durum_dis.setPixmap(QtGui.QPixmap("../source/attitudeout2.png"))
        self.durum_dis.setObjectName("durum_dis")
        self.logo = QtWidgets.QLabel(self.arayuz)
        self.logo.setGeometry(QtCore.QRect(550, -30, 685, 151))
        self.logo.setStyleSheet("background-color: rgba(204, 0, 0, 0);\n"
"image: url(:/samet/text1.png);")
        self.logo.setText("")
        self.logo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logo.setObjectName("logo")
        self.irtifa_minOk = QtWidgets.QLabel(self.arayuz)
        self.irtifa_minOk.setGeometry(QtCore.QRect(220, 90, 400, 400))
        self.irtifa_minOk.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.irtifa_minOk.setText("")
        self.irtifa_minOk.setPixmap(QtGui.QPixmap("../source/shortarrow.png"))
        self.irtifa_minOk.setObjectName("irtifa_minOk")
        self.irtifa_minOk.setAlignment(QtCore.Qt.AlignCenter)
        self.mini_arr_pixmap = QPixmap("../source/shortarrow.png")
        self.irtifa_ok = QtWidgets.QLabel(self.arayuz)
        self.irtifa_ok.setGeometry(QtCore.QRect(220, 90, 400, 400))
        self.irtifa_ok.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.irtifa_ok.setText("")
        self.irtifa_ok.setPixmap(QtGui.QPixmap("../source/arrow.png"))
        self.irtifa_ok.setObjectName("irtifa_ok")
        self.irtifa_ok.setAlignment(QtCore.Qt.AlignCenter) 
        self.arr_pixmap = QPixmap("../source/arrow.png")        
        self.hava_hizi_ok = QtWidgets.QLabel(self.arayuz)
        self.hava_hizi_ok.setGeometry(QtCore.QRect(690, 90, 400, 400))
        self.hava_hizi_ok.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.hava_hizi_ok.setText("")
        self.hava_hizi_ok.setPixmap(QtGui.QPixmap("../source/arrow.png"))
        self.hava_hizi_ok.setObjectName("hava_hizi_ok")
        self.hava_hizi_ok.setAlignment(QtCore.Qt.AlignCenter) 
        self.hava_hizi_pixmap = QPixmap("../source/arrow.png") 
        self.pusula_gostergeci = QtWidgets.QLabel(self.arayuz)
        self.pusula_gostergeci.setGeometry(QtCore.QRect(1160, 90, 400, 400))
        self.pusula_gostergeci.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.pusula_gostergeci.setText("")
        self.pusula_gostergeci.setPixmap(QtGui.QPixmap("../source/compassindicator.png"))
        self.pusula_gostergeci.setObjectName("pusula_gostergeci")
        self.ucak = QtWidgets.QLabel(self.arayuz)
        self.ucak.setGeometry(QtCore.QRect(220, 560, 400, 400))
        self.ucak.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.ucak.setText("")
        self.ucak.setPixmap(QtGui.QPixmap("../source/Turn CoordinatorPlane.png"))
        self.ucak.setObjectName("ucak")
        self.ucak.setAlignment(QtCore.Qt.AlignCenter) 
        self.ucak_pixmap = QPixmap("../source/Turn CoordinatorPlane.png")
        self.donus_imleci = QtWidgets.QLabel(self.arayuz)
        self.donus_imleci.setGeometry(QtCore.QRect(220, 619, 400, 400))
        self.donus_imleci.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.donus_imleci.setText("")
        self.donus_imleci.setPixmap(QtGui.QPixmap("../source/Turn CoordinatorDot.png"))
        self.donus_imleci.setObjectName("donus_imleci")
        self.dikey_hiz_ok = QtWidgets.QLabel(self.arayuz)
        self.dikey_hiz_ok.setGeometry(QtCore.QRect(690, 560, 400, 400))
        self.dikey_hiz_ok.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.dikey_hiz_ok.setText("")
        self.dikey_hiz_ok.setPixmap(QtGui.QPixmap("../source/arrow.png"))
        self.dikey_hiz_ok.setObjectName("dikey_hiz_ok")
        self.dikey_hiz_ok.setAlignment(QtCore.Qt.AlignCenter)
        self.dikey_hiz_pixmap = QPixmap("../source/arrow.png")
        self.aci = QtWidgets.QLabel(self.arayuz)
        self.aci.setGeometry(QtCore.QRect(1160, 560, 400, 400))
        self.aci.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.aci.setText("")
        self.aci.setPixmap(QtGui.QPixmap("../source/bank angle.png"))
        self.aci.setObjectName("aci")
        self.aci.setAlignment(QtCore.Qt.AlignCenter) 
        self.aci_pixmap = QPixmap("../source/bank angle.png")
        self.yesil_mavi_alan = QtWidgets.QLabel(self.arayuz)
        self.yesil_mavi_alan.setGeometry(QtCore.QRect(358, -240, 2000, 2000))
        self.yesil_mavi_alan.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.yesil_mavi_alan.setText("")
        self.yesil_mavi_alan.setPixmap(QtGui.QPixmap("../source/attitude indicatoryesildogru.png"))
        self.yesil_mavi_alan.setObjectName("yesil_mavi_alan")
        self.yesil_mavi_alan.raise_()
        self.yesil_pixmap = QPixmap("../source/attitude indicatoryesildogru.png")
        self.yesil_mavi_alan.setAlignment(QtCore.Qt.AlignCenter)
        self.arkaplan = QtWidgets.QLabel(self.arayuz)
        self.arkaplan.setGeometry(QtCore.QRect(-70, -410, 2000, 2000))
        self.arkaplan.setStyleSheet("background-color: rgba(204, 0, 0, 0);")
        self.arkaplan.setText("")
        self.arkaplan.setPixmap(QtGui.QPixmap("../source/arkablanBBB.png"))
        self.arkaplan.setObjectName("arkaplan")
        self.moddurum = QtWidgets.QLabel(self.arayuz)
        self.moddurum.setGeometry(QtCore.QRect(80, 10, 121, 41))
        self.moddurum.setObjectName("moddurum")
        self.mod = QtWidgets.QLabel(self.arayuz)
        self.mod.setGeometry(QtCore.QRect(10, 10, 71, 41))
        self.mod.setObjectName("mod")
        self.arm = QtWidgets.QLabel(self.arayuz)
        self.arm.setGeometry(QtCore.QRect(10, 50, 71, 41))
        self.arm.setObjectName("arm")
        self.armdurum = QtWidgets.QLabel(self.arayuz)
        self.armdurum.setGeometry(QtCore.QRect(80, 50, 141, 41))
        self.armdurum.setObjectName("armdurum")
    # Bu fonksiyonda uçuş gösterge resimlerinin katmanları ayarlanmıştır.
    def konumAyarla(self):
        self.yesil_mavi_alan.raise_()
        self.arkaplan.raise_()
        self.hava_hizi.raise_()
        self.irtifa.raise_()
        self.text.raise_()
        self.irtifa_ok.raise_()
        self.pusula.raise_()
        self.donus_kor.raise_()
        self.dikey_hiz.raise_()
        self.durum_dis.raise_()
        self.logo.raise_()
        self.irtifa_minOk.raise_()
        self.hava_hizi_ok.raise_()
        self.pusula_gostergeci.raise_()
        self.ucak.raise_()
        self.donus_imleci.raise_()
        self.dikey_hiz_ok.raise_()
        self.aci.raise_()
        self.moddurum.raise_()
        self.mod.raise_()
        self.arm.raise_()
        self.armdurum.raise_()
    # Bu fonksiyon bağlan butonuna tıklandığında çalıştırılır ve Dronekit kütüphanesinde bulunan connect fonksiyonu kullanılarak ihayla bağlantı kurur. Bağlantı kurulursa uçuş göstergelerinin bulunduğu sayfaya geçilirken, bağlantı kurulamadığı takdirde hata mesajı ekrana gelir. 
    def baglan(self):
        kontrol = 0
        try:
            self.iha=connect(self.comboBox.currentText(), wait_ready=True ,baud = int(self.comboBox_2.currentText()))
        except:
            kontrol = 1
            hata_dialog = QtWidgets.QErrorMessage()
            hata_dialog.showMessage('Connection Failed!')
            hata_dialog.exec()
        if kontrol != 1:
            flag.x = 1
            StackedWidget.setCurrentIndex(self,1)
    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        self.moddurum.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.mod.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-weight:600;\">MOD:</span></p></body></html>"))
        self.arm.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-weight:600;\">ARM:</span></p></body></html>"))
        self.armdurum.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        StackedWidget.setWindowTitle(_translate("GTU AYAZ YER ISTASYONU", "GTU AYAZ YER ISTASYONU"))
        self.pushButton.setText(_translate("StackedWidget", "BAGLAN"))

class StackedWidget(QStackedWidget,Ui_StackedWidget):
    def __init__(self, parent=None):
        super(StackedWidget, self).__init__(parent)
        self.setupUi(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.verileriGuncelle)
        timer.start(1)
        time.sleep(0.5)
        self.verileriGuncelle()
    # Bu fonksiyonda iha ile bağlantı kurulduğu takdirde ihadan sürekli veri akışı sağlanır. Elde edilen verilerle göstergeler hareket kazanır.
    def verileriGuncelle(self):
        if(flag.x != 0):
            pusula = self.iha.heading # ihanın yönünü tutar.
            havahizi = self.iha.airspeed # ihanın hava hızını tutar.
            pixmap_rotated = self.pusula_pixmap.transformed(QTransform().rotate(-pusula),QtCore.Qt.SmoothTransformation) # verilen aci değerine göre resmi döndürür.
            self.pusula.setPixmap(pixmap_rotated) # döndürülen resmi ilgili etikete atar.
            if havahizi > 60:
                havahizi = 60
            pixmap_rotated = self.hava_hizi_pixmap.transformed(QTransform().rotate(havahizi*4.5),QtCore.Qt.SmoothTransformation) # verilen aci değerine göre resmi döndürür.
            self.hava_hizi_ok.setPixmap(pixmap_rotated) # döndürülen resmi ilgili etikete atar.
            yukseklik = self.iha.location.global_relative_frame.alt # ihanın irtifa değerini tutar
            if yukseklik < 0:
                yukseklik = 0
            pixmap_rotated = self.arr_pixmap.transformed(QTransform().rotate(3.6*yukseklik+135),QtCore.Qt.SmoothTransformation) # verilen aci değerine göre resmi döndürür.
            self.irtifa_ok.setPixmap(pixmap_rotated) # döndürülen resmi ilgili etikete atar.
            pixmap_rotated =  self.mini_arr_pixmap.transformed(QTransform().rotate((3.6*yukseklik)/10+90),QtCore.Qt.SmoothTransformation) # verilen aci değerine göre resmi döndürür.
            self.irtifa_minOk.setPixmap(pixmap_rotated) # döndürülen resmi ilgili etikete atar.
            dikeyhiz = -(self.iha.velocity[2]) # ihanın dikey hızı tutar
            if(dikeyhiz > 10):
                dikeyhiz = 10
            elif(dikeyhiz < -10):
                dikeyhiz = -10
            pixmap_rotated = self.dikey_hiz_pixmap.transformed(QTransform().rotate(45+dikeyhiz*15),QtCore.Qt.SmoothTransformation) # verilen aci değerine göre resmi döndürür.
            self.dikey_hiz_ok.setPixmap(pixmap_rotated) # döndürülen resmi ilgili etikete atar.
            kanatdurumu = self.iha.attitude.roll # ihanın kanat durumunu tutar
            burundurumu = self.iha.attitude.pitch # ihanın burnunun durumunu tutar
            pixmap_rotated = self.aci_pixmap.transformed(QTransform().rotate(kanatdurumu*60),QtCore.Qt.SmoothTransformation) # verilen aci değerine göre resmi döndürür.
            self.aci.setPixmap(pixmap_rotated) # döndürülen resmi ilgili etikete atar.
            pixmap_rotated = self.yesil_pixmap.transformed(QTransform().rotate(kanatdurumu*60),QtCore.Qt.SmoothTransformation) # verilen aci değerine göre resmi döndürür.
            self.yesil_mavi_alan.setPixmap(pixmap_rotated) # döndürülen resmi ilgili etikete atar.
            self.yesil_mavi_alan.setGeometry(QtCore.QRect(358, -240+int((burundurumu*240)), 2000, 2000))
            pixmap_rotated = self.ucak_pixmap.transformed(QTransform().rotate(kanatdurumu*8),QtCore.Qt.SmoothTransformation) # verilen aci değerine göre resmi döndürür.
            self.ucak.setPixmap(pixmap_rotated) # döndürülen resmi ilgili etikete atar.
            donus = self.iha.velocity[1]
            if(donus> 1):
                if(kanatdurumu > 0):
                    self.donus_imleci.setGeometry(QtCore.QRect(220+int((self.iha.velocity[1]))+5, 619, 400, 400))
                elif(kanatdurumu == 0):
                    self.donus_imleci.setGeometry(QtCore.QRect(220, 619, 400, 400))
                else:
                    self.donus_imleci.setGeometry(QtCore.QRect(220-(int(self.iha.velocity[1]))+5, 619, 400, 400))
            else:
                self.donus_imleci.setGeometry(QtCore.QRect(220, 619, 400, 400))
            if(self.iha.armed): # ihanın arm olup olmadığını kontrol eder.
                self.armdurum.setText("Arm oldu.")
            else:
                self.armdurum.setText("Arm olmadı.")
            self.armdurum.setFont(QFont('Arial', 15))
            self.moddurum.setText(self.iha.mode.name) # ihanın modunu gösterir.
            self.moddurum.setFont(QFont('Arial', 15))
            flag.mod = self.iha.mode.name
            flag.arm = self.iha.armed

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stackedWidget = StackedWidget()
    stackedWidget.show()
    sys.exit(app.exec_())
