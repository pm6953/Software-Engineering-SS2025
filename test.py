
import my_classes
from my_classes import Subject

def test_workflow():
    # Erstelle ein Subject mit einer ID
    print("Erstelle ein neues Subject...")
    subject = Subject("Max", "Mustermann", "1990-12-04", "male", "max.mustermann@example.com", "1")  # Setze die ID auf "1"
    print(f"Subject erstellt: {subject.first_name} {subject.last_name}, ID: {subject.id}")

    # Führe einen PUT-Request aus, um das Subject auf dem Server anzulegen
    print("Sende PUT-Request, um das Subject auf dem Server anzulegen...")
    put_response = subject.put()
    if put_response is None:
        print("PUT-Request fehlgeschlagen. Stelle sicher, dass der Server läuft.")
    else:
        print(f"PUT-Response: {put_response.status_code}, {put_response.text}")

   

if __name__ == "__main__":
    test_workflow()