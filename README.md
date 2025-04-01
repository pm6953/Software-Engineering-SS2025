# Software-Engineering-SS2025
Sakai Aufgabe 2 - Use Case

Name und Identifikationsnummer: UC 1.03 Alarm bei zu hoher Herzfrequenz

Beschreibung: Während der Leistungsdiagnostik wird die Herzfrequenz aufgezeichnet. Wird diese zu hoch erscheint ein Alarmsignal zur Sicherstellung, dass es dem Sportler/-in gut geht

Beteiligte Akteure Diagnostiker: in, Proband: in

Status Andauernd bei Durchführung einer Leistungsdiagnostik

Verwendete Anwendungsfälle UC 1.04 (Alarm bei Leistungsabweichung) UC 1.06 (Anstrengungsbewertung mittels BORG-Skala) UC 1.07 (Abbruch des Leistungstests)

Auslöser Die Herzfrequenz des Sportlers überschreitet eine bestimmte Schwelle

Vorbedingungen UC 1.01 (Probandin anlegen) UC 1.02 (Leistungstest anlegen) UC 1.04 (Alarm bei Leistungsabweichung)

Invarianten Aufzeichnung der bis zum Abbruch erhobenen Daten

Nachbedingung/Ergebnis Ergometer reduziert die Leistung bis zum Stillstand, sobald die Testdauer erreicht wurde

Standardablauf Während des Testes wird die Herzfrequenz durchgehend kontrolliert und aufgezeichnet

Alternative Ablaufschritte

Proband bricht ab
Diagnostiker bricht ab
Alarmsignal wegen zu hoher Herzfrequenz ertönt
Hinweise

Änderungsgeschichte 0.01; 17.03.2025; Sophia Gwiggner, Pia Schratt
