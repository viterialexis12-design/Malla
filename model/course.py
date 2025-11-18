class Course:
    def __init__(self,code,name,prerequisites,cd,cpe,ca,hs,hpao,cd_hours,cpe_hours,ca_hours,presential_hours,total_credits, x,y):
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

    def __repr__(self):
        return f"Course(code='{self.code}', name='{self.name}', prereq={self.prerequisites})"
    
    