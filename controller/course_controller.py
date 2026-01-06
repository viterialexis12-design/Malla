from PySide6.QtWidgets import QWidget 
from view.Ui_course import Form
from PySide6.QtWidgets import QSizePolicy
import os

def cargar_estilo_qss(ruta_archivo):
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: Archivo de estilo no encontrado en {ruta_archivo}")
            return ""

class CourseWidget(QWidget):
    def __init__(self, parent=None,click_handler=None):
        super().__init__(parent)
        self.course=None
        self.click_handler=click_handler
        self.ui = Form()
        self.ui.setupUi(self)
        self.setFixedSize(400, 140)

    def aplicar_tema(self, tema):
        ruta_base = os.path.dirname(os.path.abspath(__file__)) 
        if tema == "dark_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "dark_theme","course.qss")
        elif tema == "light_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "light_theme","course.qss")
        else:
            print("Tema no válido.")
            return
        estilo = cargar_estilo_qss(ruta_estilo)
        self.setStyleSheet(estilo)
        
    def set_course_data(self, course):
        self.course = course
        self.ui.label_code.setText(course.code)
        self.ui.label_name.setText(course.name)
        self.ui.label_cd.setText(str(course.cd))
        self.ui.label_cpe.setText(str(course.cpe))
        self.ui.label_ca.setText(str(course.ca))
        self.ui.label_hs.setText(str(course.hs))
        self.ui.label_hpao.setText(str(course.hpao))
        self.ui.label_cd_hours.setText(str(course.cd_hours))
        self.ui.label_cpe_hours.setText(str(course.cpe_hours))
        self.ui.label_ca_hours.setText(str(course.ca_hours))
        self.ui.label_presential_hours.setText(str(course.presential_hours))
        self.ui.label_total_credits.setText(str(course.total_credits))

    def mousePressEvent(self, event):
        if self.course and self.click_handler:
            self.click_handler(self.course)  
        super().mousePressEvent(event)