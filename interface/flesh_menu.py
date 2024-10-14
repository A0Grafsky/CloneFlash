from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    """Flesh menu"""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(622, 788)
        Dialog.setStyleSheet("background-color:rgb(63, 63, 63)")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setStyleSheet("font: 700 16pt \"Bell MT\";\n"
                                 "color:White; \n"
                                 "font-size: 45px\n"
                                 "")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("\n"
                                      "font: 36pt \"Tahoma\";\n"
                                      "color:White; \n"
                                      "font-size: 22px\n"
                                      "")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_2.addWidget(self.listWidget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.refresh_button = QtWidgets.QPushButton(parent=Dialog)
        self.refresh_button.setMinimumSize(QtCore.QSize(400, 0))
        self.refresh_button.setMaximumSize(QtCore.QSize(450, 55))
        self.refresh_button.setStyleSheet("QPushButton {\n"
                                       "    font: 700 16pt \"Bell MT\";\n"
                                       "background-color: rgb(162, 176, 165);\n"
                                       "color:White; \n"
                                       "border: 2px solid #000000; \n"
                                       "border-radius: 7px;\n"
                                       "width: 20px;\n"
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
        self.refresh_button.setObjectName("refresh_button")
        self.verticalLayout_2.addWidget(self.refresh_button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.about_us_button = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_us_button.sizePolicy().hasHeightForWidth())
        self.about_us_button.setSizePolicy(sizePolicy)
        self.about_us_button.setMinimumSize(QtCore.QSize(500, 0))
        self.about_us_button.setMaximumSize(QtCore.QSize(500, 54))
        self.about_us_button.setStyleSheet("QPushButton {\n"
                                           "    font: 700 16pt \"Bell MT\";\n"
                                           "background-color: rgb(76, 112, 84);\n"
                                           "color:White; \n"
                                           "border: 2px solid #000000; \n"
                                           "border-radius: 7px;\n"
                                           "width: 10px;\n"
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
        self.about_us_button.setObjectName("about_us_button")
        self.verticalLayout.addWidget(self.about_us_button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:34pt;\">💾Cписок Файлов💾</span></p></body></html>"))
        self.refresh_button.setText(_translate("Dialog", "ОБНОВИТЬ"))
        self.about_us_button.setText(_translate("Dialog", "ВЫЙТИ"))
