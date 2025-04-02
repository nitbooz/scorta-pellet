"""Sensor platform for Scorta Pellet."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo

from . import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Scorta Pellet sensor."""
    sensor = ScortaPelletSensor(hass, config_entry)
    hass.data[DOMAIN][config_entry.entry_id]["sensor"] = sensor
    async_add_entities([sensor])

class ScortaPelletSensor(SensorEntity):
    """Representation of a Scorta Pellet sensor."""

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        """Initialize the sensor."""
        self.hass = hass
        self.config_entry = config_entry
        self._attr_unique_id = f"{config_entry.entry_id}_pellet_stock"
        self._attr_name = "Scorta Pellet"
        self._attr_native_unit_of_measurement = "sacchi"
        self._attr_icon = "mdi:fireplace"

    @property
    def native_value(self) -> int:
        """Return the current number of pellet bags."""
        return self.hass.data[DOMAIN][self.config_entry.entry_id]["total_pellets"]

    @property
    def extra_state_attributes(self) -> dict:
        """Return additional state attributes."""
        return {
            "history": self.hass.data[DOMAIN][self.config_entry.entry_id]["history"][-10:]
        }

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.config_entry.entry_id)},
            name="Scorta Pellet",
            manufacturer="Custom Components",
            model="Pellet Stock Manager",
            sw_version="1.0.0"
        )