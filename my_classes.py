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
    def __init__(self, first_name, last_name, date_of_birth, sex, email, id):
        super().__init__(first_name, last_name, date_of_birth, sex)
        self.email = email
        self.id = id  # ID wird jetzt korrekt übergeben und gespeichert

    def put(self):
        """
        Sendet einen PUT-Request, um das Subject auf dem Server zu speichern oder zu aktualisieren.
        """
        url = f"http://127.0.0.1:5000/person/{self.id}"  # Verwende die ID in der URL
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self._Person__date_of_birth,
            "sex": self.sex,
            "email": self.email
        }
        try:
            response = requests.put(url, json=data)
            if response.status_code in [200, 201]:
                print("Subject erfolgreich auf dem Server angelegt oder aktualisiert.")
            else:
                print(f"Fehler beim PUT-Request: {response.status_code}, {response.text}")
            return response
        except Exception as e:
            print(f"Fehler beim PUT-Request: {e}")
            return None

    def update_email(self, new_email):
        """
        Aktualisiert die E-Mail-Adresse des Subjects auf dem Server.
        """
        url = f"http://127.0.0.1:5000/person/{self.id}/email"
        data = {"email": new_email}
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                self.email = new_email  # Aktualisiere die lokale E-Mail-Adresse
                print("E-Mail erfolgreich aktualisiert.")
            else:
                print(f"Fehler beim POST-Request: {response.status_code}, {response.text}")
            return response
        except Exception as e:
            print(f"Fehler beim POST-Request: {e}")
            return None

class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, date_of_birth=None, sex=None)

class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subject = None
        self.supervisor = None

    def add_subject(self, subject):
        """
        Verknüpft ein Subject mit dem Experiment.
        """
        self.subject = subject

    def add_supervisor(self, supervisor):
        """
        Verknüpft einen Supervisor mit dem Experiment.
        """
        self.supervisor = supervisor