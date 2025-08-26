from http import HTTPStatus
from typing import Any, Optional, Union

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
    sort: Union[Unset, str] = "id:asc",
    default: Union[None, Unset, bool] = UNSET,
    cost_center_code: Union[None, Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["sort"] = sort

    json_default: Union[None, Unset, bool]
    if isinstance(default, Unset):
        json_default = UNSET
    else:
        json_default = default
    params["default"] = json_default

    json_cost_center_code: Union[None, Unset, list[str]]
    if isinstance(cost_center_code, Unset):
        json_cost_center_code = UNSET
    elif isinstance(cost_center_code, list):
        json_cost_center_code = cost_center_code

    else:
        json_cost_center_code = cost_center_code
    params["costCenterCode"] = json_cost_center_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/supply/companies/{company_id}/cost-center",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HTTPValidationError]:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HTTPValidationError]:
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
    sort: Union[Unset, str] = "id:asc",
    default: Union[None, Unset, bool] = UNSET,
    cost_center_code: Union[None, Unset, list[str]] = UNSET,
) -> Response[HTTPValidationError]:
    """Load Cost Center By Company Id

     Load cost centers by company id.

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        sort (Union[Unset, str]): Sort fields. Example: id:asc. Default: 'id:asc'.
        default (Union[None, Unset, bool]): Filter for loading default cost center.
        cost_center_code (Union[None, Unset, list[str]]): Filter for loading cost center by code.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        sort=sort,
        default=default,
        cost_center_code=cost_center_code,
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
    sort: Union[Unset, str] = "id:asc",
    default: Union[None, Unset, bool] = UNSET,
    cost_center_code: Union[None, Unset, list[str]] = UNSET,
) -> Optional[HTTPValidationError]:
    """Load Cost Center By Company Id

     Load cost centers by company id.

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        sort (Union[Unset, str]): Sort fields. Example: id:asc. Default: 'id:asc'.
        default (Union[None, Unset, bool]): Filter for loading default cost center.
        cost_center_code (Union[None, Unset, list[str]]): Filter for loading cost center by code.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        default=default,
        cost_center_code=cost_center_code,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    sort: Union[Unset, str] = "id:asc",
    default: Union[None, Unset, bool] = UNSET,
    cost_center_code: Union[None, Unset, list[str]] = UNSET,
) -> Response[HTTPValidationError]:
    """Load Cost Center By Company Id

     Load cost centers by company id.

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        sort (Union[Unset, str]): Sort fields. Example: id:asc. Default: 'id:asc'.
        default (Union[None, Unset, bool]): Filter for loading default cost center.
        cost_center_code (Union[None, Unset, list[str]]): Filter for loading cost center by code.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        sort=sort,
        default=default,
        cost_center_code=cost_center_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    sort: Union[Unset, str] = "id:asc",
    default: Union[None, Unset, bool] = UNSET,
    cost_center_code: Union[None, Unset, list[str]] = UNSET,
) -> Optional[HTTPValidationError]:
    """Load Cost Center By Company Id

     Load cost centers by company id.

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        sort (Union[Unset, str]): Sort fields. Example: id:asc. Default: 'id:asc'.
        default (Union[None, Unset, bool]): Filter for loading default cost center.
        cost_center_code (Union[None, Unset, list[str]]): Filter for loading cost center by code.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
            sort=sort,
            default=default,
            cost_center_code=cost_center_code,
        )
    ).parsed
