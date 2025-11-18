from model.adg import ADG
from model.pdf_parser import Pdf_Parser
import sys
from PySide6.QtWidgets import QApplication
from controller.main_window import MainWindowForm
#=======================================================================
x0= 223                                                               #| 
y0= 162                                                               #|  
pdf_path = "data/mesh/malla.pdf"                                      #| 
json_path = "data/mesh/academic_adg.json"                             #| 
rows = 8                                                              #| 
columns = 6                                                           #| 
#=======================================================================

# academic_adg = ADG()
# pdf_parser = Pdf_Parser(pdf_path,x0,y0,0,0)

# academic_adg.load_from_json(json_path)
# academic_adg.build_from_pdf(pdf_parser, rows, columns, x0, y0, json_path)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindowForm()
    window.show()
    sys.exit(app.exec())

