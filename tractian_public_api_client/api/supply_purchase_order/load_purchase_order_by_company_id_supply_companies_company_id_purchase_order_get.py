from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_api_supply_purchase_order import (
    PaginationApiSupplyPurchaseOrder,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    search: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_search: Union[None, Unset, str]
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/supply/companies/{company_id}/purchase-order",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]]:
    if response.status_code == 200:
        response_200 = PaginationApiSupplyPurchaseOrder.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    search: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]]:
    """Load Purchase Order By Company Id

     Load a purchase order by company id

    Args:
        company_id (str):
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        search (Union[None, Unset, str]): Search for purchase order by name or number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    search: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]]:
    """Load Purchase Order By Company Id

     Load a purchase order by company id

    Args:
        company_id (str):
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        search (Union[None, Unset, str]): Search for purchase order by name or number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
        search=search,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    search: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]]:
    """Load Purchase Order By Company Id

     Load a purchase order by company id

    Args:
        company_id (str):
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        search (Union[None, Unset, str]): Search for purchase order by name or number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    search: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]]:
    """Load Purchase Order By Company Id

     Load a purchase order by company id

    Args:
        company_id (str):
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        search (Union[None, Unset, str]): Search for purchase order by name or number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginationApiSupplyPurchaseOrder]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
            search=search,
        )
    ).parsed
