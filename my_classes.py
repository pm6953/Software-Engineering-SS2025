import requests  # Für HTTP-Requests
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, date_of_birth, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.__date_of_birth = date_of_birth
        self.sex = sex

    def get_age(self):
        date_format = "%Y-%m-%d"
        date_of_birth_temp = datetime.strptime(self.__date_of_birth, date_format)
        age = datetime.today().year - date_of_birth_temp.year
        return age

class Subject(Person):
    def __init__(self, first_name, last_name, date_of_birth, sex, email):
        super().__init__(first_name, last_name, date_of_birth, sex)
        self.email = email
        self.id = id 

    def put(self):
        import requests
        url = f"http://127.0.0.1:5000/person/{self.id}"  # Füge die ID hinzu
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self._Person__date_of_birth,
            "sex": self.sex,
            "email": self.email
        }
        try:
            response = requests.put(url, json=data)
            return response
        except Exception as e:
            print(f"Fehler beim PUT-Request: {e}")
            return None

    def update_email(self, new_email):
        url = f"http://127.0.0.1:5000/person/{self.first_name}/{self.last_name}/email"
        data = {"email": new_email}
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                self.email = new_email
                print("E-Mail erfolgreich aktualisiert.")
            else:
                print(f"Fehler beim POST-Request: {response.status_code}, {response.text}")
            return response
        except Exception as e:
            print(f"Fehler beim POST-Request: {e}")
            return None

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
