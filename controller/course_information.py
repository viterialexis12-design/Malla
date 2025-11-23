from PySide6.QtWidgets import QWidget 
from view.Ui_course_information import Form
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtGui import QIcon
import os

def cargar_estilo_qss(ruta_archivo):
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: Archivo de estilo no encontrado en {ruta_archivo}")
            return ""

class CourseWidgetInformation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Form()
        self.ui.setupUi(self)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, 
            QSizePolicy.Policy.Preferred 
        )
        self.icon_paths = {
            "dark_theme": {
                "boton_editar": "../Malla/view/resources/dark_theme/pencil.svg",
            },
            "light_theme": {
                "boton_editar": "../Malla/view/resources/light_theme/pencil.svg",
            }
        }

    def aplicar_tema(self, tema):
        ruta_base = os.path.dirname(os.path.abspath(__file__)) 
        if tema == "dark_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "dark_theme","course_information.qss")
        elif tema == "light_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "light_theme","course_information.qss")
        else:
            print("Tema no válido.")
            return
        estilo = cargar_estilo_qss(ruta_estilo)
        self.setStyleSheet(estilo)

        if tema in self.icon_paths:
            editar_icono = self.icon_paths[tema]["boton_editar"]
            self.ui.boton_editar.setIcon(QIcon(editar_icono))
        
