from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_work_orders_motor import PaginationWorkOrdersMotor
from ...models.work_orders_motor_request_api import WorkOrdersMotorRequestAPI
from ...types import Response


def _get_kwargs(
    *,
    body: WorkOrdersMotorRequestAPI,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workorders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    if response.status_code == 201:
        response_201 = PaginationWorkOrdersMotor.from_dict(response.json())

        return response_201
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkOrdersMotorRequestAPI,
) -> Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    """Create a work order

     This endpoint creates a new work order.

    Args:
        body (WorkOrdersMotorRequestAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkOrdersMotorRequestAPI,
) -> Optional[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    """Create a work order

     This endpoint creates a new work order.

    Args:
        body (WorkOrdersMotorRequestAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkOrdersMotorRequestAPI,
) -> Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    """Create a work order

     This endpoint creates a new work order.

    Args:
        body (WorkOrdersMotorRequestAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkOrdersMotorRequestAPI,
) -> Optional[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    """Create a work order

     This endpoint creates a new work order.

    Args:
        body (WorkOrdersMotorRequestAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
