from datetime import datetime

class Person():
    def __init__(self, first_name, last_name, date_of_birth, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.__date_of_birth = date_of_birth #__ vor date zum Verstecken
        self.sex = sex 
    
    def get_age(self):
        date_format = "%Y-%m-%d " #Format für die Eingabe des Geburtsdatums
        date_of_birth_temp = datetime.strptime(self.__date_of_birth, date_format)
        age = datetime.today().year - date_of_birth_temp.year
        return age
    
        
    
class Subject(Person):
    def __init__(self, first_name, last_name, date_of_birth, sex):
        super().__init__(first_name, last_name, date_of_birth, sex)
        

    def estimate_max_hr(self) -> int: 
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * super().get_age()
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  super().get_age()
        else:
            max_hr_bpm  = 0 #Meldung bei Fehler
        return int(max_hr_bpm)
        

class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, date_of_birth = None, sex= None)
       
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
