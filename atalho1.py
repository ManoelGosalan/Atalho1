import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QInputDialog, QLineEdit, QMenu, QSystemTrayIcon, QStyle, QMessageBox, QDialog
from PyQt6.QtCore import Qt, QUrl, pyqtSignal
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap, QIcon, QDesktopServices
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:/Users/manoe/AppData/Local/Programs/Python/Python311/Lib/site-packages/PyQt6/Qt6/plugins'


class Aplicativo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atalho")
        self.setGeometry(450, 100, 500, 500)
        self.setStyleSheet("background-color: #D3D3D3;")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon("image/icone.ico"))
        # fundo
        fundo = QLabel(self)
        fundo.setPixmap(QPixmap("image/pdv.png"))
        fundo.setGeometry(0, 0, 500, 500)

        # versão
        versão = QLabel(self)
        versão.setText("Versão 2.0 ")
        versão.move(10, 5)
        versão.setStyleSheet(
            "background-color: rgba(220,220,220, 0); color: black; font: bold 12px Arial; border: 0px; border-radius: 10px;")
        # botões

        ETrade = QPushButton("ETrade", self)
        ETrade.setGeometry(10, 20, 150, 70)
        ETrade.setStyleSheet(
            "font: 18pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")

        ETrade.clicked.connect(self.abrir_etrade)

        Pdv = QPushButton("PDV", self)
        Pdv.setGeometry(180, 20, 150, 70)
        Pdv.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FFD700, stop: 1 #FF8C00);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FF8C00, stop: 1#FFD700);")
        Pdv.clicked.connect(self.abrir_pdv)

        Suporte = QPushButton("Suporte", self)
        Suporte.setGeometry(350, 20, 150, 70)
        Suporte.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D3D3D3, stop: 1 #A9A9A9);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A9A9A9, stop: 1 #D3D3D3);")

        Suporte.clicked.connect(self.abrir_suporte)

        Pasta = QPushButton("Pasta", self)
        Pasta.setGeometry(400, 290, 100, 50)
        Pasta.setStyleSheet(
            "background-color: rgba(220,220,220, 0); color: white; font: bold 26px Arial; border: 0px; border-radius: 10px;")

        Pasta.clicked.connect(self.abrir_pasta)

        Config = QPushButton("Config", self)
        Config.setGeometry(300, 230, 100, 50)
        Config.setStyleSheet(
            "background-color: rgba(220,220,220, 0); color: white; font: bold 26px Arial; border: 0px; border-radius: 10px;")

        Config.clicked.connect(self.abrir_config)

        Minizar = QPushButton("Minimizar", self)
        Minizar.setGeometry(350, 425, 150, 48)
        Minizar.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: Black; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        Minizar.clicked.connect(self.minimizar_minizar)

        # Criar a janela de suporte
        self.janela_suporte = JanelaSuporte(self)

    def abrir_etrade(self):
        QDesktopServices().openUrl(QUrl("C:/ETrade/ETrade.exe"))
        self.showMinimized()
        QMessageBox.information(self, "ETrade", "ETrade aberto com sucesso!")

    def abrir_pdv(self):
        QDesktopServices().openUrl(QUrl("C:/ETrade/PDV.exe"))
        QDesktopServices().openUrl(QUrl("C:/ETrade/Bridge.exe"))

        self.showMinimized()

    def abrir_pasta(self):
        QDesktopServices().openUrl(QUrl("C:/ETrade/"))
        self.showMinimized()

    def abrir_config(self):
        QDesktopServices().openUrl(QUrl("C:/ETrade/ProgramaBackup.exe"))
        QDesktopServices().openUrl(QUrl("C:/ETrade/UtilitarioBD.exe"))
        self.showMinimized()

    def minimizar_minizar(self):
        self.showMinimized()

    def abrir_suporte(self):
        self.hide()
        self.janela_suporte.show()


