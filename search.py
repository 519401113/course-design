# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_departure = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_departure.sizePolicy().hasHeightForWidth())
        self.label_departure.setSizePolicy(sizePolicy)
        self.label_departure.setAlignment(QtCore.Qt.AlignCenter)
        self.label_departure.setObjectName("label_departure")
        self.horizontalLayout_2.addWidget(self.label_departure)
        self.comboBox_departure = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_departure.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_departure.sizePolicy().hasHeightForWidth())
        self.comboBox_departure.setSizePolicy(sizePolicy)
        self.comboBox_departure.setEditable(False)
        self.comboBox_departure.setObjectName("comboBox_departure")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_departure)
        self.label_destination = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_destination.sizePolicy().hasHeightForWidth())
        self.label_destination.setSizePolicy(sizePolicy)
        self.label_destination.setAlignment(QtCore.Qt.AlignCenter)
        self.label_destination.setObjectName("label_destination")
        self.horizontalLayout_2.addWidget(self.label_destination)
        self.comboBox_destination = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_destination.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_destination.sizePolicy().hasHeightForWidth())
        self.comboBox_destination.setSizePolicy(sizePolicy)
        self.comboBox_destination.setEditable(False)
        self.comboBox_destination.setObjectName("comboBox_destination")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_destination)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout_4.addWidget(self.label_date)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setAlignment(QtCore.Qt.AlignCenter)
        self.label_class.setObjectName("label_class")
        self.horizontalLayout_5.addWidget(self.label_class)
        self.comboBox_class = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_class.setObjectName("comboBox_class")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_class)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setObjectName("Search")
        self.verticalLayout.addWidget(self.Search)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu_2)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_2)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionregister = QtWidgets.QAction(MainWindow)
        self.actionregister.setObjectName("actionregister")
        self.actionbuy = QtWidgets.QAction(MainWindow)
        self.actionbuy.setObjectName("actionbuy")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.actionds = QtWidgets.QAction(MainWindow)
        self.actionds.setObjectName("actionds")
        self.actionkj = QtWidgets.QAction(MainWindow)
        self.actionkj.setObjectName("actionkj")
        self.menu.addAction(self.actionregister)
        self.menu_3.addAction(self.action1)
        self.menu_3.addAction(self.actionds)
        self.menu_4.addAction(self.actionkj)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_2.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_departure.setText(_translate("MainWindow", "Departure"))
        self.comboBox_departure.setCurrentText(_translate("MainWindow", "北京"))
        self.comboBox_departure.setItemText(0, _translate("MainWindow", "北京"))
        self.comboBox_departure.setItemText(1, _translate("MainWindow", "成都"))
        self.comboBox_departure.setItemText(2, _translate("MainWindow", "香港"))
        self.comboBox_departure.setItemText(3, _translate("MainWindow", "哈尔滨"))
        self.comboBox_departure.setItemText(4, _translate("MainWindow", "海南"))
        self.comboBox_departure.setItemText(5, _translate("MainWindow", "上海"))
        self.comboBox_departure.setItemText(6, _translate("MainWindow", "长春"))
        self.comboBox_departure.setItemText(7, _translate("MainWindow", "兰州"))
        self.comboBox_departure.setItemText(8, _translate("MainWindow", "广州"))
        self.comboBox_departure.setItemText(9, _translate("MainWindow", "长沙"))
        self.comboBox_departure.setItemText(10, _translate("MainWindow", "南昌"))
        self.label_destination.setText(_translate("MainWindow", "Destination"))
        self.comboBox_destination.setItemText(0, _translate("MainWindow", "北京"))
        self.comboBox_destination.setItemText(1, _translate("MainWindow", "成都"))
        self.comboBox_destination.setItemText(2, _translate("MainWindow", "香港"))
        self.comboBox_destination.setItemText(3, _translate("MainWindow", "哈尔滨"))
        self.comboBox_destination.setItemText(4, _translate("MainWindow", "海南"))
        self.comboBox_destination.setItemText(5, _translate("MainWindow", "上海"))
        self.comboBox_destination.setItemText(6, _translate("MainWindow", "长春"))
        self.comboBox_destination.setItemText(7, _translate("MainWindow", "兰州"))
        self.comboBox_destination.setItemText(8, _translate("MainWindow", "广州"))
        self.comboBox_destination.setItemText(9, _translate("MainWindow", "长沙"))
        self.comboBox_destination.setItemText(10, _translate("MainWindow", "南昌"))
        self.label_date.setText(_translate("MainWindow", "DATE"))
        self.label_class.setText(_translate("MainWindow", "Class"))
        self.comboBox_class.setItemText(0, _translate("MainWindow", "头等舱"))
        self.comboBox_class.setItemText(1, _translate("MainWindow", "商务舱"))
        self.comboBox_class.setItemText(2, _translate("MainWindow", "经济舱"))
        self.Search.setText(_translate("MainWindow", "Search"))
        self.menu.setTitle(_translate("MainWindow", "注册"))
        self.menu_2.setTitle(_translate("MainWindow", "功能"))
        self.menu_3.setTitle(_translate("MainWindow", "用户"))
        self.menu_4.setTitle(_translate("MainWindow", "管理员"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionregister.setText(_translate("MainWindow", "用户注册"))
        self.actionbuy.setText(_translate("MainWindow", "机票购买"))
        self.action1.setText(_translate("MainWindow", "机票购买"))
        self.actionds.setText(_translate("MainWindow", "我的机票"))
        self.actionkj.setText(_translate("MainWindow", "添加数据"))

