

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QInputDialog
import D_Applicazione
import D_Mixer
import cv2
import glob
import os
import numpy as np

class Ui_MainWindow(object):

    # METODO PER SALVARE IL PERCORSO DEL DATASET
    def salvaDataset (self, pathDataset):
        self.pathDataset = pathDataset

    def salvaNumeroFoto (self, numFoto):
        self.numFoto = numFoto
        print(self.numFoto)

    def setupUi(self, MainWindow):

        # SET DELLA FINESTRA PRINCIPALE DEL PROGRAMMA
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 788)
        MainWindow.setStyleSheet("background-color: rgb(144, 200, 160);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # SET DELLA GROUPBOX RIFERITA AL CONFRONTO TRAMITE TECNICHE
        self.groupBox_confronto = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_confronto.setGeometry(QtCore.QRect(20, 20, 1081, 391))
        font = QtGui.QFont()
        font.setFamily("OpineHeavy")
        font.setPointSize(18)
        self.groupBox_confronto.setFont(font)
        self.groupBox_confronto.setAutoFillBackground(False)
        self.groupBox_confronto.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox_confronto.setFlat(True)
        self.groupBox_confronto.setCheckable(False)
        self.groupBox_confronto.setChecked(False)
        self.groupBox_confronto.setObjectName("groupBox_confronto")
        self.groupBox_confrontoInput = QtWidgets.QGroupBox(self.groupBox_confronto)
        self.groupBox_confrontoInput.setGeometry(QtCore.QRect(360, 70, 341, 311))
        font = QtGui.QFont()
        font.setFamily("OpineHeavy")
        font.setPointSize(11)
        self.groupBox_confrontoInput.setFont(font)
        self.groupBox_confrontoInput.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox_confrontoInput.setFlat(True)
        self.groupBox_confrontoInput.setObjectName("groupBox_confrontoInput")
        self.groupBox_confrontoInput.setTitle("Immagine Input")

        # SET LABEL IN CUI VIENE INSERITA L'IMMAGINE INPUT
        self.label_confrontoFoto = QtWidgets.QLabel(self.groupBox_confrontoInput)
        self.label_confrontoFoto.setGeometry(QtCore.QRect(0, 20, 341, 291))
        self.label_confrontoFoto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_confrontoFoto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_confrontoFoto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_confrontoFoto.setLineWidth(1)
        self.label_confrontoFoto.setText("")
        self.label_confrontoFoto.setObjectName("label_confrontoFoto")

        # SET GROUPBOX PER LA VISUALIZZAZIONE DELLE IMMAGINE IN OUTPUT
        self.groupBox_confrontoOutput = QtWidgets.QGroupBox(self.groupBox_confronto)
        self.groupBox_confrontoOutput.setGeometry(QtCore.QRect(720, 70, 331, 311))
        font = QtGui.QFont()
        font.setFamily("OpineHeavy")
        font.setPointSize(11)
        self.groupBox_confrontoOutput.setFont(font)
        self.groupBox_confrontoOutput.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.groupBox_confrontoOutput.setTitle("Immagini Output")
        self.groupBox_confrontoOutput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_confrontoOutput.setFlat(True)
        self.groupBox_confrontoOutput.setObjectName("groupBox_confrontoOutput")

        # SET SCROLL AREA PER LA VISUALIZZAZIONE DELLE IMMAGINI IN OUTPUT
        self.scroll_area_confrontoOutput = QtWidgets.QScrollArea(self.groupBox_confrontoOutput)
        self.scroll_area_confrontoOutput.setGeometry(QtCore.QRect(0, 20, 331, 291))
        self.scroll_area_confrontoOutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scroll_area_confrontoOutput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_confrontoOutput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_confrontoOutput.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scroll_area_confrontoOutput.setWidgetResizable(True)
        self.scroll_area_confrontoOutput.setObjectName("scroll_area_confrontoOutput")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setFixedWidth(327)
        self.scrollAreaWidgetContents.setAutoFillBackground(True)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        # PERMETTERE LA VISIONE DELLA FOTO IN OUTPUT CON LE SCROLL BARS
        self.scroll_area_confrontoOutput.setWidget(self.scrollAreaWidgetContents)

        # SET COMBOBOX (MENU A TENDINA) PER LA SCELTA DELLA TECNICA DI CONFRONTO
        self.comboBox_confronto = QtWidgets.QComboBox(self.groupBox_confronto)
        self.comboBox_confronto.setGeometry(QtCore.QRect(50, 180, 265, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.comboBox_confronto.setFont(font)
        self.comboBox_confronto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_confronto.setObjectName("comboBox_confronto")
        self.comboBox_confronto.addItem("")
        self.comboBox_confronto.addItem("")
        self.comboBox_confronto.addItem("")

        # SET LABEL PER IL TITOLO ("Scelta tecnica di confronto...")
        self.label_confronto = QtWidgets.QLabel(self.groupBox_confronto)
        self.label_confronto.setGeometry(QtCore.QRect(10, 70, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_confronto.setFont(font)
        self.label_confronto.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.label_confronto.setFrameShape(QtWidgets.QFrame.Box)
        self.label_confronto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_confronto.setLineWidth(0)
        self.label_confronto.setMidLineWidth(0)
        self.label_confronto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_confronto.setObjectName("label_confronto")

        # SET BOTTONE "cerca" PER L'APPLICAZIONE DELLA TECNICA DI CONFRONTO
        self.pushButton_cercaConfronto = QtWidgets.QPushButton(self.groupBox_confronto)
        self.pushButton_cercaConfronto.setGeometry(QtCore.QRect(130, 310, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cercaConfronto.setFont(font)
        self.pushButton_cercaConfronto.setStyleSheet("background-color: rgb(47, 141, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        
        # INSERIMENTO IMMAGINE AL BOTTONE "cerca"
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Lente nera-trasparente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("D:/Cose DODO/UNI/3^ Anno/Comunicazione Multimediale/Progetto/Lente nera-trasparente.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_cercaConfronto.setIcon(icon)
        self.pushButton_cercaConfronto.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_cercaConfronto.setObjectName("pushButton_cercaConfronto")

        # SET LABEL RIFERITA ALL'INSERIMENTO DELL'IMMAGINE INPUT
        self.label_confronto_2 = QtWidgets.QLabel(self.groupBox_confronto)
        self.label_confronto_2.setGeometry(QtCore.QRect(360, 30, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_confronto_2.setFont(font)
        self.label_confronto_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_confronto_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_confronto_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_confronto_2.setLineWidth(1)
        self.label_confronto_2.setMidLineWidth(0)
        self.label_confronto_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_confronto_2.setObjectName("label_confronto_2")

        # SET BOTTONE "browse" PER L'INSERIMENTO DI UN' IMMAGINE INPUT
        self.pushButton_browseInput = QtWidgets.QPushButton(self.groupBox_confronto)
        self.pushButton_browseInput.setGeometry(QtCore.QRect(710, 30, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_browseInput.setFont(font)
        self.pushButton_browseInput.setStyleSheet("background-color: rgb(47, 141, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")

        #SET BOTTONE "browse" PER LA SCELTA DEL "file index.csv"
        self.pushButton_browseIndex = QtWidgets.QPushButton(self.groupBox_confronto)
        self.pushButton_browseIndex.setGeometry(QtCore.QRect(830, 30, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_browseIndex.setFont(font)
        self.pushButton_browseIndex.setStyleSheet("background-color: rgb(47, 141, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")

        #SET BOTTONE "browse" PER LA SCELTA DEL DATASET
        self.pushButton_browseDataset = QtWidgets.QPushButton(self.groupBox_confronto)
        self.pushButton_browseDataset.setGeometry(QtCore.QRect(950, 30, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_browseDataset.setFont(font)
        self.pushButton_browseDataset.setStyleSheet("background-color: rgb(47, 141, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")

        # INSERIMENTO IMMAGINE AL BOTTONE "browse"
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../simbolo upload-trasparente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("D:/Cose DODO/UNI/3^ Anno/Comunicazione Multimediale/Progetto/simbolo upload-trasparente.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_browseInput.setIcon(icon1)
        self.pushButton_browseInput.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_browseInput.setObjectName("pushButton_browseInput")

        # SET DELLA GROUPBOX RIFERITA AL CONFRONTO TRAMITE LABELS ("parola chiave")
        self.groupBox_sceltaLabel = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_sceltaLabel.setGeometry(QtCore.QRect(20, 450, 701, 281))
        font = QtGui.QFont()
        font.setFamily("OpineHeavy")
        font.setPointSize(18)
        self.groupBox_sceltaLabel.setFont(font)
        self.groupBox_sceltaLabel.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.groupBox_sceltaLabel.setFlat(True)
        self.groupBox_sceltaLabel.setObjectName("groupBox_sceltaLabel")

        # SET COMBOBOX (MENU A TENDINA) PER LA SCELTA DELLA LABEL ("parola chiave") PER IL CONFRONTO
        self.comboBox_sceltaLabel = QtWidgets.QComboBox(self.groupBox_sceltaLabel)
        self.comboBox_sceltaLabel.setGeometry(QtCore.QRect(100, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_sceltaLabel.setFont(font)
        self.comboBox_sceltaLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_sceltaLabel.setObjectName("comboBox_sceltaLabel")
        self.comboBox_sceltaLabel.addItem("")
        self.comboBox_sceltaLabel.addItem("")
        self.comboBox_sceltaLabel.addItem("")
        self.comboBox_sceltaLabel.addItem("")
        self.comboBox_sceltaLabel.addItem("")

        # SET LABEL PER IL TITOLO ("Scelta label...")
        self.label_sceltaLabel = QtWidgets.QLabel(self.groupBox_sceltaLabel)
        self.label_sceltaLabel.setGeometry(QtCore.QRect(10, 70, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_sceltaLabel.setFont(font)
        self.label_sceltaLabel.setLineWidth(1)
        self.label_sceltaLabel.setMidLineWidth(0)
        self.label_sceltaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sceltaLabel.setObjectName("label_sceltaLabel")

        # SET BOTTONE "cerca" PER L'APPLICAZIONE DELLA LABEL ("parola chiave")
        self.pushButton_cercaLabel = QtWidgets.QPushButton(self.groupBox_sceltaLabel)
        self.pushButton_cercaLabel.setGeometry(QtCore.QRect(520, 140, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cercaLabel.setFont(font)
        self.pushButton_cercaLabel.setStyleSheet("background-color: rgb(47, 141, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")


        # INSERIMENTO IMMAGINE AL BOTTONE "cerca"
        self.pushButton_cercaLabel.setIcon(icon)
        self.pushButton_cercaLabel.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_cercaLabel.setObjectName("pushButton_cercaLabel")

        # SET DELLA LABEL CONTENENTE IL LOGO DEL NOSTRO GRUPPO ("4 immagini 1 gruppo")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(830, 450, 181, 181))
        self.label_logo.setFrameShape(QtWidgets.QFrame.Box)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("/Users/lucacampana/Desktop/4Immagini1Gruppo/4immagini1Gruppo.jpeg"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")

        # SET BOTTONE "reset"
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(870, 700, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")

        # INSERIMENTO IMMAGINE AL BOTTONE "reset" 
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../freccia reset-trasparente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("D:/Cose DODO/UNI/3^ Anno/Comunicazione Multimediale/Progetto/freccia reset-trasparente.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_reset.setIcon(icon2)
        self.pushButton_reset.setObjectName("pushButton_reset")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # CHIAMATA METODO SET TITLE PER LE COMPONENTI DELL'INTEFACCIA
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # CHIAMATA METODO CARICAMENTO IMMAGINE BOTTONE "BROWSER" PER L'IMMAGINE
        self.pushButton_browseInput.clicked.connect(self.openImage)

        # CHIAMATA METODO CARICAMENTO IMMAGINE BOTTONE "BROWSER" PER IL FILE "index.csv"
        self.pushButton_browseIndex.clicked.connect(self.openIndex)

        # CHIAMATA METODO CARICAMENTO IMMAGINE BOTTONE "BROWSER" PER IL DATASET
        self.pushButton_browseDataset.clicked.connect(self.openDataset)

        # CHIAMATA METODO CERCA IMMAGINE TRAMITE CONFRONTO BOTTONE "CERCA-CONFRONTO"
        self.pushButton_cercaConfronto.clicked.connect(self.inputNumeroFotoAlg)

        # CHIAMATA METODO CERCA IMMAGINE TRAMITE LABELS
        self.pushButton_cercaLabel.clicked.connect(self.inputNumeroFotoLabels)

        # CHIAMATA METODI PULIZIA BOTTONE "RESET"
        self.pushButton_reset.clicked.connect(self.reset)
        
    # DEFINIZIONE FUNZIONE PER IL SET DEI TITOLI ALLE COMPONENTI DELL'INTERFACCIA
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_confronto.setTitle(_translate("MainWindow", "Input Immagine"))
        self.groupBox_confrontoInput.setTitle(_translate("MainWindow", "Immagine Input"))
        self.comboBox_confronto.setItemText(0, _translate("MainWindow", "..."))
        self.comboBox_confronto.setItemText(1, _translate("MainWindow", "Confronto per istogrammi"))
        self.comboBox_confronto.setItemText(2, _translate("MainWindow", "Tecnica Sift"))
        self.label_confronto.setText(_translate("MainWindow", "Scelta tecnica di confronto..."))
        self.pushButton_cercaConfronto.setText(_translate("MainWindow", "CERCA"))
        self.label_confronto_2.setText(_translate("MainWindow", "premere per inserire foto, index file e dataset -->"))
        self.pushButton_browseInput.setText(_translate("MainWindow", "Browse pic"))
        self.pushButton_browseIndex.setText(_translate("MainWindow", "Browse index"))
        self.pushButton_browseDataset.setText(_translate("MainWindow", "Browse dataset"))
        self.groupBox_sceltaLabel.setTitle(_translate("MainWindow", "Labels"))
        self.comboBox_sceltaLabel.setItemText(0, _translate("MainWindow", "..."))
        self.comboBox_sceltaLabel.setItemText(1, _translate("MainWindow", "Edifici"))
        self.comboBox_sceltaLabel.setItemText(2, _translate("MainWindow", "Calcio"))
        self.comboBox_sceltaLabel.setItemText(3, _translate("MainWindow", "Tramonto"))
        self.comboBox_sceltaLabel.setItemText(4, _translate("MainWindow", "Mare"))
        self.label_sceltaLabel.setText(_translate("MainWindow", "Scelta label..."))
        self.pushButton_cercaLabel.setText(_translate("MainWindow", "CERCA"))
        self.pushButton_reset.setText(_translate("MainWindow", "RESET"))


    # METODO PER VISUALIZZARE UN'IMMAGINE SUL LABEL DELL'IMMAGINE IN INPUT
    def loadImageInput(self, image):
        self.label_confrontoFoto.setPixmap(image)
        self.label_confrontoFoto.setScaledContents(True)


    #METODO PER CARICARE UN FILE IMMAGINE COME INPUT PER IL CONFRONTO
    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName(None, "SCEGLI L'IMMAGINE", "", "jpg(*.jpg)")
        print("Path foto input: " + imagePath)

        D_Applicazione.salvaPathInput(self, imagePath)
        D_Mixer.salvaPathInput(self, imagePath)
        
        pixmap = QPixmap(imagePath)
        self.loadImageInput(pixmap)

    def visualizzaImageInput(self):
        imageImage = self.label_confrontoFoto.pixmap()
        return imageImage


    # METODO PER CARICARE FILE "index.csv" E SALVARE IL SUO PERCORSO
    def openIndex(self):
        indexPath, _ = QFileDialog.getOpenFileName(None, "Only file .csv", "", "csv(*.csv)")

        print("Path index [.cvs]: " + indexPath)

        nomeIndexSift = "index.json"
        pathIndexSift = self.creazionePercorsoFile(indexPath, nomeIndexSift, "")

        print("Path index [.json]: " + pathIndexSift)

        D_Applicazione.salvaPathIndex(self, indexPath)
        D_Mixer.salvaPathIndexIsto(self, indexPath)
        D_Mixer.salvaPathIndexSift(self, pathIndexSift)

    
    # METODO PER CARICARE IL DATASET E SALVARE IL SUO PERCORSO
    def openDataset(self):
        DatasetPath = QFileDialog.getExistingDirectory()

        print("Path dataset: " + DatasetPath)
        
        self.salvaDataset(DatasetPath)


    # DEFIZIONE METODO PER IL RESET DELL'INTEFACCIA 
    def reset(self):
        indexConfronto = self.comboBox_confronto.findText("...", QtCore.Qt.MatchFixedString)
        self.comboBox_confronto.setCurrentIndex(indexConfronto)
        indexSceltaLabel = self.comboBox_sceltaLabel.findText("...", QtCore.Qt.MatchFixedString)
        self.comboBox_sceltaLabel.setCurrentIndex(indexSceltaLabel)
        self.label_confrontoFoto.clear()
        
        # PER RIPULIRE LA FINESTRA DI VISUALIZZAZIONE OUTPUT
        for i in reversed(range(self.verticalLayout.count())): 
            self.verticalLayout.itemAt(i).widget().deleteLater()

        

    # FUNZIONE PER DETERMINARE QUALE ALGORITMO E' STATO SCELTO TRAMITE LA COMBOBOX
    def sceltaAlgoritmo(self):
        sceltaComboBox = self.comboBox_confronto.currentText()

        # EVENTO GESTITO NEL CASO IN CUI NELLA PRIMA GROUPBOX VENGA SELEZIONATA "..."
        if sceltaComboBox == "...":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Nessuna tecnica per il confronto selezionata')
            msg.setWindowTitle("!ERRORE!")
            msg.exec_()

        # EVENTO GESTITO NEL CASO IN CUI NELLA PRIMA GROUPBOX VENGA SELEZIONATA "Confronto per istogrammi"
        if sceltaComboBox == "Confronto per istogrammi":
            pix = self.label_confrontoFoto.pixmap()

            if pix == None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('Nessuna immagine in input per il confronto')
                msg.setWindowTitle("!ERRORE!")
                msg.exec_()
            else:                
                numeroFoto = self.inputNumeroFotoAlg
                immaginiOutput = D_Applicazione.applicazione(self, self.numFoto)
                print(immaginiOutput)
                self.visualizzazioneMultiplaImmagini(immaginiOutput)

        # EVENTO GESTITO NEL CASO IN CUI NELLA PRIMA GROUPBOX VENGA SELEZIONATA "Tecnica Sift"
        if sceltaComboBox == "Tecnica Sift":
            pix = self.label_confrontoFoto.pixmap()

            if pix == None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('Nessuna immagine in input per il confronto')
                msg.setWindowTitle("!ERRORE!")
                msg.exec_()
            else:
                immaginiOutput = D_Mixer.mixer(self, self.numFoto)
                print(immaginiOutput)
                self.visualizzazioneMultiplaImmagini(immaginiOutput)


    # FUNZIONE PER DETERMINARE QUALE LABEL ("PAROLA CHIAVE") E' STATA SCELTA TRAMITE LA COMBOBOX
    def sceltaLabel(self):
        sceltaComboBox = self.comboBox_sceltaLabel.currentText()
        nomeCartellaLabels = "Labels"

        # EVENTO GESTITO NEL CASO IN CUI NELLA PRIMA GROUPBOX VENGA SELEZIONATA "..."
        if sceltaComboBox == "...":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Nessuna label per il confronto selezionata')
            msg.setWindowTitle("!ERRORE!")
            msg.exec_()

        if sceltaComboBox == "Tramonto":
            # STRINGHE NECESSARIE: foto dell'immagine "fissa" (di un tramonto) per il confronto e il nome della cartella che la contiene
            nomeFoto = "tramonto2.jpg"            
            # CHIAMATA DELLA FUNZIONE PER AVERE IL PERCORSO DELLA CARTELLA CHE CONTIENE LE FOTO DA USARE PER LE LABELS
            pathLabel = self.creazionePercorsoFile(self.pathDataset, nomeFoto, nomeCartellaLabels)
            # APPLICAZIONE DELL'ALGORITMO ISTOGRAMMA
            D_Applicazione.salvaPathInput(self, pathLabel)
            immaginiOutput = D_Applicazione.applicazione(self, self.numFoto)
            print(immaginiOutput)
            self.visualizzazioneMultiplaImmagini(immaginiOutput)

        if sceltaComboBox == "Edifici":
            # STRINGHE NECESSARIE: foto dell'immagine "fissa" (di un tramonto) per il confronto e il nome della cartella che la contiene
            nomeFoto = "edificio1.jpg"            
            # CHIAMATA DELLA FUNZIONE PER AVERE IL PERCORSO DELLA CARTELLA CHE CONTIENE LE FOTO DA USARE PER LE LABELS
            pathLabel = self.creazionePercorsoFile(self.pathDataset, nomeFoto, nomeCartellaLabels)
            # APPLICAZIONE DELL'ALGORITMO ISTOGRAMMA
            D_Mixer.salvaPathInput(self, pathLabel)
            immaginiOutput = D_Mixer.mixer(self, self.numFoto)
            print(immaginiOutput)
            self.visualizzazioneMultiplaImmagini(immaginiOutput)
        
        if sceltaComboBox == "Calcio":
            # STRINGHE NECESSARIE: foto dell'immagine "fissa" (di un tramonto) per il confronto e il nome della cartella che la contiene
            nomeFoto = "calcio7.jpg"            
            # CHIAMATA DELLA FUNZIONE PER AVERE IL PERCORSO DELLA CARTELLA CHE CONTIENE LE FOTO DA USARE PER LE LABELS
            pathLabel = self.creazionePercorsoFile(self.pathDataset, nomeFoto, nomeCartellaLabels)
            # APPLICAZIONE DELL'ALGORITMO ISTOGRAMMA
            D_Applicazione.salvaPathInput(self, pathLabel)
            immaginiOutput = D_Applicazione.applicazione(self, self.numFoto)
            print(immaginiOutput)
            self.visualizzazioneMultiplaImmagini(immaginiOutput)
        
        if sceltaComboBox == "Mare":
            # STRINGHE NECESSARIE: foto dell'immagine "fissa" (di un tramonto) per il confronto e il nome della cartella che la contiene
            nomeFoto = "mare28.jpg"            
            # CHIAMATA DELLA FUNZIONE PER AVERE IL PERCORSO DELLA CARTELLA CHE CONTIENE LE FOTO DA USARE PER LE LABELS
            pathLabel = self.creazionePercorsoFile(self.pathDataset, nomeFoto, nomeCartellaLabels)
            # APPLICAZIONE DELL'ALGORITMO ISTOGRAMMA
            D_Applicazione.salvaPathInput(self, pathLabel)
            immaginiOutput = D_Applicazione.applicazione(self, self.numFoto)
            print(immaginiOutput)
            self.visualizzazioneMultiplaImmagini(immaginiOutput)

            

    # FUNZIONI CHE PERMETTONO LA VISUALIZZAZIONE DI PIU' IMMAGINI ALL'INTERNO DELLA LABEL DI VISUALIZZAZIONE OUTPUT
    def visualizzazioneMultiplaImmagini(self, arrayFoto):

        arrayImg = []
        arrayScore = []

        for (score, resultID) in arrayFoto:
            arrayImg.append(resultID)
            val = 100 - score
            num = round(val, 2)
            arrayScore.append(num)

        self.file_it = iter(arrayImg)
        self.score_it = iter(arrayScore)
        self._timer = QtCore.QTimer(MainWindow, interval=1)
        self._timer.timeout.connect(self.on_timeout)
        self._timer.start()

    # FUNZIONE CHE PERMETTE LA VISUALIZZAZIONE DELLE FOTO SCANSIONATE DA UN TIMER PER RIDURRE IL TEMPO DI ATTESA PER IL CARICAMENTO
    def on_timeout(self):

        datasetImg = self.pathDataset
        
        try:
            file = next(self.file_it)
            punto = next(self.score_it)
            pixmap = QtGui.QPixmap(datasetImg + "/" + file)
            self.add_pixmap(pixmap, punto)            
        except StopIteration:
            self._timer.stop()

    # FUNZIONE PER L'AGGIUNTA DELLE FOTO ALL'INTERFACCIA
    def add_pixmap(self, pixmap, score):
        if not pixmap.isNull():

            label = QtWidgets.QLabel(pixmap=pixmap)            
            label.setScaledContents(True)
            label.setFixedWidth(285)
            label.setFixedHeight(275)
            label.setToolTip('Precisione: ' + str(score) + "%")
            self.verticalLayout.addWidget(label)
    

    # FUNZIONE PER RISCRIVERE IL PERCORSO NECCESSARIO USANDO IL NOME DELLA FOTO DI RIFERIMENTO E IL NOME DELLA CARTELLA CONTENENTE TALE FOTO
    def creazionePercorsoFile (self, percorsoStandard, nomeFile, cartellaFile):

        # PERCORSO DEL DATASET
        datasetImg = percorsoStandard
        # SUDDIVIDO IL PERCORCO NELLE VARIE CARTELLE PER RAGGIUNGERE IL DATASET ["/" è il divisore]
        x = datasetImg.split("/")
        # RISCRIVO IL COLLEGAMENTO ANDANDO A PRENDERE SOLO LE PRIME 5 CARTELLE (senza il dataset)
        path = x[0:5]
        # USO IL METODO "join" PER UNIRE OGGETTI IN UNA LISTA IN UNA SINGOLA STRINGA
        string = '/'.join(path)
        # RISCRIVO IL COLLEGMANTO CORRETTO PER APRIRE LA CARTELLA "Labels" CONTENENTE LA FOTO PER IL CONFRONTO
        pathFile = string + "/" + cartellaFile + "/" + nomeFile
        
        return pathFile

    def inputNumeroFotoAlg(self, limit):
        text, ok = QInputDialog.getText(None, "Numero foto", "da 1 a 20 (numeri maggiori di 20 vengono contati come 20)", QtWidgets.QLineEdit.Normal, "")
        if ok and text != '':
            numero = int(text)
            if(numero > 20):
                self.salvaNumeroFoto(20)
                self.sceltaAlgoritmo()
            if(numero < 1):
                self.salvaNumeroFoto(1)
                self.sceltaAlgoritmo()
            else:
                self.salvaNumeroFoto(numero)
                self.sceltaAlgoritmo()

    def inputNumeroFotoLabels(self, limit):
        text, ok = QInputDialog.getText(None, "Numero foto", "da 1 a 20 (numeri maggiori di 20 vengono contati come 20)", QtWidgets.QLineEdit.Normal, "")
        if ok and text != '':
            numero = int(text)
            if(numero > 20):
                self.salvaNumeroFoto(20)
                self.sceltaLabel()
            if(numero < 1):
                self.salvaNumeroFoto(1)
                self.sceltaLabel()
            else:
                self.salvaNumeroFoto(numero)
                self.sceltaLabel()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





