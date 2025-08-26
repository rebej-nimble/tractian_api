from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_asset_motor import AddAssetMotor
from ...models.asset import Asset
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    asset_id: str,
    *,
    body: AddAssetMotor,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/assets/{asset_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Asset, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = Asset.from_dict(response.json())

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
) -> Response[Union[Any, Asset, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddAssetMotor,
) -> Response[Union[Any, Asset, HTTPValidationError]]:
    """Update an asset by ID

     This endpoint updates an asset by its unique identifier.

    Args:
        asset_id (str): Unique identifier for the asset on TracOS
        body (AddAssetMotor):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Asset, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddAssetMotor,
) -> Optional[Union[Any, Asset, HTTPValidationError]]:
    """Update an asset by ID

     This endpoint updates an asset by its unique identifier.

    Args:
        asset_id (str): Unique identifier for the asset on TracOS
        body (AddAssetMotor):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Asset, HTTPValidationError]
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddAssetMotor,
) -> Response[Union[Any, Asset, HTTPValidationError]]:
    """Update an asset by ID

     This endpoint updates an asset by its unique identifier.

    Args:
        asset_id (str): Unique identifier for the asset on TracOS
        body (AddAssetMotor):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Asset, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddAssetMotor,
) -> Optional[Union[Any, Asset, HTTPValidationError]]:
    """Update an asset by ID

     This endpoint updates an asset by its unique identifier.

    Args:
        asset_id (str): Unique identifier for the asset on TracOS
        body (AddAssetMotor):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Asset, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
