from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_category_motor_response import ApiCategoryMotorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    category_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/workorders/categories/{category_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiCategoryMotorResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ApiCategoryMotorResponse.from_dict(response.json())

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
) -> Response[Union[Any, ApiCategoryMotorResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    category_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ApiCategoryMotorResponse, HTTPValidationError]]:
    """List workorder categories by category ID

     This endpoint retrieves a category by ID

    Args:
        category_id (str): Unique identifier for the category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiCategoryMotorResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    category_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ApiCategoryMotorResponse, HTTPValidationError]]:
    """List workorder categories by category ID

     This endpoint retrieves a category by ID

    Args:
        category_id (str): Unique identifier for the category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiCategoryMotorResponse, HTTPValidationError]
    """

    return sync_detailed(
        category_id=category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    category_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ApiCategoryMotorResponse, HTTPValidationError]]:
    """List workorder categories by category ID

     This endpoint retrieves a category by ID

    Args:
        category_id (str): Unique identifier for the category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiCategoryMotorResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    category_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ApiCategoryMotorResponse, HTTPValidationError]]:
    """List workorder categories by category ID

     This endpoint retrieves a category by ID

    Args:
        category_id (str): Unique identifier for the category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiCategoryMotorResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            category_id=category_id,
            client=client,
        )
    ).parsed
