from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_supply_measurement_unit_put_request import (
    ApiSupplyMeasurementUnitPutRequest,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    measurement_unit_id: str,
    *,
    body: ApiSupplyMeasurementUnitPutRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/supply/measurement-unit/{measurement_unit_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HTTPValidationError]:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    measurement_unit_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiSupplyMeasurementUnitPutRequest,
) -> Response[HTTPValidationError]:
    """Put Supply Measurement Unit

     Update a supply measurement unit

    Args:
        measurement_unit_id (str):
        body (ApiSupplyMeasurementUnitPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        measurement_unit_id=measurement_unit_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    measurement_unit_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiSupplyMeasurementUnitPutRequest,
) -> Optional[HTTPValidationError]:
    """Put Supply Measurement Unit

     Update a supply measurement unit

    Args:
        measurement_unit_id (str):
        body (ApiSupplyMeasurementUnitPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        measurement_unit_id=measurement_unit_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    measurement_unit_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiSupplyMeasurementUnitPutRequest,
) -> Response[HTTPValidationError]:
    """Put Supply Measurement Unit

     Update a supply measurement unit

    Args:
        measurement_unit_id (str):
        body (ApiSupplyMeasurementUnitPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        measurement_unit_id=measurement_unit_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    measurement_unit_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiSupplyMeasurementUnitPutRequest,
) -> Optional[HTTPValidationError]:
    """Put Supply Measurement Unit

     Update a supply measurement unit

    Args:
        measurement_unit_id (str):
        body (ApiSupplyMeasurementUnitPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            measurement_unit_id=measurement_unit_id,
            client=client,
            body=body,
        )
    ).parsed
