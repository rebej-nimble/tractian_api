from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.update_insight_status_tractian_request import (
    UpdateInsightStatusTractianRequest,
)
from ...types import Response


def _get_kwargs(
    insight_id: str,
    *,
    body: UpdateInsightStatusTractianRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/insights/{insight_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
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
    client: AuthenticatedClient,
    body: UpdateInsightStatusTractianRequest,
) -> Response[Union[Any, HTTPValidationError]]:
    """Update an insight status

     Updates the status of an existing insight with the provided status.

    Args:
        insight_id (str):
        body (UpdateInsightStatusTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        insight_id=insight_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    insight_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateInsightStatusTractianRequest,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Update an insight status

     Updates the status of an existing insight with the provided status.

    Args:
        insight_id (str):
        body (UpdateInsightStatusTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        insight_id=insight_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    insight_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateInsightStatusTractianRequest,
) -> Response[Union[Any, HTTPValidationError]]:
    """Update an insight status

     Updates the status of an existing insight with the provided status.

    Args:
        insight_id (str):
        body (UpdateInsightStatusTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        insight_id=insight_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    insight_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateInsightStatusTractianRequest,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Update an insight status

     Updates the status of an existing insight with the provided status.

    Args:
        insight_id (str):
        body (UpdateInsightStatusTractianRequest):

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
            body=body,
        )
    ).parsed
