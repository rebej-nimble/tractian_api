from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.transfer_request import TransferRequest
from ...types import Response


def _get_kwargs(
    transfer_request_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/supply/transfer-request/{transfer_request_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, TransferRequest]]:
    if response.status_code == 200:
        response_200 = TransferRequest.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, TransferRequest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transfer_request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, HTTPValidationError, TransferRequest]]:
    """Load Transfer Request By Id

     Load transfer request by id.

    Args:
        transfer_request_id (str): Transfer request id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TransferRequest]]
    """

    kwargs = _get_kwargs(
        transfer_request_id=transfer_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transfer_request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, HTTPValidationError, TransferRequest]]:
    """Load Transfer Request By Id

     Load transfer request by id.

    Args:
        transfer_request_id (str): Transfer request id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TransferRequest]
    """

    return sync_detailed(
        transfer_request_id=transfer_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    transfer_request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, HTTPValidationError, TransferRequest]]:
    """Load Transfer Request By Id

     Load transfer request by id.

    Args:
        transfer_request_id (str): Transfer request id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TransferRequest]]
    """

    kwargs = _get_kwargs(
        transfer_request_id=transfer_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transfer_request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, HTTPValidationError, TransferRequest]]:
    """Load Transfer Request By Id

     Load transfer request by id.

    Args:
        transfer_request_id (str): Transfer request id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TransferRequest]
    """

    return (
        await asyncio_detailed(
            transfer_request_id=transfer_request_id,
            client=client,
        )
    ).parsed
