from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_cerberus import EventCerberus
from ...models.http_validation_error import HTTPValidationError
from ...models.update_events_tractian_request import UpdateEventsTractianRequest
from ...types import Response


def _get_kwargs(
    event_id: str,
    *,
    body: UpdateEventsTractianRequest,
    user_id: str,
    company_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["user-id"] = user_id

    headers["company-id"] = company_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/events/{event_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventCerberus, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = EventCerberus.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
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
) -> Response[Union[Any, EventCerberus, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEventsTractianRequest,
    user_id: str,
    company_id: str,
) -> Response[Union[Any, EventCerberus, HTTPValidationError]]:
    """Update an event status

     Updates the fix status of an existing event. The status can be set to either fixed or not fixed.

    Args:
        event_id (str):
        user_id (str):
        company_id (str):
        body (UpdateEventsTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventCerberus, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
        user_id=user_id,
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEventsTractianRequest,
    user_id: str,
    company_id: str,
) -> Optional[Union[Any, EventCerberus, HTTPValidationError]]:
    """Update an event status

     Updates the fix status of an existing event. The status can be set to either fixed or not fixed.

    Args:
        event_id (str):
        user_id (str):
        company_id (str):
        body (UpdateEventsTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventCerberus, HTTPValidationError]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        body=body,
        user_id=user_id,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEventsTractianRequest,
    user_id: str,
    company_id: str,
) -> Response[Union[Any, EventCerberus, HTTPValidationError]]:
    """Update an event status

     Updates the fix status of an existing event. The status can be set to either fixed or not fixed.

    Args:
        event_id (str):
        user_id (str):
        company_id (str):
        body (UpdateEventsTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventCerberus, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
        user_id=user_id,
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEventsTractianRequest,
    user_id: str,
    company_id: str,
) -> Optional[Union[Any, EventCerberus, HTTPValidationError]]:
    """Update an event status

     Updates the fix status of an existing event. The status can be set to either fixed or not fixed.

    Args:
        event_id (str):
        user_id (str):
        company_id (str):
        body (UpdateEventsTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventCerberus, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            body=body,
            user_id=user_id,
            company_id=company_id,
        )
    ).parsed
