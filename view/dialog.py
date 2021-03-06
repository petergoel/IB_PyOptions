# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exchange(object):
    def setupUi(self, exchange):
        exchange.setObjectName("exchange")
        exchange.resize(1369, 686)
        self.button_UpdateVol = QtWidgets.QPushButton(exchange)
        self.button_UpdateVol.setGeometry(QtCore.QRect(830, 240, 91, 23))
        self.button_UpdateVol.setObjectName("button_UpdateVol")
        self.layoutWidget = QtWidgets.QWidget(exchange)
        self.layoutWidget.setGeometry(QtCore.QRect(450, 50, 331, 152))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_ImpVol = QtWidgets.QLabel(self.layoutWidget)
        self.lb_ImpVol.setObjectName("lb_ImpVol")
        self.gridLayout.addWidget(self.lb_ImpVol, 3, 0, 1, 1)
        self.impliedVol = QtWidgets.QLineEdit(self.layoutWidget)
        self.impliedVol.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.impliedVol.setText("")
        self.impliedVol.setReadOnly(True)
        self.impliedVol.setObjectName("impliedVol")
        self.gridLayout.addWidget(self.impliedVol, 3, 1, 1, 1)
        self.lb_totalInt = QtWidgets.QLabel(self.layoutWidget)
        self.lb_totalInt.setObjectName("lb_totalInt")
        self.gridLayout.addWidget(self.lb_totalInt, 3, 2, 1, 1)
        self.lb_openInt = QtWidgets.QLabel(self.layoutWidget)
        self.lb_openInt.setObjectName("lb_openInt")
        self.gridLayout.addWidget(self.lb_openInt, 0, 2, 1, 1)
        self.lb_stockLast = QtWidgets.QLabel(self.layoutWidget)
        self.lb_stockLast.setObjectName("lb_stockLast")
        self.gridLayout.addWidget(self.lb_stockLast, 0, 0, 1, 1)
        self.callOpenInterest = QtWidgets.QLineEdit(self.layoutWidget)
        self.callOpenInterest.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.callOpenInterest.setText("")
        self.callOpenInterest.setReadOnly(True)
        self.callOpenInterest.setObjectName("callOpenInterest")
        self.gridLayout.addWidget(self.callOpenInterest, 0, 3, 1, 1)
        self.lb_putCallInt = QtWidgets.QLabel(self.layoutWidget)
        self.lb_putCallInt.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lb_putCallInt.setObjectName("lb_putCallInt")
        self.gridLayout.addWidget(self.lb_putCallInt, 1, 2, 1, 1)
        self.stockLast = QtWidgets.QLineEdit(self.layoutWidget)
        self.stockLast.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.stockLast.setText("")
        self.stockLast.setReadOnly(True)
        self.stockLast.setObjectName("stockLast")
        self.gridLayout.addWidget(self.stockLast, 0, 1, 1, 1)
        self.stockClose = QtWidgets.QLineEdit(self.layoutWidget)
        self.stockClose.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.stockClose.setText("")
        self.stockClose.setReadOnly(True)
        self.stockClose.setObjectName("stockClose")
        self.gridLayout.addWidget(self.stockClose, 1, 1, 1, 1)
        self.lb_stockClose = QtWidgets.QLabel(self.layoutWidget)
        self.lb_stockClose.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lb_stockClose.setObjectName("lb_stockClose")
        self.gridLayout.addWidget(self.lb_stockClose, 1, 0, 1, 1)
        self.putOpenInterest = QtWidgets.QLineEdit(self.layoutWidget)
        self.putOpenInterest.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.putOpenInterest.setText("")
        self.putOpenInterest.setReadOnly(True)
        self.putOpenInterest.setObjectName("putOpenInterest")
        self.gridLayout.addWidget(self.putOpenInterest, 1, 3, 1, 1)
        self.totalOpenInterest = QtWidgets.QLineEdit(self.layoutWidget)
        self.totalOpenInterest.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.totalOpenInterest.setText("")
        self.totalOpenInterest.setReadOnly(True)
        self.totalOpenInterest.setObjectName("totalOpenInterest")
        self.gridLayout.addWidget(self.totalOpenInterest, 3, 3, 1, 1)
        self.daysFromExpiry = QtWidgets.QLineEdit(self.layoutWidget)
        self.daysFromExpiry.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.daysFromExpiry.setText("")
        self.daysFromExpiry.setReadOnly(True)
        self.daysFromExpiry.setObjectName("daysFromExpiry")
        self.gridLayout.addWidget(self.daysFromExpiry, 5, 1, 1, 1)
        self.lb_Exp = QtWidgets.QLabel(self.layoutWidget)
        self.lb_Exp.setObjectName("lb_Exp")
        self.gridLayout.addWidget(self.lb_Exp, 5, 0, 1, 1)
        self.lb_callVol = QtWidgets.QLabel(self.layoutWidget)
        self.lb_callVol.setObjectName("lb_callVol")
        self.gridLayout.addWidget(self.lb_callVol, 4, 2, 1, 1)
        self.historicVol = QtWidgets.QLineEdit(self.layoutWidget)
        self.historicVol.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.historicVol.setText("")
        self.historicVol.setReadOnly(True)
        self.historicVol.setObjectName("historicVol")
        self.gridLayout.addWidget(self.historicVol, 4, 1, 1, 1)
        self.labelExpiry_2 = QtWidgets.QLabel(self.layoutWidget)
        self.labelExpiry_2.setObjectName("labelExpiry_2")
        self.gridLayout.addWidget(self.labelExpiry_2, 4, 0, 1, 1)
        self.putVolume = QtWidgets.QLineEdit(self.layoutWidget)
        self.putVolume.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.putVolume.setText("")
        self.putVolume.setReadOnly(True)
        self.putVolume.setObjectName("putVolume")
        self.gridLayout.addWidget(self.putVolume, 5, 3, 1, 1)
        self.callVolume = QtWidgets.QLineEdit(self.layoutWidget)
        self.callVolume.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.callVolume.setText("")
        self.callVolume.setReadOnly(True)
        self.callVolume.setObjectName("callVolume")
        self.gridLayout.addWidget(self.callVolume, 4, 3, 1, 1)
        self.lb_putVol = QtWidgets.QLabel(self.layoutWidget)
        self.lb_putVol.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lb_putVol.setObjectName("lb_putVol")
        self.gridLayout.addWidget(self.lb_putVol, 5, 2, 1, 1)
        self.lb_totalVol = QtWidgets.QLabel(self.layoutWidget)
        self.lb_totalVol.setObjectName("lb_totalVol")
        self.gridLayout.addWidget(self.lb_totalVol, 6, 2, 1, 1)
        self.totalVolume = QtWidgets.QLineEdit(self.layoutWidget)
        self.totalVolume.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.totalVolume.setText("")
        self.totalVolume.setReadOnly(True)
        self.totalVolume.setObjectName("totalVolume")
        self.gridLayout.addWidget(self.totalVolume, 6, 3, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(exchange)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 50, 291, 126))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lb_expiry = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_expiry.setObjectName("lb_expiry")
        self.gridLayout_2.addWidget(self.lb_expiry, 3, 0, 1, 1)
        self.lb_SecType = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_SecType.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lb_SecType.setObjectName("lb_SecType")
        self.gridLayout_2.addWidget(self.lb_SecType, 1, 0, 1, 1)
        self.lb_symbol = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_symbol.setObjectName("lb_symbol")
        self.gridLayout_2.addWidget(self.lb_symbol, 0, 0, 1, 1)
        self.strike = QtWidgets.QLineEdit(self.layoutWidget1)
        self.strike.setText("")
        self.strike.setObjectName("strike")
        self.gridLayout_2.addWidget(self.strike, 0, 3, 1, 1)
        self.securityType = QtWidgets.QComboBox(self.layoutWidget1)
        self.securityType.setMaxCount(10)
        self.securityType.setObjectName("securityType")
        self.gridLayout_2.addWidget(self.securityType, 1, 1, 1, 1)
        self.exchangeLoc = QtWidgets.QComboBox(self.layoutWidget1)
        self.exchangeLoc.setMaxCount(10)
        self.exchangeLoc.setObjectName("exchangeLoc")
        self.gridLayout_2.addWidget(self.exchangeLoc, 2, 1, 1, 1)
        self.lb_exchange = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_exchange.setObjectName("lb_exchange")
        self.gridLayout_2.addWidget(self.lb_exchange, 2, 0, 1, 1)
        self.dateExpiry = QtWidgets.QDateEdit(self.layoutWidget1)
        self.dateExpiry.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateExpiry.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 31), QtCore.QTime(12, 59, 59)))
        self.dateExpiry.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 9, 14), QtCore.QTime(2, 0, 0)))
        self.dateExpiry.setObjectName("dateExpiry")
        self.gridLayout_2.addWidget(self.dateExpiry, 3, 1, 1, 1)
        self.lb_callPut = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_callPut.setObjectName("lb_callPut")
        self.gridLayout_2.addWidget(self.lb_callPut, 1, 2, 1, 1)
        self.lb_currency = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_currency.setObjectName("lb_currency")
        self.gridLayout_2.addWidget(self.lb_currency, 2, 2, 1, 1)
        self.lb_stk = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_stk.setObjectName("lb_stk")
        self.gridLayout_2.addWidget(self.lb_stk, 0, 2, 1, 1)
        self.symbol = QtWidgets.QLineEdit(self.layoutWidget1)
        self.symbol.setInputMask("")
        self.symbol.setText("")
        self.symbol.setPlaceholderText("")
        self.symbol.setObjectName("symbol")
        self.gridLayout_2.addWidget(self.symbol, 0, 1, 1, 1)
        self.callPut = QtWidgets.QComboBox(self.layoutWidget1)
        self.callPut.setObjectName("callPut")
        self.gridLayout_2.addWidget(self.callPut, 1, 3, 1, 1)
        self.currency = QtWidgets.QComboBox(self.layoutWidget1)
        self.currency.setObjectName("currency")
        self.gridLayout_2.addWidget(self.currency, 2, 3, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(exchange)
        self.layoutWidget2.setGeometry(QtCore.QRect(830, 50, 241, 181))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rangeUSD_45Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rangeUSD_45Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.rangeUSD_45Days.setText("")
        self.rangeUSD_45Days.setReadOnly(True)
        self.rangeUSD_45Days.setObjectName("rangeUSD_45Days")
        self.gridLayout_3.addWidget(self.rangeUSD_45Days, 4, 2, 1, 1)
        self.maxDaysSpinBox = QtWidgets.QSpinBox(self.layoutWidget2)
        self.maxDaysSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.maxDaysSpinBox.setMinimum(20)
        self.maxDaysSpinBox.setMaximum(50)
        self.maxDaysSpinBox.setProperty("value", 45)
        self.maxDaysSpinBox.setObjectName("maxDaysSpinBox")
        self.gridLayout_3.addWidget(self.maxDaysSpinBox, 0, 2, 1, 1)
        self.minDaysSpinBox = QtWidgets.QSpinBox(self.layoutWidget2)
        self.minDaysSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.minDaysSpinBox.setMinimum(20)
        self.minDaysSpinBox.setMaximum(50)
        self.minDaysSpinBox.setProperty("value", 35)
        self.minDaysSpinBox.setObjectName("minDaysSpinBox")
        self.gridLayout_3.addWidget(self.minDaysSpinBox, 0, 1, 1, 1)
        self.rangeUSD_30Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rangeUSD_30Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.rangeUSD_30Days.setText("")
        self.rangeUSD_30Days.setReadOnly(True)
        self.rangeUSD_30Days.setObjectName("rangeUSD_30Days")
        self.gridLayout_3.addWidget(self.rangeUSD_30Days, 4, 1, 1, 1)
        self.rangePercent_30Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rangePercent_30Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.rangePercent_30Days.setText("")
        self.rangePercent_30Days.setReadOnly(True)
        self.rangePercent_30Days.setObjectName("rangePercent_30Days")
        self.gridLayout_3.addWidget(self.rangePercent_30Days, 3, 1, 1, 1)
        self.lb_volPerc = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_volPerc.setObjectName("lb_volPerc")
        self.gridLayout_3.addWidget(self.lb_volPerc, 1, 0, 1, 1)
        self.volUSD_45Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.volUSD_45Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.volUSD_45Days.setText("")
        self.volUSD_45Days.setReadOnly(True)
        self.volUSD_45Days.setObjectName("volUSD_45Days")
        self.gridLayout_3.addWidget(self.volUSD_45Days, 2, 2, 1, 1)
        self.lb_rangeUSD = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_rangeUSD.setObjectName("lb_rangeUSD")
        self.gridLayout_3.addWidget(self.lb_rangeUSD, 4, 0, 1, 1)
        self.rangePercent_45Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rangePercent_45Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.rangePercent_45Days.setText("")
        self.rangePercent_45Days.setReadOnly(True)
        self.rangePercent_45Days.setObjectName("rangePercent_45Days")
        self.gridLayout_3.addWidget(self.rangePercent_45Days, 3, 2, 1, 1)
        self.volUSD_30Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.volUSD_30Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.volUSD_30Days.setText("")
        self.volUSD_30Days.setReadOnly(True)
        self.volUSD_30Days.setObjectName("volUSD_30Days")
        self.gridLayout_3.addWidget(self.volUSD_30Days, 2, 1, 1, 1)
        self.volPercent_30Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.volPercent_30Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.volPercent_30Days.setText("")
        self.volPercent_30Days.setReadOnly(True)
        self.volPercent_30Days.setObjectName("volPercent_30Days")
        self.gridLayout_3.addWidget(self.volPercent_30Days, 1, 1, 1, 1)
        self.lb_rangePerc = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_rangePerc.setObjectName("lb_rangePerc")
        self.gridLayout_3.addWidget(self.lb_rangePerc, 3, 0, 1, 1)
        self.lb_VolUSD = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_VolUSD.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lb_VolUSD.setObjectName("lb_VolUSD")
        self.gridLayout_3.addWidget(self.lb_VolUSD, 2, 0, 1, 1)
        self.volPercent_45Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.volPercent_45Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.volPercent_45Days.setText("")
        self.volPercent_45Days.setReadOnly(True)
        self.volPercent_45Days.setObjectName("volPercent_45Days")
        self.gridLayout_3.addWidget(self.volPercent_45Days, 1, 2, 1, 1)
        self.rangeUSD_up_30Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rangeUSD_up_30Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.rangeUSD_up_30Days.setText("")
        self.rangeUSD_up_30Days.setReadOnly(True)
        self.rangeUSD_up_30Days.setObjectName("rangeUSD_up_30Days")
        self.gridLayout_3.addWidget(self.rangeUSD_up_30Days, 6, 1, 1, 1)
        self.lb_rangeUp = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_rangeUp.setObjectName("lb_rangeUp")
        self.gridLayout_3.addWidget(self.lb_rangeUp, 6, 0, 1, 1)
        self.lb_rangeDown = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_rangeDown.setObjectName("lb_rangeDown")
        self.gridLayout_3.addWidget(self.lb_rangeDown, 7, 0, 1, 1)
        self.rangeUSD_up_45Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rangeUSD_up_45Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.rangeUSD_up_45Days.setText("")
        self.rangeUSD_up_45Days.setReadOnly(True)
        self.rangeUSD_up_45Days.setObjectName("rangeUSD_up_45Days")
        self.gridLayout_3.addWidget(self.rangeUSD_up_45Days, 6, 2, 1, 1)
        self.rangeUSD_down_30Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rangeUSD_down_30Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.rangeUSD_down_30Days.setText("")
        self.rangeUSD_down_30Days.setReadOnly(True)
        self.rangeUSD_down_30Days.setObjectName("rangeUSD_down_30Days")
        self.gridLayout_3.addWidget(self.rangeUSD_down_30Days, 7, 1, 1, 1)
        self.rangeUSD_down_45Days = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rangeUSD_down_45Days.setStyleSheet("background-color: rgb(202, 226, 163);")
        self.rangeUSD_down_45Days.setText("")
        self.rangeUSD_down_45Days.setReadOnly(True)
        self.rangeUSD_down_45Days.setObjectName("rangeUSD_down_45Days")
        self.gridLayout_3.addWidget(self.rangeUSD_down_45Days, 7, 2, 1, 1)
        self.lb_MinMaxRg = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_MinMaxRg.setObjectName("lb_MinMaxRg")
        self.gridLayout_3.addWidget(self.lb_MinMaxRg, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(exchange)
        self.label.setGeometry(QtCore.QRect(150, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(exchange)
        self.label_2.setGeometry(QtCore.QRect(810, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(exchange)
        self.line.setGeometry(QtCore.QRect(370, 25, 401, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(exchange)
        self.line_2.setGeometry(QtCore.QRect(1050, 20, 31, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.buttonGetDetail = QtWidgets.QPushButton(exchange)
        self.buttonGetDetail.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.buttonGetDetail.setObjectName("buttonGetDetail")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.button_UpdateVol.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.buttonGetDetail.raise_()

        self.retranslateUi(exchange)
        QtCore.QMetaObject.connectSlotsByName(exchange)

    def retranslateUi(self, exchange):
        _translate = QtCore.QCoreApplication.translate
        exchange.setWindowTitle(_translate("exchange", "IB Option Trader "))
        self.button_UpdateVol.setText(_translate("exchange", "Update Volatility"))
        self.lb_ImpVol.setText(_translate("exchange", "Implied Volatility"))
        self.lb_totalInt.setText(_translate("exchange", "Total Interest:"))
        self.lb_openInt.setText(_translate("exchange", "<html><head/><body><p>Call Open Interest</p></body></html>"))
        self.lb_stockLast.setText(_translate("exchange", "Stock Last:"))
        self.lb_putCallInt.setText(_translate("exchange", "<html><head/><body><p>Put Open Interest</p></body></html>"))
        self.lb_stockClose.setText(_translate("exchange", "Stock Close:"))
        self.lb_Exp.setText(_translate("exchange", "<html><head/><body><p>Days from Expiry:</p></body></html>"))
        self.lb_callVol.setText(_translate("exchange", "Call Volume"))
        self.labelExpiry_2.setText(_translate("exchange", "<html><head/><body><p>Historic Volitility</p></body></html>"))
        self.lb_putVol.setText(_translate("exchange", "Put Volume"))
        self.lb_totalVol.setText(_translate("exchange", "Total Volume:"))
        self.lb_expiry.setText(_translate("exchange", "<html><head/><body><p>Option Expiry:</p></body></html>"))
        self.lb_SecType.setText(_translate("exchange", "Security Type:"))
        self.lb_symbol.setText(_translate("exchange", "Symbol:"))
        self.lb_exchange.setText(_translate("exchange", "Exchange:"))
        self.lb_callPut.setText(_translate("exchange", "Call/Put"))
        self.lb_currency.setText(_translate("exchange", "Currency"))
        self.lb_stk.setText(_translate("exchange", "Strike"))
        self.lb_volPerc.setText(_translate("exchange", "Volitility %"))
        self.lb_rangeUSD.setText(_translate("exchange", "<html><head/><body><p>$ Range +/-</p></body></html>"))
        self.lb_rangePerc.setText(_translate("exchange", "% Range +/-"))
        self.lb_VolUSD.setText(_translate("exchange", "Volatility USD$"))
        self.lb_rangeUp.setText(_translate("exchange", "<html><head/><body><p>$ Range (+) up</p></body></html>"))
        self.lb_rangeDown.setText(_translate("exchange", "<html><head/><body><p>$ Range (-) down</p></body></html>"))
        self.lb_MinMaxRg.setText(_translate("exchange", "Min/Max day Range"))
        self.label.setText(_translate("exchange", "Underlying Detail"))
        self.label_2.setText(_translate("exchange", "Projected Volatility"))
        self.buttonGetDetail.setText(_translate("exchange", "Get Detail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exchange = QtWidgets.QDialog()
    ui = Ui_exchange()
    ui.setupUi(exchange)
    exchange.show()
    sys.exit(app.exec_())

