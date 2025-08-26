from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_dto_asset_motor import PaginationDTOAssetMotor
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/assets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PaginationDTOAssetMotor]]:
    if response.status_code == 200:
        response_200 = PaginationDTOAssetMotor.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, HTTPValidationError, PaginationDTOAssetMotor]]:
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
) -> Response[Union[Any, HTTPValidationError, PaginationDTOAssetMotor]]:
    """List assets by company ID

     This endpoint retrieves a list of assets by company / plant, its response is paginated.

    Args:
        company_id (str): Unique identifier for the company / plant on TracOS
        page (Union[Unset, int]): Page number to retrieve. Default: 1.
        limit (Union[Unset, int]): Number of items per page. Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationDTOAssetMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
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
) -> Optional[Union[Any, HTTPValidationError, PaginationDTOAssetMotor]]:
    """List assets by company ID

     This endpoint retrieves a list of assets by company / plant, its response is paginated.

    Args:
        company_id (str): Unique identifier for the company / plant on TracOS
        page (Union[Unset, int]): Page number to retrieve. Default: 1.
        limit (Union[Unset, int]): Number of items per page. Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationDTOAssetMotor]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
) -> Response[Union[Any, HTTPValidationError, PaginationDTOAssetMotor]]:
    """List assets by company ID

     This endpoint retrieves a list of assets by company / plant, its response is paginated.

    Args:
        company_id (str): Unique identifier for the company / plant on TracOS
        page (Union[Unset, int]): Page number to retrieve. Default: 1.
        limit (Union[Unset, int]): Number of items per page. Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationDTOAssetMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
) -> Optional[Union[Any, HTTPValidationError, PaginationDTOAssetMotor]]:
    """List assets by company ID

     This endpoint retrieves a list of assets by company / plant, its response is paginated.

    Args:
        company_id (str): Unique identifier for the company / plant on TracOS
        page (Union[Unset, int]): Page number to retrieve. Default: 1.
        limit (Union[Unset, int]): Number of items per page. Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationDTOAssetMotor]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
        )
    ).parsed
