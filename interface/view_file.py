from PyQt6 import QtCore, QtGui, QtWidgets


class ViewPrintObject2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(817, 879)
        Form.setStyleSheet("background-color:rgb(63, 63, 63)")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.file_view = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_view.sizePolicy().hasHeightForWidth())
        self.file_view.setSizePolicy(sizePolicy)
        self.file_view.setMinimumSize(QtCore.QSize(700, 0))
        self.file_view.setObjectName("file_view")
        self.gridLayout_2.addWidget(self.file_view, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.print_button = QtWidgets.QPushButton(parent=Form)
        self.print_button.setMinimumSize(QtCore.QSize(400, 0))
        self.print_button.setMaximumSize(QtCore.QSize(450, 55))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.print_button.setFont(font)
        self.print_button.setStyleSheet("QPushButton {\n"
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
        self.print_button.setObjectName("print_button")
        self.verticalLayout.addWidget(self.print_button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.exit_button_from_list_file = QtWidgets.QPushButton(parent=Form)
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
        self.verticalLayout.addWidget(self.exit_button_from_list_file, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.left_button = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_button.sizePolicy().hasHeightForWidth())
        self.left_button.setSizePolicy(sizePolicy)
        self.left_button.setMinimumSize(QtCore.QSize(200, 0))
        self.left_button.setMaximumSize(QtCore.QSize(200, 55))
        self.left_button.setStyleSheet("QPushButton {\n"
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
        self.left_button.setObjectName("left_button")
        self.gridLayout.addWidget(self.left_button, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.right_button = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_button.sizePolicy().hasHeightForWidth())
        self.right_button.setSizePolicy(sizePolicy)
        self.right_button.setMinimumSize(QtCore.QSize(200, 0))
        self.right_button.setMaximumSize(QtCore.QSize(300, 55))
        self.right_button.setStyleSheet("QPushButton {\n"
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
        self.right_button.setObjectName("right_button")
        self.gridLayout.addWidget(self.right_button, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.file_view.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.print_button.setText(_translate("Form", "Печать"))
        self.exit_button_from_list_file.setText(_translate("Form", "ВЫЙТИ"))
        self.left_button.setText(_translate("Form", "Назад"))
        self.right_button.setText(_translate("Form", "Далее"))
