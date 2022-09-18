from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QFont, QScreen, QIcon
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow, QLineEdit, \
    QHBoxLayout, QMessageBox

import Banco

TAMANHO_FONTE = 30

layout = QVBoxLayout()
app = QApplication()
base = QWidget()
widget_botoes = QWidget()
layout_botoes = QHBoxLayout()
widget_botoes.setLayout(layout_botoes)
janela_login = QMainWindow()

janela_login.setWindowTitle('Login')
janela_login.setMaximumWidth(300)
janela_login.setMaximumHeight(180)

icone = QIcon()
icone.addFile('recursos/logo.jpg')

janela_login.setWindowIcon(icone)

font = QFont()
font.setPixelSize(TAMANHO_FONTE)

lbl_titulo = QLabel('Infinity School')
lbl_titulo.setFont(font)
lbl_titulo.setAlignment(Qt.AlignCenter)

lbl_login = QLabel('Login')
lbl_login.setAlignment(Qt.AlignCenter)
lbl_senha = QLabel('Senha')
lbl_senha.setAlignment(Qt.AlignCenter)

msg = QMessageBox()
msg.setIcon(QMessageBox.Warning)
msg.setText("Login e/ou senha incorreto(s)")
msg.setInformativeText("Tente novamente")
msg.setWindowTitle("Erro de Autenticação")
# msg.setDetailedText("The details are as follows:")
msg.setStandardButtons(QMessageBox.Ok)  # | QMessageBox.Cancel)

lbl_msg = QLabel('')
lbl_msg.setAlignment(Qt.AlignCenter)

txt_login = QLineEdit()

txt_senha = QLineEdit()
txt_senha.setEchoMode(QLineEdit.Password)

btn_enviar = QPushButton('Entrar')
btn_enviar.setMinimumHeight(40)
btn_cadastrar = QPushButton('Cadastrar')
btn_cadastrar.setMinimumHeight(40)


def verifica_login_e_senha():
    resultado = Banco.verifica_login_senha(txt_login.text(), txt_senha.text())

    if resultado:
        lbl_msg.setText('Informações de login corretas. Redirecionando...')
        lbl_msg.setStyleSheet('color: blue')
    else:
        lbl_msg.setStyleSheet('color: red')
        lbl_msg.setText('Informações de login incorretas. Tente novamente.')
        txt_login.setText('')
        txt_senha.setText('')
        txt_login.setFocus()
        msg.exec()
        lbl_msg.setText('')


layout.addWidget(lbl_titulo)
layout.addWidget(lbl_login)
layout.addWidget(txt_login)

layout.addWidget(lbl_senha)
layout.addWidget(txt_senha)
layout.addWidget(lbl_msg)

layout_botoes.addWidget(btn_enviar)
layout_botoes.addWidget(btn_cadastrar)
widget_botoes.setLayout(layout_botoes)

layout.addWidget(widget_botoes)

base.setLayout(layout)
janela_login.setCentralWidget(base)
janela_login.setGeometry(QRect(50, 50, 300, 180))

center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
geo = janela_login.frameGeometry()
geo.moveCenter(center)
janela_login.move(geo.topLeft())

btn_enviar.clicked.connect(verifica_login_e_senha)

janela_login.show()
app.exec()
