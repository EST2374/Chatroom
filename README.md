# 💬 Python Chatroom: Ein Multi-Client-Chatsystem



Ein **einfaches, funktionales Multi-Client-Chatsystem**, komplett in Python implementiert. Es nutzt das native **`socket`-Modul** für die Netzwerkkommunikation und **`threading`** zur effizienten gleichzeitigen Verarbeitung mehrerer Benutzerverbindungen.

---

## ✨ Features

Unser Chatroom-System bietet eine Reihe von Kernfunktionen, die eine reibungslose Kommunikation ermöglichen:

* **Multi-Client-fähig:** Unterstützt die simultane **Verbindung und Kommunikation** von beliebig vielen Benutzern.
* **Flexibler Verbindungsaufbau:** Ermöglicht die Übergabe von **IP-Adresse, Port und Nickname** wahlweise über Kommandozeilen-Argumente oder interaktive Konsoleneingaben.
* **Nicknames:** Jeder Benutzer identifiziert sich mit einem **eindeutigen Spitznamen**.
* **Broadcast-Funktion:** Eingehende Nachrichten werden automatisch an **alle anderen verbundenen Clients** weitergeleitet.
* **Statusmeldungen:** Alle Teilnehmer werden informiert, wenn ein Benutzer den Chat **betritt** oder **verlässt**.
* **Exit-Befehl:** Clients können die Verbindung jederzeit elegant mit dem Befehl **`.exit`** trennen.

---

## 🚀 Installation & Setup

Dieses Projekt wurde auf **Minimalismus** ausgelegt. Es benötigt lediglich eine lauffähige **Python 3.x**-Installation und **keine externen Bibliotheken**.

### 1. Dateien

Stellen Sie sicher, dass sich die folgenden zwei Dateien im **selben Verzeichnis** befinden:
1.  `server.py`
2.  `client.py`

### 2. Server starten

Öffnen Sie **zuerst** ein Terminal-Fenster und starten Sie den Chat-Server:

```bash
python server.py

    Standard-Port: Der Server läuft in der Regel auf Port 9001, falls nicht anders konfiguriert.

💻 Client starten & Verbinden

Der Client ist sehr flexibel und unterstützt sowohl die Übergabe von Parametern über die Kommandozeile als auch die interaktive Abfrage fehlender Werte (Hybrid-Modus).

Nutzungsschema

Bash

python client.py [-i <IP_ADRESSE>] [-p <PORT>] [-u <USERNAME>]

Parameter	Kurzform	Beschreibung	Beispiel
--ip	-i	Die IP-Adresse des Servers (z.B. 127.0.0.1 für lokal).	-i 192.168.1.10
--port	-p	Der Port, auf dem der Server läuft (Standard: 9001).	-p 9001
--user	-u	Der gewünschte Nickname für den Chat.	-u MaxMustermann

Anwendungsbeispiele

Szenario	Befehl	Beschreibung
Volle Übergabe	python client.py -i 127.0.0.1 -p 9001 -u Alice	Alle Informationen werden direkt übergeben.
Hybrid-Modus	python client.py -u Bob	Nur der Username wird übergeben. IP und Port werden interaktiv abgefragt.
Interaktiver Modus	python client.py	Alle drei Werte werden interaktiv über die Konsole eingegeben.

🛑 Chat verlassen

Um den Chat ordnungsgemäß zu verlassen und alle anderen Teilnehmer zu informieren, geben Sie einfach den folgenden Befehl ein:

.exit
