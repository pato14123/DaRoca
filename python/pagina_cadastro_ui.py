# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagina_cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_janela_cadastro(object):
    def setupUi(self, janela_cadastro):
        if not janela_cadastro.objectName():
            janela_cadastro.setObjectName(u"janela_cadastro")
        janela_cadastro.resize(569, 257)
        self.centralwidget = QWidget(janela_cadastro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnCadastrar = QPushButton(self.centralwidget)
        self.btnCadastrar.setObjectName(u"btnCadastrar")
        self.btnCadastrar.setGeometry(QRect(450, 180, 101, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 1, 541, 161))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.nomeProduto = QLineEdit(self.widget)
        self.nomeProduto.setObjectName(u"nomeProduto")

        self.gridLayout.addWidget(self.nomeProduto, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spbvalor = QDoubleSpinBox(self.widget)
        self.spbvalor.setObjectName(u"spbvalor")

        self.gridLayout.addWidget(self.spbvalor, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.nomeImagem = QLineEdit(self.widget)
        self.nomeImagem.setObjectName(u"nomeImagem")

        self.gridLayout.addWidget(self.nomeImagem, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.produtoId = QLineEdit(self.widget)
        self.produtoId.setObjectName(u"produtoId")

        self.gridLayout.addWidget(self.produtoId, 3, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.tipo_produto = QLineEdit(self.widget)
        self.tipo_produto.setObjectName(u"tipo_produto")

        self.gridLayout.addWidget(self.tipo_produto, 4, 1, 1, 1)

        janela_cadastro.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(janela_cadastro)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 569, 21))
        janela_cadastro.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(janela_cadastro)
        self.statusbar.setObjectName(u"statusbar")
        janela_cadastro.setStatusBar(self.statusbar)

        self.retranslateUi(janela_cadastro)

        QMetaObject.connectSlotsByName(janela_cadastro)
    # setupUi

    def retranslateUi(self, janela_cadastro):
        janela_cadastro.setWindowTitle(QCoreApplication.translate("janela_cadastro", u"Cadastro de Produtos", None))
        self.btnCadastrar.setText(QCoreApplication.translate("janela_cadastro", u"Cadastrar", None))
        self.label.setText(QCoreApplication.translate("janela_cadastro", u"Nome do Produto:", None))
        self.label_2.setText(QCoreApplication.translate("janela_cadastro", u"Valor:", None))
        self.label_3.setText(QCoreApplication.translate("janela_cadastro", u"Imagem:", None))
        self.label_4.setText(QCoreApplication.translate("janela_cadastro", u"Id:", None))
        self.label_5.setText(QCoreApplication.translate("janela_cadastro", u"Tipo:", None))
    # retranslateUi

