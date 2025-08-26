from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_consumption_samples_without_tariff_station_response import (
    ApiConsumptionSamplesWithoutTariffStationResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    asset: str,
    *,
    start: str,
    end: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/assets/{asset}/energy/consumption",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]
]:
    if response.status_code == 200:
        response_200 = ApiConsumptionSamplesWithoutTariffStationResponse.from_dict(
            response.json()
        )

        return response_200
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
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
) -> Response[
    Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: str,
    end: str,
) -> Response[
    Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]
]:
    """Load Energy Consumption by Asset ID

     Fetches energy consumption data (Wh - Watt-hour) for a specified asset within a given date range.
    This endpoint provides energy consumption samples that meet specific criteria, such as whether the
    asset was powered on or if only specialist samples are required. Ensure that the asset ID is valid,
    and that the date range follows the ISO8601 format in UTC (e.g., `2023-05-01T03:00:00.000Z`).

    Args:
        asset (str): Unique asset identifier, e.g., '63ac6c36838ebf001da10e70'.
        start (str): Start date and time in ISO8601 format with UTC timezone. Example:
            `2023-05-01T03:00:00.000Z`.
        end (str): End date and time in ISO8601 format with UTC timezone. Example:
            `2023-05-01T04:00:00.000Z`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        asset=asset,
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: str,
    end: str,
) -> Optional[
    Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]
]:
    """Load Energy Consumption by Asset ID

     Fetches energy consumption data (Wh - Watt-hour) for a specified asset within a given date range.
    This endpoint provides energy consumption samples that meet specific criteria, such as whether the
    asset was powered on or if only specialist samples are required. Ensure that the asset ID is valid,
    and that the date range follows the ISO8601 format in UTC (e.g., `2023-05-01T03:00:00.000Z`).

    Args:
        asset (str): Unique asset identifier, e.g., '63ac6c36838ebf001da10e70'.
        start (str): Start date and time in ISO8601 format with UTC timezone. Example:
            `2023-05-01T03:00:00.000Z`.
        end (str): End date and time in ISO8601 format with UTC timezone. Example:
            `2023-05-01T04:00:00.000Z`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]
    """

    return sync_detailed(
        asset=asset,
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    asset: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: str,
    end: str,
) -> Response[
    Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]
]:
    """Load Energy Consumption by Asset ID

     Fetches energy consumption data (Wh - Watt-hour) for a specified asset within a given date range.
    This endpoint provides energy consumption samples that meet specific criteria, such as whether the
    asset was powered on or if only specialist samples are required. Ensure that the asset ID is valid,
    and that the date range follows the ISO8601 format in UTC (e.g., `2023-05-01T03:00:00.000Z`).

    Args:
        asset (str): Unique asset identifier, e.g., '63ac6c36838ebf001da10e70'.
        start (str): Start date and time in ISO8601 format with UTC timezone. Example:
            `2023-05-01T03:00:00.000Z`.
        end (str): End date and time in ISO8601 format with UTC timezone. Example:
            `2023-05-01T04:00:00.000Z`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        asset=asset,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: str,
    end: str,
) -> Optional[
    Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]
]:
    """Load Energy Consumption by Asset ID

     Fetches energy consumption data (Wh - Watt-hour) for a specified asset within a given date range.
    This endpoint provides energy consumption samples that meet specific criteria, such as whether the
    asset was powered on or if only specialist samples are required. Ensure that the asset ID is valid,
    and that the date range follows the ISO8601 format in UTC (e.g., `2023-05-01T03:00:00.000Z`).

    Args:
        asset (str): Unique asset identifier, e.g., '63ac6c36838ebf001da10e70'.
        start (str): Start date and time in ISO8601 format with UTC timezone. Example:
            `2023-05-01T03:00:00.000Z`.
        end (str): End date and time in ISO8601 format with UTC timezone. Example:
            `2023-05-01T04:00:00.000Z`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiConsumptionSamplesWithoutTariffStationResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            asset=asset,
            client=client,
            start=start,
            end=end,
        )
    ).parsed
