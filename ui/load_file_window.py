# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_file_window.ui'
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
        MainWindow.resize(404, 194)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAcceptDrops(False)
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.formLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName(u"lbl_status")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_status)

        self.load_progress = QProgressBar(self.centralwidget)
        self.load_progress.setObjectName(u"load_progress")
        self.load_progress.setEnabled(True)
        self.load_progress.setMinimumSize(QSize(0, 20))
        self.load_progress.setCursor(QCursor(Qt.WaitCursor))
        self.load_progress.setAutoFillBackground(False)
        self.load_progress.setMinimum(0)
        self.load_progress.setMaximum(0)
        self.load_progress.setValue(-1)
        self.load_progress.setInvertedAppearance(False)

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.load_progress)

        self.btn_open_file = QPushButton(self.centralwidget)
        self.btn_open_file.setObjectName(u"btn_open_file")
        self.btn_open_file.setMinimumSize(QSize(380, 50))

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.btn_open_file)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dbv By Yxqsnz.", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"Status: Esperando por um arquivo", None))
#if QT_CONFIG(whatsthis)
        self.load_progress.setWhatsThis(QCoreApplication.translate("MainWindow", u"Progresso do carregamento (:", None))
#endif // QT_CONFIG(whatsthis)
        self.load_progress.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.btn_open_file.setText(QCoreApplication.translate("MainWindow", u"Abrir arquivo", None))
    # retranslateUi

