from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    status: Union[None, Unset, str] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_status: Union[None, Unset, str]
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_sort: Union[None, Unset, str]
    if isinstance(sort, Unset):
        json_sort = UNSET
    else:
        json_sort = sort
    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/supply/companies/{company_id}/transfer-request",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
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
) -> Response[Union[Any, HTTPValidationError]]:
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
    status: Union[None, Unset, str] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
) -> Response[Union[Any, HTTPValidationError]]:
    """Load Transfer Request By Company Id

     Load transfer requests by company id.

    Args:
        company_id (str): Company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Filter for loading transfer request by status.
        sort (Union[None, Unset, str]): Sort by supplier name. Default: 'id:asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        status=status,
        sort=sort,
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
    status: Union[None, Unset, str] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
) -> Optional[Union[Any, HTTPValidationError]]:
    """Load Transfer Request By Company Id

     Load transfer requests by company id.

    Args:
        company_id (str): Company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Filter for loading transfer request by status.
        sort (Union[None, Unset, str]): Sort by supplier name. Default: 'id:asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
        status=status,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    status: Union[None, Unset, str] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
) -> Response[Union[Any, HTTPValidationError]]:
    """Load Transfer Request By Company Id

     Load transfer requests by company id.

    Args:
        company_id (str): Company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Filter for loading transfer request by status.
        sort (Union[None, Unset, str]): Sort by supplier name. Default: 'id:asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        status=status,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    status: Union[None, Unset, str] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
) -> Optional[Union[Any, HTTPValidationError]]:
    """Load Transfer Request By Company Id

     Load transfer requests by company id.

    Args:
        company_id (str): Company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Filter for loading transfer request by status.
        sort (Union[None, Unset, str]): Sort by supplier name. Default: 'id:asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
            status=status,
            sort=sort,
        )
    ).parsed
