from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.inventory_mongo_db import InventoryMongoDB
from ...types import Response


def _get_kwargs(
    company_id: str,
    identifier_code: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/inventory/identifier/{identifier_code}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, InventoryMongoDB]]:
    if response.status_code == 200:
        response_200 = InventoryMongoDB.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, InventoryMongoDB]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    identifier_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, InventoryMongoDB]]:
    """Load Inventory By Identifier Code

     **If your company already use Supply Module you must use the Supply routes.**

    Use `GET /supply/companies/{company_id}/inventory` with filters instead.

    This endpoint loads an inventory item by its identifier code.

    Args:
        company_id (str):
        identifier_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, InventoryMongoDB]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        identifier_code=identifier_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    identifier_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, InventoryMongoDB]]:
    """Load Inventory By Identifier Code

     **If your company already use Supply Module you must use the Supply routes.**

    Use `GET /supply/companies/{company_id}/inventory` with filters instead.

    This endpoint loads an inventory item by its identifier code.

    Args:
        company_id (str):
        identifier_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, InventoryMongoDB]
    """

    return sync_detailed(
        company_id=company_id,
        identifier_code=identifier_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    identifier_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, InventoryMongoDB]]:
    """Load Inventory By Identifier Code

     **If your company already use Supply Module you must use the Supply routes.**

    Use `GET /supply/companies/{company_id}/inventory` with filters instead.

    This endpoint loads an inventory item by its identifier code.

    Args:
        company_id (str):
        identifier_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, InventoryMongoDB]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        identifier_code=identifier_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    identifier_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, InventoryMongoDB]]:
    """Load Inventory By Identifier Code

     **If your company already use Supply Module you must use the Supply routes.**

    Use `GET /supply/companies/{company_id}/inventory` with filters instead.

    This endpoint loads an inventory item by its identifier code.

    Args:
        company_id (str):
        identifier_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, InventoryMongoDB]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            identifier_code=identifier_code,
            client=client,
        )
    ).parsed
