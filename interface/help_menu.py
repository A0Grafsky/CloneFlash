
from PyQt6 import QtCore, QtGui, QtWidgets


class HelpUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(981, 661)
        Dialog.setStyleSheet("background-color:rgb(63, 63, 63)")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(700, 0))
        self.label_2.setStyleSheet("font: 700 16pt \"Bell MT\";\n"
"color:White; \n"
"font-size: 40px;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(700, 400))
        self.label.setMaximumSize(QtCore.QSize(700, 400))
        self.label.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.label.setStyleSheet("font: 700 16pt \"Bell MT\";\n"
"color:White; \n"
"font-size: 25px;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 700 16pt \"Bell MT\";\n"
"background-color: rgb(162, 176, 165);\n"
"color:White; \n"
"border: 2px solid #000000; \n"
"border-radius: 7px;\n"
"widht: 20px;\n"
"height: 65px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 181, 136);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(57, 112, 70);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; text-decoration: underline;\">ПОМОЩЬ</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Для того, чтобы распечатать документ, его нужно, либо выбрать с флешки, либо отправить на указанную почту. После его можно будет осмотреть перед печатью, и если Вас все будет устраивать, то тогда выбираем кнопку `ПЕЧАТЬ` и переходим на меню с выбором копий (ВАЖНО! Выбор копий - это количество итоговой печать, то есть 12 листов и 2 копии - 24 листа).\n"
"\n"
"Оплата происходит по QR-коду, после оплаты нажмите `ПРОВЕРИТЬ ОПЛАТУ` и в случае успешной операция начнется печать документов.\n"
"\n"
"Спасибо за внимание."))
        self.pushButton.setText(_translate("Dialog", "НАЗАД"))
