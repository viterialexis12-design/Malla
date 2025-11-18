from PySide6.QtWidgets import QMainWindow, QWidget
from view.Ui_main_window_1 import MainWindow 
import os
from PySide6.QtGui import QIcon

def cargar_estilo_qss(ruta_archivo):
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: Archivo de estilo no encontrado en {ruta_archivo}")
            return ""
        
class MainWindowForm(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tema_actual = "dark_theme"
        self.icon_paths = {
            "dark_theme": {
                "boton_tema": "../Malla/view/resources/dark_theme/sun2.svg",
                "boton_github": "../Malla/view/resources/dark_theme/Github_logo.svg",
                "boton_ayuda": "../Malla/view/resources/dark_theme/help.svg",
                "boton_crear_perfil": "../Malla/view/resources/dark_theme/mas.svg",
                "boton_buscar": "../Malla/view/resources/dark_theme/search.svg",
            },
            "light_theme": {
                "boton_tema": "../Malla/view/resources/light_theme/moon.svg",
                "boton_github": "../Malla/view/resources/light_theme/Github_logo.svg",
                "boton_ayuda": "../Malla/view/resources/light_theme/help.svg",
                "boton_crear_perfil": "../Malla/view/resources/light_theme/mas.svg",
                "boton_buscar": "../Malla/view/resources/light_theme/search.svg",
            }
        }
        self.aplicar_tema(self.tema_actual)

        
    def aplicar_tema(self, tema):
        ruta_base = os.path.dirname(os.path.abspath(__file__)) 
        if tema == "dark_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "dark_theme.qss")
        elif tema == "light_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "light_theme.qss")
        else:
            print("Tema no válido.")
            return
        estilo = cargar_estilo_qss(ruta_estilo)
        self.setStyleSheet(estilo)

        if tema in self.icon_paths:
            current_icons = self.icon_paths[tema]
            botones = [self.boton_tema, self.boton_github, self.boton_ayuda, 
                       self.boton_crear_perfil, self.boton_buscar]
            
            for boton in botones:
                obj_name = boton.objectName()
                if obj_name in current_icons:
                    icon = QIcon(current_icons[obj_name])
                    boton.setIcon(icon)

        self.tema_actual = tema
        print(f"Tema cambiado a: {tema}")

    def cambiar_tema(self):
        if self.tema_actual == "dark_theme":
            self.aplicar_tema("light_theme")
        else:
            self.aplicar_tema("dark_theme")

    