from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    reservation_id: str,
    *,
    company_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["company-id"] = company_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/reservations/{reservation_id}/withdrawn",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reservation_id: str,
    *,
    client: AuthenticatedClient,
    company_id: str,
) -> Response[Union[Any, HTTPValidationError]]:
    """Close Item Reservation By Id

    Args:
        reservation_id (str):
        company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reservation_id: str,
    *,
    client: AuthenticatedClient,
    company_id: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Close Item Reservation By Id

    Args:
        reservation_id (str):
        company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        reservation_id=reservation_id,
        client=client,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    reservation_id: str,
    *,
    client: AuthenticatedClient,
    company_id: str,
) -> Response[Union[Any, HTTPValidationError]]:
    """Close Item Reservation By Id

    Args:
        reservation_id (str):
        company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reservation_id: str,
    *,
    client: AuthenticatedClient,
    company_id: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Close Item Reservation By Id

    Args:
        reservation_id (str):
        company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            reservation_id=reservation_id,
            client=client,
            company_id=company_id,
        )
    ).parsed
