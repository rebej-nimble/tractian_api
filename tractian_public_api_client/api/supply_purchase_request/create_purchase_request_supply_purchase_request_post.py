from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_supply_purchase_requisition_request import (
    ApiSupplyPurchaseRequisitionRequest,
)
from ...models.api_supply_purchase_requisition_response import (
    ApiSupplyPurchaseRequisitionResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: list["ApiSupplyPurchaseRequisitionRequest"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/supply/purchase-request",
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
) -> Optional[Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ApiSupplyPurchaseRequisitionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSupplyPurchaseRequisitionRequest"],
) -> Response[Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    """Create Purchase Request

     Create a purchase request

    Args:
        body (list['ApiSupplyPurchaseRequisitionRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]
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
    body: list["ApiSupplyPurchaseRequisitionRequest"],
) -> Optional[Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    """Create Purchase Request

     Create a purchase request

    Args:
        body (list['ApiSupplyPurchaseRequisitionRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSupplyPurchaseRequisitionRequest"],
) -> Response[Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    """Create Purchase Request

     Create a purchase request

    Args:
        body (list['ApiSupplyPurchaseRequisitionRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSupplyPurchaseRequisitionRequest"],
) -> Optional[Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    """Create Purchase Request

     Create a purchase request

    Args:
        body (list['ApiSupplyPurchaseRequisitionRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
