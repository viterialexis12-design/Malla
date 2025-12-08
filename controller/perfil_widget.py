from PySide6.QtWidgets import QWidget 
from view.Ui_perfil import Form
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

class PerfilWidget(QWidget):
    def __init__(self, parent=None,click_handler=None):
        super().__init__(parent)
        self.profile = None
        self.click_handler = click_handler
        self.ui = Form()
        self.ui.setupUi(self)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, 
            QSizePolicy.Policy.Preferred 
        )
        self.icon_paths = {
            "dark_theme": {
                "boton_editar_perfil": "../Malla/view/resources/dark_theme/pencil.svg",
                "boton_borrar_perfil": "../Malla/view/resources/dark_theme/trash.svg",
            },
            "light_theme": {
                "boton_editar_perfil": "../Malla/view/resources/light_theme/pencil.svg",
                "boton_borrar_perfil": "../Malla/view/resources/light_theme/trash.svg",
            }
        }
        
    def aplicar_tema(self, tema):
        ruta_base = os.path.dirname(os.path.abspath(__file__)) 
        if tema == "dark_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "dark_theme","perfil.qss")
        elif tema == "light_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "light_theme","perfil.qss")
        else:
            print("Tema no válido.")
            return
        estilo = cargar_estilo_qss(ruta_estilo)
        self.setStyleSheet(estilo)

        if tema in self.icon_paths:
            editar_icono = self.icon_paths[tema]["boton_editar_perfil"]
            borrar_icono = self.icon_paths[tema]["boton_borrar_perfil"]

            self.ui.boton_editar_perfil.setIcon(QIcon(editar_icono))
            self.ui.boton_borrar_perfil.setIcon(QIcon(borrar_icono))
        
    def set_profile_data(self, profile):
        self.profile = profile
        self.ui.nombre_perfil.setText(profile.name)
        self.ui.label_malla_perfil.setText(profile.mesh_id)
        self.ui.label_fecha_creada_perfil.setText(profile.creation_date)
        self.ui.label_nota_perfil.setText(profile.note)

    def mousePressEvent(self, event):
        if self.profile and self.click_handler:
            self.click_handler(self.profile) 
            
        super().mousePressEvent(event)
