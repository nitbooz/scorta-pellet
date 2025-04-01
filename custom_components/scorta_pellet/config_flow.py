"""Config flow for Scorta Pellet integration."""
from __future__ import annotations

from typing import Any

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

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
                data_schema=None,
            )

        return self.async_create_entry(
            title="Scorta Pellet",
            data={},
        )