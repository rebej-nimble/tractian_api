from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_type import EventType
from ...models.http_validation_error import HTTPValidationError
from ...models.pagination_event_cerberus import PaginationEventCerberus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    start_date_start: Union[None, Unset, str] = UNSET,
    start_date_end: Union[None, Unset, str] = UNSET,
    end_date_start: Union[None, Unset, str] = UNSET,
    end_date_end: Union[None, Unset, str] = UNSET,
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[None, Unset, str] = UNSET,
    event_types: Union[None, Unset, list[EventType]] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date_start: Union[None, Unset, str]
    if isinstance(start_date_start, Unset):
        json_start_date_start = UNSET
    else:
        json_start_date_start = start_date_start
    params["startDateStart"] = json_start_date_start

    json_start_date_end: Union[None, Unset, str]
    if isinstance(start_date_end, Unset):
        json_start_date_end = UNSET
    else:
        json_start_date_end = start_date_end
    params["startDateEnd"] = json_start_date_end

    json_end_date_start: Union[None, Unset, str]
    if isinstance(end_date_start, Unset):
        json_end_date_start = UNSET
    else:
        json_end_date_start = end_date_start
    params["endDateStart"] = json_end_date_start

    json_end_date_end: Union[None, Unset, str]
    if isinstance(end_date_end, Unset):
        json_end_date_end = UNSET
    else:
        json_end_date_end = end_date_end
    params["endDateEnd"] = json_end_date_end

    json_created_at_start: Union[None, Unset, str]
    if isinstance(created_at_start, Unset):
        json_created_at_start = UNSET
    else:
        json_created_at_start = created_at_start
    params["createdAtStart"] = json_created_at_start

    json_created_at_end: Union[None, Unset, str]
    if isinstance(created_at_end, Unset):
        json_created_at_end = UNSET
    else:
        json_created_at_end = created_at_end
    params["createdAtEnd"] = json_created_at_end

    json_event_types: Union[None, Unset, list[str]]
    if isinstance(event_types, Unset):
        json_event_types = UNSET
    elif isinstance(event_types, list):
        json_event_types = []
        for event_types_type_0_item_data in event_types:
            event_types_type_0_item: str = event_types_type_0_item_data
            json_event_types.append(event_types_type_0_item)

    else:
        json_event_types = event_types
    params["eventTypes"] = json_event_types

    params["page"] = page

    params["limit"] = limit

    params["deleted"] = deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/companies/{company_id}/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PaginationEventCerberus]]:
    if response.status_code == 200:
        response_200 = PaginationEventCerberus.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, PaginationEventCerberus]]:
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
    start_date_start: Union[None, Unset, str] = UNSET,
    start_date_end: Union[None, Unset, str] = UNSET,
    end_date_start: Union[None, Unset, str] = UNSET,
    end_date_end: Union[None, Unset, str] = UNSET,
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[None, Unset, str] = UNSET,
    event_types: Union[None, Unset, list[EventType]] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, PaginationEventCerberus]]:
    """List events by company ID

     Fetches a list of events associated with the specified company. The events provide information about
    asset activities and incidents. If no events are found, returns an empty list with a 200 OK status
    code.

    Args:
        company_id (str):
        start_date_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        start_date_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        end_date_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        end_date_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        created_at_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        created_at_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        event_types (Union[None, Unset, list[EventType]]): List of event types to filter by
        page (Union[Unset, int]): Page number for the events Default: 1.
        limit (Union[Unset, int]): Number of events per page Default: 10.
        deleted (Union[Unset, bool]): Filter events by deleted status Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationEventCerberus]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        start_date_start=start_date_start,
        start_date_end=start_date_end,
        end_date_start=end_date_start,
        end_date_end=end_date_end,
        created_at_start=created_at_start,
        created_at_end=created_at_end,
        event_types=event_types,
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
    client: AuthenticatedClient,
    start_date_start: Union[None, Unset, str] = UNSET,
    start_date_end: Union[None, Unset, str] = UNSET,
    end_date_start: Union[None, Unset, str] = UNSET,
    end_date_end: Union[None, Unset, str] = UNSET,
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[None, Unset, str] = UNSET,
    event_types: Union[None, Unset, list[EventType]] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, PaginationEventCerberus]]:
    """List events by company ID

     Fetches a list of events associated with the specified company. The events provide information about
    asset activities and incidents. If no events are found, returns an empty list with a 200 OK status
    code.

    Args:
        company_id (str):
        start_date_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        start_date_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        end_date_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        end_date_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        created_at_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        created_at_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        event_types (Union[None, Unset, list[EventType]]): List of event types to filter by
        page (Union[Unset, int]): Page number for the events Default: 1.
        limit (Union[Unset, int]): Number of events per page Default: 10.
        deleted (Union[Unset, bool]): Filter events by deleted status Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationEventCerberus]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        start_date_start=start_date_start,
        start_date_end=start_date_end,
        end_date_start=end_date_start,
        end_date_end=end_date_end,
        created_at_start=created_at_start,
        created_at_end=created_at_end,
        event_types=event_types,
        page=page,
        limit=limit,
        deleted=deleted,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    start_date_start: Union[None, Unset, str] = UNSET,
    start_date_end: Union[None, Unset, str] = UNSET,
    end_date_start: Union[None, Unset, str] = UNSET,
    end_date_end: Union[None, Unset, str] = UNSET,
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[None, Unset, str] = UNSET,
    event_types: Union[None, Unset, list[EventType]] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, PaginationEventCerberus]]:
    """List events by company ID

     Fetches a list of events associated with the specified company. The events provide information about
    asset activities and incidents. If no events are found, returns an empty list with a 200 OK status
    code.

    Args:
        company_id (str):
        start_date_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        start_date_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        end_date_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        end_date_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        created_at_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        created_at_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        event_types (Union[None, Unset, list[EventType]]): List of event types to filter by
        page (Union[Unset, int]): Page number for the events Default: 1.
        limit (Union[Unset, int]): Number of events per page Default: 10.
        deleted (Union[Unset, bool]): Filter events by deleted status Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PaginationEventCerberus]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        start_date_start=start_date_start,
        start_date_end=start_date_end,
        end_date_start=end_date_start,
        end_date_end=end_date_end,
        created_at_start=created_at_start,
        created_at_end=created_at_end,
        event_types=event_types,
        page=page,
        limit=limit,
        deleted=deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    start_date_start: Union[None, Unset, str] = UNSET,
    start_date_end: Union[None, Unset, str] = UNSET,
    end_date_start: Union[None, Unset, str] = UNSET,
    end_date_end: Union[None, Unset, str] = UNSET,
    created_at_start: Union[None, Unset, str] = UNSET,
    created_at_end: Union[None, Unset, str] = UNSET,
    event_types: Union[None, Unset, list[EventType]] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    deleted: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, PaginationEventCerberus]]:
    """List events by company ID

     Fetches a list of events associated with the specified company. The events provide information about
    asset activities and incidents. If no events are found, returns an empty list with a 200 OK status
    code.

    Args:
        company_id (str):
        start_date_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        start_date_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        end_date_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        end_date_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        created_at_start (Union[None, Unset, str]): Start date for filtering events in ISO 8601
            format
        created_at_end (Union[None, Unset, str]): End date for filtering events in ISO 8601 format
        event_types (Union[None, Unset, list[EventType]]): List of event types to filter by
        page (Union[Unset, int]): Page number for the events Default: 1.
        limit (Union[Unset, int]): Number of events per page Default: 10.
        deleted (Union[Unset, bool]): Filter events by deleted status Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PaginationEventCerberus]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            start_date_start=start_date_start,
            start_date_end=start_date_end,
            end_date_start=end_date_start,
            end_date_end=end_date_end,
            created_at_start=created_at_start,
            created_at_end=created_at_end,
            event_types=event_types,
            page=page,
            limit=limit,
            deleted=deleted,
        )
    ).parsed
