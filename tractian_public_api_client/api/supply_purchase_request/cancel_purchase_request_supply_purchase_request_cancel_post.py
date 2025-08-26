from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_supply_purchase_request_action import ApiSupplyPurchaseRequestAction
from ...models.api_supply_purchase_requisition_response import (
    ApiSupplyPurchaseRequisitionResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: ApiSupplyPurchaseRequestAction,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/supply/purchase-request/cancel",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ApiSupplyPurchaseRequisitionResponse.from_dict(response.json())

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
) -> Response[Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiSupplyPurchaseRequestAction,
    authorization: str,
) -> Response[Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    """Cancel Purchase Request

    Args:
        authorization (str):
        body (ApiSupplyPurchaseRequestAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiSupplyPurchaseRequestAction,
    authorization: str,
) -> Optional[Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    """Cancel Purchase Request

    Args:
        authorization (str):
        body (ApiSupplyPurchaseRequestAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiSupplyPurchaseRequestAction,
    authorization: str,
) -> Response[Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    """Cancel Purchase Request

    Args:
        authorization (str):
        body (ApiSupplyPurchaseRequestAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiSupplyPurchaseRequestAction,
    authorization: str,
) -> Optional[Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]]:
    """Cancel Purchase Request

    Args:
        authorization (str):
        body (ApiSupplyPurchaseRequestAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSupplyPurchaseRequisitionResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
