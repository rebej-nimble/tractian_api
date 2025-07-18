from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_work_orders_motor import PaginationWorkOrdersMotor
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    status: Union[None, Unset, str] = UNSET,
    due_date: Union[None, Unset, str] = UNSET,
    created_at: Union[None, Unset, str] = UNSET,
    updated_at: Union[None, Unset, str] = UNSET,
    planning_status: Union[None, Unset, str] = UNSET,
    planned_start_date: Union[None, Unset, str] = UNSET,
    load_work_order_operations: Union[None, Unset, str] = "true",
    load_custom_fields: Union[None, Unset, str] = "true",
    ignore_sort: Union[None, Unset, str] = "true",
    deleted: Union[None, Unset, str] = UNSET,
    number: Union[None, Unset, str] = UNSET,
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

    json_due_date: Union[None, Unset, str]
    if isinstance(due_date, Unset):
        json_due_date = UNSET
    else:
        json_due_date = due_date
    params["dueDate"] = json_due_date

    json_created_at: Union[None, Unset, str]
    if isinstance(created_at, Unset):
        json_created_at = UNSET
    else:
        json_created_at = created_at
    params["createdAt"] = json_created_at

    json_updated_at: Union[None, Unset, str]
    if isinstance(updated_at, Unset):
        json_updated_at = UNSET
    else:
        json_updated_at = updated_at
    params["updatedAt"] = json_updated_at

    json_planning_status: Union[None, Unset, str]
    if isinstance(planning_status, Unset):
        json_planning_status = UNSET
    else:
        json_planning_status = planning_status
    params["planningStatus"] = json_planning_status

    json_planned_start_date: Union[None, Unset, str]
    if isinstance(planned_start_date, Unset):
        json_planned_start_date = UNSET
    else:
        json_planned_start_date = planned_start_date
    params["plannedStartDate"] = json_planned_start_date

    json_load_work_order_operations: Union[None, Unset, str]
    if isinstance(load_work_order_operations, Unset):
        json_load_work_order_operations = UNSET
    else:
        json_load_work_order_operations = load_work_order_operations
    params["loadWorkOrderOperations"] = json_load_work_order_operations

    json_load_custom_fields: Union[None, Unset, str]
    if isinstance(load_custom_fields, Unset):
        json_load_custom_fields = UNSET
    else:
        json_load_custom_fields = load_custom_fields
    params["loadCustomFields"] = json_load_custom_fields

    json_ignore_sort: Union[None, Unset, str]
    if isinstance(ignore_sort, Unset):
        json_ignore_sort = UNSET
    else:
        json_ignore_sort = ignore_sort
    params["ignoreSort"] = json_ignore_sort

    json_deleted: Union[None, Unset, str]
    if isinstance(deleted, Unset):
        json_deleted = UNSET
    else:
        json_deleted = deleted
    params["deleted"] = json_deleted

    json_number: Union[None, Unset, str]
    if isinstance(number, Unset):
        json_number = UNSET
    else:
        json_number = number
    params["number"] = json_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/workorders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    if response.status_code == 200:
        response_200 = PaginationWorkOrdersMotor.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
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
    status: Union[None, Unset, str] = UNSET,
    due_date: Union[None, Unset, str] = UNSET,
    created_at: Union[None, Unset, str] = UNSET,
    updated_at: Union[None, Unset, str] = UNSET,
    planning_status: Union[None, Unset, str] = UNSET,
    planned_start_date: Union[None, Unset, str] = UNSET,
    load_work_order_operations: Union[None, Unset, str] = "true",
    load_custom_fields: Union[None, Unset, str] = "true",
    ignore_sort: Union[None, Unset, str] = "true",
    deleted: Union[None, Unset, str] = UNSET,
    number: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    """List work orders by company ID

     This endpoint retrieves a list of work orders by company / plant, its response is paginated.

    Args:
        company_id (str): ID of the workorder to be loaded
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Work order status
        due_date (Union[None, Unset, str]): Due date range
        created_at (Union[None, Unset, str]): Creation date range
        updated_at (Union[None, Unset, str]): Update date range
        planning_status (Union[None, Unset, str]): Planning status
        planned_start_date (Union[None, Unset, str]): Planned start date range
        load_work_order_operations (Union[None, Unset, str]): Load work order operations Default:
            'true'.
        load_custom_fields (Union[None, Unset, str]): Load custom fields Default: 'true'.
        ignore_sort (Union[None, Unset, str]): Ignore sorting Default: 'true'.
        deleted (Union[None, Unset, str]): Filter deleted work orders
        number (Union[None, Unset, str]): Work order number

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        status=status,
        due_date=due_date,
        created_at=created_at,
        updated_at=updated_at,
        planning_status=planning_status,
        planned_start_date=planned_start_date,
        load_work_order_operations=load_work_order_operations,
        load_custom_fields=load_custom_fields,
        ignore_sort=ignore_sort,
        deleted=deleted,
        number=number,
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
    status: Union[None, Unset, str] = UNSET,
    due_date: Union[None, Unset, str] = UNSET,
    created_at: Union[None, Unset, str] = UNSET,
    updated_at: Union[None, Unset, str] = UNSET,
    planning_status: Union[None, Unset, str] = UNSET,
    planned_start_date: Union[None, Unset, str] = UNSET,
    load_work_order_operations: Union[None, Unset, str] = "true",
    load_custom_fields: Union[None, Unset, str] = "true",
    ignore_sort: Union[None, Unset, str] = "true",
    deleted: Union[None, Unset, str] = UNSET,
    number: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    """List work orders by company ID

     This endpoint retrieves a list of work orders by company / plant, its response is paginated.

    Args:
        company_id (str): ID of the workorder to be loaded
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Work order status
        due_date (Union[None, Unset, str]): Due date range
        created_at (Union[None, Unset, str]): Creation date range
        updated_at (Union[None, Unset, str]): Update date range
        planning_status (Union[None, Unset, str]): Planning status
        planned_start_date (Union[None, Unset, str]): Planned start date range
        load_work_order_operations (Union[None, Unset, str]): Load work order operations Default:
            'true'.
        load_custom_fields (Union[None, Unset, str]): Load custom fields Default: 'true'.
        ignore_sort (Union[None, Unset, str]): Ignore sorting Default: 'true'.
        deleted (Union[None, Unset, str]): Filter deleted work orders
        number (Union[None, Unset, str]): Work order number

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
        status=status,
        due_date=due_date,
        created_at=created_at,
        updated_at=updated_at,
        planning_status=planning_status,
        planned_start_date=planned_start_date,
        load_work_order_operations=load_work_order_operations,
        load_custom_fields=load_custom_fields,
        ignore_sort=ignore_sort,
        deleted=deleted,
        number=number,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    status: Union[None, Unset, str] = UNSET,
    due_date: Union[None, Unset, str] = UNSET,
    created_at: Union[None, Unset, str] = UNSET,
    updated_at: Union[None, Unset, str] = UNSET,
    planning_status: Union[None, Unset, str] = UNSET,
    planned_start_date: Union[None, Unset, str] = UNSET,
    load_work_order_operations: Union[None, Unset, str] = "true",
    load_custom_fields: Union[None, Unset, str] = "true",
    ignore_sort: Union[None, Unset, str] = "true",
    deleted: Union[None, Unset, str] = UNSET,
    number: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    """List work orders by company ID

     This endpoint retrieves a list of work orders by company / plant, its response is paginated.

    Args:
        company_id (str): ID of the workorder to be loaded
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Work order status
        due_date (Union[None, Unset, str]): Due date range
        created_at (Union[None, Unset, str]): Creation date range
        updated_at (Union[None, Unset, str]): Update date range
        planning_status (Union[None, Unset, str]): Planning status
        planned_start_date (Union[None, Unset, str]): Planned start date range
        load_work_order_operations (Union[None, Unset, str]): Load work order operations Default:
            'true'.
        load_custom_fields (Union[None, Unset, str]): Load custom fields Default: 'true'.
        ignore_sort (Union[None, Unset, str]): Ignore sorting Default: 'true'.
        deleted (Union[None, Unset, str]): Filter deleted work orders
        number (Union[None, Unset, str]): Work order number

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        status=status,
        due_date=due_date,
        created_at=created_at,
        updated_at=updated_at,
        planning_status=planning_status,
        planned_start_date=planned_start_date,
        load_work_order_operations=load_work_order_operations,
        load_custom_fields=load_custom_fields,
        ignore_sort=ignore_sort,
        deleted=deleted,
        number=number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    status: Union[None, Unset, str] = UNSET,
    due_date: Union[None, Unset, str] = UNSET,
    created_at: Union[None, Unset, str] = UNSET,
    updated_at: Union[None, Unset, str] = UNSET,
    planning_status: Union[None, Unset, str] = UNSET,
    planned_start_date: Union[None, Unset, str] = UNSET,
    load_work_order_operations: Union[None, Unset, str] = "true",
    load_custom_fields: Union[None, Unset, str] = "true",
    ignore_sort: Union[None, Unset, str] = "true",
    deleted: Union[None, Unset, str] = UNSET,
    number: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]]:
    """List work orders by company ID

     This endpoint retrieves a list of work orders by company / plant, its response is paginated.

    Args:
        company_id (str): ID of the workorder to be loaded
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Work order status
        due_date (Union[None, Unset, str]): Due date range
        created_at (Union[None, Unset, str]): Creation date range
        updated_at (Union[None, Unset, str]): Update date range
        planning_status (Union[None, Unset, str]): Planning status
        planned_start_date (Union[None, Unset, str]): Planned start date range
        load_work_order_operations (Union[None, Unset, str]): Load work order operations Default:
            'true'.
        load_custom_fields (Union[None, Unset, str]): Load custom fields Default: 'true'.
        ignore_sort (Union[None, Unset, str]): Ignore sorting Default: 'true'.
        deleted (Union[None, Unset, str]): Filter deleted work orders
        number (Union[None, Unset, str]): Work order number

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationWorkOrdersMotor]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
            status=status,
            due_date=due_date,
            created_at=created_at,
            updated_at=updated_at,
            planning_status=planning_status,
            planned_start_date=planned_start_date,
            load_work_order_operations=load_work_order_operations,
            load_custom_fields=load_custom_fields,
            ignore_sort=ignore_sort,
            deleted=deleted,
            number=number,
        )
    ).parsed
