from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(339, 240)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(339, 240))
        Dialog.setMaximumSize(QSize(339, 240))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 341, 241))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 40, 47, 13))
        font1 = QFont()
        font1.setFamily(u"Lucida Sans")
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.runBtn = QPushButton(self.tab)
        self.runBtn.setObjectName(u"runBtn")
        self.runBtn.setGeometry(QRect(70, 90, 91, 41))
        font2 = QFont()
        font2.setFamily(u"Lucida Sans")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.runBtn.setFont(font2)
        self.stopBtn = QPushButton(self.tab)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setGeometry(QRect(170, 90, 91, 41))
        self.stopBtn.setFont(font2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.chromeLabel = QLabel(self.tab_2)
        self.chromeLabel.setObjectName(u"chromeLabel")
        self.chromeLabel.setGeometry(QRect(40, 10, 71, 16))
        self.chrome_toolBtn = QToolButton(self.tab_2)
        self.chrome_toolBtn.setObjectName(u"chrome_toolBtn")
        self.chrome_toolBtn.setGeometry(QRect(290, 30, 25, 20))
        self.chrome_toolBtn.setCheckable(False)
        self.edge_toolBtn = QToolButton(self.tab_2)
        self.edge_toolBtn.setObjectName(u"edge_toolBtn")
        self.edge_toolBtn.setGeometry(QRect(290, 80, 25, 20))
        self.edge_toolBtn.setCheckable(False)
        self.edgeLabel = QLabel(self.tab_2)
        self.edgeLabel.setObjectName(u"edgeLabel")
        self.edgeLabel.setGeometry(QRect(40, 60, 71, 16))
        self.yandex_toolBtn = QToolButton(self.tab_2)
        self.yandex_toolBtn.setObjectName(u"yandex_toolBtn")
        self.yandex_toolBtn.setGeometry(QRect(290, 130, 25, 20))
        self.yandex_toolBtn.setCheckable(False)
        self.yandexLabel = QLabel(self.tab_2)
        self.yandexLabel.setObjectName(u"yandexLabel")
        self.yandexLabel.setGeometry(QRect(40, 110, 71, 16))
        self.teams_toolBtn = QToolButton(self.tab_2)
        self.teams_toolBtn.setObjectName(u"teams_toolBtn")
        self.teams_toolBtn.setGeometry(QRect(290, 180, 25, 20))
        self.teams_toolBtn.setCheckable(False)
        self.teamsLabel = QLabel(self.tab_2)
        self.teamsLabel.setObjectName(u"teamsLabel")
        self.teamsLabel.setGeometry(QRect(40, 160, 71, 16))
        self.chrome_path_line = QLineEdit(self.tab_2)
        self.chrome_path_line.setObjectName(u"chrome_path_line")
        self.chrome_path_line.setGeometry(QRect(40, 30, 241, 20))
        self.edge_path_line = QLineEdit(self.tab_2)
        self.edge_path_line.setObjectName(u"edge_path_line")
        self.edge_path_line.setGeometry(QRect(40, 80, 241, 20))
        self.yandex_path_line = QLineEdit(self.tab_2)
        self.yandex_path_line.setObjectName(u"yandex_path_line")
        self.yandex_path_line.setGeometry(QRect(40, 130, 241, 20))
        self.teams_path_line = QLineEdit(self.tab_2)
        self.teams_path_line.setObjectName(u"teams_path_line")
        self.teams_path_line.setGeometry(QRect(40, 180, 241, 20))
        self.google_checkBox = QCheckBox(self.tab_2)
        self.google_checkBox.setObjectName(u"google_checkBox")
        self.google_checkBox.setGeometry(QRect(20, 30, 20, 20))
        self.edge_checkBox = QCheckBox(self.tab_2)
        self.edge_checkBox.setObjectName(u"edge_checkBox")
        self.edge_checkBox.setGeometry(QRect(20, 80, 20, 20))
        self.yandex_checkBox = QCheckBox(self.tab_2)
        self.yandex_checkBox.setObjectName(u"yandex_checkBox")
        self.yandex_checkBox.setGeometry(QRect(20, 130, 20, 20))
        self.teams_checkBox = QCheckBox(self.tab_2)
        self.teams_checkBox.setObjectName(u"teams_checkBox")
        self.teams_checkBox.setGeometry(QRect(20, 180, 20, 20))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Status: ", None))
        self.runBtn.setText(QCoreApplication.translate("Dialog", u"Run bot", None))
        self.stopBtn.setText(QCoreApplication.translate("Dialog", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Start menu", None))
        self.chromeLabel.setText(QCoreApplication.translate("Dialog", u"Chrome path", None))
        self.chrome_toolBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.edge_toolBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.edgeLabel.setText(QCoreApplication.translate("Dialog", u"Edge path", None))
        self.yandex_toolBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.yandexLabel.setText(QCoreApplication.translate("Dialog", u"Yandex path", None))
        self.teams_toolBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.teamsLabel.setText(QCoreApplication.translate("Dialog", u"Teams path", None))
        self.google_checkBox.setText("")
        self.edge_checkBox.setText("")
        self.yandex_checkBox.setText("")
        self.teams_checkBox.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Settings", None))
    # retranslateUi
