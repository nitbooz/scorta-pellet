# Scorta Pellet per Home Assistant

Questa integrazione personalizzata per Home Assistant ti permette di tenere traccia della tua scorta di pellet, con la possibilità di aggiungere o rimuovere quantità quando acquisti o consumi pellet.

## Caratteristiche

- Monitoraggio della quantità totale di pellet disponibile
- Servizi per aggiungere o rimuovere pellet dalla scorta
- Storico delle operazioni di aggiunta e rimozione
- Sensore con lo stato attuale della scorta

## Installazione

### Tramite HACS (consigliato)

1. Assicurati di avere [HACS](https://hacs.xyz/) installato
2. Vai su HACS > Integrazioni > Menu (⋮) > Repository personalizzati
3. Aggiungi questo repository
4. Cerca "Scorta Pellet" nelle integrazioni HACS
5. Installa l'integrazione
6. Riavvia Home Assistant

### Manualmente

1. Copia la cartella `custom_components/scorta_pellet` nella directory `custom_components` della tua installazione Home Assistant
2. Riavvia Home Assistant

## Configurazione

1. Vai su Impostazioni > Dispositivi e Servizi
2. Clicca sul pulsante "+ Aggiungi Integrazione"
3. Cerca "Scorta Pellet"
4. Segui la procedura di configurazione

## Utilizzo

### Servizi Disponibili

L'integrazione fornisce due servizi principali:

#### Aggiungere Pellet
```yaml
service: scorta_pellet.add_pellets
data:
  amount: 15  # Quantità in sacchi da aggiungere
```

#### Rimuovere Pellet
```yaml
service: scorta_pellet.remove_pellets
data:
  amount: 1  # Quantità in sacchi da rimuovere
```

### Card Lovelace Suggerita

```yaml
type: entities
entities:
  - entity: sensor.scorta_pellet
    name: Scorta Pellet Attuale
```

## Supporto

Se riscontri problemi o hai suggerimenti per migliorare l'integrazione, apri una issue su GitHub.

## Licenza

Questo progetto è rilasciato sotto licenza MIT.