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
   

    supervisor = Supervisor("Pia", "Schratt")
    subject = Subject(first_name, last_name,"2024-12-04", sex)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2025-04-05")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print("experiment")