from http import HTTPStatus
from typing import Any, Literal, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset import Asset
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    load_asset_custom_fields: Union[
        Literal["false"], Literal["true"], None, Unset
    ] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_load_asset_custom_fields: Union[Literal["false"], Literal["true"], None, Unset]
    if isinstance(load_asset_custom_fields, Unset):
        json_load_asset_custom_fields = UNSET
    else:
        json_load_asset_custom_fields = load_asset_custom_fields
    params["loadAssetCustomFields"] = json_load_asset_custom_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/assets/{asset_id}",
        "params": params,
    }

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
    load_asset_custom_fields: Union[
        Literal["false"], Literal["true"], None, Unset
    ] = UNSET,
) -> Response[Union[Any, Asset, HTTPValidationError]]:
    """Load an asset by ID

     This endpoint retrieves an asset by its unique identifier.

    Args:
        asset_id (str): Unique identifier for the asset on TracOS
        load_asset_custom_fields (Union[Literal['false'], Literal['true'], None, Unset]): If
            provided, controls whether to load custom fields for the asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Asset, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        load_asset_custom_fields=load_asset_custom_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    load_asset_custom_fields: Union[
        Literal["false"], Literal["true"], None, Unset
    ] = UNSET,
) -> Optional[Union[Any, Asset, HTTPValidationError]]:
    """Load an asset by ID

     This endpoint retrieves an asset by its unique identifier.

    Args:
        asset_id (str): Unique identifier for the asset on TracOS
        load_asset_custom_fields (Union[Literal['false'], Literal['true'], None, Unset]): If
            provided, controls whether to load custom fields for the asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Asset, HTTPValidationError]
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        load_asset_custom_fields=load_asset_custom_fields,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    load_asset_custom_fields: Union[
        Literal["false"], Literal["true"], None, Unset
    ] = UNSET,
) -> Response[Union[Any, Asset, HTTPValidationError]]:
    """Load an asset by ID

     This endpoint retrieves an asset by its unique identifier.

    Args:
        asset_id (str): Unique identifier for the asset on TracOS
        load_asset_custom_fields (Union[Literal['false'], Literal['true'], None, Unset]): If
            provided, controls whether to load custom fields for the asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Asset, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        load_asset_custom_fields=load_asset_custom_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    load_asset_custom_fields: Union[
        Literal["false"], Literal["true"], None, Unset
    ] = UNSET,
) -> Optional[Union[Any, Asset, HTTPValidationError]]:
    """Load an asset by ID

     This endpoint retrieves an asset by its unique identifier.

    Args:
        asset_id (str): Unique identifier for the asset on TracOS
        load_asset_custom_fields (Union[Literal['false'], Literal['true'], None, Unset]): If
            provided, controls whether to load custom fields for the asset.

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
            load_asset_custom_fields=load_asset_custom_fields,
        )
    ).parsed
