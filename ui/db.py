# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db_view.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(444, 394)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.formLayout)

        self.le_table_name = QLineEdit(self.centralwidget)
        self.le_table_name.setObjectName(u"le_table_name")
        self.le_table_name.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_table_name)

        self.btn_ok = QPushButton(self.centralwidget)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(20, 20))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.btn_ok)

        self.tw_table_info = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tw_table_info.setHeaderItem(__qtreewidgetitem)
        self.tw_table_info.setObjectName(u"tw_table_info")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.tw_table_info)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 444, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.le_table_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome da tabela", None))
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

