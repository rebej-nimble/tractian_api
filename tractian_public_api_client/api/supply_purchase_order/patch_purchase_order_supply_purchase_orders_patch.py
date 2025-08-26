from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_supply_purchase_order import ApiSupplyPurchaseOrder
from ...models.api_supply_purchase_order_request import ApiSupplyPurchaseOrderRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: list["ApiSupplyPurchaseOrderRequest"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/supply/purchase-orders",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiSupplyPurchaseOrder, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ApiSupplyPurchaseOrder.from_dict(response.json())

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
) -> Response[Union[ApiSupplyPurchaseOrder, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSupplyPurchaseOrderRequest"],
) -> Response[Union[ApiSupplyPurchaseOrder, HTTPValidationError]]:
    """Patch Purchase Order

     Update a purchase order

    Args:
        body (list['ApiSupplyPurchaseOrderRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSupplyPurchaseOrder, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSupplyPurchaseOrderRequest"],
) -> Optional[Union[ApiSupplyPurchaseOrder, HTTPValidationError]]:
    """Patch Purchase Order

     Update a purchase order

    Args:
        body (list['ApiSupplyPurchaseOrderRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSupplyPurchaseOrder, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSupplyPurchaseOrderRequest"],
) -> Response[Union[ApiSupplyPurchaseOrder, HTTPValidationError]]:
    """Patch Purchase Order

     Update a purchase order

    Args:
        body (list['ApiSupplyPurchaseOrderRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSupplyPurchaseOrder, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSupplyPurchaseOrderRequest"],
) -> Optional[Union[ApiSupplyPurchaseOrder, HTTPValidationError]]:
    """Patch Purchase Order

     Update a purchase order

    Args:
        body (list['ApiSupplyPurchaseOrderRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSupplyPurchaseOrder, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
