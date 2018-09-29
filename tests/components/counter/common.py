"""Collection of helper methods.

All containing methods are legacy helpers that should not be used by new
components. Instead call the service directly.
"""
from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.components.counter import (
    DOMAIN, SERVICE_DECREMENT, SERVICE_INCREMENT, SERVICE_RESET)
from homeassistant.core import callback
from homeassistant.loader import bind_hass


@bind_hass
def increment(hass, entity_id):
    """Increment a counter."""
    hass.add_job(async_increment, hass, entity_id)


@callback
@bind_hass
def async_increment(hass, entity_id):
    """Increment a counter."""
    hass.async_add_job(hass.services.async_call(
        DOMAIN, SERVICE_INCREMENT, {ATTR_ENTITY_ID: entity_id}))


@bind_hass
def decrement(hass, entity_id):
    """Decrement a counter."""
    hass.add_job(async_decrement, hass, entity_id)


@callback
@bind_hass
def async_decrement(hass, entity_id):
    """Decrement a counter."""
    hass.async_add_job(hass.services.async_call(
        DOMAIN, SERVICE_DECREMENT, {ATTR_ENTITY_ID: entity_id}))


@bind_hass
def reset(hass, entity_id):
    """Reset a counter."""
    hass.add_job(async_reset, hass, entity_id)


@callback
@bind_hass
def async_reset(hass, entity_id):
    """Reset a counter."""
    hass.async_add_job(hass.services.async_call(
        DOMAIN, SERVICE_RESET, {ATTR_ENTITY_ID: entity_id}))