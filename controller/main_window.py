from PySide6.QtWidgets import QMainWindow, QWidget
from view.Ui_main_window_1 import MainWindow 
import os
from PySide6.QtGui import QIcon
from controller.perfil_widget import PerfilWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt
from controller.perfil_information_widget import PerfilWidgetInformation 
from controller.planification_information import PlanificationWidgetInformation
from controller.course_information import CourseWidgetInformation
from controller.course_controller import CourseWidget
from model.course import Course
from model.profile import Profile
from model.adg import ADG
from model.mesh import Mesh
from PySide6.QtWidgets import QLayout

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
        self.profiles_adg = ADG()
        self.profiles_adg.load_from_json_profiles("data/profiles/profiles.json")
        self.current_profile = Profile()
        self.aplicar_tema(self.tema_actual)
        self.resizeScrollArea_perfil_cards()
        self.load_perfil_cards()
        self.load_perfil_information_widget()
        self.load_planification_information_widget()
        self.boton_tema.clicked.connect(self.cambiar_tema)

    def load_perfil_cards(self):
        while self.vertical_layout.count() > 1: 
            child = self.vertical_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        profiles_to_display = self.profiles_adg.profiles
        for profile in profiles_to_display:
            card = PerfilWidget(click_handler=self.handle_profile_click)
            card.set_profile_data(profile)  
            card.aplicar_tema(self.tema_actual)
            self.vertical_layout.insertWidget(self.vertical_layout.count() - 1, card)

    def handle_profile_click(self, profile_object):
        print(f"--> Clic directo detectado en el perfil: {profile_object.name}")
        self.current_profile = profile_object
        self.load_mesh(profile_object)

    def _clear_layout(self, layout):
        if layout is None: return
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                if isinstance(item.layout(), QLayout):
                    self._clear_layout(item.layout())
    
    def handle_course_click(self, course_object):
        print(f"--> Clic directo detectado en el curso: {course_object.name}")
        self.current_course = course_object
        self.load_course_information_widget(course_object)

    def update_width_profile_cards(self, event):
        viewport_width = self.scroll_area.viewport().width()
        self.scroll_content.setFixedWidth(viewport_width)
        
    def aplicar_tema(self, tema):
        ruta_base = os.path.dirname(os.path.abspath(__file__)) 
        if tema == "dark_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles","dark_theme", "main_window.qss")
        elif tema == "light_theme":
            ruta_estilo = os.path.join(ruta_base, "..", "view", "styles", "light_theme","main_window.qss")
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
        nuevo_tema = "light_theme" if self.tema_actual == "dark_theme" else "dark_theme"
        self.aplicar_tema(nuevo_tema)
        self.update_profile_cards_theme(nuevo_tema)
        self.update_mesh_theme(nuevo_tema)
        self.update_profile_info_theme(nuevo_tema)
        self.update_planification_info_theme(nuevo_tema)
        self.update_course_info_theme(nuevo_tema)
        
    def update_mesh_theme(self, tema):
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if widget and hasattr(widget, 'aplicar_tema'):
                widget.aplicar_tema(tema)
    
    def update_profile_cards_theme(self, theme):
        for i in range(self.vertical_layout.count() - 1): 
            widget = self.vertical_layout.itemAt(i).widget()
            if widget and hasattr(widget, 'aplicar_tema'):
                widget.aplicar_tema(theme)

    def update_profile_info_theme(self, theme):
        if hasattr(self, 'perfil_info_widget'):
            self.perfil_info_widget.aplicar_tema(theme)

    def update_planification_info_theme(self, theme):
        if hasattr(self, 'planification_info_widget'):
            self.planification_info_widget.aplicar_tema(theme)

    def update_course_info_theme(self, theme):
        if hasattr(self, 'course_info_widget'):
            self.course_info_widget.aplicar_tema(theme)

    def resizeScrollArea_perfil_cards(self):
        self.scroll_area = self.scrollArea 
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True) 
        self.scroll_content = QWidget()
        self.vertical_layout = QVBoxLayout(self.scroll_content)
        self.vertical_layout.setSpacing(20)
        self.vertical_layout.addStretch(1) 
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.resizeEvent = self.update_width_profile_cards
        self.update_width_profile_cards(None) 

    def load_perfil_information_widget(self):
        card = PerfilWidgetInformation()
        card.aplicar_tema(self.tema_actual)
        self.perfil_info_widget = card
        info_layout = self.frame_informacion_perfil.layout() 
        if info_layout is None:
            info_layout = QVBoxLayout(self.frame_informacion_perfil)
            print("Advertencia: Se creó un nuevo QVBoxLayout para el frame de información.")
        info_layout.addWidget(card)

    def load_planification_information_widget(self):
        card= PlanificationWidgetInformation()
        card.aplicar_tema(self.tema_actual)
        self.planification_info_widget = card
        info_layout = self.frame_informacion_planificacion.layout() 
        if info_layout is None:
            info_layout = QVBoxLayout(self.frame_informacion_planificacion)
            print("Advertencia: Se creó un nuevo QVBoxLayout para el frame de información.")
        info_layout.addWidget(card)

    def load_course_information_widget(self, course):
    
        info_layout = self.frame_informacion_curso.layout() 
        if info_layout is None:
            info_layout = QVBoxLayout(self.frame_informacion_curso)
        else:
            self._clear_layout(info_layout) 
        card = CourseWidgetInformation()
        card.set_data(course)
        card.aplicar_tema(self.tema_actual)
        self.course_info_widget = card 
        info_layout.addWidget(card)

    def load_mesh(self,perfil):
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        mesh = Mesh()
        mesh.load_from_json_mesh("data/mesh", perfil.mesh_id)
        courses_to_display = mesh.adg_courses.courses.values()
        print(f"Cargando malla '{mesh.name}' con {len(courses_to_display)} cursos...")
        for course_object in courses_to_display:
            try:
                row = course_object.x
                col = course_object.y
            except AttributeError:
                print(f"Advertencia: El curso {course_object.code} no tiene coordenadas 'x' o 'y'. Se omitirá.")
                continue
            new_course_widget = CourseWidget(click_handler=self.handle_course_click)
            new_course_widget.set_course_data(course_object) 
            new_course_widget.aplicar_tema(self.tema_actual)
            self.gridLayout.addWidget(new_course_widget, row, col)
            
        print("Carga de malla completada.")