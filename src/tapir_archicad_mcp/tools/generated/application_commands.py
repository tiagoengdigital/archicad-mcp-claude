# This file is auto-generated by generate_tools.py. DO NOT EDIT.
import logging
from pydantic import ValidationError
from multiconn_archicad.basic_types import Port
from tapir_archicad_mcp.app import mcp
from tapir_archicad_mcp.context import multi_conn_instance

from multiconn_archicad.models.commands import (
    GetAddOnVersionResult,
GetCurrentWindowTypeResult
)


log = logging.getLogger()


@mcp.tool(
    name="app_get_add_on_version",
    title="GetAddOnVersion",
    description="Retrieves the version of the Tapir Additional JSON Commands Add-On."
)
def get_add_on_version(port: int) -> GetAddOnVersionResult:
    """
    Retrieves the version of the Tapir Additional JSON Commands Add-On.

    To find a valid 'port' number, use the 'tapir_discovery_list_active_archicads' tool.
    """
    log.info(f"Executing get_add_on_version tool on port {port}")
    multi_conn = multi_conn_instance.get()
    target_port = Port(port)
    if target_port not in multi_conn.active:
        raise ValueError(f"Port {port} is not an active Archicad connection.")
    conn_header = multi_conn.active[target_port]
    try:

        result_dict = conn_header.core.post_tapir_command(
            command="GetAddOnVersion",
            parameters={}
        )
        return GetAddOnVersionResult.model_validate(result_dict)

    except ValidationError as e:
        log.error(f"Validation error for GetAddOnVersion result: {e}")
        raise ValueError(f"Received an invalid response from the Archicad API: {e}")
    except Exception as e:
        log.error(f"Error executing GetAddOnVersion on port {port}: {e}")
        raise e



@mcp.tool(
    name="app_get_current_window_type",
    title="GetCurrentWindowType",
    description="Returns the type of the current (active) window."
)
def get_current_window_type(port: int) -> GetCurrentWindowTypeResult:
    """
    Returns the type of the current (active) window.

    To find a valid 'port' number, use the 'tapir_discovery_list_active_archicads' tool.
    """
    log.info(f"Executing get_current_window_type tool on port {port}")
    multi_conn = multi_conn_instance.get()
    target_port = Port(port)
    if target_port not in multi_conn.active:
        raise ValueError(f"Port {port} is not an active Archicad connection.")
    conn_header = multi_conn.active[target_port]
    try:

        result_dict = conn_header.core.post_tapir_command(
            command="GetCurrentWindowType",
            parameters={}
        )
        return GetCurrentWindowTypeResult.model_validate(result_dict)

    except ValidationError as e:
        log.error(f"Validation error for GetCurrentWindowType result: {e}")
        raise ValueError(f"Received an invalid response from the Archicad API: {e}")
    except Exception as e:
        log.error(f"Error executing GetCurrentWindowType on port {port}: {e}")
        raise e
