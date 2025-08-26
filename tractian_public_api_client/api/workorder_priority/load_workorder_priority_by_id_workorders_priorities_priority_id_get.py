from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.work_order_priorities_motor_response_api import (
    WorkOrderPrioritiesMotorResponseAPI,
)
from ...types import Response


def _get_kwargs(
    priority_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/workorders/priorities/{priority_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]]:
    if response.status_code == 200:
        response_200 = WorkOrderPrioritiesMotorResponseAPI.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    priority_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]]:
    """Load Workorder Priority By Id

     Load workorder priority by id.

    Args:
        priority_id (str): Workorder priority id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]]
    """

    kwargs = _get_kwargs(
        priority_id=priority_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    priority_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]]:
    """Load Workorder Priority By Id

     Load workorder priority by id.

    Args:
        priority_id (str): Workorder priority id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]
    """

    return sync_detailed(
        priority_id=priority_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    priority_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]]:
    """Load Workorder Priority By Id

     Load workorder priority by id.

    Args:
        priority_id (str): Workorder priority id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]]
    """

    kwargs = _get_kwargs(
        priority_id=priority_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    priority_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]]:
    """Load Workorder Priority By Id

     Load workorder priority by id.

    Args:
        priority_id (str): Workorder priority id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, WorkOrderPrioritiesMotorResponseAPI]
    """

    return (
        await asyncio_detailed(
            priority_id=priority_id,
            client=client,
        )
    ).parsed
