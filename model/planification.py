class Planification:

    def __init__(self, name="", note="", creation_date="", courses_id=None):
        self.name = name
        self.creation_date = creation_date
        self.note = note
        self.courses_id = courses_id if courses_id is not None else []

    def add_course(self, course_id):
        self.courses_id.append(course_id)