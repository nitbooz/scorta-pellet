\"""
Sensor for pellet stock management.
"""
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import Entity

class PelletSensor(SensorEntity):
    """Representation of a Pellet Stock sensor."""

    def __init__(self, hass):
        """Initialize the sensor."""
        self._hass = hass
        self._state = None
        self._name = "Scorta Pellet"
        self._unit_of_measurement = "sacchi"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    def update(self):
        """Fetch new state data for the sensor."""
        self._state = self._hass.data[DOMAIN]["total"]