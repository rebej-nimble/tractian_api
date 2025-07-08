from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_item_reservation_motor import PaginationItemReservationMotor
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    number: Union[None, Unset, int] = UNSET,
    work_order_id: Union[None, Unset, str] = UNSET,
    deleted: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_number: Union[None, Unset, int]
    if isinstance(number, Unset):
        json_number = UNSET
    else:
        json_number = number
    params["number"] = json_number

    json_work_order_id: Union[None, Unset, str]
    if isinstance(work_order_id, Unset):
        json_work_order_id = UNSET
    else:
        json_work_order_id = work_order_id
    params["workOrderId"] = json_work_order_id

    json_deleted: Union[None, Unset, str]
    if isinstance(deleted, Unset):
        json_deleted = UNSET
    else:
        json_deleted = deleted
    params["deleted"] = json_deleted

    json_status: Union[None, Unset, str]
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/reservations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, PaginationItemReservationMotor]]:
    if response.status_code == 200:
        response_200 = PaginationItemReservationMotor.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, PaginationItemReservationMotor]]:
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
    number: Union[None, Unset, int] = UNSET,
    work_order_id: Union[None, Unset, str] = UNSET,
    deleted: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, PaginationItemReservationMotor]]:
    """Load Item Reservations By Company Id

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        number (Union[None, Unset, int]):
        work_order_id (Union[None, Unset, str]):
        deleted (Union[None, Unset, str]):
        status (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginationItemReservationMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        number=number,
        work_order_id=work_order_id,
        deleted=deleted,
        status=status,
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
    number: Union[None, Unset, int] = UNSET,
    work_order_id: Union[None, Unset, str] = UNSET,
    deleted: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, PaginationItemReservationMotor]]:
    """Load Item Reservations By Company Id

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        number (Union[None, Unset, int]):
        work_order_id (Union[None, Unset, str]):
        deleted (Union[None, Unset, str]):
        status (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginationItemReservationMotor]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
        number=number,
        work_order_id=work_order_id,
        deleted=deleted,
        status=status,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    number: Union[None, Unset, int] = UNSET,
    work_order_id: Union[None, Unset, str] = UNSET,
    deleted: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, PaginationItemReservationMotor]]:
    """Load Item Reservations By Company Id

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        number (Union[None, Unset, int]):
        work_order_id (Union[None, Unset, str]):
        deleted (Union[None, Unset, str]):
        status (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginationItemReservationMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        number=number,
        work_order_id=work_order_id,
        deleted=deleted,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    number: Union[None, Unset, int] = UNSET,
    work_order_id: Union[None, Unset, str] = UNSET,
    deleted: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, PaginationItemReservationMotor]]:
    """Load Item Reservations By Company Id

    Args:
        company_id (str): company id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        number (Union[None, Unset, int]):
        work_order_id (Union[None, Unset, str]):
        deleted (Union[None, Unset, str]):
        status (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginationItemReservationMotor]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
            number=number,
            work_order_id=work_order_id,
            deleted=deleted,
            status=status,
        )
    ).parsed
