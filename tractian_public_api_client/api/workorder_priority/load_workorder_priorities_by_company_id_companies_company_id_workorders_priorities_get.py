from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_work_order_priorities_motor_response_api import (
    PaginationWorkOrderPrioritiesMotorResponseAPI,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[None, Unset, bool] = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/workorders/priorities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]
]:
    if response.status_code == 200:
        response_200 = PaginationWorkOrderPrioritiesMotorResponseAPI.from_dict(
            response.json()
        )

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
) -> Response[
    Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]
]:
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
    deleted: Union[None, Unset, bool] = UNSET,
) -> Response[
    Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]
]:
    """Load Workorder Priorities By Company Id

     Load workorder priorities by company id.

    Args:
        company_id (str): Company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        deleted (Union[None, Unset, bool]): Filter for loading deleted items.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        deleted=deleted,
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
    deleted: Union[None, Unset, bool] = UNSET,
) -> Optional[
    Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]
]:
    """Load Workorder Priorities By Company Id

     Load workorder priorities by company id.

    Args:
        company_id (str): Company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        deleted (Union[None, Unset, bool]): Filter for loading deleted items.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
        deleted=deleted,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[None, Unset, bool] = UNSET,
) -> Response[
    Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]
]:
    """Load Workorder Priorities By Company Id

     Load workorder priorities by company id.

    Args:
        company_id (str): Company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        deleted (Union[None, Unset, bool]): Filter for loading deleted items.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        deleted=deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[None, Unset, bool] = UNSET,
) -> Optional[
    Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]
]:
    """Load Workorder Priorities By Company Id

     Load workorder priorities by company id.

    Args:
        company_id (str): Company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        deleted (Union[None, Unset, bool]): Filter for loading deleted items.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginationWorkOrderPrioritiesMotorResponseAPI]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
            deleted=deleted,
        )
    ).parsed
