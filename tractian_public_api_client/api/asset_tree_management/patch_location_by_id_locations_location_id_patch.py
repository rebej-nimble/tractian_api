from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_locations import ApiLocations
from ...models.api_locations_put_request import ApiLocationsPutRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    location_id: str,
    *,
    body: ApiLocationsPutRequest,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/locations/{location_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiLocations, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ApiLocations.from_dict(response.json())

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
) -> Response[Union[ApiLocations, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    location_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiLocationsPutRequest,
    authorization: str,
) -> Response[Union[ApiLocations, HTTPValidationError]]:
    """Update a location

     This endpoint updates a location.

    Args:
        location_id (str):
        authorization (str):
        body (ApiLocationsPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLocations, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    location_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiLocationsPutRequest,
    authorization: str,
) -> Optional[Union[ApiLocations, HTTPValidationError]]:
    """Update a location

     This endpoint updates a location.

    Args:
        location_id (str):
        authorization (str):
        body (ApiLocationsPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLocations, HTTPValidationError]
    """

    return sync_detailed(
        location_id=location_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    location_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiLocationsPutRequest,
    authorization: str,
) -> Response[Union[ApiLocations, HTTPValidationError]]:
    """Update a location

     This endpoint updates a location.

    Args:
        location_id (str):
        authorization (str):
        body (ApiLocationsPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLocations, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    location_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiLocationsPutRequest,
    authorization: str,
) -> Optional[Union[ApiLocations, HTTPValidationError]]:
    """Update a location

     This endpoint updates a location.

    Args:
        location_id (str):
        authorization (str):
        body (ApiLocationsPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLocations, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            location_id=location_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
