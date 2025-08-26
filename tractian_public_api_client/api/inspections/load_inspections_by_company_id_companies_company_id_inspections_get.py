from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_list_inspections_response import ApiListInspectionsResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    load_procedures: Union[Unset, bool] = False,
    load_insights_prescriptions: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created_at_start: Union[None, Unset, str]
    if isinstance(created_at_start, Unset):
        json_created_at_start = UNSET
    else:
        json_created_at_start = created_at_start
    params["createdAtStart"] = json_created_at_start

    params["createdAtEnd"] = created_at_end

    params["page"] = page

    params["limit"] = limit

    params["loadProcedures"] = load_procedures

    params["loadInsightsPrescriptions"] = load_insights_prescriptions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/inspections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, list["ApiListInspectionsResponse"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiListInspectionsResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[Union[Any, HTTPValidationError, list["ApiListInspectionsResponse"]]]:
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
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    load_procedures: Union[Unset, bool] = False,
    load_insights_prescriptions: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, list["ApiListInspectionsResponse"]]]:
    """List inspections by company ID

     Fetches a list of inspections associated with the specified company. If no inspections are found,
    returns an empty list with a 200 OK status code.

    Args:
        company_id (str):
        created_at_start (Union[None, Unset, str]): Start date for the inspection period in ISO
            8601 format
        created_at_end (Union[Unset, str]): End date for the inspection period in ISO 8601 format
        page (Union[Unset, int]): Page number for the inspection period Default: 1.
        limit (Union[Unset, int]): Limit for the inspection period Default: 10.
        load_procedures (Union[Unset, bool]): Whether to load procedures for the inspection
            Default: False.
        load_insights_prescriptions (Union[Unset, bool]): Whether to load insights prescriptions
            for the inspection Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, list['ApiListInspectionsResponse']]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        created_at_start=created_at_start,
        created_at_end=created_at_end,
        page=page,
        limit=limit,
        load_procedures=load_procedures,
        load_insights_prescriptions=load_insights_prescriptions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    load_procedures: Union[Unset, bool] = False,
    load_insights_prescriptions: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, list["ApiListInspectionsResponse"]]]:
    """List inspections by company ID

     Fetches a list of inspections associated with the specified company. If no inspections are found,
    returns an empty list with a 200 OK status code.

    Args:
        company_id (str):
        created_at_start (Union[None, Unset, str]): Start date for the inspection period in ISO
            8601 format
        created_at_end (Union[Unset, str]): End date for the inspection period in ISO 8601 format
        page (Union[Unset, int]): Page number for the inspection period Default: 1.
        limit (Union[Unset, int]): Limit for the inspection period Default: 10.
        load_procedures (Union[Unset, bool]): Whether to load procedures for the inspection
            Default: False.
        load_insights_prescriptions (Union[Unset, bool]): Whether to load insights prescriptions
            for the inspection Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, list['ApiListInspectionsResponse']]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        created_at_start=created_at_start,
        created_at_end=created_at_end,
        page=page,
        limit=limit,
        load_procedures=load_procedures,
        load_insights_prescriptions=load_insights_prescriptions,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    load_procedures: Union[Unset, bool] = False,
    load_insights_prescriptions: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, list["ApiListInspectionsResponse"]]]:
    """List inspections by company ID

     Fetches a list of inspections associated with the specified company. If no inspections are found,
    returns an empty list with a 200 OK status code.

    Args:
        company_id (str):
        created_at_start (Union[None, Unset, str]): Start date for the inspection period in ISO
            8601 format
        created_at_end (Union[Unset, str]): End date for the inspection period in ISO 8601 format
        page (Union[Unset, int]): Page number for the inspection period Default: 1.
        limit (Union[Unset, int]): Limit for the inspection period Default: 10.
        load_procedures (Union[Unset, bool]): Whether to load procedures for the inspection
            Default: False.
        load_insights_prescriptions (Union[Unset, bool]): Whether to load insights prescriptions
            for the inspection Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, list['ApiListInspectionsResponse']]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        created_at_start=created_at_start,
        created_at_end=created_at_end,
        page=page,
        limit=limit,
        load_procedures=load_procedures,
        load_insights_prescriptions=load_insights_prescriptions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    load_procedures: Union[Unset, bool] = False,
    load_insights_prescriptions: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, list["ApiListInspectionsResponse"]]]:
    """List inspections by company ID

     Fetches a list of inspections associated with the specified company. If no inspections are found,
    returns an empty list with a 200 OK status code.

    Args:
        company_id (str):
        created_at_start (Union[None, Unset, str]): Start date for the inspection period in ISO
            8601 format
        created_at_end (Union[Unset, str]): End date for the inspection period in ISO 8601 format
        page (Union[Unset, int]): Page number for the inspection period Default: 1.
        limit (Union[Unset, int]): Limit for the inspection period Default: 10.
        load_procedures (Union[Unset, bool]): Whether to load procedures for the inspection
            Default: False.
        load_insights_prescriptions (Union[Unset, bool]): Whether to load insights prescriptions
            for the inspection Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, list['ApiListInspectionsResponse']]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            page=page,
            limit=limit,
            load_procedures=load_procedures,
            load_insights_prescriptions=load_insights_prescriptions,
        )
    ).parsed
