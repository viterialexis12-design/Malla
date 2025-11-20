# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_1.ui'
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
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1044)
        MainWindow.setStyleSheet(u"QFrame , QWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"    color: #212121;\n"
"}\n"
"#titulo{\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#frame_barra_busqueda, #frame_contenedor_perfiles, #frame_informacion_perfil, #frame_informacion_planificacion,#frame_contenedor_planificaciones,#frame_informacion_curso, #frame_contenedor_malla{\n"
"    background-color: #F0F4F7; \n"
"    border-radius: 10px;\n"
"    color: black;	\n"
"}\n"
"\n"
"#frame_contenedor_perfiles, #frame_barra_superior{\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#boton_tema , #boton_github, #boton_ayuda {\n"
"    border: none;\n"
"	color: black; \n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"}\n"
"#boton_tema:hover,\n"
"#boton_github:hover,\n"
"#boton_buscar:hover,\n"
"#boton_crear_perfil:hover,\n"
"#boton_ayuda:hover {\n"
"    background-color: #dbe0e3;         \n"
"	 border-radius: 10px;      \n"
"}\n"
"\n"
"#boton_crear_perfil{\n"
"    background-color: #212121; \n"
""
                        "	border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"#boton_buscar{\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	background-color: rgba(0,0,0,0);\n"
"    padding: 5px;\n"
"}\n"
"\n"
" #linea_buscar{\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.frame_barra_superior = QFrame(self.centralwidget)
        self.frame_barra_superior.setObjectName(u"frame_barra_superior")
        self.frame_barra_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_barra_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_barra_superior)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, -1, 10, -1)
        self.titulo = QLabel(self.frame_barra_superior)
        self.titulo.setObjectName(u"titulo")

        self.horizontalLayout_4.addWidget(self.titulo)

        self.horizontalSpacer = QSpacerItem(1563, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.boton_tema = QPushButton(self.frame_barra_superior)
        self.boton_tema.setObjectName(u"boton_tema")
        # icon = QIcon()
        # icon.addFile(u"../resources/light_theme/moon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_tema.setIcon(icon)
        self.boton_tema.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.boton_tema)

        self.boton_github = QPushButton(self.frame_barra_superior)
        self.boton_github.setObjectName(u"boton_github")
        # icon1 = QIcon()
        # icon1.addFile(u"../resources/light_theme/Github_logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_github.setIcon(icon1)
        self.boton_github.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.boton_github)

        self.boton_ayuda = QPushButton(self.frame_barra_superior)
        self.boton_ayuda.setObjectName(u"boton_ayuda")
        # icon2 = QIcon()
        # icon2.addFile(u"../resources/light_theme/help.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_ayuda.setIcon(icon2)
        self.boton_ayuda.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.boton_ayuda)


        self.verticalLayout.addWidget(self.frame_barra_superior)

        self.frame_contenedor = QFrame(self.centralwidget)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_contenedor)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.barra_izquierda = QFrame(self.frame_contenedor)
        self.barra_izquierda.setObjectName(u"barra_izquierda")
        self.barra_izquierda.setFrameShape(QFrame.Shape.StyledPanel)
        self.barra_izquierda.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.barra_izquierda)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_barra_busqueda = QFrame(self.barra_izquierda)
        self.frame_barra_busqueda.setObjectName(u"frame_barra_busqueda")
        self.frame_barra_busqueda.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_barra_busqueda.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_barra_busqueda)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.barra_buscar = QHBoxLayout()
        self.barra_buscar.setSpacing(0)
        self.barra_buscar.setObjectName(u"barra_buscar")
        self.linea_buscar = QLineEdit(self.frame_barra_busqueda)
        self.linea_buscar.setObjectName(u"linea_buscar")

        self.barra_buscar.addWidget(self.linea_buscar)

        self.boton_buscar = QPushButton(self.frame_barra_busqueda)
        self.boton_buscar.setObjectName(u"boton_buscar")
        # icon3 = QIcon()
        # icon3.addFile(u"../resources/light_theme/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_buscar.setIcon(icon3)
        self.boton_buscar.setIconSize(QSize(20, 20))

        self.barra_buscar.addWidget(self.boton_buscar)


        self.horizontalLayout_6.addLayout(self.barra_buscar)

        self.boton_crear_perfil = QPushButton(self.frame_barra_busqueda)
        self.boton_crear_perfil.setObjectName(u"boton_crear_perfil")
        # icon4 = QIcon()
        # icon4.addFile(u"../resources/light_theme/mas.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.boton_crear_perfil.setIcon(icon4)
        self.boton_crear_perfil.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.boton_crear_perfil)


        self.verticalLayout_4.addWidget(self.frame_barra_busqueda)

        self.frame_contenedor_perfiles = QFrame(self.barra_izquierda)
        self.frame_contenedor_perfiles.setObjectName(u"frame_contenedor_perfiles")
        self.frame_contenedor_perfiles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenedor_perfiles.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_contenedor_perfiles)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea = QScrollArea(self.frame_contenedor_perfiles)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.contenedor = QWidget()
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setGeometry(QRect(0, 0, 365, 904))
        self.verticalLayout_5 = QVBoxLayout(self.contenedor)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea.setWidget(self.contenedor)

        self.horizontalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.frame_contenedor_perfiles)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 15)

        self.horizontalLayout.addWidget(self.barra_izquierda)

        self.frame_5 = QFrame(self.frame_contenedor)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 0, 0, 0)
        self.frame_contenedor_malla = QFrame(self.frame)
        self.frame_contenedor_malla.setObjectName(u"frame_contenedor_malla")
        self.frame_contenedor_malla.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenedor_malla.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_contenedor_malla)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 1, 1, 1)
        self.frame_informacion_curso = QFrame(self.frame_4)
        self.frame_informacion_curso.setObjectName(u"frame_informacion_curso")
        self.frame_informacion_curso.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_informacion_curso.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frame_informacion_curso)

        self.frame_contenedor_planificaciones = QFrame(self.frame_4)
        self.frame_contenedor_planificaciones.setObjectName(u"frame_contenedor_planificaciones")
        self.frame_contenedor_planificaciones.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenedor_planificaciones.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frame_contenedor_planificaciones)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.horizontalLayout_3.setStretch(0, 7)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 1, 1, 1)
        self.frame_informacion_perfil = QFrame(self.frame_2)
        self.frame_informacion_perfil.setObjectName(u"frame_informacion_perfil")
        self.frame_informacion_perfil.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_informacion_perfil.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_informacion_perfil)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout_2.addWidget(self.frame_informacion_perfil)

        self.frame_informacion_planificacion = QFrame(self.frame_2)
        self.frame_informacion_planificacion.setObjectName(u"frame_informacion_planificacion")
        self.frame_informacion_planificacion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_informacion_planificacion.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_informacion_planificacion)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_2.addWidget(self.frame_informacion_planificacion)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 3)

        self.horizontalLayout.addWidget(self.frame_5)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout.addWidget(self.frame_contenedor)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 35)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Malla Proyect", None))
        self.boton_tema.setText("")
        self.boton_github.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.boton_ayuda.setText("")
        self.linea_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar perfiles", None))
        self.boton_buscar.setText("")
        self.boton_crear_perfil.setText("")
    # retranslateUi

