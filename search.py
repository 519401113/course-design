# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *
import sys
import register
import login
import search
import register_win
import register_fail

class Register_Window(QDialog, register.Ui_Dialog):
    def __init__(self, parent = None):
        super(Register_Window, self).__init__(parent)
        self.setupUi(self)

class Login_Window(QDialog, login.Ui_Dialog):
    def __init__(self, parent = None):
        super(Login_Window, self).__init__(parent)
        self.setupUi(self)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 384)
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
        self.output_search = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_search.sizePolicy().hasHeightForWidth())
        self.output_search.setSizePolicy(sizePolicy)
        self.output_search.setObjectName("output_search")
        self.horizontalLayout.addWidget(self.output_search)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setObjectName("register_2")
        self.gridLayout.addWidget(self.register_2, 1, 0, 1, 1)
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 22))
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
        self.Search.clicked.connect(self.searchresult)
        self.login.clicked.connect(self.open_login)
        self.register_2.clicked.connect(self.open_register)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # # def function_login(self):
    #     child_login, child_login_ui = login.Ui_Dialog.instantiation(login)
    #     child_login_ui.button_connect(child_login, self.login)
    #
    # # def function_register(self):
    #     child_register, child_register_ui = register.Ui_Dialog.instantiation(register)
    #     child_register_ui.button_connect(child_register, self.register_2)

    def searchresult(self):
        # query_departure = QSqlQuery()
        # query_departure.prepare("SELECT 机场代码 FROM 机场 where 所在城市 = :departure")
        # query_departure.bindValue(":departure", self.comboBox_departure.currentText())
        # query_departure.exec_()
        # list_departure = list()
        # while query_departure.next():
        #     print(query_departure.value(0))
        #
        # query_destination = QSqlQuery()
        # query_destination.prepare("SELECT 机场代码 FROM 机场 where 所在城市 = :destination")
        # query_destination.bindValue(":destination", self.comboBox_destination.currentText())
        # query_destination.exec_()
        # list_destination = list()
        # while query_destination.next():
        #     print(query_destination.value(0))

        query_flight = QSqlQuery()  # 新建QSqlQuery对象
        query_flight.prepare('SELECT 航班编号 FROM 航班 '
                             'WHERE 航班.出发机场代码 in (SELECT 机场代码 FROM 机场 where 所在城市 = :departure) '
                             'and 航班.到达机场代码 in (SELECT 机场代码 FROM 机场 where 所在城市 = :destination)')  # 输入SQL语句
        query_flight.bindValue(":departure", self.comboBox_departure.currentText())
        query_flight.bindValue(":destination", self.comboBox_destination.currentText())  # 绑定占位符和相应的功能
        query_flight.exec_()  # 执行
        flight = "("
        while query_flight.next():
            flight += "'" + query_flight.value(0) + "'"
            if query_flight.next():
                flight += ","
                query_flight.previous()
        flight += ")"  # flight ： (A, B, ....)

        self.model = QSqlTableModel()  # 新建SQLTableModel 对象
        self.output_search.setModel(self.model)  # 绑定到tableview对象上
        self.model.setTable('飞行计划安排')  # 相当于 from 语句
        self.model.setFilter("航班编号 in %s" % (flight))  # 相当于where语句
        print(self.model.filter())
        self.model.select()  # 执行SQL select

        self.output_search.show()  # 显示


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
        self.register_2.setText(_translate("MainWindow", "注册"))
        self.login.setText(_translate("MainWindow", "登录"))
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

    def open_login(self):
        login_window = Login_Window()
        login_window.exec_()

    def open_register(self):
        register_window = Register_Window()
        register_window.exec_()