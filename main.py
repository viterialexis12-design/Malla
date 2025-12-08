from model.adg import ADG
from model.pdf_parser import Pdf_Parser
from model.profile import Profile
from model.planification import Planification
from model.course import Course
import sys
from PySide6.QtWidgets import QApplication
from controller.main_window import MainWindowForm
from model.mesh import Mesh
#=======================================================================
x0= 223                                                               #| 
y0= 162          
data_directory= "data/mesh"                                           #|  
pdf_path_malla = "data/mesh/malla.pdf"                                #| 
json_path_profiles = "data/profiles/profiles.json"                    #| 
rows = 8                                                              #| 
columns = 6                                                           #| 
#=======================================================================
malla_name = "Malla 2024"
perfil=Profile()
academic_adg = ADG()
pdf_parser = Pdf_Parser(pdf_path_malla,x0,y0,0,0)
malla = Mesh(malla_name,academic_adg)

# malla.adg_courses.build_from_pdf_mesh(pdf_parser, rows, columns, x0, y0)
# malla.save_in_json_mesh(data_directory)

# profiles_adg = ADG()        
# profiles_adg.load_from_json_profiles(json_path_profiles)
# perfil=profiles_adg.find_profile_by_exaxt_name("perfil_alex")
# malla.load_from_json_mesh(data_directory,perfil.mesh_id)
# malla.adg_courses.print_graph_courses()

# profiles_adg.load_from_json_profiles(json_path_profiles)
# prerrequisite_list=academic_adg.get_neighbors("EXCTA0301")
# for elemento in prerrequisite_list:
#     print("Elemento:", elemento)
#     course=academic_adg.find_course_by_code(elemento)
#     print("Curso:", course.name)
#     print("Creditos:", course.total_credits)
#     print("Horas presenciales:", course.presential_hours)
#     print("Horas de CD:", course.cd_hours)
#     print("Horas de CPE:", course.cpe_hours)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindowForm()
    window.show()
    sys.exit(app.exec())

