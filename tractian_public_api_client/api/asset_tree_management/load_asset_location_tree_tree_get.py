from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bonsai_asset_tree import BonsaiAssetTree
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    nodes: str,
    include_deleted: Union[Unset, bool] = True,
    include_disabled: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["nodes"] = nodes

    params["include_deleted"] = include_deleted

    params["include_disabled"] = include_disabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tree",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, list["BonsaiAssetTree"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BonsaiAssetTree.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, HTTPValidationError, list["BonsaiAssetTree"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    nodes: str,
    include_deleted: Union[Unset, bool] = True,
    include_disabled: Union[Unset, bool] = True,
) -> Response[Union[Any, HTTPValidationError, list["BonsaiAssetTree"]]]:
    """Retrieve Asset/Location Hierarchical Tree

     Fetches a hierarchical structure representing assets and locations based on a unique identifier for
    each node. The resulting tree includes parent and child relationships, enabling a visual or logical
    representation of the nested structure.

    Args:
        nodes (str): Unique identifier of location or asset. Example:
            nodes=`64caef2ab5e5fcd2f01d7e8c,64caef2bb5e5fcd2f01d7e8d`.
        include_deleted (Union[Unset, bool]): Flag to include or not deleted asset/locations.
            False to exclude deleted assets/locations. True to include deleted assets/locations.
            `If all the provided node ID is deleted and this filter is false, the response will be an
            empty list.` Default: True.
        include_disabled (Union[Unset, bool]): Flag to include or not disabled asset/locations.
            False to exclude disabled assets/locations. True to include disabled assets/locations.
            `If all the provided node IDs is disabled and this filter is false, the response will be
            an empty list.` Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, list['BonsaiAssetTree']]]
    """

    kwargs = _get_kwargs(
        nodes=nodes,
        include_deleted=include_deleted,
        include_disabled=include_disabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    nodes: str,
    include_deleted: Union[Unset, bool] = True,
    include_disabled: Union[Unset, bool] = True,
) -> Optional[Union[Any, HTTPValidationError, list["BonsaiAssetTree"]]]:
    """Retrieve Asset/Location Hierarchical Tree

     Fetches a hierarchical structure representing assets and locations based on a unique identifier for
    each node. The resulting tree includes parent and child relationships, enabling a visual or logical
    representation of the nested structure.

    Args:
        nodes (str): Unique identifier of location or asset. Example:
            nodes=`64caef2ab5e5fcd2f01d7e8c,64caef2bb5e5fcd2f01d7e8d`.
        include_deleted (Union[Unset, bool]): Flag to include or not deleted asset/locations.
            False to exclude deleted assets/locations. True to include deleted assets/locations.
            `If all the provided node ID is deleted and this filter is false, the response will be an
            empty list.` Default: True.
        include_disabled (Union[Unset, bool]): Flag to include or not disabled asset/locations.
            False to exclude disabled assets/locations. True to include disabled assets/locations.
            `If all the provided node IDs is disabled and this filter is false, the response will be
            an empty list.` Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, list['BonsaiAssetTree']]
    """

    return sync_detailed(
        client=client,
        nodes=nodes,
        include_deleted=include_deleted,
        include_disabled=include_disabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    nodes: str,
    include_deleted: Union[Unset, bool] = True,
    include_disabled: Union[Unset, bool] = True,
) -> Response[Union[Any, HTTPValidationError, list["BonsaiAssetTree"]]]:
    """Retrieve Asset/Location Hierarchical Tree

     Fetches a hierarchical structure representing assets and locations based on a unique identifier for
    each node. The resulting tree includes parent and child relationships, enabling a visual or logical
    representation of the nested structure.

    Args:
        nodes (str): Unique identifier of location or asset. Example:
            nodes=`64caef2ab5e5fcd2f01d7e8c,64caef2bb5e5fcd2f01d7e8d`.
        include_deleted (Union[Unset, bool]): Flag to include or not deleted asset/locations.
            False to exclude deleted assets/locations. True to include deleted assets/locations.
            `If all the provided node ID is deleted and this filter is false, the response will be an
            empty list.` Default: True.
        include_disabled (Union[Unset, bool]): Flag to include or not disabled asset/locations.
            False to exclude disabled assets/locations. True to include disabled assets/locations.
            `If all the provided node IDs is disabled and this filter is false, the response will be
            an empty list.` Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, list['BonsaiAssetTree']]]
    """

    kwargs = _get_kwargs(
        nodes=nodes,
        include_deleted=include_deleted,
        include_disabled=include_disabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    nodes: str,
    include_deleted: Union[Unset, bool] = True,
    include_disabled: Union[Unset, bool] = True,
) -> Optional[Union[Any, HTTPValidationError, list["BonsaiAssetTree"]]]:
    """Retrieve Asset/Location Hierarchical Tree

     Fetches a hierarchical structure representing assets and locations based on a unique identifier for
    each node. The resulting tree includes parent and child relationships, enabling a visual or logical
    representation of the nested structure.

    Args:
        nodes (str): Unique identifier of location or asset. Example:
            nodes=`64caef2ab5e5fcd2f01d7e8c,64caef2bb5e5fcd2f01d7e8d`.
        include_deleted (Union[Unset, bool]): Flag to include or not deleted asset/locations.
            False to exclude deleted assets/locations. True to include deleted assets/locations.
            `If all the provided node ID is deleted and this filter is false, the response will be an
            empty list.` Default: True.
        include_disabled (Union[Unset, bool]): Flag to include or not disabled asset/locations.
            False to exclude disabled assets/locations. True to include disabled assets/locations.
            `If all the provided node IDs is disabled and this filter is false, the response will be
            an empty list.` Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, list['BonsaiAssetTree']]
    """

    return (
        await asyncio_detailed(
            client=client,
            nodes=nodes,
            include_deleted=include_deleted,
            include_disabled=include_disabled,
        )
    ).parsed
