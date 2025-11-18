from .course import Course
import json

class ADG:
    def __init__(self):
        self.courses = {}
        self.adjacencies = {}
        
    def add_course(self, course_object):
        if course_object.code not in self.courses:
            self.courses[course_object.code] = course_object
            self.adjacencies[course_object.code] = [] # Inicializa la lista de adyacentes
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

    def print_graph(self):
        
        print("\n--- Estructura del ADG ---")
        for course_code, adyacentes in self.adjacencies.items():
            course_name = self.courses[course_code].name
            print(f"**{course_code} - {course_name}** es prerrequisito para:")
            for adyacente_code in adyacentes:
                adyacente_name = self.courses[adyacente_code].name
                print(f"  -> {adyacente_code} - {adyacente_name}")
        print("--------------------------")
    
    def save_in_json(self, filename):
        
        graph_data = {
            "courses": {},
            "adjacencies": self.adjacencies
        }
        
        for code, course in self.courses.items():
            graph_data["courses"][code] = {
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
                "y": course.y
            }
        
        with open(filename, 'w',encoding='utf-8') as json_file:
            json.dump(graph_data, json_file, indent=4, ensure_ascii=False)
        
        print(f"Grafo guardado en {filename}")

    def load_from_json(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as json_file:
                graph_data = json.load(json_file)
        except FileNotFoundError:
            print(f"Error: El archivo {filename} no fue encontrado.")
            return
        except json.JSONDecodeError:
            print(f"Error: El archivo {filename} no es un JSON válido.")
            return
        self.adjacencies = graph_data.get("adjacencies", {})
        courses_data = graph_data.get("courses", {})
        self.courses = {} 
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
                y=data.get("y", 0)
            )
            self.courses[code] = course
        print(f"Grafo cargado exitosamente desde {filename}.")
        self.print_graph()

    def build_from_pdf(self, pdf_parser, rows, columns, x0, y0, json_path):
        for row in range(rows):
            for col in range(columns):
                celda_x0 = x0 + (col * 320)
                celda_y0 = y0 + (row * 165)
                pdf_parser.x0 = celda_x0
                pdf_parser.y0 = celda_y0
                print(f"\n===== INICIANDO CELDA ({row}, {col}). BASE: x0={celda_x0}, y0={celda_y0} =====")
                pdf_parser.read_blocks(row, col, self)
        self.build_dependencies()
        self.save_in_json(json_path)
        self.print_graph()
    