class Profile:
    def __init__(self, name="", mesh_id="", creation_date="", note="", planifications=None):
        self.name = name
        self.mesh_id = mesh_id
        self.creation_date = creation_date
        self.note = note
        self.planifications = planifications if planifications is not None else []

    def add_planification(self, planification):
        self.planifications.append(planification)

    def find_planification_by_name(self, search_string):
        coincidences = []
        lower_search_string = search_string.lower()    
        for planification in self.planifications:
            planification_name_lower = planification.name.lower()
            if lower_search_string in planification_name_lower:
                coincidences.append(planification)
        return coincidences

    