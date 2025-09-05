from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_api_supply_purchase_requisition_response import (
    PaginationApiSupplyPurchaseRequisitionResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    status: Union[None, Unset, str] = UNSET,
    load_custom_fields: Union[None, Unset, str] = "true",
    load_created_by_system: Union[None, Unset, bool] = UNSET,
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

    json_load_custom_fields: Union[None, Unset, str]
    if isinstance(load_custom_fields, Unset):
        json_load_custom_fields = UNSET
    else:
        json_load_custom_fields = load_custom_fields
    params["loadCustomFields"] = json_load_custom_fields

    json_load_created_by_system: Union[None, Unset, bool]
    if isinstance(load_created_by_system, Unset):
        json_load_created_by_system = UNSET
    else:
        json_load_created_by_system = load_created_by_system
    params["loadCreatedBySystem"] = json_load_created_by_system

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/supply/companies/{company_id}/purchase-request",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]
]:
    if response.status_code == 200:
        response_200 = PaginationApiSupplyPurchaseRequisitionResponse.from_dict(
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
    Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]
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
    status: Union[None, Unset, str] = UNSET,
    load_custom_fields: Union[None, Unset, str] = "true",
    load_created_by_system: Union[None, Unset, bool] = UNSET,
) -> Response[
    Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]
]:
    """Load Purchase Request By Company Id

     Load a purchase request by company id

    Args:
        company_id (str):
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Filter for loading purchase requisition by status.
        load_custom_fields (Union[None, Unset, str]): Filter for loading custom fields. Default:
            'true'.
        load_created_by_system (Union[None, Unset, bool]): Filter for loading created
            automatically by system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        status=status,
        load_custom_fields=load_custom_fields,
        load_created_by_system=load_created_by_system,
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
    load_custom_fields: Union[None, Unset, str] = "true",
    load_created_by_system: Union[None, Unset, bool] = UNSET,
) -> Optional[
    Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]
]:
    """Load Purchase Request By Company Id

     Load a purchase request by company id

    Args:
        company_id (str):
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Filter for loading purchase requisition by status.
        load_custom_fields (Union[None, Unset, str]): Filter for loading custom fields. Default:
            'true'.
        load_created_by_system (Union[None, Unset, bool]): Filter for loading created
            automatically by system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
        status=status,
        load_custom_fields=load_custom_fields,
        load_created_by_system=load_created_by_system,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    status: Union[None, Unset, str] = UNSET,
    load_custom_fields: Union[None, Unset, str] = "true",
    load_created_by_system: Union[None, Unset, bool] = UNSET,
) -> Response[
    Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]
]:
    """Load Purchase Request By Company Id

     Load a purchase request by company id

    Args:
        company_id (str):
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Filter for loading purchase requisition by status.
        load_custom_fields (Union[None, Unset, str]): Filter for loading custom fields. Default:
            'true'.
        load_created_by_system (Union[None, Unset, bool]): Filter for loading created
            automatically by system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        status=status,
        load_custom_fields=load_custom_fields,
        load_created_by_system=load_created_by_system,
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
    load_custom_fields: Union[None, Unset, str] = "true",
    load_created_by_system: Union[None, Unset, bool] = UNSET,
) -> Optional[
    Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]
]:
    """Load Purchase Request By Company Id

     Load a purchase request by company id

    Args:
        company_id (str):
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        status (Union[None, Unset, str]): Filter for loading purchase requisition by status.
        load_custom_fields (Union[None, Unset, str]): Filter for loading custom fields. Default:
            'true'.
        load_created_by_system (Union[None, Unset, bool]): Filter for loading created
            automatically by system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginationApiSupplyPurchaseRequisitionResponse]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
            status=status,
            load_custom_fields=load_custom_fields,
            load_created_by_system=load_created_by_system,
        )
    ).parsed
