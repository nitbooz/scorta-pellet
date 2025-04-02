"""The Scorta Pellet integration."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

LOGGER = logging.getLogger(__name__)
DOMAIN = "scorta_pellet"
PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Scorta Pellet from a config entry."""
    initial_stock = entry.data.get("initial_stock", 0)
    hass.data.setdefault(entry.entry_id, {
        "total_pellets": initial_stock,
        "history": [("initial", initial_stock)] if initial_stock > 0 else []
    })

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    async def add_pellets(call):
        """Service to add pellets to the stock."""
        amount = call.data.get("amount", 0)
        if amount > 0:
            hass.data[entry.entry_id]["total_pellets"] += amount
            hass.data[entry.entry_id]["history"].append(("add", amount))
            await hass.data[entry.entry_id]["sensor"].async_update_ha_state()

    async def remove_pellets(call):
        """Service to remove pellets from the stock."""
        amount = call.data.get("amount", 0)
        if amount > 0 and amount <= hass.data[entry.entry_id]["total_pellets"]:
            hass.data[entry.entry_id]["total_pellets"] -= amount
            hass.data[entry.entry_id]["history"].append(("remove", amount))
            await hass.data[entry.entry_id]["sensor"].async_update_ha_state()

    hass.services.async_register(DOMAIN, "add_pellets", add_pellets)
    hass.services.async_register(DOMAIN, "remove_pellets", remove_pellets)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data.pop(entry.entry_id)

    return unload_ok