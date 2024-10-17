from PyQt6 import QtCore, QtGui, QtWidgets


class UiDialogEmailTest(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(718, 762)
        Dialog.setStyleSheet("background-color:rgb(63, 63, 63)")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setStyleSheet("font: 700 16pt \"Bell MT\";\n"
                                 "color:White; \n"
                                 "font-size: 45px\n"
                                 "")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setStyleSheet("background-color:rgb(63, 63, 63)")
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.refresh_button_email = QtWidgets.QPushButton(parent=Dialog)
        self.refresh_button_email.setMinimumSize(QtCore.QSize(400, 0))
        self.refresh_button_email.setMaximumSize(QtCore.QSize(450, 55))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.refresh_button_email.setFont(font)
        self.refresh_button_email.setStyleSheet("QPushButton {\n"
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
                                                "}\n"
                                                "")
        self.refresh_button_email.setObjectName("refresh_button_email")
        self.verticalLayout.addWidget(self.refresh_button_email, 0,
                                      QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.exit_button = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setMinimumSize(QtCore.QSize(500, 0))
        self.exit_button.setMaximumSize(QtCore.QSize(500, 54))
        self.exit_button.setStyleSheet("QPushButton {\n"
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
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.listWidget_email = QtWidgets.QListWidget(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_email.sizePolicy().hasHeightForWidth())
        self.listWidget_email.setSizePolicy(sizePolicy)
        self.listWidget_email.setMinimumSize(QtCore.QSize(700, 0))
        self.listWidget_email.setStyleSheet("\n"
                                            "font: 36pt \"Tahoma\";\n"
                                            "color:White; \n"
                                            "font-size: 45px\n"
                                            "")
        self.listWidget_email.setObjectName("listWidget_email")
        self.gridLayout.addWidget(self.listWidget_email, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\"><span style=\" "
                                      "font-size:24pt;\">ОТПРАВТЕ ДОКУМЕНТ </span></p><p align=\"center\"><span "
                                      "style=\" font-size:24pt;\">НА ЭТУ ПОЧТУ</span></p></body></html>"))
        self.widget.setWhatsThis(_translate("Dialog", "<html><head/><body><p>ccxzcxzc</p></body></html>"))
        self.refresh_button_email.setText(_translate("Dialog", "ОБНОВИТЬ"))
        self.exit_button.setText(_translate("Dialog", "ВЫЙТИ"))
