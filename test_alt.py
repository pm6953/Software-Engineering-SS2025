from my_functions import ask_name, ask_number, ask_sex
from my_classes import Subject, Supervisor, Experiment

from my_functions import ask_name, ask_number, ask_sex
from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstest
    print("Bitte geben Sie die Probandendaten ein:")
    print(" Geben Sie den Vornamen des Probanden ein:")
    first_name = ask_name()
    print(" Geben Sie den Nachnamen des Probanden ein:")
    last_name = ask_name()
    print(" Geben Sie das Geschlecht des Probanden ein:")
    sex = ask_sex()
    print("Geben Sie ihre Email Adresseein:")
    email = ask_name()
    print("Geben Sie ihre Maximale herzfrequenz an:")
    max_hr = ask_number()
   

    supervisor = Supervisor("Pia", "Schratt")
    subject = Subject(first_name, last_name,"1990-12-04", sex, email)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2025-04-05")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print(f"Experiment: {experiment.name}, Datum: {experiment.date}")
    print(f"Supervisor: {experiment.supervisor.first_name} {experiment.supervisor.last_name}")
    print(f"Subject: {experiment.subject.first_name} {experiment.subject.last_name}, Geschlecht: {experiment.subject.sex}")
    