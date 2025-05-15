
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QProgressBar, QListWidget, QRadioButton, QButtonGroup
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap


# Kullanıcı verileri
user_data = []

# Karakterler
characters = ["McQueen", "Mater", "Sally", "Guido", "Finn McRocket", "Storm", "Hudson Hornet", "Chick", "Luigi", "Franchesco" , "Holly", "Cruz Ramirez"]



# Kullanıcı seçimleri
karakter_puanları = {char: 0 for char in characters}

def karakter_belirle():
    """En yüksek puana sahip karakteri belirleme"""
    return max(karakter_puanları, key=karakter_puanları.get)

# Giriş Ekranı
class Girisekranı(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QMainWindow {background-image: url('images/radiator_springs.jpeg'); background-repeat: no-repeat; background-position: center; background-size: contain;}")
        self.setWindowTitle("Disney Cars Test")
        self.setGeometry(200, 200, 400, 300)

        logo = QPixmap("images/logo.png") 

        self.label = QLabel("HANGİ DISNEY CARS KARAKTERİSİN\nÖĞRENMEK İÇİN İSMİNİ GİR!")
        self.label.setStyleSheet("font-size: 20px; font-weight: bold; color: black; font-family:'Impact';")
        self.label.setAlignment(Qt.AlignCenter)
        self.input_name = QLineEdit()
        self.basla_button = QPushButton("Teste Başla")
        self.cikis_button = QPushButton("Çıkış")
        
        self.basla_button.clicked.connect(self.teste_basla)
        self.cikis_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_name)
        layout.addWidget(self.basla_button)
        layout.addWidget(self.cikis_button)
        
        container = QWidget()
        
       

        container.setLayout(layout)
        self.setCentralWidget(container)

    def teste_basla(self):
        global kullanici_isim
        kullanici_isim = self.input_name.text()
        if kullanici_isim:
            self.test_ekrani = TestEkrani()
            self.test_ekrani.show()
            self.close()
            

