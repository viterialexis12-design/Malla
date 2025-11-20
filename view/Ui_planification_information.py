# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'planification_information.ui'
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
        Form.resize(800, 250)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #212121;\n"
"    border: none;\n"
"    color: #B0BEC5;\n"
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
"#boton_borrar{\n"
"  	background-color: #D32F2F; \n"
"}\n"
"#boton_editar:hover {\n"
"    background-color: #8ed1f0; \n"
"}\n"
"#boton_borrar:hover {\n"
"    background-color: #df7b79; \n"
"}\n"
"\n"
"#frame_barra_superior{\n"
"	background-color: #434444; \n"
"	border-top-right-radius: 10px;\n"
"	padding:5%;\n"
"}\n"
"\n"
"#frame_contenido{\n"
"	border-right: 1px solid #434444;\n"
"	border-left: 1px solid #434444;\n"
"	border-bottom: 1px solid #434444;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#label_planificacion{\n"
"    font-weight: bold;     \n"
"}\n"
"\n"
"#label_nombre_planificacion, #label_planificacion ,#label_nota,#frame_inferior{\n"
"	background-color: #434444; \n"
"	color: #FFFFFF;    \n"
"}\n"
"\n"
"#frame_inferior, #frame_contenido{\n"
"	"
                        "border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#scrollArea_planificacion,#scrollArea_proximo{\n"
"    border: 1px solid #434444;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 0, 0, 0)
        self.frame_barra_superior = QFrame(Form)
        self.frame_barra_superior.setObjectName(u"frame_barra_superior")
        self.frame_barra_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_barra_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_barra_superior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 0, 0, 0)
        self.label_planificacion = QLabel(self.frame_barra_superior)
        self.label_planificacion.setObjectName(u"label_planificacion")

        self.horizontalLayout_2.addWidget(self.label_planificacion)

        self.label_nombre_planificacion = QLabel(self.frame_barra_superior)
        self.label_nombre_planificacion.setObjectName(u"label_nombre_planificacion")

        self.horizontalLayout_2.addWidget(self.label_nombre_planificacion)

        self.horizontalSpacer = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.boton_editar = QPushButton(self.frame_barra_superior)
        self.boton_editar.setObjectName(u"boton_editar")
        # icon = QIcon()
        # icon.addFile(u"../resources/light_theme/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_editar.setIcon(icon)
        self.boton_editar.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.boton_editar)

        self.boton_borrar = QPushButton(self.frame_barra_superior)
        self.boton_borrar.setObjectName(u"boton_borrar")
        # icon1 = QIcon()
        # icon1.addFile(u"../resources/light_theme/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_borrar.setIcon(icon1)
        self.boton_borrar.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.boton_borrar)


        self.verticalLayout.addWidget(self.frame_barra_superior)

        self.frame_contenido = QFrame(Form)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenido)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_central = QFrame(self.frame_contenido)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_central)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_planificacion = QScrollArea(self.frame_central)
        self.scrollArea_planificacion.setObjectName(u"scrollArea_planificacion")
        self.scrollArea_planificacion.setWidgetResizable(True)
        self.scrollAreaWidgetContents_planificacion = QWidget()
        self.scrollAreaWidgetContents_planificacion.setObjectName(u"scrollAreaWidgetContents_planificacion")
        self.scrollAreaWidgetContents_planificacion.setGeometry(QRect(0, 0, 397, 161))
        self.scrollArea_planificacion.setWidget(self.scrollAreaWidgetContents_planificacion)

        self.horizontalLayout.addWidget(self.scrollArea_planificacion)

        self.scrollArea_proximo = QScrollArea(self.frame_central)
        self.scrollArea_proximo.setObjectName(u"scrollArea_proximo")
        self.scrollArea_proximo.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2_proximo = QWidget()
        self.scrollAreaWidgetContents_2_proximo.setObjectName(u"scrollAreaWidgetContents_2_proximo")
        self.scrollAreaWidgetContents_2_proximo.setGeometry(QRect(0, 0, 396, 161))
        self.scrollArea_proximo.setWidget(self.scrollAreaWidgetContents_2_proximo)

        self.horizontalLayout.addWidget(self.scrollArea_proximo)


        self.verticalLayout_2.addWidget(self.frame_central)

        self.frame_inferior = QFrame(self.frame_contenido)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_inferior)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_nota = QLabel(self.frame_inferior)
        self.label_nota.setObjectName(u"label_nota")

        self.verticalLayout_3.addWidget(self.label_nota)


        self.verticalLayout_2.addWidget(self.frame_inferior)

        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_contenido)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_planificacion.setText(QCoreApplication.translate("Form", u"planificacion:", None))
        self.label_nombre_planificacion.setText(QCoreApplication.translate("Form", u"label_nombre_planificacion", None))
        self.boton_editar.setText("")
        self.boton_borrar.setText("")
        self.label_nota.setText(QCoreApplication.translate("Form", u"Nota:", None))
    # retranslateUi

