# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'course.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 250)
        Form.setStyleSheet(u"QWidget{\n"
"    background-color: #212121;\n"
"}\n"
"QLabel{\n"
"    border: 1px solid #5A5A5A;\n"
"    color: #B0BEC5;\n"
"}\n"
"#frame_container{\n"
"    background-color: #212121;\n"
"    border-radius: 15%;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"#label_code,#label_name{\n"
"    font: bold;\n"
"    background-color: #5A5A5A; \n"
"    color: #FFFFFF;\n"
"    padding-left: 5%;\n"
"    padding-right: 5%;\n"
"}\n"
"\n"
"#frame_top_bar{\n"
"    background-color: #5A5A5A; \n"
"    border-top-right-radius: 10%;\n"
"    border-top-left-radius: 10%;\n"
"    padding:5%;\n"
"}\n"
"\n"
"#frame_grid{\n"
"    border-bottom-right-radius: 10%;\n"
"    border-bottom-left-radius: 10%;\n"
"}\n"
"#label_total_credits{\n"
"    border-bottom-right-radius: 10%;\n"
"}\n"
"\n"
"#label_cd_hours{\n"
"    border-bottom-left-radius: 10%;\n"
"}\n"
"\n"
"#frame_prerequisites{\n"
"    border:none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_container = QFrame(Form)
        self.frame_container.setObjectName(u"frame_container")
        self.frame_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_bar = QFrame(self.frame_container)
        self.frame_top_bar.setObjectName(u"frame_top_bar")
        self.frame_top_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_top_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_code = QLabel(self.frame_top_bar)
        self.label_code.setObjectName(u"label_code")

        self.horizontalLayout_2.addWidget(self.label_code)

        self.horizontalSpacer = QSpacerItem(172, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_name = QLabel(self.frame_top_bar)
        self.label_name.setObjectName(u"label_name")

        self.horizontalLayout_2.addWidget(self.label_name)


        self.verticalLayout.addWidget(self.frame_top_bar)

        self.frame_prerequisites = QFrame(self.frame_container)
        self.frame_prerequisites.setObjectName(u"frame_prerequisites")
        self.frame_prerequisites.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_prerequisites.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_prerequisites)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_prerequisites)

        self.frame_grid = QFrame(self.frame_container)
        self.frame_grid.setObjectName(u"frame_grid")
        self.frame_grid.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grid.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_grid)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_cd_t = QLabel(self.frame_grid)
        self.label_cd_t.setObjectName(u"label_cd_t")
        self.label_cd_t.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_cd_t, 0, 0, 1, 1)

        self.label_cpe_t = QLabel(self.frame_grid)
        self.label_cpe_t.setObjectName(u"label_cpe_t")
        self.label_cpe_t.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_cpe_t, 0, 1, 1, 1)

        self.label_ca_t = QLabel(self.frame_grid)
        self.label_ca_t.setObjectName(u"label_ca_t")
        self.label_ca_t.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_ca_t, 0, 2, 1, 1)

        self.label_hs_t = QLabel(self.frame_grid)
        self.label_hs_t.setObjectName(u"label_hs_t")
        self.label_hs_t.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_hs_t, 0, 3, 1, 1)

        self.label_hpao_t = QLabel(self.frame_grid)
        self.label_hpao_t.setObjectName(u"label_hpao_t")
        self.label_hpao_t.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_hpao_t, 0, 4, 1, 1)

        self.label_cd = QLabel(self.frame_grid)
        self.label_cd.setObjectName(u"label_cd")
        self.label_cd.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_cd, 1, 0, 1, 1)

        self.label_cpe = QLabel(self.frame_grid)
        self.label_cpe.setObjectName(u"label_cpe")
        self.label_cpe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_cpe, 1, 1, 1, 1)

        self.label_ca = QLabel(self.frame_grid)
        self.label_ca.setObjectName(u"label_ca")
        self.label_ca.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_ca, 1, 2, 1, 1)

        self.label_hs = QLabel(self.frame_grid)
        self.label_hs.setObjectName(u"label_hs")
        self.label_hs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_hs, 1, 3, 1, 1)

        self.label_hpao = QLabel(self.frame_grid)
        self.label_hpao.setObjectName(u"label_hpao")
        self.label_hpao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_hpao, 1, 4, 1, 1)

        self.label_cd_hours = QLabel(self.frame_grid)
        self.label_cd_hours.setObjectName(u"label_cd_hours")
        self.label_cd_hours.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_cd_hours, 2, 0, 1, 1)

        self.label_cpe_hours = QLabel(self.frame_grid)
        self.label_cpe_hours.setObjectName(u"label_cpe_hours")
        self.label_cpe_hours.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_cpe_hours, 2, 1, 1, 1)

        self.label_ca_hours = QLabel(self.frame_grid)
        self.label_ca_hours.setObjectName(u"label_ca_hours")
        self.label_ca_hours.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_ca_hours, 2, 2, 1, 1)

        self.label_presential_hours = QLabel(self.frame_grid)
        self.label_presential_hours.setObjectName(u"label_presential_hours")
        self.label_presential_hours.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_presential_hours, 2, 3, 1, 1)

        self.label_total_credits = QLabel(self.frame_grid)
        self.label_total_credits.setObjectName(u"label_total_credits")
        self.label_total_credits.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_total_credits, 2, 4, 1, 1)


        self.verticalLayout.addWidget(self.frame_grid)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)

        self.horizontalLayout.addWidget(self.frame_container)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_code.setText(QCoreApplication.translate("Form", u"EXCTA0301", None))
        self.label_name.setText(QCoreApplication.translate("Form", u"Calculo Diferencial e Integral", None))
        self.label_cd_t.setText(QCoreApplication.translate("Form", u"CD", None))
        self.label_cpe_t.setText(QCoreApplication.translate("Form", u"CPE", None))
        self.label_ca_t.setText(QCoreApplication.translate("Form", u"CA", None))
        self.label_hs_t.setText(QCoreApplication.translate("Form", u"HS", None))
        self.label_hpao_t.setText(QCoreApplication.translate("Form", u"HPAO", None))
        self.label_cd.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_cpe.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_ca.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_hs.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_hpao.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_cd_hours.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_cpe_hours.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_ca_hours.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_presential_hours.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_total_credits.setText(QCoreApplication.translate("Form", u"3", None))
    # retranslateUi

