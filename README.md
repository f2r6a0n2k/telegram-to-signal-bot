# Telegram to Signal Bot

Ein einfacher Python-Bot, der Telegram-Nachrichten an Signal weiterleitet.

## Voraussetzungen

- Python 3
- `python-telegram-bot`
- `python-dotenv`
- `signal-cli`

## Installation

1. Repository klonen oder ZIP herunterladen und entpacken.
2. `.env.example` kopieren und als `.env` anpassen.

```
cp .env.example .env
nano .env
```

3. Abhängigkeiten installieren:

```
pip install python-telegram-bot python-dotenv
```

4. Bot starten:

```
python3 bot.py
```

## systemd Service (optional)

1. `telegram_signal_bot.service` anpassen (Pfad und Nutzer).
2. Service installieren:

```
sudo cp telegram_signal_bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable telegram_signal_bot
sudo systemctl start telegram_signal_bot
```

## Hinweise

- `signal-cli` muss installiert und konfiguriert sein.
- Empfänger*innen müssen bei Signal registriert sein.