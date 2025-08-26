from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.load_insights_info_by_id_insights_insight_id_get_language import (
    LoadInsightsInfoByIdInsightsInsightIdGetLanguage,
)
from ...models.load_insights_info_by_id_insights_insight_id_get_layout_type import (
    LoadInsightsInfoByIdInsightsInsightIdGetLayoutType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    insight_id: str,
    *,
    layout_type: Union[
        Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType
    ] = "web",
    language: Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage] = "pt",
    load_events: Union[Unset, bool] = False,
    include_values: Union[Unset, bool] = False,
    load_event_insight_ids: Union[Unset, bool] = False,
    x_company_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-company-id"] = x_company_id

    params: dict[str, Any] = {}

    json_layout_type: Union[Unset, str] = UNSET
    if not isinstance(layout_type, Unset):
        json_layout_type = layout_type

    params["layout_type"] = json_layout_type

    json_language: Union[Unset, str] = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    params["load_events"] = load_events

    params["include_values"] = include_values

    params["load_event_insight_ids"] = load_event_insight_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/insights/{insight_id}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    insight_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    layout_type: Union[
        Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType
    ] = "web",
    language: Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage] = "pt",
    load_events: Union[Unset, bool] = False,
    include_values: Union[Unset, bool] = False,
    load_event_insight_ids: Union[Unset, bool] = False,
    x_company_id: str,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get detailed insight information by ID

     Fetches detailed information about a specific insight by its ID. Returns comprehensive insight data
    including status, reference date, and associated metadata.

    Args:
        insight_id (str):
        layout_type (Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType]):  Default:
            'web'.
        language (Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage]):  Default: 'pt'.
        load_events (Union[Unset, bool]):  Default: False.
        include_values (Union[Unset, bool]):  Default: False.
        load_event_insight_ids (Union[Unset, bool]):  Default: False.
        x_company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        insight_id=insight_id,
        layout_type=layout_type,
        language=language,
        load_events=load_events,
        include_values=include_values,
        load_event_insight_ids=load_event_insight_ids,
        x_company_id=x_company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    insight_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    layout_type: Union[
        Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType
    ] = "web",
    language: Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage] = "pt",
    load_events: Union[Unset, bool] = False,
    include_values: Union[Unset, bool] = False,
    load_event_insight_ids: Union[Unset, bool] = False,
    x_company_id: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get detailed insight information by ID

     Fetches detailed information about a specific insight by its ID. Returns comprehensive insight data
    including status, reference date, and associated metadata.

    Args:
        insight_id (str):
        layout_type (Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType]):  Default:
            'web'.
        language (Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage]):  Default: 'pt'.
        load_events (Union[Unset, bool]):  Default: False.
        include_values (Union[Unset, bool]):  Default: False.
        load_event_insight_ids (Union[Unset, bool]):  Default: False.
        x_company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        insight_id=insight_id,
        client=client,
        layout_type=layout_type,
        language=language,
        load_events=load_events,
        include_values=include_values,
        load_event_insight_ids=load_event_insight_ids,
        x_company_id=x_company_id,
    ).parsed


async def asyncio_detailed(
    insight_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    layout_type: Union[
        Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType
    ] = "web",
    language: Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage] = "pt",
    load_events: Union[Unset, bool] = False,
    include_values: Union[Unset, bool] = False,
    load_event_insight_ids: Union[Unset, bool] = False,
    x_company_id: str,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get detailed insight information by ID

     Fetches detailed information about a specific insight by its ID. Returns comprehensive insight data
    including status, reference date, and associated metadata.

    Args:
        insight_id (str):
        layout_type (Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType]):  Default:
            'web'.
        language (Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage]):  Default: 'pt'.
        load_events (Union[Unset, bool]):  Default: False.
        include_values (Union[Unset, bool]):  Default: False.
        load_event_insight_ids (Union[Unset, bool]):  Default: False.
        x_company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        insight_id=insight_id,
        layout_type=layout_type,
        language=language,
        load_events=load_events,
        include_values=include_values,
        load_event_insight_ids=load_event_insight_ids,
        x_company_id=x_company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    insight_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    layout_type: Union[
        Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType
    ] = "web",
    language: Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage] = "pt",
    load_events: Union[Unset, bool] = False,
    include_values: Union[Unset, bool] = False,
    load_event_insight_ids: Union[Unset, bool] = False,
    x_company_id: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get detailed insight information by ID

     Fetches detailed information about a specific insight by its ID. Returns comprehensive insight data
    including status, reference date, and associated metadata.

    Args:
        insight_id (str):
        layout_type (Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLayoutType]):  Default:
            'web'.
        language (Union[Unset, LoadInsightsInfoByIdInsightsInsightIdGetLanguage]):  Default: 'pt'.
        load_events (Union[Unset, bool]):  Default: False.
        include_values (Union[Unset, bool]):  Default: False.
        load_event_insight_ids (Union[Unset, bool]):  Default: False.
        x_company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            insight_id=insight_id,
            client=client,
            layout_type=layout_type,
            language=language,
            load_events=load_events,
            include_values=include_values,
            load_event_insight_ids=load_event_insight_ids,
            x_company_id=x_company_id,
        )
    ).parsed
