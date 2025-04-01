"""
Scorta Pellet integration for Home Assistant.
"""
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "scorta_pellet"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Scorta Pellet component."""
    # Initialize data structure to store pellet purchases
    hass.data[DOMAIN] = {"total": 0, "purchases": []}
    return True