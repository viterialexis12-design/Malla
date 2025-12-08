from .profile import Profile
from .planification import Planification
import json

class ADG:
    def __init__(self):
        self.courses = {}
        self.adjacencies = {}
        self.profiles = []
        
    def add_course(self, course_object):
        if course_object.code not in self.courses:
            self.courses[course_object.code] = course_object
            self.adjacencies[course_object.code] = [] 
            print(f"Curso agregado: {course_object.code} - {course_object.name}")
        else:
            print(f"Advertencia: El curso {course_object.code} ya existe.")

    def build_dependencies(self):
        
        print("\nConstruyendo dependencias (aristas)...")
        for course_code, course_object in self.courses.items():
            
            for prerequisite_code in course_object.prerequisites:

                if prerequisite_code in self.adjacencies:
                    if course_code not in self.adjacencies[prerequisite_code]:
                        self.adjacencies[prerequisite_code].append(course_code)
                        print(f"Dependencia agregada: {prerequisite_code} -> {course_code}")
                else:
                    print(f"Error: Prerrequisito '{prerequisite_code}' para '{course_code}' no encontrado en el grafo.")
                    
    def get_neighbors(self, course_code):
        return self.adjacencies.get(course_code, [])

    def print_graph_courses(self):
        
        print("\n--- Estructura del ADG ---")
        for course_code, adyacentes in self.adjacencies.items():
            course_name = self.courses[course_code].name
            print(f"**{course_code} - {course_name}** es prerrequisito para:")
            for adyacente_code in adyacentes:
                adyacente_name = self.courses[adyacente_code].name
                print(f"  -> {adyacente_code} - {adyacente_name}")
        print("--------------------------")

    def print_graph_profiles(self):
        print("\n--- Estructura del ADG ---")
        for profile in self.profiles:
            print(f"Perfil: {profile.name}, Mesh ID: {profile.mesh_id}, Creación: {profile.creation_date}, Nota: {profile.note}")
            if profile.planifications:
                print("  Planificaciones:")
                for planif in profile.planifications:
                    print(f"    - Nombre: {planif.name}, Nota: {planif.note}, Cursos ID: {planif.courses_id}")
            else:
                print("  Sin planificaciones.")
        print("--------------------------")

    def build_from_pdf_mesh(self, pdf_parser, rows, columns, x0, y0):
        for row in range(rows):
            for col in range(columns):
                celda_x0 = x0 + (col * 320)
                celda_y0 = y0 + (row * 165)
                pdf_parser.x0 = celda_x0
                pdf_parser.y0 = celda_y0
                print(f"\n===== INICIANDO CELDA ({row}, {col}). BASE: x0={celda_x0}, y0={celda_y0} =====")
                pdf_parser.read_blocks(row, col, self)
        self.build_dependencies()
        self.print_graph_courses()
    
    def add_profile(self, profile_object):
        if profile_object.name not in self.profiles:
            self.profiles[profile_object.name] = profile_object
            print(f"Perfil agregado: {profile_object.name} - {profile_object.mesh_id}")
        else:
            print(f"Advertencia: El perfil {profile_object.name} ya existe.")

    def save_in_json_profiles(self, filename):
        graph_data = {
            "profiles": {}
        }
        
        for name, profile in self.profiles.items():
            planifications_list = []
            for planif in profile.planifications:
                planifications_list.append({
                    "name": planif.name,
                    "note": planif.note,
                    "creation_date": planif.creation_date,
                    "courses_id": planif.courses_id  # Lista de IDs de cursos
                })
            
            graph_data["profiles"][name] = {
                "mesh_id": profile.mesh_id,
                "creation_date": profile.creation_date,
                "note": profile.note,
                "planifications": planifications_list # Guardar la lista serializada
            }
        
        try:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(graph_data, json_file, indent=4, ensure_ascii=False)
            print(f"Grafo de perfiles guardado exitosamente en {filename}.")
        except Exception as e:
            print(f"Error al intentar guardar en JSON: {e}")

    def load_from_json_profiles(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as json_file:
                graph_data = json.load(json_file)
        except FileNotFoundError:
            print(f"Error: El archivo {filename} no fue encontrado.")
            return
        except json.JSONDecodeError:
            print(f"Error: El archivo {filename} no es un JSON válido.")
            return
        
        profiles_data = graph_data.get("profiles", {})
        self.profiles = [] 
        
        for name, data in profiles_data.items():
            planifications_list = []
            planifications_data = data.get("planifications", [])
            for planif_data in planifications_data:
                planif = Planification(
                    name=planif_data.get("name", ""),
                    note=planif_data.get("note", ""),
                    creation_date=planif_data.get("creation_date", ""),
                    courses_id=planif_data.get("courses_id", []) 
                )
                planifications_list.append(planif)
            profile = Profile(
                name=name,
                mesh_id=data.get("mesh_id", ""),
                creation_date=data.get("creation_date", ""),
                note=data.get("note", ""),
                planifications=planifications_list 
            )
            self.profiles.append(profile)
            
        print(f"Grafo de perfiles cargado exitosamente desde {filename}.")
        self.print_graph_profiles()

    def find_course_by_code(self, course_code):
        return self.courses.get(course_code, None)
    
    def find_profile_by_name(self, search_string):
        coincidences = []
        lower_search_string = search_string.lower()
        for profile in self.profiles.values():
            profile_name_lower = profile.name.lower()
            if lower_search_string in profile_name_lower:
                coincidences.append(profile)
        return coincidences
    
    def find_profile_by_exaxt_name(self, name):
        return self.profiles.get(name, None)