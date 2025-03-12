# Opentrace-Backend
Das OpenTrace Backend ist ein Open-Source-Projekt, das die neueste Version der OpenTrace-Datenbank herunterlädt und als serverseitige API bereitstellt. Dies dient als BackEnd für die OpenTrace Mobile App. Den Nutzern wird es somit ermöglicht, die Herkunft und CO2-Emissionen von Konsumgütern anzufordern um bewusster einzukaufen.

Das Backend stellt sicher, dass die App stets mit den aktuellsten Daten versorgt wird, indem es die Datenbank regelmäßig aktualisiert und über eine API zugänglich macht.

Um selbst ein Produkt hinzuzufügen, folge die Anweisungen auf [opentrace-database](https://github.com/TheTrueOrigin/opentrace-database?tab=readme-ov-file#eigenen-beitrag).

## Endpunkte
- GET `/produkt/id/{id}` - Gibt das Produkt mit jeweiliger ID im JSON-Format aus
- GET `/produkt/barcode/{barcode}` - Gibt das Produkt mit jeweiligem Barcode im JSON-Format aus
- GET `/produkt/name/{name}` - Gibt Produkte mit ähnlichem Namen im JSON-Format aus

## Produkt JSON-Schema
Beispiel: `Meßmer Tee Klassik`
```json
{
  "Name": "Meßmer Tee Klassik",
  "Unternehmen": {
    "Name": "Meßmer",
    "Land": "Österreich",
    "Gründung": 1990,
    "Website": "meßmer.at"
  },
  "Barcode": "4001257218503",
  "Größe": "20pcs",
  "Kategorie": "Tee",
  "Herstellungsort": "Österreich",
  "Nährwerte": {
    "Brennwert": "3kJ/1kcal",
    "Fettgehalt": "0g",
    "Gesättigte_Fettsäuren": "0g",
    "Kohlenhydrate": "0.2g",
    "Zuckergehalt": "0.1g",
    "Eiweißgehalt": "0g",
    "Salzgehalt": "0,01g"
  },
  "Labels": [
    "Glutenfrei"
  ],
  "Allergene": [
    "Histamin"
  ],
  "Bestandteile": [
    {
      "Name": "Nalli Silks Seide",
      "Herstellungsort": "Indien",
      "Unternehmen": {
        "Name": "Nalli Silks",
        "Land": "Indien",
        "Gründung": 1990,
        "Website": "nallisilks.com"
      }
    },
    {
      "Name": "Tata Tea Limited Schwarztee Blätter",
      "Herstellungsort": "Indien",
      "Unternehmen": {
        "Name": "Tata Tea Limited",
        "Land": "Indien",
        "Gründung": 1893,
        "Website": "tata.com"
      }
    },
    {
      "Name": "Geissinger Karton Verpackung",
      "Herstellungsort": "Österreich",
      "Unternehmen": {
        "Name": "Geissinger",
        "Land": "Österreich",
        "Gründung": 1990,
        "Website": "geissinger.at"
      }
    }
  ]
}
```

## Web-Server starten
1. Fast-API installieren mit `pip install fastapi`
2. Webserver starten mit `python -m fastapi run endpoints.py`

Der Server startet unter dem Port 8000
