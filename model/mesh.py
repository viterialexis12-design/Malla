import uuid, json
from model.adg import ADG
from model.course import Course
import os
class Mesh:
    def __init__(self, name="", adg_courses=None):
        self.mesh_id=""
        self.name = name
        self.adg_courses = adg_courses if adg_courses is not None else ADG()
        

    def create_mesh_id(self):
        self.mesh_id = uuid.uuid1()
        print(f"Mesh ID creado: {self.mesh_id}")

    def save_in_json_mesh(self, directory_path):
        self.create_mesh_id()
        os.makedirs(directory_path, exist_ok=True) 
        filename = f"{self.mesh_id}.json"
        file_path = os.path.join(directory_path, filename) 
        mesh_data = {
            "mesh_id": str(self.mesh_id),
            "name": self.name,
            "adg_data": { 
                "courses": {},
                "adjacencies": self.adg_courses.adjacencies
            }
        }
        for code, course in self.adg_courses.courses.items():
            course_data = {
                "name": course.name,
                "prerequisites": course.prerequisites,
                "cd": course.cd,
                "cpe": course.cpe,
                "ca": course.ca,
                "hs": course.hs,
                "hpao": course.hpao,
                "cd_hours": course.cd_hours,
                "cpe_hours": course.cpe_hours,
                "ca_hours": course.ca_hours,
                "presential_hours": course.presential_hours,
                "total_credits": course.total_credits,
                "x": course.x,
                "y": course.y,
                "state": course.state
            }
            mesh_data["adg_data"]["courses"][code] = course_data
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(mesh_data, json_file, indent=4, ensure_ascii=False)
            print(f"Malla '{self.name}' guardada exitosamente en: {file_path}")
        except IOError as e:
            print(f"Error al escribir en el archivo {file_path}: {e}")

    def load_from_json_mesh(self, directory_path,mesh_id):
        os.makedirs(directory_path, exist_ok=True) 
        filename = f"{mesh_id}.json"
        file_path = os.path.join(directory_path, filename) 
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                mesh_data = json.load(json_file)
        except FileNotFoundError:
            print(f"Error: El archivo {file_path} no fue encontrado.")
            return False 
        except json.JSONDecodeError:
            print(f"Error: El archivo {file_path} no es un JSON válido.")
            return False
        name = mesh_data.get("name", "")
        mesh_id = mesh_data.get("mesh_id", "")
        adg_data = mesh_data.get("adg_data", {})

        adg_courses_temp = ADG()

        adg_courses_temp.adjacencies = adg_data.get("adjacencies", {})
        courses_data = adg_data.get("courses", {})
        adg_courses_temp.courses = {} 

        for code, data in courses_data.items():
            course = Course(
                name=data.get("name", ""),
                code=code, 
                prerequisites=data.get("prerequisites", []),
                cd=data.get("cd", 0),
                cpe=data.get("cpe", 0),
                ca=data.get("ca", 0),
                hs=data.get("hs", 0),
                hpao=data.get("hpao", 0),
                cd_hours=data.get("cd_hours", 0),
                cpe_hours=data.get("cpe_hours", 0),
                ca_hours=data.get("ca_hours", 0),
                presential_hours=data.get("presential_hours", 0),
                total_credits=data.get("total_credits", 0),
                x=data.get("x", 0),
                y=data.get("y", 0),
                state=data.get("state", "unvisited")
            )
            adg_courses_temp.courses[code] = course

        self.name = name
        self.mesh_id = mesh_id
        self.adg_courses = adg_courses_temp

        print(f"Malla '{self.name}' cargada exitosamente desde {file_path}.")
        return True
    
    def get_courses(self):
       return list(self.adg_courses.courses.values())