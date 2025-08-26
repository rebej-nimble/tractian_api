from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.load_requests_by_company_id_companies_company_id_requests_get_filter_type_0 import (
    LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0,
)
from ...models.load_requests_by_company_id_companies_company_id_requests_get_load_custom_fields_type_0 import (
    LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0,
)
from ...models.pagination_requests_motor import PaginationRequestsMotor
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    load_custom_fields: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0,
        None,
        Unset,
    ] = UNSET,
    filter_: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None, Unset
    ] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_load_custom_fields: Union[None, Unset, str]
    if isinstance(load_custom_fields, Unset):
        json_load_custom_fields = UNSET
    elif isinstance(load_custom_fields, str):
        json_load_custom_fields = load_custom_fields
    else:
        json_load_custom_fields = load_custom_fields
    params["loadCustomFields"] = json_load_custom_fields

    json_filter_: Union[None, Unset, str]
    if isinstance(filter_, Unset):
        json_filter_ = UNSET
    elif isinstance(filter_, str):
        json_filter_ = filter_
    else:
        json_filter_ = filter_
    params["filter"] = json_filter_

    json_start_date: Union[None, Unset, str]
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: Union[None, Unset, str]
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PaginationRequestsMotor]]:
    if response.status_code == 200:
        response_200 = PaginationRequestsMotor.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, PaginationRequestsMotor]]:
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
    load_custom_fields: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0,
        None,
        Unset,
    ] = UNSET,
    filter_: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None, Unset
    ] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, PaginationRequestsMotor]]:
    """Retrieve Requests by Company ID

    Args:
        company_id (str): company_id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        load_custom_fields
            (Union[LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0, None,
            Unset]): Load custom fields
        filter_ (Union[LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None,
            Unset]): Filter
        start_date (Union[None, Unset, str]): Filter start date
        end_date (Union[None, Unset, str]): Filter end date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationRequestsMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        load_custom_fields=load_custom_fields,
        filter_=filter_,
        start_date=start_date,
        end_date=end_date,
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
    load_custom_fields: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0,
        None,
        Unset,
    ] = UNSET,
    filter_: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None, Unset
    ] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, PaginationRequestsMotor]]:
    """Retrieve Requests by Company ID

    Args:
        company_id (str): company_id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        load_custom_fields
            (Union[LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0, None,
            Unset]): Load custom fields
        filter_ (Union[LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None,
            Unset]): Filter
        start_date (Union[None, Unset, str]): Filter start date
        end_date (Union[None, Unset, str]): Filter end date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationRequestsMotor]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        limit=limit,
        load_custom_fields=load_custom_fields,
        filter_=filter_,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    load_custom_fields: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0,
        None,
        Unset,
    ] = UNSET,
    filter_: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None, Unset
    ] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, PaginationRequestsMotor]]:
    """Retrieve Requests by Company ID

    Args:
        company_id (str): company_id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        load_custom_fields
            (Union[LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0, None,
            Unset]): Load custom fields
        filter_ (Union[LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None,
            Unset]): Filter
        start_date (Union[None, Unset, str]): Filter start date
        end_date (Union[None, Unset, str]): Filter end date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationRequestsMotor]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        limit=limit,
        load_custom_fields=load_custom_fields,
        filter_=filter_,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    load_custom_fields: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0,
        None,
        Unset,
    ] = UNSET,
    filter_: Union[
        LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None, Unset
    ] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, PaginationRequestsMotor]]:
    """Retrieve Requests by Company ID

    Args:
        company_id (str): company_id
        page (Union[Unset, int]): Page number Default: 1.
        limit (Union[Unset, int]): Limit Default: 10.
        load_custom_fields
            (Union[LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0, None,
            Unset]): Load custom fields
        filter_ (Union[LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, None,
            Unset]): Filter
        start_date (Union[None, Unset, str]): Filter start date
        end_date (Union[None, Unset, str]): Filter end date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationRequestsMotor]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            limit=limit,
            load_custom_fields=load_custom_fields,
            filter_=filter_,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
