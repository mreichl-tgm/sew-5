Erstellen Sie einen Client, der eine Auto-Navigation mittels Google Drive API ermöglicht.
```
url = "http://maps.googleapis.com/maps/api/directions/json"
```
Beachten Sie bei der Umsetzung auch das MVC-Pattern.
Verwenden Sie auch eine Statusinformation für Berechnung bzw. Fehler aufgrund der Start/Ziel-Adressen
Für die Umsetzung ist Python empfohlen, jedoch sind auch andere Plattformen denkbar, die für die Beurteiler vorhanden sind (JavaScript oder Java) 
Richtlinien für die gegenseitige Beurteilung

##### 1. Die Beurteilung eines Kriteriums erfolgt anhand von vier Stufen:
Vollständig erfüllt: Das Kriterium wurde (bis auf kleine Makel) zur Gänze erfüllt
Größtenteils erfüllt:Das Meiste (Richtwert: 70%) wurde erfüllt
Überwiegend erfüllt: Mehr als die Hälfte (50%) des Kriteriums wurde erfüllt
Mangelhaft bzw. nicht erfüllt: Weniger als die Hälfte des Kriteriums wurde erfüllt

##### 2. Feedback
Sinnvolles Feedback zu geben ist das Kernelement der gegenseitigen Beurteilung!
Es ist für jedes Kriterium Feedback zur Verbesserung zu geben!
Es ist insbesondere aufzuschlüsseln, welche Elemente des Kriteriums nicht erfüllt wurden inkl. Vorschlägen zur Verbesserung
Fehlendes Feedback führt im Nachhinein zu Punkteabzügen durch die Lehrer

##### 3. Dokumentation
Wenn Dokumentation gefordert ist, gilt grundsätzlich, dass die Implementierung nachvollziehbar sein muss
Die Angabe des Autors ist irrelevant und führt weder zu Punkteabzug noch zu Bonuspunkten. Für eine anonyme Beurteilung empfiehlt es sich jedoch, den Namen wegzulassen
Das Dokumentieren von get- und set-Methoden ist nur dann verpflichtend, wenn darin noch etwas Anderes als das simple Setzen bzw. Re­tour­nie­ren des jeweiligen Attributs gemacht wird. Im Idealfall lässt man sich die Dokumentation für solche Methoden von der IDE generieren.

##### 4. Funktionalität
Nicht geforderte Funktionalität fließt nicht in die Beurteilung ein
Dies gilt jedoch nicht für Rahmenbedingungen: Ist beispielsweise in der Aufgabenstellung eine gewisse Technologie (z.B. Hibernate) gefordert und es gibt kein explizites Kriterium dafür, so können dafür sehr wohl Punkte abgezogen werden! Hier ist Augenmaß gefragt, d.h. es sind nicht automatisch 0 Punkte. Im Zweifelsfall mit den Lehrern abstimmen (per Mail oder im Forum)!

##### 5. Plagiate
Bei einem Plagiatsverdacht wird trotzdem textuelles Feedback gegeben (als ob es kein Plagiat wäre)
Es ist in jedem Fall hineinzuschreiben, dass es deswegen Punkteabzüge gab, weil es sich um ein Plagiat handelt inkl. Quelle
Richtwert für Plagiatstools: 60-70%, wobei jedoch auch Augenmaß angewandt wird (wurden nur die Variablen und Kommentare geändert, ...)
Dieser Richtwert ist sehr hoch angesetzt - wenn Code selbstständig geschrieben wird, erreicht man solche Werte nie! Daher sollte vor allem beim Kopieren von Code aus Tutorials o.ä. aufgepasst werden!
Wenn begründeter Verdacht besteht, können je nach Schweregrad ein oder zwei Bewertungsstufen abgezogen werden (d.h. ein "vollständig erfüllt" wird z.B. "überwiegend erfüllt" oder "größtenteils erfüllt", jedoch kein "nicht erfüllt")
Beurteilungskriterien

### Kriterien
##### Kriterium 1: MVC-Pattern
Model, View und Controller sind eigene Klassen, voneinander getrennt und befinden sich in eigenen Modulen
Das MVC-Pattern wurde nach den bekannten Standards implementiert

##### Kriterium 2: Grafische Oberfläche
Es gibt zwei Eingabefelder: Start und Ziel
Es gibt einen Ausgabebereich, welcher das Ergebnis einerseits in Gesamt und andererseits im Detail darstellt
Die wesentlichen Informationen werden hervorgehoben
Es gibt drei Buttons
Submit: Schickt die Anfrage mit Start und Ziel an die Google API
Reset: Leert alle Eingabe- und Ausgabefelder
Close: Mit Close kann die Applikation beendet werden
In der Statusleiste (unten) wird der Fortschritt der Berechnung bzw. Fehler wiedergegeben

##### Kriterium 3: REST-Service
Bei einem Klick auf Submit wird die angegebene URL mit den jeweiligen Parametern angesprochen
Wird eine andere Plattform als Python verwendet, so ist dies in der Dokumentation zu begründen
Das Ergebnis-XML wird korrekt geparsed und in dem GUI angezeigt
Im Fehlerfall wird eine entsprechende Information in der Statusleiste angezeigt und der Fehler wird im Ausgabebereich angezeigt

##### Kriterium 4: Dokumentation
Methoden (außer Getter und Setter) sind kommentiert
Es existiert eine vollständige Sphinx-Dokumentation (inkl. Übersicht des Moduls)
Der Code ist nachvollziehbar kommentiert

##### Kriterium 5: Fehlerbehandlung
Wenn das Service nicht verfügbar ist, wird eine entsprechende Fehlermeldung angezeigt
Start und Ende sind auffindbar, ansonsten wird eine Fehlermeldung angezeigt
In der Statusleiste (unten) wird angezeigt, ob der letzte Request erfolgreich war oder nicht

##### Kriterium 6: XML-Modus (Erweiterung)
Es existiert die Möglichkeit, die XML-Variante der Google Maps API anzusprechen
Eine entsprechende Eingabemöglichkeit (z.B. RadioButton) steuert, ob die XML- oder JSON-Variante verwendet wird