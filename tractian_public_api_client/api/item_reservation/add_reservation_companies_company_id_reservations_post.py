from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.item_reservation_motor import ItemReservationMotor
from ...models.item_reservation_request_api import ItemReservationRequestAPI
from ...types import Response


def _get_kwargs(
    company_id: str,
    *,
    body: ItemReservationRequestAPI,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/companies/{company_id}/reservations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ItemReservationMotor]]:
    if response.status_code == 201:
        response_201 = ItemReservationMotor.from_dict(response.json())

        return response_201
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, ItemReservationMotor]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    body: ItemReservationRequestAPI,
) -> Response[Union[HTTPValidationError, ItemReservationMotor]]:
    """Add Reservation

    Args:
        company_id (str):
        body (ItemReservationRequestAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ItemReservationMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    body: ItemReservationRequestAPI,
) -> Optional[Union[HTTPValidationError, ItemReservationMotor]]:
    """Add Reservation

    Args:
        company_id (str):
        body (ItemReservationRequestAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ItemReservationMotor]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    body: ItemReservationRequestAPI,
) -> Response[Union[HTTPValidationError, ItemReservationMotor]]:
    """Add Reservation

    Args:
        company_id (str):
        body (ItemReservationRequestAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ItemReservationMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    body: ItemReservationRequestAPI,
) -> Optional[Union[HTTPValidationError, ItemReservationMotor]]:
    """Add Reservation

    Args:
        company_id (str):
        body (ItemReservationRequestAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ItemReservationMotor]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            body=body,
        )
    ).parsed