# Test Soruları Ekranı
class TestEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #B0C4DE;")

        for char in karakter_puanları:
            karakter_puanları[char] = 0


        self.setWindowTitle("Test Ekranı")
        self.setGeometry(200, 200, 600, 400)
        
        #soru1
        self.label = QLabel("1) En sevdiğin renk?")
        self.label.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        self.birinci_grup = QButtonGroup()
        self.red_button = QRadioButton("Kırmızı")
        self.brown_button = QRadioButton("Kahverengi")
        self.blue_button = QRadioButton("Mavi")
        self.black_button = QRadioButton("Siyah")
        self.green_button = QRadioButton("Yeşil")
        self.yellow_button = QRadioButton("Sarı")
        self.purple_button = QRadioButton("Mor")
        
        self.birinci_grup.addButton(self.red_button)
        self.birinci_grup.addButton(self.brown_button)
        self.birinci_grup.addButton(self.blue_button)
        self.birinci_grup.addButton(self.black_button)
        self.birinci_grup.addButton(self.green_button)
        self.birinci_grup.addButton(self.yellow_button)
        self.birinci_grup.addButton(self.purple_button)
        
        #soru2
        self.label2 = QLabel("2) Favori Cars serin hangisi?")
        self.label2.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.ikinci_grup = QButtonGroup()
        self.cars1_button = QRadioButton("Cars 1")
        self.cars2_button = QRadioButton("Cars 2")
        self.cars3_button = QRadioButton("Cars 3")
        
        self.ikinci_grup.addButton(self.cars1_button)
        self.ikinci_grup.addButton(self.cars2_button)
        self.ikinci_grup.addButton(self.cars3_button)
        
        #soru3
        self.label3 = QLabel("3) Yarışa girsen hangi stratejiyi kullanırsın?")
        self.label3.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.ucuncu_grup = QButtonGroup()
        self.hizli_cikis = QRadioButton("Hızlı başlarım, liderliği alırım.")
        self.yavas_cikis = QRadioButton("Yavaş başlarım, sonradan hızlanırım.")
        self.tuzak_hareket = QRadioButton("Rakipleri kandırırım, akıllıca hareket ederim.")
        self.riskli_hamle = QRadioButton("Riske girerim, en çılgın hamleleri yaparım!")
        self.dikkatli_surus = QRadioButton("Dikkatli sürerim, hata yapmamaya çalışırım.")
        
        self.ucuncu_grup.addButton(self.hizli_cikis)
        self.ucuncu_grup.addButton(self.yavas_cikis)
        self.ucuncu_grup.addButton(self.tuzak_hareket)
        self.ucuncu_grup.addButton(self.riskli_hamle)
        self.ucuncu_grup.addButton(self.dikkatli_surus)

        #soru4
        self.label4= QLabel("4) Yarış esnasında biri seni geçerse ne yaparsın?")
        self.label4.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.dorduncu_grup= QButtonGroup()
        self.karsi_atak =QRadioButton("Hemen karşı atağa geçerim")
        self.sakin= QRadioButton("Sakin kalırım, son turda geçerim hepsini zaten")
        self.analiz= QRadioButton("Rakibimi analiz ederim, planlama yaparım ")
        self.ofke= QRadioButton("Öfkelenirim, onları geçmek için elimden geleni yaparım")
        self.umutsuzluk= QRadioButton("Umutsuzluğa kapılırım, kaybettiğimi hissederim")

        self.dorduncu_grup.addButton(self.karsi_atak)
        self.dorduncu_grup.addButton(self.sakin)
        self.dorduncu_grup.addButton(self.analiz)
        self.dorduncu_grup.addButton(self.ofke)
        self.dorduncu_grup.addButton(self.umutsuzluk)

        #soru5 
        self.label5=QLabel("5) Son olarak, Yarışı kaybettin ne yaparsın?")
        self.label5.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.besinci_grup=QButtonGroup()
        self.tekrar=QRadioButton("Pes etmem bir sonraki yarışı ben kazanacağım")
        self.pes=QRadioButton("Vazgeçerim. Demek ki benlik bir şey değilmiş")
        self.analiz2=QRadioButton( "Hatalarımı analiz ederim")
        self.kibir=QRadioButton("Muhtemelen bir başkası benim kaybetmeme sebep oldu. Ben hata yapmam")
        self.normal=QRadioButton("Normal karşılarım. Alt tarafı bir yarış, önemi yok")

        
        
    


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.red_button)
        layout.addWidget(self.brown_button)
        layout.addWidget(self.blue_button)
        layout.addWidget(self.black_button)
        layout.addWidget(self.green_button)
        layout.addWidget(self.yellow_button)
        layout.addWidget(self.purple_button)

        layout.addWidget(self.label2)
        layout.addWidget(self.cars1_button)
        layout.addWidget(self.cars2_button)
        layout.addWidget(self.cars3_button)

        layout.addWidget(self.label3)
        layout.addWidget(self.hizli_cikis)
        layout.addWidget(self.yavas_cikis)
        layout.addWidget(self.tuzak_hareket)
        layout.addWidget(self.riskli_hamle)
        layout.addWidget(self.dikkatli_surus)

        layout.addWidget(self.label4)
        layout.addWidget(self.karsi_atak)
        layout.addWidget(self.sakin)
        layout.addWidget(self.analiz)
        layout.addWidget(self.ofke)
        layout.addWidget(self.umutsuzluk)

        layout.addWidget(self.label5)
        layout.addWidget(self.tekrar)
        layout.addWidget(self.pes)
        layout.addWidget(self.analiz2)
        layout.addWidget(self.kibir)
        layout.addWidget(self.normal)



        
        self.next_button = QPushButton("Sonucunu Gör")
        self.next_button.clicked.connect(self.show_progress)
        layout.addWidget(self.next_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        
    def show_progress(self):

        if self.red_button.isChecked():
            karakter_puanları["McQueen"] += 1
            karakter_puanları["Franchesco"] += 1
        elif self.brown_button.isChecked():
            karakter_puanları["Mater"] += 1
        elif self.blue_button.isChecked():
            karakter_puanları["Sally"] += 1
            karakter_puanları["Guido"] += 1
            karakter_puanları["Hudson Hornet"] +=1
            karakter_puanları["Finn McRocket"] +=1
        elif self.black_button.isChecked():
            karakter_puanları["Storm"] += 1
        elif self.green_button.isChecked():
            karakter_puanları["Chick"] += 1
        elif self.yellow_button.isChecked():
            karakter_puanları["Luigi"] += 1
            karakter_puanları["Cruz Ramirez"] += 1
        elif self.purple_button.isChecked():
            karakter_puanları["Holly"] += 1 

        if self.cars1_button.isChecked():
            for char in ["McQueen", "Mater", "Sally", "Guido", "Hudson Hornet", "Chick"]:
                karakter_puanları[char] += 1
        elif self.cars2_button.isChecked():
            for char in ["Finn McRocket", "Franchesco", "Holly"]:
                karakter_puanları[char] += 1
        elif self.cars3_button.isChecked():
            for char in ["Storm", "Hudson Hornet","Cruz Ramirez"]:
                karakter_puanları[char] += 1


        if self.hizli_cikis.isChecked():
            karakter_puanları["McQueen"] += 1
            karakter_puanları["Franchesco"] += 1
        elif self.yavas_cikis.isChecked():
            karakter_puanları["Hudson Hornet"] += 1
            karakter_puanları["Guido"] += 1
        elif self.tuzak_hareket.isChecked():
            karakter_puanları["Chick"] += 1
            karakter_puanları["Finn McRocket"] += 1
        elif self.riskli_hamle.isChecked():
            karakter_puanları["Mater"] += 1
            karakter_puanları["Storm"] += 1
            karakter_puanları["Cruz Ramirez"] +=1
        elif self.dikkatli_surus.isChecked():
            karakter_puanları["Sally"] += 1
            karakter_puanları["Luigi"] += 1
            karakter_puanları["Holly"] += 1


        if self.karsi_atak.isChecked():
            karakter_puanları["Franchesco"] += 1
            karakter_puanları["Mater"] += 1
            karakter_puanları["Cruz Ramirez"] += 1
        elif self.sakin.isChecked(): 
            karakter_puanları["Hudson Hornet"] += 1
            karakter_puanları["McQueen"] += 1
            karakter_puanları["Guido"]   += 1
        elif self.analiz.isChecked():  
            karakter_puanları["Sally"] += 1
            karakter_puanları["Finn McRocket"] += 1
            karakter_puanları["Holly"]  += 1
        elif self.ofke.isChecked():  
            karakter_puanları["Chick"] += 1
            karakter_puanları["Storm"] += 1
        elif self.umutsuzluk.isChecked():
            karakter_puanları["Luigi"]  += 1


        if self.tekrar.isChecked():
            karakter_puanları["McQueen"] +=1
            karakter_puanları["Cruz Ramirez"] += 1
        elif self.pes.isChecked(): 
            karakter_puanları["Mater"] +=1
            karakter_puanları["Luigi"] +=1
        elif self.analiz2.isChecked():
            karakter_puanları["Sally"] +=1
            karakter_puanları["Holly"] +=1
            karakter_puanları["Finn McRocket"] +=1
            karakter_puanları["Hudson Hornet"] +=1
        elif self.kibir.isChecked():
            karakter_puanları["Storm"] +=1
            karakter_puanları["Chick"] +=1
            karakter_puanları["Franchesco"] +=1
        elif self.normal.isChecked():
            karakter_puanları["Guido"] +=1  
        
       
     
       



        self.progress_screen = ProgressScreen()
        self.progress_screen.show()
        self.close()

# Yüklenme Ekranı
class ProgressScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sonuçlar Yükleniyor...")
        self.setGeometry(200, 200, 400, 200)
        
        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, 50, 300, 30)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        self.timer.start(100)
        
        layout = QVBoxLayout()
        layout.addWidget(self.progress)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 10
            self.progress.setValue(self.progress_value)
        else:
            self.timer.stop()
            self.result_screen = ResultScreen()
            self.result_screen.show()
            self.close()

