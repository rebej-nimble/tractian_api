from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.item_reservation_motor import ItemReservationMotor
from ...models.item_reservation_update_api import ItemReservationUpdateAPI
from ...types import Response


def _get_kwargs(
    reservation_id: str,
    *,
    body: ItemReservationUpdateAPI,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/reservations/{reservation_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ItemReservationMotor]]:
    if response.status_code == 200:
        response_200 = ItemReservationMotor.from_dict(response.json())

        return response_200
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
    reservation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ItemReservationUpdateAPI,
) -> Response[Union[HTTPValidationError, ItemReservationMotor]]:
    """Update Item Reservations By Id

     **If your company already use Supply Module you must use the Supply routes.**

    This endpoint updates an existing item reservation.

    Args:
        reservation_id (str):
        body (ItemReservationUpdateAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ItemReservationMotor]]
    """

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reservation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ItemReservationUpdateAPI,
) -> Optional[Union[HTTPValidationError, ItemReservationMotor]]:
    """Update Item Reservations By Id

     **If your company already use Supply Module you must use the Supply routes.**

    This endpoint updates an existing item reservation.

    Args:
        reservation_id (str):
        body (ItemReservationUpdateAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ItemReservationMotor]
    """

    return sync_detailed(
        reservation_id=reservation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    reservation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ItemReservationUpdateAPI,
) -> Response[Union[HTTPValidationError, ItemReservationMotor]]:
    """Update Item Reservations By Id

     **If your company already use Supply Module you must use the Supply routes.**

    This endpoint updates an existing item reservation.

    Args:
        reservation_id (str):
        body (ItemReservationUpdateAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ItemReservationMotor]]
    """

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reservation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ItemReservationUpdateAPI,
) -> Optional[Union[HTTPValidationError, ItemReservationMotor]]:
    """Update Item Reservations By Id

     **If your company already use Supply Module you must use the Supply routes.**

    This endpoint updates an existing item reservation.

    Args:
        reservation_id (str):
        body (ItemReservationUpdateAPI):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ItemReservationMotor]
    """

    return (
        await asyncio_detailed(
            reservation_id=reservation_id,
            client=client,
            body=body,
        )
    ).parsed
