from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.inspection_motor import InspectionMotor
from ...models.update_inspection_status_tractian_request import (
    UpdateInspectionStatusTractianRequest,
)
from ...types import Response


def _get_kwargs(
    inspection_id: str,
    *,
    body: UpdateInspectionStatusTractianRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/inspections/{inspection_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, InspectionMotor]]:
    if response.status_code == 200:
        response_200 = InspectionMotor.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, InspectionMotor]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inspection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateInspectionStatusTractianRequest,
) -> Response[Union[Any, HTTPValidationError, InspectionMotor]]:
    """Update inspection status

     Updates the status of a specific inspection. The status can be set to 'open', 'onHold',
    'inProgress', or 'closed'.

    Args:
        inspection_id (str):
        body (UpdateInspectionStatusTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, InspectionMotor]]
    """

    kwargs = _get_kwargs(
        inspection_id=inspection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    inspection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateInspectionStatusTractianRequest,
) -> Optional[Union[Any, HTTPValidationError, InspectionMotor]]:
    """Update inspection status

     Updates the status of a specific inspection. The status can be set to 'open', 'onHold',
    'inProgress', or 'closed'.

    Args:
        inspection_id (str):
        body (UpdateInspectionStatusTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, InspectionMotor]
    """

    return sync_detailed(
        inspection_id=inspection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    inspection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateInspectionStatusTractianRequest,
) -> Response[Union[Any, HTTPValidationError, InspectionMotor]]:
    """Update inspection status

     Updates the status of a specific inspection. The status can be set to 'open', 'onHold',
    'inProgress', or 'closed'.

    Args:
        inspection_id (str):
        body (UpdateInspectionStatusTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, InspectionMotor]]
    """

    kwargs = _get_kwargs(
        inspection_id=inspection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    inspection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateInspectionStatusTractianRequest,
) -> Optional[Union[Any, HTTPValidationError, InspectionMotor]]:
    """Update inspection status

     Updates the status of a specific inspection. The status can be set to 'open', 'onHold',
    'inProgress', or 'closed'.

    Args:
        inspection_id (str):
        body (UpdateInspectionStatusTractianRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, InspectionMotor]
    """

    return (
        await asyncio_detailed(
            inspection_id=inspection_id,
            client=client,
            body=body,
        )
    ).parsed
