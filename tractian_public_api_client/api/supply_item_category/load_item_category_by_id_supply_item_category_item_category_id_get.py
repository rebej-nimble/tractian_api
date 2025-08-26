from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_supply_item_category import ApiSupplyItemCategory
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    item_category_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/supply/item-category/{item_category_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiSupplyItemCategory, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ApiSupplyItemCategory.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiSupplyItemCategory, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_category_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ApiSupplyItemCategory, HTTPValidationError]]:
    """Load Item Category By Id

     Load item category by id.

    Args:
        item_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiSupplyItemCategory, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        item_category_id=item_category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_category_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ApiSupplyItemCategory, HTTPValidationError]]:
    """Load Item Category By Id

     Load item category by id.

    Args:
        item_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiSupplyItemCategory, HTTPValidationError]
    """

    return sync_detailed(
        item_category_id=item_category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    item_category_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ApiSupplyItemCategory, HTTPValidationError]]:
    """Load Item Category By Id

     Load item category by id.

    Args:
        item_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiSupplyItemCategory, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        item_category_id=item_category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_category_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ApiSupplyItemCategory, HTTPValidationError]]:
    """Load Item Category By Id

     Load item category by id.

    Args:
        item_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiSupplyItemCategory, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            item_category_id=item_category_id,
            client=client,
        )
    ).parsed