# Sonuç Ekranı
class ResultScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sonuç Ekranı")
        self.setGeometry(200, 200, 450, 450)
        
        character = karakter_belirle()
        user_data.append((kullanici_isim, character))
        
        self.result_label = QLabel(f"Senin karakterin: {character}!")
        self.result_label.setStyleSheet("font-family: 'Impact'; font-size: 20px;")
        self.result_label.setAlignment(Qt.AlignCenter)

        image_map = {
            "McQueen":       "images/mcqueen.png",
            "Mater":         "images/mater.png",
            "Sally":         "images/sally2.png",
            "Guido":         "images/guido.webp",
            "Finn McRocket": "images/finn.png",
            "Storm":         "images/storm.png",
            "Hudson Hornet": "images/hudson.png",
            "Chick":         "images/chick.png",
            "Luigi":         "images/luigi.png",
            "Franchesco":    "images/francesco.png",
            "Holly":         "images/holly.webp",
            "Cruz Ramirez":  "images/cruz.png",
        }


        pic = QLabel()
        pix = QPixmap(image_map[character])
        pic.setPixmap(pix.scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        pic.setAlignment(Qt.AlignCenter)


        prompt_map = { "McQueen":       "Senin ruhun pistlerde parlayan bir yıldız gibi – liderlik senin işin, hıza tutkun ve asla pes etmiyorsun.",
        "Mater":         "Senin içtenliğin ve sadeliğin etrafındakilere güven verir; arkadaş canlısı yapınla herkesin yol arkadaşısın.",
        "Sally":         "Zarafet ve soğukkanlılık sende birleşiyor; ne olursa olsun dengeni korur, her virajı ustalıkla alırsın.",
        "Guido":         "Çevikliğin ve pratik zekânla her durumu avantaja çevirirsin; hız ve becerikliliğinle pistin yıldızı olursun.",
        "Finn McRocket": "Merhametli bir lider ruhsun; zorluklar karşısında soğukkanlı kalır, ekip arkadaşlarını korur ve her zaman doğru olanı yaparsın.",
        "Storm":         "Doğanın gücünü andıran kararlılığın var; engeller seni yıldırmaz, fırtına gibi yoluna devam edersin.",
        "Hudson Hornet": "Deneyimin ve stratejinin bir araya geldiği nadir bir ruhsun; geçmişin dersleriyle geleceği fethediyorsun.",
        "Chick":         "Gözü pekliğin ve cesaretinle dikkat çekiyorsun; risk almayı seversin, yarışın heyecanı senin kanında var.",
        "Luigi":         "Neşen, pozitif enerjin ve yardımseverliğinle ortamı aydınlatıyorsun; yanındakilere her zaman moral verirsin.",
        "Franchesco":    "Keskin stratejilerin ve soğukkanlı hamlelerinle rakipsizsin; her yarışı planlı adımlarla domine edersin.",
        "Holly":         "İçindeki incelik ve zarafet her hareketine yansır; sakin duruşunla bile ilgi odağı olmayı başarıyorsun.",
        "Cruz Ramirez":  "Azmin ve hırsın senin en büyük gücün; her zorluğu fırsata çevirir, sonunda hep zirvede sen olursun.",
}
        
        lbl_prompt = QLabel(prompt_map[character])
        lbl_prompt.setWordWrap(True)
        lbl_prompt.setAlignment(Qt.AlignCenter)
        lbl_prompt.setStyleSheet("font-style: italic; color: gray;")

        
        self.back_button = QPushButton("Geri Dön")
        self.back_button.clicked.connect(self.go_back)
        
        self.view_results_button = QPushButton("Diğer Sonuçları Gör")
        self.view_results_button.clicked.connect(self.show_results)
        
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addWidget(pic)
        layout.addWidget(lbl_prompt)    
        layout.addWidget(self.back_button)
        layout.addWidget(self.view_results_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def go_back(self):
        self.welcome_screen = Girisekranı()
        self.welcome_screen.show()
        self.close()
    
    def show_results(self):
        self.results_screen = ResultsScreen()
        self.results_screen.show()
        self.close()

# Sonuçları Listeleyen Ekran
class ResultsScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sonuçlar")
        self.setGeometry(200, 200, 400, 400)
        
        self.results_list = QListWidget()
        for name, character in user_data:
            self.results_list.addItem(f"{name} - {character}")
        
        self.back_button = QPushButton("Geri Dön")
        self.back_button.clicked.connect(self.go_back)
        
        self.cikis_button = QPushButton("Çıkış")
        self.cikis_button.clicked.connect(self.close)

        self.clear_results_button = QPushButton("Temizle")
        self.clear_results_button.clicked.connect(self.clear_results)
        
        layout = QVBoxLayout()
        layout.addWidget(self.results_list)
        layout.addWidget(self.back_button)
        layout.addWidget(self.cikis_button)
        layout.addWidget(self.clear_results_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
        
    def go_back(self):
        self.welcome_screen = Girisekranı()
        self.welcome_screen.show()
        self.close()
    
    def clear_results(self):
         user_data.clear()
         self.results_list.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Girisekranı()
    window.show()
    sys.exit(app.exec_())