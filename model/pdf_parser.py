import re
import fitz 
from .course import Course
class Pdf_Parser:

    def __init__(self, pdf_path,x0,y0,x1,y1):
        self.pdf_path = pdf_path
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
            
    def extract_text(self,x0,y0,x1,y1):
        with fitz.open(self.pdf_path) as pdf_document:
            page = pdf_document[0]
            rect = fitz.Rect(x0,y0,x1,y1) 
            extracted_text = page.get_text(clip=rect)
            return extracted_text
    
    def adjust_coordinates_0(self):
        return self.x0, self.y0,self.x0+312, self.y0+74
    
    def adjust_coordinates_1(self):
        return self.x0, self.y0+74, self.x0+312, self.y0+92.5
    
    def adjust_coordinates_2(self):
        return self.x0, self.y0+92.5, self.x0+53, self.y0+148
    
    def adjust_coordinates_3(self):
        return self.x0+53, self.y0+92.5, self.x0+106, self.y0+148
    
    def adjust_coordinates_4(self):
        return self.x0+106, self.y0+92.5, self.x0+159, self.y0+148
    
    def adjust_coordinates_5(self):
        return self.x0+159, self.y0+92.5, self.x0+212, self.y0+148
    
    def adjust_coordinates_6(self):
        return self.x0+212, self.y0+92.5, self.x0+312, self.y0+148
    
    def read_blocks(self, row, col, academic_adg):
        course = Course('', '', [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0)
        for block_index in range(7):
            adjust_method = getattr(self, f'adjust_coordinates_{block_index}')
            x0, y0, x1, y1 = adjust_method()
            extracted_text = self.extract_text(x0, y0, x1, y1)
            self.organice_text(block_index, extracted_text, course)
        if course.code and course.name:
            course.x = row
            course.y = col
            academic_adg.add_course(course)
        else:
            print(f"Advertencia: Celda ({row}, {col}) omitida por falta de Código o Nombre.")
  
    def organice_text(self, block_index, extracted_text,course):
        if block_index == 0:
            self.organice_text_block_0(extracted_text,course)
            pass
        elif block_index == 1:
            self.organice_text_block_1(extracted_text,course)
            pass
        elif block_index == 2:
            self.organice_text_block_2(extracted_text,course)
            pass
        elif block_index == 3:
            self.organice_text_block_3(extracted_text,course)
            pass
        elif block_index == 4:
            self.organice_text_block_4(extracted_text,course)
            pass
        elif block_index == 5:
            self.organice_text_block_5(extracted_text,course)
            pass
        elif block_index == 6:
            self.organice_text_block_6(extracted_text,course)
            pass
        else:
            raise ValueError("Índice de bloque no válido")

    def organice_text_block_0(self, extracted_text, course):
        lines = [line.strip() for line in extracted_text.strip().splitlines() if line.strip()]
        codigo_pattern = re.compile(r'^[A-Z0-9]{8,9}$') 
        nombre = ""
        codigo = ""
        for line in lines:
            if codigo_pattern.match(line):
                codigo = line
            else:
                nombre += line + " "
        course.name = nombre.strip()  
        course.code = codigo
        if not course.code and not course.name:
            print(f"Advertencia: No se encontraron los datos necesarios en el bloque 1.")
        pass

    def organice_text_block_1(self,extracted_text,course):
        lines = [line.strip() for line in extracted_text.strip().splitlines() if line.strip()]
        codigo_pattern = re.compile(r'^[A-Z0-9]{8,9}$') 
        prerequisitos_encontrados = []
        for line in lines:
            normalized_line = line.upper() 
            normalized_code_candidate = normalized_line.replace(' ', '')
            palabras_clave_a_descartar = ("NIVELACION", "N/A")
            if normalized_code_candidate in palabras_clave_a_descartar:
                print(f"Descartando palabra clave: {line}")
                continue 
            if codigo_pattern.match(normalized_code_candidate):
                prerequisitos_encontrados.append(normalized_code_candidate)
            else:
                print(f"Advertencia: Texto no identificado como código o palabra clave: {line}")
        course.prerequisites = prerequisitos_encontrados
        pass

    def organice_text_block_2(self,extracted_text,course):
 
        lines = [line.strip() for line in extracted_text.strip().splitlines() if line.strip()]
        numeros = []
        for line in lines:
            try:
                numeros.append(int(line))
            except ValueError:
                pass
        if len(numeros) >= 2:
            n1 = numeros[0]
            n2 = numeros[1]
            creditos_cd = min(n1, n2)
            horas_cd = max(n1, n2)

            if creditos_cd <= horas_cd:
                course.cd = creditos_cd
                course.cd_hours = horas_cd
            else:
                print(f"Advertencia: Orden o formato incorrecto en Bloque 2. Créditos ({creditos_cd}) no es menor que Horas ({horas_cd}).")
        else:
            print(f"Advertencia: No se encontraron los datos necesarios en el bloque 2. Encontrados: {len(numeros)}.")
        pass

    def organice_text_block_3(self,extracted_text,course):
 
        lines = [line.strip() for line in extracted_text.strip().splitlines() if line.strip()]
        numeros = []
        for line in lines:
            try:
                numeros.append(int(line))
            except ValueError:
                pass
        if len(numeros) >= 2:
            n1 = numeros[0]
            n2 = numeros[1]
            creditos_cpe = min(n1, n2)
            horas_cpe = max(n1, n2)

            if creditos_cpe <= horas_cpe:
                course.cpe = creditos_cpe
                course.cpe_hours = horas_cpe
            else:
                print(f"Advertencia: Orden o formato incorrecto en Bloque 2. Créditos ({creditos_cpe}) no es menor que Horas ({horas_cpe}).")
        else:
            print(f"Advertencia: No se encontraron los datos necesarios en el bloque 3. Encontrados: {len(numeros)}.")
        pass

    def organice_text_block_4(self,extracted_text,course):
 
        lines = [line.strip() for line in extracted_text.strip().splitlines() if line.strip()]
        numeros = []
        for line in lines:
            try:
                numeros.append(int(line))
            except ValueError:
                pass
        if len(numeros) >= 2:
            n1 = numeros[0]
            n2 = numeros[1]
            creditos_ca = min(n1, n2)
            horas_ca = max(n1, n2)

            if creditos_ca <= horas_ca:
                course.ca = creditos_ca
                course.ca_hours = horas_ca
            else:
                print(f"Advertencia: Orden o formato incorrecto en Bloque 2. Créditos ({creditos_ca}) no es menor que Horas ({horas_ca}).")
        else:
            print(f"Advertencia: No se encontraron los datos necesarios en el bloque 4. Encontrados: {len(numeros)}.")
        pass

    def organice_text_block_5(self,extracted_text,course):
 
        lines = [line.strip() for line in extracted_text.strip().splitlines() if line.strip()]
        numeros = []
        for line in lines:
            try:
                numeros.append(int(line))
            except ValueError:
                pass
        if len(numeros) >= 2:
            n1 = numeros[0]
            n2 = numeros[1]
            hs_total = max(n1, n2)
            presential_hours = min(n1, n2)
            if hs_total >= presential_hours:
                course.hs = hs_total
                course.presential_hours = presential_hours
            else:
                print(f"Advertencia: Orden o formato incorrecto en Bloque 5 (HS). El mayor ({hs_total}) no es mayor que el menor ({presential_hours}).")
        else:
            print(f"Advertencia: No se encontraron los datos necesarios en el bloque 5. Encontrados: {len(numeros)}.")
        pass

    def organice_text_block_6(self,extracted_text,course):
        lines = [line.strip() for line in extracted_text.strip().splitlines() if line.strip()]
        numeros = []
        for line in lines:
            try:
                numeros.append(int(line))
            except ValueError:
                pass
        if len(numeros) >= 2:
            n1 = numeros[0]
            n2 = numeros[1]
            hpao = max(n1, n2)
            total_credits = min(n1, n2)
            if hpao >= total_credits:
                course.hpao = hpao
                course.total_credits = total_credits
            else:
                print(f"Advertencia: Orden o formato incorrecto en Bloque 6 (HPAO). El mayor ({hpao}) no es mayor que el menor ({total_credits}).")
        else:
            print(f"Advertencia: No se encontraron los datos necesarios en el bloque 6. Encontrados: {len(numeros)}.")
        pass
