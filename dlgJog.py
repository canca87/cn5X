# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgJog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgJog(object):
  def setupUi(self, dlgJog):
    dlgJog.setObjectName("dlgJog")
    dlgJog.resize(345, 260)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/cn5X/images/XYZAB.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    dlgJog.setWindowIcon(icon)
    self.horizontalLayout_3 = QtWidgets.QHBoxLayout(dlgJog)
    self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
    self.horizontalLayout_3.setSpacing(4)
    self.horizontalLayout_3.setObjectName("horizontalLayout_3")
    self.qwGauche = QtWidgets.QWidget(dlgJog)
    self.qwGauche.setObjectName("qwGauche")
    self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.qwGauche)
    self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_4.setSpacing(0)
    self.verticalLayout_4.setObjectName("verticalLayout_4")
    self.frmMWPos = QtWidgets.QFrame(self.qwGauche)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.frmMWPos.sizePolicy().hasHeightForWidth())
    self.frmMWPos.setSizePolicy(sizePolicy)
    self.frmMWPos.setObjectName("frmMWPos")
    self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmMWPos)
    self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_2.setSpacing(0)
    self.verticalLayout_2.setObjectName("verticalLayout_2")
    self.rbtMPos = QtWidgets.QRadioButton(self.frmMWPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.rbtMPos.sizePolicy().hasHeightForWidth())
    self.rbtMPos.setSizePolicy(sizePolicy)
    self.rbtMPos.setObjectName("rbtMPos")
    self.verticalLayout_2.addWidget(self.rbtMPos)
    self.rbtWPos = QtWidgets.QRadioButton(self.frmMWPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.rbtWPos.sizePolicy().hasHeightForWidth())
    self.rbtWPos.setSizePolicy(sizePolicy)
    self.rbtWPos.setChecked(True)
    self.rbtWPos.setObjectName("rbtWPos")
    self.verticalLayout_2.addWidget(self.rbtWPos)
    self.verticalLayout_4.addWidget(self.frmMWPos)
    self.widget = QtWidgets.QWidget(self.qwGauche)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
    self.widget.setSizePolicy(sizePolicy)
    self.widget.setObjectName("widget")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 8)
    self.horizontalLayout.setSpacing(0)
    self.horizontalLayout.setObjectName("horizontalLayout")
    spacerItem = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.frmG90G91 = QtWidgets.QFrame(self.widget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.frmG90G91.sizePolicy().hasHeightForWidth())
    self.frmG90G91.setSizePolicy(sizePolicy)
    self.frmG90G91.setFrameShape(QtWidgets.QFrame.Box)
    self.frmG90G91.setObjectName("frmG90G91")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.frmG90G91)
    self.verticalLayout.setContentsMargins(4, 2, 4, 0)
    self.verticalLayout.setSpacing(0)
    self.verticalLayout.setObjectName("verticalLayout")
    self.rbtG90 = QtWidgets.QRadioButton(self.frmG90G91)
    self.rbtG90.setChecked(True)
    self.rbtG90.setObjectName("rbtG90")
    self.verticalLayout.addWidget(self.rbtG90)
    self.rbtG91 = QtWidgets.QRadioButton(self.frmG90G91)
    self.rbtG91.setObjectName("rbtG91")
    self.verticalLayout.addWidget(self.rbtG91)
    self.horizontalLayout.addWidget(self.frmG90G91)
    spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem1)
    self.verticalLayout_4.addWidget(self.widget)
    self.gridValues = QtWidgets.QWidget(self.qwGauche)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.gridValues.sizePolicy().hasHeightForWidth())
    self.gridValues.setSizePolicy(sizePolicy)
    self.gridValues.setObjectName("gridValues")
    self.gridLayout = QtWidgets.QGridLayout(self.gridValues)
    self.gridLayout.setContentsMargins(0, 0, 0, 0)
    self.gridLayout.setVerticalSpacing(2)
    self.gridLayout.setObjectName("gridLayout")
    self.chkJogX = QtWidgets.QCheckBox(self.gridValues)
    self.chkJogX.setObjectName("chkJogX")
    self.gridLayout.addWidget(self.chkJogX, 0, 0, 1, 1)
    self.dsbJogX = QtWidgets.QDoubleSpinBox(self.gridValues)
    self.dsbJogX.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbJogX.setStyleSheet("color: #bebebe;")
    self.dsbJogX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbJogX.setDecimals(3)
    self.dsbJogX.setMinimum(-10000.0)
    self.dsbJogX.setMaximum(10000.0)
    self.dsbJogX.setSingleStep(0.1)
    self.dsbJogX.setProperty("value", 0.0)
    self.dsbJogX.setObjectName("dsbJogX")
    self.gridLayout.addWidget(self.dsbJogX, 0, 1, 1, 1)
    self.btnJogX = cnQPushButton(self.gridValues)
    self.btnJogX.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnJogX.sizePolicy().hasHeightForWidth())
    self.btnJogX.setSizePolicy(sizePolicy)
    self.btnJogX.setMinimumSize(QtCore.QSize(46, 23))
    self.btnJogX.setMaximumSize(QtCore.QSize(46, 23))
    self.btnJogX.setBaseSize(QtCore.QSize(60, 60))
    self.btnJogX.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnJogX.setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(":/cn5X/images/btnJogX.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnJogX.setIcon(icon1)
    self.btnJogX.setIconSize(QtCore.QSize(42, 21))
    self.btnJogX.setAutoDefault(False)
    self.btnJogX.setObjectName("btnJogX")
    self.gridLayout.addWidget(self.btnJogX, 0, 2, 1, 1)
    self.chkJogY = QtWidgets.QCheckBox(self.gridValues)
    self.chkJogY.setObjectName("chkJogY")
    self.gridLayout.addWidget(self.chkJogY, 1, 0, 1, 1)
    self.dsbJogY = QtWidgets.QDoubleSpinBox(self.gridValues)
    self.dsbJogY.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbJogY.setStyleSheet("color: #bebebe;")
    self.dsbJogY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbJogY.setDecimals(3)
    self.dsbJogY.setMinimum(-10000.0)
    self.dsbJogY.setMaximum(10000.0)
    self.dsbJogY.setSingleStep(0.1)
    self.dsbJogY.setProperty("value", 0.0)
    self.dsbJogY.setObjectName("dsbJogY")
    self.gridLayout.addWidget(self.dsbJogY, 1, 1, 1, 1)
    self.btnJogY = cnQPushButton(self.gridValues)
    self.btnJogY.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnJogY.sizePolicy().hasHeightForWidth())
    self.btnJogY.setSizePolicy(sizePolicy)
    self.btnJogY.setMinimumSize(QtCore.QSize(46, 23))
    self.btnJogY.setMaximumSize(QtCore.QSize(46, 23))
    self.btnJogY.setBaseSize(QtCore.QSize(60, 60))
    self.btnJogY.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnJogY.setText("")
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(":/cn5X/images/btnJogY.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnJogY.setIcon(icon2)
    self.btnJogY.setIconSize(QtCore.QSize(42, 21))
    self.btnJogY.setAutoDefault(False)
    self.btnJogY.setObjectName("btnJogY")
    self.gridLayout.addWidget(self.btnJogY, 1, 2, 1, 1)
    self.chkJogZ = QtWidgets.QCheckBox(self.gridValues)
    self.chkJogZ.setObjectName("chkJogZ")
    self.gridLayout.addWidget(self.chkJogZ, 2, 0, 1, 1)
    self.dsbJogZ = QtWidgets.QDoubleSpinBox(self.gridValues)
    self.dsbJogZ.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbJogZ.setStyleSheet("color: #bebebe;")
    self.dsbJogZ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbJogZ.setDecimals(3)
    self.dsbJogZ.setMinimum(-10000.0)
    self.dsbJogZ.setMaximum(10000.0)
    self.dsbJogZ.setSingleStep(0.1)
    self.dsbJogZ.setProperty("value", 0.0)
    self.dsbJogZ.setObjectName("dsbJogZ")
    self.gridLayout.addWidget(self.dsbJogZ, 2, 1, 1, 1)
    self.btnJogZ = cnQPushButton(self.gridValues)
    self.btnJogZ.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnJogZ.sizePolicy().hasHeightForWidth())
    self.btnJogZ.setSizePolicy(sizePolicy)
    self.btnJogZ.setMinimumSize(QtCore.QSize(46, 23))
    self.btnJogZ.setMaximumSize(QtCore.QSize(46, 23))
    self.btnJogZ.setBaseSize(QtCore.QSize(60, 60))
    self.btnJogZ.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnJogZ.setText("")
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(":/cn5X/images/btnJogZ.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnJogZ.setIcon(icon3)
    self.btnJogZ.setIconSize(QtCore.QSize(42, 21))
    self.btnJogZ.setAutoDefault(False)
    self.btnJogZ.setObjectName("btnJogZ")
    self.gridLayout.addWidget(self.btnJogZ, 2, 2, 1, 1)
    self.chkJogA = QtWidgets.QCheckBox(self.gridValues)
    self.chkJogA.setObjectName("chkJogA")
    self.gridLayout.addWidget(self.chkJogA, 3, 0, 1, 1)
    self.dsbJogA = QtWidgets.QDoubleSpinBox(self.gridValues)
    self.dsbJogA.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbJogA.setStyleSheet("color: #bebebe;")
    self.dsbJogA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbJogA.setDecimals(3)
    self.dsbJogA.setMinimum(-10000.0)
    self.dsbJogA.setMaximum(10000.0)
    self.dsbJogA.setSingleStep(0.1)
    self.dsbJogA.setProperty("value", 0.0)
    self.dsbJogA.setObjectName("dsbJogA")
    self.gridLayout.addWidget(self.dsbJogA, 3, 1, 1, 1)
    self.btnJogA = cnQPushButton(self.gridValues)
    self.btnJogA.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnJogA.sizePolicy().hasHeightForWidth())
    self.btnJogA.setSizePolicy(sizePolicy)
    self.btnJogA.setMinimumSize(QtCore.QSize(46, 23))
    self.btnJogA.setMaximumSize(QtCore.QSize(46, 23))
    self.btnJogA.setBaseSize(QtCore.QSize(60, 60))
    self.btnJogA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnJogA.setText("")
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(":/cn5X/images/btnJogA.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnJogA.setIcon(icon4)
    self.btnJogA.setIconSize(QtCore.QSize(42, 21))
    self.btnJogA.setAutoDefault(False)
    self.btnJogA.setObjectName("btnJogA")
    self.gridLayout.addWidget(self.btnJogA, 3, 2, 1, 1)
    self.chkJogB = QtWidgets.QCheckBox(self.gridValues)
    self.chkJogB.setObjectName("chkJogB")
    self.gridLayout.addWidget(self.chkJogB, 4, 0, 1, 1)
    self.dsbJogB = QtWidgets.QDoubleSpinBox(self.gridValues)
    self.dsbJogB.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbJogB.setStyleSheet("color: #bebebe;")
    self.dsbJogB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbJogB.setDecimals(3)
    self.dsbJogB.setMinimum(-10000.0)
    self.dsbJogB.setMaximum(10000.0)
    self.dsbJogB.setSingleStep(0.1)
    self.dsbJogB.setProperty("value", 0.0)
    self.dsbJogB.setObjectName("dsbJogB")
    self.gridLayout.addWidget(self.dsbJogB, 4, 1, 1, 1)
    self.btnJogB = cnQPushButton(self.gridValues)
    self.btnJogB.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnJogB.sizePolicy().hasHeightForWidth())
    self.btnJogB.setSizePolicy(sizePolicy)
    self.btnJogB.setMinimumSize(QtCore.QSize(46, 23))
    self.btnJogB.setMaximumSize(QtCore.QSize(46, 23))
    self.btnJogB.setBaseSize(QtCore.QSize(60, 60))
    self.btnJogB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnJogB.setText("")
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap(":/cn5X/images/btnJogB.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnJogB.setIcon(icon5)
    self.btnJogB.setIconSize(QtCore.QSize(42, 21))
    self.btnJogB.setAutoDefault(False)
    self.btnJogB.setObjectName("btnJogB")
    self.gridLayout.addWidget(self.btnJogB, 4, 2, 1, 1)
    self.chkJogC = QtWidgets.QCheckBox(self.gridValues)
    self.chkJogC.setObjectName("chkJogC")
    self.gridLayout.addWidget(self.chkJogC, 5, 0, 1, 1)
    self.dsbJogC = QtWidgets.QDoubleSpinBox(self.gridValues)
    self.dsbJogC.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbJogC.setStyleSheet("color: #bebebe;")
    self.dsbJogC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbJogC.setDecimals(3)
    self.dsbJogC.setMinimum(-10000.0)
    self.dsbJogC.setMaximum(10000.0)
    self.dsbJogC.setSingleStep(0.1)
    self.dsbJogC.setProperty("value", 0.0)
    self.dsbJogC.setObjectName("dsbJogC")
    self.gridLayout.addWidget(self.dsbJogC, 5, 1, 1, 1)
    self.btnJogC = cnQPushButton(self.gridValues)
    self.btnJogC.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnJogC.sizePolicy().hasHeightForWidth())
    self.btnJogC.setSizePolicy(sizePolicy)
    self.btnJogC.setMinimumSize(QtCore.QSize(46, 23))
    self.btnJogC.setMaximumSize(QtCore.QSize(46, 23))
    self.btnJogC.setBaseSize(QtCore.QSize(60, 60))
    self.btnJogC.setText("")
    icon6 = QtGui.QIcon()
    icon6.addPixmap(QtGui.QPixmap(":/cn5X/images/btnJogC.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnJogC.setIcon(icon6)
    self.btnJogC.setIconSize(QtCore.QSize(42, 21))
    self.btnJogC.setAutoDefault(False)
    self.btnJogC.setObjectName("btnJogC")
    self.gridLayout.addWidget(self.btnJogC, 5, 2, 1, 1)
    self.verticalLayout_4.addWidget(self.gridValues)
    self.horizontalLayout_3.addWidget(self.qwGauche)
    self.qwDroite = QtWidgets.QWidget(dlgJog)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.qwDroite.sizePolicy().hasHeightForWidth())
    self.qwDroite.setSizePolicy(sizePolicy)
    self.qwDroite.setObjectName("qwDroite")
    self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.qwDroite)
    self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_6.setSpacing(0)
    self.verticalLayout_6.setObjectName("verticalLayout_6")
    self.qwJogSpeed = QtWidgets.QWidget(self.qwDroite)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.qwJogSpeed.sizePolicy().hasHeightForWidth())
    self.qwJogSpeed.setSizePolicy(sizePolicy)
    self.qwJogSpeed.setObjectName("qwJogSpeed")
    self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.qwJogSpeed)
    self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_3.setSpacing(0)
    self.verticalLayout_3.setObjectName("verticalLayout_3")
    self.label = QtWidgets.QLabel(self.qwJogSpeed)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setObjectName("label")
    self.verticalLayout_3.addWidget(self.label)
    self.dsbJogSpeed = QtWidgets.QDoubleSpinBox(self.qwJogSpeed)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.dsbJogSpeed.sizePolicy().hasHeightForWidth())
    self.dsbJogSpeed.setSizePolicy(sizePolicy)
    self.dsbJogSpeed.setMaximumSize(QtCore.QSize(80, 80))
    self.dsbJogSpeed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbJogSpeed.setDecimals(2)
    self.dsbJogSpeed.setMaximum(10000.0)
    self.dsbJogSpeed.setProperty("value", 100.0)
    self.dsbJogSpeed.setObjectName("dsbJogSpeed")
    self.verticalLayout_3.addWidget(self.dsbJogSpeed)
    self.verticalLayout_6.addWidget(self.qwJogSpeed)
    spacerItem2 = QtWidgets.QSpacerItem(25, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.verticalLayout_6.addItem(spacerItem2)
    self.qwButtonsV = QtWidgets.QWidget(self.qwDroite)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.qwButtonsV.sizePolicy().hasHeightForWidth())
    self.qwButtonsV.setSizePolicy(sizePolicy)
    self.qwButtonsV.setObjectName("qwButtonsV")
    self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.qwButtonsV)
    self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_5.setSpacing(2)
    self.verticalLayout_5.setObjectName("verticalLayout_5")
    self.btnJog = cnQPushButton(self.qwButtonsV)
    self.btnJog.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnJog.sizePolicy().hasHeightForWidth())
    self.btnJog.setSizePolicy(sizePolicy)
    self.btnJog.setMinimumSize(QtCore.QSize(80, 80))
    self.btnJog.setMaximumSize(QtCore.QSize(80, 80))
    self.btnJog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnJog.setText("")
    self.btnJog.setIcon(icon)
    self.btnJog.setIconSize(QtCore.QSize(78, 78))
    self.btnJog.setAutoDefault(False)
    self.btnJog.setDefault(True)
    self.btnJog.setObjectName("btnJog")
    self.verticalLayout_5.addWidget(self.btnJog)
    self.btnJogStop = cnQPushButton(self.qwButtonsV)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnJogStop.sizePolicy().hasHeightForWidth())
    self.btnJogStop.setSizePolicy(sizePolicy)
    self.btnJogStop.setMinimumSize(QtCore.QSize(80, 80))
    self.btnJogStop.setMaximumSize(QtCore.QSize(80, 80))
    self.btnJogStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnJogStop.setText("")
    icon7 = QtGui.QIcon()
    icon7.addPixmap(QtGui.QPixmap(":/cn5X/images/btnJogStop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnJogStop.setIcon(icon7)
    self.btnJogStop.setIconSize(QtCore.QSize(78, 78))
    self.btnJogStop.setAutoDefault(False)
    self.btnJogStop.setObjectName("btnJogStop")
    self.verticalLayout_5.addWidget(self.btnJogStop)
    self.buttonBox = QtWidgets.QDialogButtonBox(self.qwButtonsV)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
    self.buttonBox.setSizePolicy(sizePolicy)
    self.buttonBox.setOrientation(QtCore.Qt.Vertical)
    self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
    self.buttonBox.setObjectName("buttonBox")
    self.verticalLayout_5.addWidget(self.buttonBox)
    self.verticalLayout_6.addWidget(self.qwButtonsV)
    self.horizontalLayout_3.addWidget(self.qwDroite)

    self.retranslateUi(dlgJog)
    QtCore.QMetaObject.connectSlotsByName(dlgJog)

  def retranslateUi(self, dlgJog):
    _translate = QtCore.QCoreApplication.translate
    dlgJog.setWindowTitle(_translate("dlgJog", "Jog to location"))
    self.rbtMPos.setText(_translate("dlgJog", "Use machine position (MPos - G53)"))
    self.rbtWPos.setText(_translate("dlgJog", "Use working position (WPos)"))
    self.rbtG90.setText(_translate("dlgJog", "Absolute move (G90)"))
    self.rbtG91.setText(_translate("dlgJog", "Relative move (G91)"))
    self.chkJogX.setText(_translate("dlgJog", "Jog X axis"))
    self.btnJogX.setToolTip(_translate("dlgJog", "Jog X axis"))
    self.chkJogY.setText(_translate("dlgJog", "Jog Y axis"))
    self.btnJogY.setToolTip(_translate("dlgJog", "Jog Y axis"))
    self.chkJogZ.setText(_translate("dlgJog", "Jog Z axis"))
    self.btnJogZ.setToolTip(_translate("dlgJog", "Jog Z axis"))
    self.chkJogA.setText(_translate("dlgJog", "Jog A axis"))
    self.btnJogA.setToolTip(_translate("dlgJog", "Jog A axis"))
    self.chkJogB.setText(_translate("dlgJog", "Jog B axis"))
    self.btnJogB.setToolTip(_translate("dlgJog", "Jog B axis"))
    self.chkJogC.setText(_translate("dlgJog", "Jog C axis"))
    self.btnJogC.setToolTip(_translate("dlgJog", "Jog C axis"))
    self.label.setText(_translate("dlgJog", "Jog speed\n"
"(mm/mn)"))
    self.btnJog.setToolTip(_translate("dlgJog", "Jog all selected axis."))
    self.btnJogStop.setToolTip(_translate("dlgJog", "Stop jogging"))

from cnQPushButton import cnQPushButton
import cn5X_rc