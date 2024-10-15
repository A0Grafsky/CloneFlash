from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    """Main menu"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 896)
        MainWindow.setStyleSheet("background-color:rgb(63, 63, 63)")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_smail = QtWidgets.QLabel(parent=self.frame)
        self.label_smail.setStyleSheet("font: 700 16pt \"Bell MT\";\n"
                                       "color:White; \n"
                                       "font-size: 90px\n"
                                       "")
        self.label_smail.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_smail.setObjectName("label_smail")
        self.verticalLayout_2.addWidget(self.label_smail)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.flesh_button = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flesh_button.sizePolicy().hasHeightForWidth())
        self.flesh_button.setSizePolicy(sizePolicy)
        self.flesh_button.setMinimumSize(QtCore.QSize(0, 0))
        self.flesh_button.setMaximumSize(QtCore.QSize(300, 79))
        self.flesh_button.setStyleSheet("QPushButton {\n"
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
        self.flesh_button.setObjectName("flesh_button")
        self.horizontalLayout.addWidget(self.flesh_button)
        self.email_button = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_button.sizePolicy().hasHeightForWidth())
        self.email_button.setSizePolicy(sizePolicy)
        self.email_button.setMinimumSize(QtCore.QSize(0, 0))
        self.email_button.setMaximumSize(QtCore.QSize(300, 79))
        self.email_button.setStyleSheet("QPushButton {\n"
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
        self.email_button.setObjectName("email_button")
        self.horizontalLayout.addWidget(self.email_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.help_button = QtWidgets.QPushButton(parent=self.frame)
        self.help_button.setMaximumSize(QtCore.QSize(605, 65))
        self.help_button.setStyleSheet("QPushButton {\n"
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
        self.help_button.setObjectName("refresh_button")
        self.verticalLayout.addWidget(self.help_button)
        self.about_us_button = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_us_button.sizePolicy().hasHeightForWidth())
        self.about_us_button.setSizePolicy(sizePolicy)
        self.about_us_button.setMaximumSize(QtCore.QSize(605, 54))
        self.about_us_button.setStyleSheet("QPushButton {\n"
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
        self.about_us_button.setObjectName("exit_to_flesh")
        self.verticalLayout.addWidget(self.about_us_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(50, 100, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_smail.setText(_translate("MainWindow",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-size:68pt;\">🕊️</span></p><p align=\"center\"><span style=\" font-size:68pt;\"> CF</span></p></body></html>"))
        self.flesh_button.setText(_translate("MainWindow", "ФЛЕШКА"))
        self.email_button.setText(_translate("MainWindow", "ПОЧТА"))
        self.help_button.setText(_translate("MainWindow", "ПОМОЩЬ"))
        self.about_us_button.setText(_translate("MainWindow", "О НАС"))
