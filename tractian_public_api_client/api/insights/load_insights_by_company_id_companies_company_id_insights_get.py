from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_api_list_insights_response import (
    PaginationApiListInsightsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    reference_date_start: Union[None, Unset, str] = UNSET,
    reference_date_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
    load_prescription: Union[Unset, bool] = False,
    load_description: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_reference_date_start: Union[None, Unset, str]
    if isinstance(reference_date_start, Unset):
        json_reference_date_start = UNSET
    else:
        json_reference_date_start = reference_date_start
    params["referenceDateStart"] = json_reference_date_start

    params["referenceDateEnd"] = reference_date_end

    params["page"] = page

    params["limit"] = limit

    params["deleted"] = deleted

    params["loadPrescription"] = load_prescription

    params["loadDescription"] = load_description

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/insights",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]]:
    if response.status_code == 200:
        response_200 = PaginationApiListInsightsResponse.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]]:
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
    reference_date_start: Union[None, Unset, str] = UNSET,
    reference_date_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
    load_prescription: Union[Unset, bool] = False,
    load_description: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]]:
    """List insights by company ID

     Fetches a list of insights overview associated with the specified company. The insights provide
    valuable information about asset performance and potential issues. If no insights are found, returns
    an empty list with a 200 OK status code.

    Args:
        company_id (str):
        reference_date_start (Union[None, Unset, str]): Start date for the inspection period in
            ISO 8601 format
        reference_date_end (Union[Unset, str]): End date for the inspection period in ISO 8601
            format
        page (Union[Unset, int]): Page number for the insights Default: 1.
        limit (Union[Unset, int]): Number of insights per page Default: 10.
        deleted (Union[Unset, bool]): Filter insights by deleted status Default: False.
        load_prescription (Union[Unset, bool]): Filter if insights will return procedure
            prescriptions Default: False.
        load_description (Union[Unset, bool]): Filter if insights will return description Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        reference_date_start=reference_date_start,
        reference_date_end=reference_date_end,
        page=page,
        limit=limit,
        deleted=deleted,
        load_prescription=load_prescription,
        load_description=load_description,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    reference_date_start: Union[None, Unset, str] = UNSET,
    reference_date_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
    load_prescription: Union[Unset, bool] = False,
    load_description: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]]:
    """List insights by company ID

     Fetches a list of insights overview associated with the specified company. The insights provide
    valuable information about asset performance and potential issues. If no insights are found, returns
    an empty list with a 200 OK status code.

    Args:
        company_id (str):
        reference_date_start (Union[None, Unset, str]): Start date for the inspection period in
            ISO 8601 format
        reference_date_end (Union[Unset, str]): End date for the inspection period in ISO 8601
            format
        page (Union[Unset, int]): Page number for the insights Default: 1.
        limit (Union[Unset, int]): Number of insights per page Default: 10.
        deleted (Union[Unset, bool]): Filter insights by deleted status Default: False.
        load_prescription (Union[Unset, bool]): Filter if insights will return procedure
            prescriptions Default: False.
        load_description (Union[Unset, bool]): Filter if insights will return description Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        reference_date_start=reference_date_start,
        reference_date_end=reference_date_end,
        page=page,
        limit=limit,
        deleted=deleted,
        load_prescription=load_prescription,
        load_description=load_description,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    reference_date_start: Union[None, Unset, str] = UNSET,
    reference_date_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
    load_prescription: Union[Unset, bool] = False,
    load_description: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]]:
    """List insights by company ID

     Fetches a list of insights overview associated with the specified company. The insights provide
    valuable information about asset performance and potential issues. If no insights are found, returns
    an empty list with a 200 OK status code.

    Args:
        company_id (str):
        reference_date_start (Union[None, Unset, str]): Start date for the inspection period in
            ISO 8601 format
        reference_date_end (Union[Unset, str]): End date for the inspection period in ISO 8601
            format
        page (Union[Unset, int]): Page number for the insights Default: 1.
        limit (Union[Unset, int]): Number of insights per page Default: 10.
        deleted (Union[Unset, bool]): Filter insights by deleted status Default: False.
        load_prescription (Union[Unset, bool]): Filter if insights will return procedure
            prescriptions Default: False.
        load_description (Union[Unset, bool]): Filter if insights will return description Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        reference_date_start=reference_date_start,
        reference_date_end=reference_date_end,
        page=page,
        limit=limit,
        deleted=deleted,
        load_prescription=load_prescription,
        load_description=load_description,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    reference_date_start: Union[None, Unset, str] = UNSET,
    reference_date_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
    load_prescription: Union[Unset, bool] = False,
    load_description: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]]:
    """List insights by company ID

     Fetches a list of insights overview associated with the specified company. The insights provide
    valuable information about asset performance and potential issues. If no insights are found, returns
    an empty list with a 200 OK status code.

    Args:
        company_id (str):
        reference_date_start (Union[None, Unset, str]): Start date for the inspection period in
            ISO 8601 format
        reference_date_end (Union[Unset, str]): End date for the inspection period in ISO 8601
            format
        page (Union[Unset, int]): Page number for the insights Default: 1.
        limit (Union[Unset, int]): Number of insights per page Default: 10.
        deleted (Union[Unset, bool]): Filter insights by deleted status Default: False.
        load_prescription (Union[Unset, bool]): Filter if insights will return procedure
            prescriptions Default: False.
        load_description (Union[Unset, bool]): Filter if insights will return description Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationApiListInsightsResponse]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            reference_date_start=reference_date_start,
            reference_date_end=reference_date_end,
            page=page,
            limit=limit,
            deleted=deleted,
            load_prescription=load_prescription,
            load_description=load_description,
        )
    ).parsed
