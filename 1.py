# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_flight.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(900, 600)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_flight_number = QtWidgets.QLabel(Dialog)
        self.label_flight_number.setObjectName("label_flight_number")
        self.horizontalLayout.addWidget(self.label_flight_number)
        self.lineEdit_flight_number = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_flight_number.setObjectName("lineEdit_flight_number")
        self.horizontalLayout.addWidget(self.lineEdit_flight_number)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_departure_time = QtWidgets.QLabel(Dialog)
        self.label_departure_time.setObjectName("label_departure_time")
        self.horizontalLayout_2.addWidget(self.label_departure_time)
        self.dateTimeEdit_departure_time = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_departure_time.setObjectName("dateTimeEdit_departure_time")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_departure_time)
        self.label_arrival_time = QtWidgets.QLabel(Dialog)
        self.label_arrival_time.setObjectName("label_arrival_time")
        self.horizontalLayout_2.addWidget(self.label_arrival_time)
        self.dateTimeEdit_arrival_time = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_arrival_time.setObjectName("dateTimeEdit_arrival_time")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_arrival_time)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.checkBox_transit = QtWidgets.QCheckBox(Dialog)
        self.checkBox_transit.setObjectName("checkBox_transit")
        self.verticalLayout.addWidget(self.checkBox_transit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_arrival_transit_time = QtWidgets.QLabel(Dialog)
        self.label_arrival_transit_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_arrival_transit_time.setObjectName("label_arrival_transit_time")
        self.horizontalLayout_3.addWidget(self.label_arrival_transit_time)
        self.dateTimeEdit_arrival_transit_time = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_arrival_transit_time.setObjectName("dateTimeEdit_arrival_transit_time")
        self.horizontalLayout_3.addWidget(self.dateTimeEdit_arrival_transit_time)
        self.label_departure_transit_time = QtWidgets.QLabel(Dialog)
        self.label_departure_transit_time.setObjectName("label_departure_transit_time")
        self.horizontalLayout_3.addWidget(self.label_departure_transit_time)
        self.dateTimeEdit_departure_transit_time = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_departure_transit_time.setObjectName("dateTimeEdit_departure_transit_time")
        self.horizontalLayout_3.addWidget(self.dateTimeEdit_departure_transit_time)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.label_departure_transit = QtWidgets.QLabel(Dialog)
        self.label_departure_transit.setObjectName("label_departure_transit")
        self.verticalLayout.addWidget(self.label_departure_transit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_price_economy_departure_transit = QtWidgets.QLabel(Dialog)
        self.label_price_economy_departure_transit.setObjectName("label_price_economy_departure_transit")
        self.horizontalLayout_4.addWidget(self.label_price_economy_departure_transit)
        self.lineEdit_price_economy_departure_transit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_economy_departure_transit.setObjectName("lineEdit_price_economy_departure_transit")
        self.horizontalLayout_4.addWidget(self.lineEdit_price_economy_departure_transit)
        self.label_price_business_departure_transit = QtWidgets.QLabel(Dialog)
        self.label_price_business_departure_transit.setObjectName("label_price_business_departure_transit")
        self.horizontalLayout_4.addWidget(self.label_price_business_departure_transit)
        self.lineEdit_price_business_departure_transit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_business_departure_transit.setObjectName("lineEdit_price_business_departure_transit")
        self.horizontalLayout_4.addWidget(self.lineEdit_price_business_departure_transit)
        self.label_price_first_departure_transit = QtWidgets.QLabel(Dialog)
        self.label_price_first_departure_transit.setObjectName("label_price_first_departure_transit")
        self.horizontalLayout_4.addWidget(self.label_price_first_departure_transit)
        self.lineEdit_price_first_departure_transit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_first_departure_transit.setObjectName("lineEdit_price_first_departure_transit")
        self.horizontalLayout_4.addWidget(self.lineEdit_price_first_departure_transit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.label_transit_arrival = QtWidgets.QLabel(Dialog)
        self.label_transit_arrival.setObjectName("label_transit_arrival")
        self.verticalLayout.addWidget(self.label_transit_arrival)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_price_economy_transit_arrival = QtWidgets.QLabel(Dialog)
        self.label_price_economy_transit_arrival.setObjectName("label_price_economy_transit_arrival")
        self.horizontalLayout_5.addWidget(self.label_price_economy_transit_arrival)
        self.lineEdit_price_economy_transit_arrival = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_economy_transit_arrival.setObjectName("lineEdit_price_economy_transit_arrival")
        self.horizontalLayout_5.addWidget(self.lineEdit_price_economy_transit_arrival)
        self.label_price_business_transit_arrival = QtWidgets.QLabel(Dialog)
        self.label_price_business_transit_arrival.setObjectName("label_price_business_transit_arrival")
        self.horizontalLayout_5.addWidget(self.label_price_business_transit_arrival)
        self.lineEdit_price_business_transit_arrival = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_business_transit_arrival.setObjectName("lineEdit_price_business_transit_arrival")
        self.horizontalLayout_5.addWidget(self.lineEdit_price_business_transit_arrival)
        self.label_price_first_transit_arrival = QtWidgets.QLabel(Dialog)
        self.label_price_first_transit_arrival.setObjectName("label_price_first_transit_arrival")
        self.horizontalLayout_5.addWidget(self.label_price_first_transit_arrival)
        self.lineEdit_price_first_transit_arrival = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_first_transit_arrival.setObjectName("lineEdit_price_first_transit_arrival")
        self.horizontalLayout_5.addWidget(self.lineEdit_price_first_transit_arrival)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.label_departure_arrival = QtWidgets.QLabel(Dialog)
        self.label_departure_arrival.setObjectName("label_departure_arrival")
        self.verticalLayout.addWidget(self.label_departure_arrival)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_price_economy_departure_arrival = QtWidgets.QLabel(Dialog)
        self.label_price_economy_departure_arrival.setObjectName("label_price_economy_departure_arrival")
        self.horizontalLayout_6.addWidget(self.label_price_economy_departure_arrival)
        self.lineEdit_price_economy_departure_arrival = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_economy_departure_arrival.setObjectName("lineEdit_price_economy_departure_arrival")
        self.horizontalLayout_6.addWidget(self.lineEdit_price_economy_departure_arrival)
        self.label_price_business_departure_arrival = QtWidgets.QLabel(Dialog)
        self.label_price_business_departure_arrival.setObjectName("label_price_business_departure_arrival")
        self.horizontalLayout_6.addWidget(self.label_price_business_departure_arrival)
        self.lineEdit_price_business_departure_arrival = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_business_departure_arrival.setObjectName("lineEdit_price_business_departure_arrival")
        self.horizontalLayout_6.addWidget(self.lineEdit_price_business_departure_arrival)
        self.label_price_first_departure_arrival = QtWidgets.QLabel(Dialog)
        self.label_price_first_departure_arrival.setObjectName("label_price_first_departure_arrival")
        self.horizontalLayout_6.addWidget(self.label_price_first_departure_arrival)
        self.lineEdit_price_first_departure_arrival = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price_first_departure_arrival.setObjectName("lineEdit_price_first_departure_arrival")
        self.horizontalLayout_6.addWidget(self.lineEdit_price_first_departure_arrival)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.pushButton_insert = QtWidgets.QPushButton(Dialog)
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.verticalLayout.addWidget(self.pushButton_insert)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.checkBox_transit.stateChanged['int'].connect(self.dateTimeEdit_arrival_transit_time.clear)
        self.checkBox_transit.stateChanged['int'].connect(self.dateTimeEdit_departure_transit_time.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加航程"))
        self.label_flight_number.setText(_translate("Dialog", "航班编号："))
        self.label_departure_time.setText(_translate("Dialog", "计划出发时间："))
        self.label_arrival_time.setText(_translate("Dialog", "计划到达时间："))
        self.checkBox_transit.setText(_translate("Dialog", "是否经停？"))
        self.label_arrival_transit_time.setText(_translate("Dialog", "计划到达经停机场时间："))
        self.label_departure_transit_time.setText(_translate("Dialog", "计划从经停机场出发时间："))
        self.label_departure_transit.setText(_translate("Dialog", "出发-经停："))
        self.label_price_economy_departure_transit.setText(_translate("Dialog", "经济舱票价:"))
        self.label_price_business_departure_transit.setText(_translate("Dialog", "商务舱票价:"))
        self.label_price_first_departure_transit.setText(_translate("Dialog", "头等舱票价:"))
        self.label_transit_arrival.setText(_translate("Dialog", "经停-到达："))
        self.label_price_economy_transit_arrival.setText(_translate("Dialog", "经济舱票价:"))
        self.label_price_business_transit_arrival.setText(_translate("Dialog", "商务舱票价:"))
        self.label_price_first_transit_arrival.setText(_translate("Dialog", "头等舱票价:"))
        self.label_departure_arrival.setText(_translate("Dialog", "出发-到达："))
        self.label_price_economy_departure_arrival.setText(_translate("Dialog", "经济舱票价:"))
        self.label_price_business_departure_arrival.setText(_translate("Dialog", "商务舱票价:"))
        self.label_price_first_departure_arrival.setText(_translate("Dialog", "头等舱票价:"))
        self.pushButton_insert.setText(_translate("Dialog", "添加"))

