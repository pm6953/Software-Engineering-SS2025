from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen einer Fahrradergometer-Leistungstest
    supervisor = Supervisor("Pia", "Schratt")
    subject = Subject("first_name", "last_name", "male", 24)
    subject.estimate_max_hr()

    experiment = Experiment("Fahrradergometer-Leistungstest", "2025-04-05")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print(experiment)