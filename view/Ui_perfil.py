# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perfil.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(553, 300)
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
"#Form{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#boton_editar_perfil{\n"
"	background-color: #FFC107; \n"
"}\n"
"#boton_borrar_perfil{\n"
"  	background-color: #DC3545; \n"
"}\n"
"#boton_editar_perfil:hover,\n"
"#boton_borrar_perfil:hover {\n"
"    background-color: #dbe0e3;      \n"
"}\n"
"\n"
"#barra_superior{\n"
"	background-color: black; \n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"#frame_contenedor_contenido_perfil, #frame_3{\n"
"	border: 1px solid black;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#nombre_perfil {\n"
"	background-color: black; \n"
"	color: white;\n"
"    font-weight: bold;     \n"
"}\n"
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
        self.nombre_perfil = QLabel(self.barra_superior)
        self.nombre_perfil.setObjectName(u"nombre_perfil")

        self.horizontalLayout_2.addWidget(self.nombre_perfil)

        self.horizontalSpacer = QSpacerItem(269, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.boton_editar_perfil = QPushButton(self.barra_superior)
        self.boton_editar_perfil.setObjectName(u"boton_editar_perfil")
        # icon = QIcon()
        # icon.addFile(u"../Malla/view/resources/light_theme/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_editar_perfil.setIcon(icon)
        self.boton_editar_perfil.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.boton_editar_perfil)

        self.boton_borrar_perfil = QPushButton(self.barra_superior)
        self.boton_borrar_perfil.setObjectName(u"boton_borrar_perfil")
        # icon1 = QIcon()
        # icon1.addFile(u"../Malla/view/resources/light_theme/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_borrar_perfil.setIcon(icon1)
        self.boton_borrar_perfil.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.boton_borrar_perfil)


        self.verticalLayout.addWidget(self.barra_superior)

        self.frame_contenedor_contenido_perfil = QFrame(Form)
        self.frame_contenedor_contenido_perfil.setObjectName(u"frame_contenedor_contenido_perfil")
        self.frame_contenedor_contenido_perfil.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenedor_contenido_perfil.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_contenedor_contenido_perfil)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_contenedor_contenido_perfil)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, 0)
        self.label_malla_perfil = QLabel(self.frame_3)
        self.label_malla_perfil.setObjectName(u"label_malla_perfil")

        self.verticalLayout_2.addWidget(self.label_malla_perfil)

        self.label_fecha_creada_perfil = QLabel(self.frame_3)
        self.label_fecha_creada_perfil.setObjectName(u"label_fecha_creada_perfil")

        self.verticalLayout_2.addWidget(self.label_fecha_creada_perfil)

        self.label_nota_perfil = QLabel(self.frame_3)
        self.label_nota_perfil.setObjectName(u"label_nota_perfil")

        self.verticalLayout_2.addWidget(self.label_nota_perfil)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalLayout.setStretch(0, 2)

        self.verticalLayout.addWidget(self.frame_contenedor_contenido_perfil)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nombre_perfil.setText(QCoreApplication.translate("Form", u"Perfil para la cosa esta aaaaa", None))
        self.boton_editar_perfil.setText("")
        self.boton_borrar_perfil.setText("")
        self.label_malla_perfil.setText(QCoreApplication.translate("Form", u"label_malla_perfil", None))
        self.label_fecha_creada_perfil.setText(QCoreApplication.translate("Form", u"label_fecha_creada_perfil", None))
        self.label_nota_perfil.setText(QCoreApplication.translate("Form", u"label_nota_perfil", None))
    # retranslateUi

