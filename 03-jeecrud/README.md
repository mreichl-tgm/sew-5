## A03 - JEE Crud
Mittels Gradle und Jetty, PrimeFaces, Hibernate and RDBMS .

### Inhalt:
CREATE
READ
UPDATE
DELETE
Präsentation:

Der Client (Thin-Client) liest bzw. gibt Information der DB-Tabelle an
1. Hauptmenü mit allen Untermenüs
2. Untermenüs

Aus jedem Menü kann man zum Hauptmenü zurückkehren

#### Read: 
Auflistung aller Datensätze
Auswahl der Spalten zur Anzeige
Rückkehr zum Hauptmenü
#### Update: 
Auswahl eines vorhanden Datensatzes 
Änderung der Werte
Bestätigung der Änderung
Rückkehr zum Hauptmenü
#### Delete:
Auswahl eines vorhanden Datensatzes
Bestätigung der Änderung
Rückkehr zum Hauptmenü
#### Create:
Eingabemöglichkeit der Felder
Bestätigung der Erstellung
Rückkehr zum Hauptmenü
#### Daten:
Person: Nr, Nachname, Vorname, Alter

### Gradle:
Folgende Tasks müssen zumindest verfügbar sein:
* jettyRun (Port 8080, context: crud)
* jettyRunWar
* eclipse
* cleanEclipse

### Dokumentation:
Ausführliche Dokumentation der Java-Sourcefiles und des Web-Deployment-Deskriptor

Geben Sie ein fehlerfrei lauffähiges Gradle-Projekt ab

Viel Erfolg!