class JanelaSuporte(QWidget):
    voltar_sinal = pyqtSignal()

    def __init__(self, aplicativo):
        super().__init__()
        self.aplicativo = aplicativo
        self.setWindowTitle("Suporte")
        self.setGeometry(450, 100, 500, 500)
        self.setStyleSheet("background-color: #D3D3D3;")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("image/icone.ico"))

        fundo = QLabel(self)
        fundo.setGeometry(0, 0, 500, 500)
        fundo.setPixmap(QtGui.QPixmap("image/Suporte.png"))

        TeamViwer = QPushButton("TeamViewer", self)
        TeamViwer.setGeometry(180, 120, 150, 50)
        TeamViwer.setStyleSheet(
            "font: 19pt Arial;margin: 2px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D3D3D3, stop: 1 #4169E1);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4169E1, stop: 1 #D3D3D3);")

        TeamViwer.clicked.connect(self.abrir_TeamViewer)

        Ammyy = QPushButton("Ammyy", self)
        Ammyy.setGeometry(180, 10, 150, 50)
        Ammyy.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FF0000, stop: 1 #A52A2A);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A52A2A, stop: 1 #FF0000);")

        Ammyy.clicked.connect(self.abrir_Ammyy)

        ShowMyPc = QPushButton("ShowMyPc", self)
        ShowMyPc.setGeometry(350, 10, 150, 50)
        ShowMyPc.setStyleSheet(
            "font: 20pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #008000, stop: 1 #00FF00);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00FF00, stop: 1 #008000);")

        ShowMyPc.clicked.connect(self.abrir_ShowMyPC)

        AnyDesk = QPushButton("AnyDesk", self)
        AnyDesk.setGeometry(10, 10, 150, 50)
        AnyDesk.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FF0000, stop: 1 #A52A2A);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A52A2A, stop: 1 #FF0000);")

        AnyDesk.clicked.connect(self.abrir_AnyDesk)

        XML = QPushButton("XML", self)
        XML.setGeometry(10, 250, 100, 50)
        XML.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D3D3D3, stop: 1 #A9A9A9);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A9A9A9, stop: 1 #D3D3D3);")

        XML.clicked.connect(self.abrir_XML)

        NCM = QPushButton("NCM", self)
        NCM.setGeometry(200, 250, 100, 50)
        NCM.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D3D3D3, stop: 1 #A9A9A9);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A9A9A9, stop: 1 #D3D3D3);")

        NCM.clicked.connect(self.abrir_NCM)

        CNPJ = QPushButton("CNPJ", self)
        CNPJ.setGeometry(400, 250, 100, 48)
        CNPJ.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D3D3D3, stop: 1 #A9A9A9);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A9A9A9, stop: 1 #D3D3D3);")

        CNPJ.clicked.connect(self.abrir_CNPJ)

        SINTREGA = QPushButton("SINTREGA", self)
        SINTREGA.setGeometry(175, 330, 180, 48)
        SINTREGA.setStyleSheet(
            "font: 20pt Arial;margin: 2px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D3D3D3, stop: 1 #A9A9A9);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A9A9A9, stop: 1 #D3D3D3);")

        SINTREGA.clicked.connect(self.abrir_SINTEGRA)

        fechar = QPushButton("FECHAR", self)
        fechar.setGeometry(370, 380, 130, 100)
        fechar.setStyleSheet(
            "font: 22pt Arial;margin: 5px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: red; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        fechar.clicked.connect(self.abrir_fechar)

        TELEFONE = QPushButton("Acessar Chat SUPORTE", self)
        TELEFONE.setGeometry(10, 380, 250, 100)
        TELEFONE.setStyleSheet(
            "font: 15pt Arial;margin: 2px; border-color: #0c457e; border-style: outset; border-radius: 15px;border-width: 1px;color: white; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D3D3D3, stop: 1 #A9A9A9);}QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A9A9A9, stop: 1 #D3D3D3);")

        TELEFONE.clicked.connect(self.abrir_TELEFONE)

    def abrir_TeamViewer(self):
        QDesktopServices().openUrl(QUrl("C:/ETrade/Uteis/TeamViewer.lnk"))
        self.showMinimized()
        QMessageBox().information(self, "Aviso", "Aguarde o TeamViewer abrir ")

    def abrir_Ammyy(self):
        QDesktopServices().openUrl(QUrl("C:/ETrade/Uteis/AA_v3.exe"))
        self.showMinimized()

    def abrir_ShowMyPC(self):
        QDesktopServices().openUrl(QUrl("C:/ETrade/Uteis/ShowMyPC3620.exe"))
        self.showMinimized()

    def abrir_AnyDesk(self):
        QDesktopServices().openUrl(QUrl("C:/ETrade/Uteis/adqs.exe"))
        self.showMinimized()

    def abrir_XML(self):
        QDesktopServices().openUrl(QUrl("https://www.fsist.com.br"))

    def abrir_NCM(self):
        QDesktopServices().openUrl(QUrl("https://cosmos.bluesoft.com.br"))

    def abrir_CNPJ(self):
        QDesktopServices().openUrl(QUrl(
            "https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp"))

    def abrir_SINTEGRA(self):
        QDesktopServices().openUrl(QUrl("http://www.sintegra.gov.br"))

    def abrir_TELEFONE(self):
        QDesktopServices().openUrl(
            QUrl("https://wa.me/556533584188?text=Ol%C3%A1%2C+Gostaria+de+uma+ajuda"))
        self.showMinimized()

    def abrir_fechar(self):
        self.hide()
        self.voltar_sinal.emit()
        self.aplicativo.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Aplicativo()
    janela.show()
    sys.exit(app.exec())
