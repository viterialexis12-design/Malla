class Course:
    def __init__(self, code="", name="", prerequisites=None, cd=0, cpe=0, ca=0, hs=0, hpao=0, cd_hours=0, cpe_hours=0, ca_hours=0, presential_hours=0, total_credits=0, x=0, y=0, state="unvisited"):
        self.name = name
        self.code = code
        self.prerequisites = prerequisites
        self.cd = cd
        self.cpe = cpe
        self.ca = ca
        self.hs = hs
        self.hpao = hpao
        self.cd_hours = cd_hours
        self.cpe_hours = cpe_hours
        self.ca_hours = ca_hours
        self.presential_hours = presential_hours
        self.total_credits = total_credits
        self.x = x
        self.y = y
        self.state = state   # habilited, completed, unvisited

    def __repr__(self):
        return f"Course(code='{self.code}', name='{self.name}', prereq={self.prerequisites}), total_credits={self.total_credits}"
    
    def change_state(self, new_state):
        self.state = new_state

    
    