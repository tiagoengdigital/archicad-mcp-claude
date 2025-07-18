# This file is auto-generated by generate_tools.py. DO NOT EDIT.
import logging
from pydantic import ValidationError
from multiconn_archicad.basic_types import Port
from tapir_archicad_mcp.app import mcp
from tapir_archicad_mcp.context import multi_conn_instance

from multiconn_archicad.models.commands import (
    ReleaseElementsParameters,
ReserveElementsParameters,
ReserveElementsResult
)


log = logging.getLogger()


@mcp.tool(
    name="teamwork_release_elements",
    title="ReleaseElements",
    description="Releases elements in Teamwork mode."
)
def release_elements(port: int, params: ReleaseElementsParameters) -> None:
    """
    Releases elements in Teamwork mode.

    To find a valid 'port' number, use the 'tapir_discovery_list_active_archicads' tool.
    """
    log.info(f"Executing release_elements tool on port {port}")
    multi_conn = multi_conn_instance.get()
    target_port = Port(port)
    if target_port not in multi_conn.active:
        raise ValueError(f"Port {port} is not an active Archicad connection.")
    conn_header = multi_conn.active[target_port]
    try:

        conn_header.core.post_tapir_command(
            command="ReleaseElements",
            parameters=params.model_dump(mode='json')
        )
        return None

    except ValidationError as e:
        log.error(f"Validation error for ReleaseElements result: {e}")
        raise ValueError(f"Received an invalid response from the Archicad API: {e}")
    except Exception as e:
        log.error(f"Error executing ReleaseElements on port {port}: {e}")
        raise e



@mcp.tool(
    name="teamwork_reserve_elements",
    title="ReserveElements",
    description="Reserves elements in Teamwork mode."
)
def reserve_elements(port: int, params: ReserveElementsParameters) -> ReserveElementsResult:
    """
    Reserves elements in Teamwork mode.

    To find a valid 'port' number, use the 'tapir_discovery_list_active_archicads' tool.
    """
    log.info(f"Executing reserve_elements tool on port {port}")
    multi_conn = multi_conn_instance.get()
    target_port = Port(port)
    if target_port not in multi_conn.active:
        raise ValueError(f"Port {port} is not an active Archicad connection.")
    conn_header = multi_conn.active[target_port]
    try:

        result_dict = conn_header.core.post_tapir_command(
            command="ReserveElements",
            parameters=params.model_dump(mode='json')
        )
        return ReserveElementsResult.model_validate(result_dict)

    except ValidationError as e:
        log.error(f"Validation error for ReserveElements result: {e}")
        raise ValueError(f"Received an invalid response from the Archicad API: {e}")
    except Exception as e:
        log.error(f"Error executing ReserveElements on port {port}: {e}")
        raise e



@mcp.tool(
    name="teamwork_teamwork_receive",
    title="TeamworkReceive",
    description="Performs a receive operation on the currently opened Teamwork project."
)
def teamwork_receive(port: int) -> None:
    """
    Performs a receive operation on the currently opened Teamwork project.

    To find a valid 'port' number, use the 'tapir_discovery_list_active_archicads' tool.
    """
    log.info(f"Executing teamwork_receive tool on port {port}")
    multi_conn = multi_conn_instance.get()
    target_port = Port(port)
    if target_port not in multi_conn.active:
        raise ValueError(f"Port {port} is not an active Archicad connection.")
    conn_header = multi_conn.active[target_port]
    try:

        conn_header.core.post_tapir_command(
            command="TeamworkReceive",
            parameters={}
        )
        return None

    except ValidationError as e:
        log.error(f"Validation error for TeamworkReceive result: {e}")
        raise ValueError(f"Received an invalid response from the Archicad API: {e}")
    except Exception as e:
        log.error(f"Error executing TeamworkReceive on port {port}: {e}")
        raise e



@mcp.tool(
    name="teamwork_teamwork_send",
    title="TeamworkSend",
    description="Performs a send operation on the currently opened Teamwork project."
)
def teamwork_send(port: int) -> None:
    """
    Performs a send operation on the currently opened Teamwork project.

    To find a valid 'port' number, use the 'tapir_discovery_list_active_archicads' tool.
    """
    log.info(f"Executing teamwork_send tool on port {port}")
    multi_conn = multi_conn_instance.get()
    target_port = Port(port)
    if target_port not in multi_conn.active:
        raise ValueError(f"Port {port} is not an active Archicad connection.")
    conn_header = multi_conn.active[target_port]
    try:

        conn_header.core.post_tapir_command(
            command="TeamworkSend",
            parameters={}
        )
        return None

    except ValidationError as e:
        log.error(f"Validation error for TeamworkSend result: {e}")
        raise ValueError(f"Received an invalid response from the Archicad API: {e}")
    except Exception as e:
        log.error(f"Error executing TeamworkSend on port {port}: {e}")
        raise e
