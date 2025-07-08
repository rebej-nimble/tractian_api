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
    deleted: Union[None, Unset, bool] = UNSET,
    disabled: Union[None, Unset, bool] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
    load_custom_fields: Union[None, Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_deleted: Union[None, Unset, bool]
    if isinstance(deleted, Unset):
        json_deleted = UNSET
    else:
        json_deleted = deleted
    params["deleted"] = json_deleted

    json_disabled: Union[None, Unset, bool]
    if isinstance(disabled, Unset):
        json_disabled = UNSET
    else:
        json_disabled = disabled
    params["disabled"] = json_disabled

    json_sort: Union[None, Unset, str]
    if isinstance(sort, Unset):
        json_sort = UNSET
    else:
        json_sort = sort
    params["sort"] = json_sort

    json_load_custom_fields: Union[None, Unset, bool]
    if isinstance(load_custom_fields, Unset):
        json_load_custom_fields = UNSET
    else:
        json_load_custom_fields = load_custom_fields
    params["loadCustomFields"] = json_load_custom_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/supply/companies/{company_id}/inventory",
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
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[None, Unset, bool] = UNSET,
    disabled: Union[None, Unset, bool] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
    load_custom_fields: Union[None, Unset, bool] = False,
) -> Response[HTTPValidationError]:
    """Load Inventory By Company Id

     Load supply items by company id.

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        deleted (Union[None, Unset, bool]): Filter for loading deleted items.
        disabled (Union[None, Unset, bool]): Filter for loading disabled items.
        sort (Union[None, Unset, str]): Field to sort the results. Default: 'id:asc'.
        load_custom_fields (Union[None, Unset, bool]): Load Custom Field Values. Default: False.

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
        deleted=deleted,
        disabled=disabled,
        sort=sort,
        load_custom_fields=load_custom_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[None, Unset, bool] = UNSET,
    disabled: Union[None, Unset, bool] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
    load_custom_fields: Union[None, Unset, bool] = False,
) -> Optional[HTTPValidationError]:
    """Load Inventory By Company Id

     Load supply items by company id.

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        deleted (Union[None, Unset, bool]): Filter for loading deleted items.
        disabled (Union[None, Unset, bool]): Filter for loading disabled items.
        sort (Union[None, Unset, str]): Field to sort the results. Default: 'id:asc'.
        load_custom_fields (Union[None, Unset, bool]): Load Custom Field Values. Default: False.

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
        deleted=deleted,
        disabled=disabled,
        sort=sort,
        load_custom_fields=load_custom_fields,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[None, Unset, bool] = UNSET,
    disabled: Union[None, Unset, bool] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
    load_custom_fields: Union[None, Unset, bool] = False,
) -> Response[HTTPValidationError]:
    """Load Inventory By Company Id

     Load supply items by company id.

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        deleted (Union[None, Unset, bool]): Filter for loading deleted items.
        disabled (Union[None, Unset, bool]): Filter for loading disabled items.
        sort (Union[None, Unset, str]): Field to sort the results. Default: 'id:asc'.
        load_custom_fields (Union[None, Unset, bool]): Load Custom Field Values. Default: False.

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
        deleted=deleted,
        disabled=disabled,
        sort=sort,
        load_custom_fields=load_custom_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[None, Unset, bool] = UNSET,
    disabled: Union[None, Unset, bool] = UNSET,
    sort: Union[None, Unset, str] = "id:asc",
    load_custom_fields: Union[None, Unset, bool] = False,
) -> Optional[HTTPValidationError]:
    """Load Inventory By Company Id

     Load supply items by company id.

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        deleted (Union[None, Unset, bool]): Filter for loading deleted items.
        disabled (Union[None, Unset, bool]): Filter for loading disabled items.
        sort (Union[None, Unset, str]): Field to sort the results. Default: 'id:asc'.
        load_custom_fields (Union[None, Unset, bool]): Load Custom Field Values. Default: False.

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
            deleted=deleted,
            disabled=disabled,
            sort=sort,
            load_custom_fields=load_custom_fields,
        )
    ).parsed
