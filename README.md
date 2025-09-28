# 💬 Python Chatroom

Ein einfaches, funktionales **Multi-Client-Chatsystem**, implementiert in Python unter Verwendung des **`socket`-Moduls** und **`threading`** für die gleichzeitige Verarbeitung von Clients.

---

## ✨ Features

* **Multi-Client-fähig:** Unterstützt die gleichzeitige Verbindung und Kommunikation mehrerer Benutzer.
* **Nicknames:** Jeder Benutzer wählt bei der Verbindung einen Spitznamen.
* **Broadcast-Funktion:** Nachrichten eines Clients werden automatisch an alle anderen verbundenen Clients gesendet.
* **Statusmeldungen:** Informiert alle Teilnehmer, wenn ein Benutzer den Chat betritt oder verlässt.
* **Asynchrone Verarbeitung:** Nutzt Threads, um das Senden und Empfangen von Nachrichten zu entkoppeln.

---

## 🚀 Installation & Setup

Dieses Projekt erfordert lediglich eine lauffähige **Python 3.x**-Installation. Es sind **keine externen Bibliotheken** erforderlich.

### 1. Dateien

Stelle sicher, dass du die folgenden zwei Dateien im selben Verzeichnis hast:

1.  `server.py`
2.  `client.py`

### 2. Server starten

Öffne ein Terminal-Fenster und starte den Server. Dies muss **zuerst** geschehen.

```bash
python server.py
