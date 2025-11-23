# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'course_information.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(336, 373)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"    color: #212121;\n"
"}\n"
"QPushButton{\n"
"    border: none;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"#boton_editar{\n"
"	background-color: #03A9F4; \n"
"}\n"
"#boton_editar:hover {\n"
"    background-color: #8ed1f0; \n"
"}\n"
"\n"
"#frame_barra_superior{\n"
"	background-color: #5c5e61; \n"
"	border-top-right-radius: 10px;\n"
"    border-top-left-radius: 10px;\n"
"	padding:5%;\n"
"}\n"
"\n"
"#label_informacion_del_curso{\n"
"    font-weight: bold;  \n"
"    background-color: #5c5e61; \n"
"	color: #FFFFFF;     \n"
"}\n"
"\n"
"#scrollArea{\n"
"    border: 1px solid #5c5e61;\n"
"\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_barra_superior = QFrame(Form)
        self.frame_barra_superior.setObjectName(u"frame_barra_superior")
        self.frame_barra_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_barra_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_barra_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 0, 0, 0)
        self.label_informacion_del_curso = QLabel(self.frame_barra_superior)
        self.label_informacion_del_curso.setObjectName(u"label_informacion_del_curso")

        self.horizontalLayout.addWidget(self.label_informacion_del_curso)

        self.horizontalSpacer = QSpacerItem(123, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.boton_editar = QPushButton(self.frame_barra_superior)
        self.boton_editar.setObjectName(u"boton_editar")
        self.boton_editar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.boton_editar)


        self.verticalLayout.addWidget(self.frame_barra_superior)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 334, 324))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_informacion_del_curso.setText(QCoreApplication.translate("Form", u"Informacion del curso:", None))
        self.boton_editar.setText("")
    # retranslateUi

