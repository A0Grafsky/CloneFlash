from PyQt6 import QtCore, QtGui, QtWidgets


class CheckBuyForPrint(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(721, 726)
        Dialog.setStyleSheet("background-color:rgb(63, 63, 63)")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setStyleSheet('font: 700 16pt "Bell MT";\n'
                                   'color:White; \n'
                                   'font-size: 40px\n'
                                   '')
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.qrcode_photo = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qrcode_photo.sizePolicy().hasHeightForWidth())
        self.qrcode_photo.setSizePolicy(sizePolicy)
        self.qrcode_photo.setMinimumSize(QtCore.QSize(500, 500))
        self.qrcode_photo.setMaximumSize(QtCore.QSize(500, 500))
        self.qrcode_photo.setText("")
        self.qrcode_photo.setObjectName("qrcode_photo")
        self.verticalLayout_2.addWidget(self.qrcode_photo, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 700 16pt \"Bell MT\";\n"
"color:White; \n"
"font-size: 40px\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.status_bar = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_bar.sizePolicy().hasHeightForWidth())
        self.status_bar.setSizePolicy(sizePolicy)
        self.status_bar.setStyleSheet("font: 700 16pt \"Bell MT\";\n"
"color:White; \n"
"font-size: 40px;\n"
" border: 1px solid rgb(255, 119, 119);")
        self.status_bar.setObjectName("status_bar")
        self.verticalLayout.addWidget(self.status_bar, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.check_buy_button = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_buy_button.sizePolicy().hasHeightForWidth())
        self.check_buy_button.setSizePolicy(sizePolicy)
        self.check_buy_button.setMinimumSize(QtCore.QSize(250, 0))
        self.check_buy_button.setMaximumSize(QtCore.QSize(300, 70))
        self.check_buy_button.setStyleSheet("QPushButton {\n"
"    font: 700 16pt \"Bell MT\";\n"
"background-color: rgb(162, 176, 165);\n"
"color:White; \n"
"border: 2px solid #000000; \n"
"border-radius: 7px;\n"
"widht: 20px;\n"
"height: 75px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 181, 136);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(57, 112, 70);\n"
"}\n"
"")
        self.check_buy_button.setObjectName("check_buy_button")
        self.gridLayout.addWidget(self.check_buy_button, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.exit_button_from_list_file = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button_from_list_file.sizePolicy().hasHeightForWidth())
        self.exit_button_from_list_file.setSizePolicy(sizePolicy)
        self.exit_button_from_list_file.setMinimumSize(QtCore.QSize(500, 0))
        self.exit_button_from_list_file.setMaximumSize(QtCore.QSize(500, 54))
        self.exit_button_from_list_file.setStyleSheet("QPushButton {\n"
"    font: 700 16pt \"Bell MT\";\n"
"background-color: rgb(76, 112, 84);\n"
"color:White; \n"
"border: 2px solid #000000; \n"
"border-radius: 7px;\n"
"widht: 10px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 181, 136);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(57, 112, 70);\n"
"}\n"
"")
        self.exit_button_from_list_file.setObjectName("exit_button_from_list_file")
        self.gridLayout.addWidget(self.exit_button_from_list_file, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">🔻ОПЛАТА🔻</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">СТАТУС ОПЕРАЦИИ</span></p></body></html>"))
        self.status_bar.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\">ОЖИДАНИЕ</p></body></html>"))
        self.check_buy_button.setText(_translate("Dialog", "ПРОВЕРИТЬ ОПЛАТУ"))
        self.exit_button_from_list_file.setText(_translate("Dialog", "ОТМЕНИТЬ"))
