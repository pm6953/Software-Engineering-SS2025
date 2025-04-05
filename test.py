from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstest
    supervisor = Supervisor("Pia", "Schratt")
    subject = Subject("first_name", "last_name","2024-12-04 10:07AM", "sex")
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2025-04-05")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print("experiment")