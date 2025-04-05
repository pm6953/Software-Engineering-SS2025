class Subject():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def estimate_max_hr(self) -> int: 
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            max_hr_bpm  = 0 #Meldung bei Fehler
        return int(max_hr_bpm)
        

class Supervisor():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
       
class Experiment():
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subject = None
        self.supervisor = None
    
    def add_subject(self, subject):
        self.subject = subject
    
    def add_supervisor(self, supervisor):
        self.supervisor = supervisor