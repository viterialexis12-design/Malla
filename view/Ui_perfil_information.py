# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perfil_information.ui'
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
"#barra_superior{\n"
"	background-color: #434444; \n"
"	border-top-right-radius: 5px;\n"
"    padding:5%;\n"
"}\n"
"\n"
"#frame_contenido{\n"
"	border-right: 1px solid #434444;\n"
"    border-left: 1px solid #434444;\n"
"    border-bottom: 1px solid #434444;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"#label_cursos_habilitados, #label_malla{\n"
"	background-color: #212121;\n"
"    font-weight: bold;     \n"
"}\n"
"\n"
"#label_informacion_perfil{\n"
"	background-color: #434444; \n"
"	color: #FFFFFF;\n"
"	font-weight: bold;     \n"
"}\n"
"#label_nombre_perfil{\n"
""
                        "	background-color: #434444; \n"
"	color: #FFFFFF;     \n"
"}\n"
"\n"
"\n"
"#frame, #frame_2{\n"
"    border: 2px solid #434444;;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.barra_superior = QFrame(Form)
        self.barra_superior.setObjectName(u"barra_superior")
        self.barra_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.barra_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.barra_superior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 0, 0, 0)
        self.label_informacion_perfil = QLabel(self.barra_superior)
        self.label_informacion_perfil.setObjectName(u"label_informacion_perfil")

        self.horizontalLayout_2.addWidget(self.label_informacion_perfil)

        self.label_nombre_perfil = QLabel(self.barra_superior)
        self.label_nombre_perfil.setObjectName(u"label_nombre_perfil")

        self.horizontalLayout_2.addWidget(self.label_nombre_perfil)

        self.horizontalSpacer = QSpacerItem(454, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.boton_editar = QPushButton(self.barra_superior)
        self.boton_editar.setObjectName(u"boton_editar")
        # icon = QIcon()
        # icon.addFile(u"../resources/light_theme/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_editar.setIcon(icon)
        self.boton_editar.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.boton_editar)

        self.boton_borrar = QPushButton(self.barra_superior)
        self.boton_borrar.setObjectName(u"boton_borrar")
        # icon1 = QIcon()
        # icon1.addFile(u"../resources/light_theme/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_borrar.setIcon(icon1)
        self.boton_borrar.setIconSize(QSize(20, 20))
        self.horizontalLayout_2.addWidget(self.boton_borrar)


        self.verticalLayout.addWidget(self.barra_superior)

        self.frame_contenido = QFrame(Form)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_contenido)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 0, 0, 0)
        self.label_cursos_habilitados = QLabel(self.frame)
        self.label_cursos_habilitados.setObjectName(u"label_cursos_habilitados")

        self.verticalLayout_2.addWidget(self.label_cursos_habilitados)

        self.scrollArea_cursos = QScrollArea(self.frame)
        self.scrollArea_cursos.setObjectName(u"scrollArea_cursos")
        self.scrollArea_cursos.setWidgetResizable(True)
        self.scrollAreaWidgetContents_cursos = QWidget()
        self.scrollAreaWidgetContents_cursos.setObjectName(u"scrollAreaWidgetContents_cursos")
        self.scrollAreaWidgetContents_cursos.setGeometry(QRect(0, 0, 394, 157))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_cursos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_cursos.setWidget(self.scrollAreaWidgetContents_cursos)

        self.verticalLayout_2.addWidget(self.scrollArea_cursos)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_contenido)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 0, 0, 0)
        self.label_malla = QLabel(self.frame_3)
        self.label_malla.setObjectName(u"label_malla")

        self.horizontalLayout_3.addWidget(self.label_malla)

        self.label_malla_nombre = QLabel(self.frame_3)
        self.label_malla_nombre.setObjectName(u"label_malla_nombre")

        self.horizontalLayout_3.addWidget(self.label_malla_nombre)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.scrollArea_malla = QScrollArea(self.frame_2)
        self.scrollArea_malla.setObjectName(u"scrollArea_malla")
        self.scrollArea_malla.setWidgetResizable(True)
        self.scrollAreaWidgetContents_malla = QWidget()
        self.scrollAreaWidgetContents_malla.setObjectName(u"scrollAreaWidgetContents_malla")
        self.scrollAreaWidgetContents_malla.setGeometry(QRect(0, 0, 394, 157))
        self.scrollArea_malla.setWidget(self.scrollAreaWidgetContents_malla)

        self.verticalLayout_3.addWidget(self.scrollArea_malla)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_contenido)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_informacion_perfil.setText(QCoreApplication.translate("Form", u"Informacion del perfil:", None))
        self.label_nombre_perfil.setText(QCoreApplication.translate("Form", u"Cosa esta aaaa", None))
        self.boton_editar.setText("")
        self.boton_borrar.setText("")
        self.label_cursos_habilitados.setText(QCoreApplication.translate("Form", u"Cursos para los que esta habilitado:", None))
        self.label_malla.setText(QCoreApplication.translate("Form", u"Malla:", None))
        self.label_malla_nombre.setText(QCoreApplication.translate("Form", u"Curso para bailar mambo", None))
    # retranslateUi

