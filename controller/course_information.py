from PySide6.QtWidgets import QWidget 
from view.Ui_course_information import Form
from PySide6.QtWidgets import QSizePolicy, QLayout, QVBoxLayout, QLabel, QScrollArea
from PySide6.QtGui import QIcon
import os
from PySide6.QtCore import Qt
from model.course import Course



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
        self.course=None
        self.ui = Form()
        self.ui.setupUi(self)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, 
            QSizePolicy.Policy.Expanding
        )
        self.ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
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

    def _clear_layout(self, layout):
        if layout is None:
            return
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()
            else:
                if isinstance(item.layout(), QLayout):
                    self._clear_layout(item.layout())

    def set_data(self, course):
        content_widget = self.ui.scrollAreaWidgetContents
        current_layout = content_widget.layout()
        if current_layout:
            self._clear_layout(current_layout) 
        
        if current_layout is None:
            v_layout = QVBoxLayout(content_widget)
        else:
            v_layout = current_layout
        habilita_info = ["Materia 1", "Materia 2"] 

        display_data = {
            "Código": course.code,
            "Prerrequisitos": ", ".join(course.prerequisites) if course.prerequisites else "No hay",
            "Semestre": course.x+1,
            "Horas a la semana": f"{course.presential_hours} horas",
            "Créditos que aporta": course.total_credits,
            "Habilita": "<br>".join(habilita_info), 
            "Estado": course.state
        }

        name_label = QLabel(f"<b>{course.name}</b> ")
        v_layout.addWidget(name_label)
        
        for key, value in display_data.items():
            if value is None or value == "":
                continue

            info_text = f"<b>{key}:</b> {value}"
            label = QLabel(info_text)
            v_layout.addWidget(label)
        v_layout.addStretch(1)
