"""Config flow for Scorta Pellet integration."""
from __future__ import annotations

from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_validation as cv

class ScortaPelletConfigFlow(config_entries.ConfigFlow, domain="scorta_pellet"):
    """Handle a config flow for Scorta Pellet."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> FlowResult:
        """Handle the initial step."""
        
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({
                    vol.Required("initial_stock", default=0): cv.positive_int,
                }),
            )

        return self.async_create_entry(
            title="Scorta Pellet",
            data={"initial_stock": user_input["initial_stock"]},
        )