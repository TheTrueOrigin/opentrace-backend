# Opentrace-Backend
Das OpenTrace Backend ist ein Open-Source-Projekt, das die neueste Version der OpenTrace-Datenbank herunterlädt und als serverseitige API bereitstellt. Dies dient als BackEnd für die OpenTrace Mobile App. Den Nutzern wird es somit ermöglicht, die Herkunft und CO2-Emissionen von Konsumgütern anzufordern um bewusster einzukaufen.

Das Backend stellt sicher, dass die App stets mit den aktuellsten Daten versorgt wird, indem es die Datenbank regelmäßig aktualisiert und über eine API zugänglich macht.

Um selbst ein Produkt hinzuzufügen, folge die Anweisungen auf [opentrace-database](https://github.com/TheTrueOrigin/opentrace-database?tab=readme-ov-file#eigenen-beitrag).

## Endpunkte
- GET `/produkt/id/{id}` - Gibt das Produkt mit jeweiliger ID im JSON-Format aus
- GET `/produkt/barcode/{barcode}` - Gibt das Produkt mit jeweiligem Barcode im JSON-Format aus
- GET `/produkt/name/{name}` - Gibt Produkte mit ähnlichem Namen im JSON-Format aus

## Produkt JSON-Schema
Beispiel: `Andechser Natur Bio Joghurt mild 3,8% Fett 500g`
```json
{
  "Emission": 0.02912519400000001,
  "Distanz": 2458,
  "Name": "Andechser Natur Bio Joghurt mild 3,8% Fett 500g",
  "Unternehmen": {
    "Name": "Andechser Natur",
    "Land": "Deutschland",
    "Gründung": 1908,
    "Website": "andechser-natur.de"
  },
  "Barcode": "4104060024757",
  "Größe": "500g",
  "Gesamtgewicht": 0.523,
  "Kategorie": "Joghurt",
  "Herstellungsort": "Andechs Bayern Deutschland",
  "Nährwerte": {
    "Brennwert": "273kJ/65kcal",
    "Fettgehalt": "3,8g",
    "Gesättigte_Fettsäuren": "2,6g",
    "Kohlenhydrate": "3,7g",
    "Zuckergehalt": "3,7g",
    "Eiweißgehalt": "4,1g",
    "Salzgehalt": "0,16g"
  },
  "Labels": [
    "EU-Bio-Siegel",
    "Bioland",
    "Bayerisches Bio-Siegel",
    "Klima-Bauer"
  ],
  "Allergene": [
    "Milch",
    "Laktose"
  ],
  "Bestandteile": [
    {
      "Name": "Europa dünnwandiger Kunststoffbecher",
      "Herstellungsort": "Europa",
      "Unternehmen": {
        "Name": "Unbekannt",
        "Land": "-",
        "Gründung": "-",
        "Website": "-"
      }
    },
    {
      "Name": "Europa Aluverbundplatine",
      "Herstellungsort": "Europa",
      "Unternehmen": {
        "Name": "Unbekannt",
        "Land": "-",
        "Gründung": "-",
        "Website": "-"
      }
    },
    {
      "Name": "Bio-Milch Alpenvorland",
      "Herstellungsort": "Bayern Deutschland",
      "Unternehmen": {
        "Name": "Unbekannt",
        "Land": "-",
        "Gründung": "-",
        "Website": "-"
      }
    },
    {
      "Name": "Europa Papierbanderole",
      "Herstellungsort": "Europa",
      "Unternehmen": {
        "Name": "Unbekannt",
        "Land": "-",
        "Gründung": "-",
        "Website": "-"
      }
    }
  ]
}
```

## Web-Server starten
1. Fast-API installieren mit `pip install fastapi`
2. Webserver starten mit `python -m fastapi run endpoints.py`

Der Server startet auf Port 8000
