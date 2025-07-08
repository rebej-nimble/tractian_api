from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkOrdersElapsedIntervalsMotor")


@_attrs_define
class WorkOrdersElapsedIntervalsMotor:
    started_at: str
    status: str
    user_id: str
    ended_at: Union[None, Unset, str] = UNSET
    duration_in_seconds: Union[None, Unset, float] = UNSET
    on_hold_reason_id: Union[None, Unset, str] = UNSET
    additional_info: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        started_at = self.started_at

        status = self.status

        user_id = self.user_id

        ended_at: Union[None, Unset, str]
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = self.ended_at

        duration_in_seconds: Union[None, Unset, float]
        if isinstance(self.duration_in_seconds, Unset):
            duration_in_seconds = UNSET
        else:
            duration_in_seconds = self.duration_in_seconds

        on_hold_reason_id: Union[None, Unset, str]
        if isinstance(self.on_hold_reason_id, Unset):
            on_hold_reason_id = UNSET
        else:
            on_hold_reason_id = self.on_hold_reason_id

        additional_info: Union[None, Unset, str]
        if isinstance(self.additional_info, Unset):
            additional_info = UNSET
        else:
            additional_info = self.additional_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startedAt": started_at,
                "status": status,
                "userId": user_id,
            }
        )
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if duration_in_seconds is not UNSET:
            field_dict["durationInSeconds"] = duration_in_seconds
        if on_hold_reason_id is not UNSET:
            field_dict["onHoldReasonId"] = on_hold_reason_id
        if additional_info is not UNSET:
            field_dict["additionalInfo"] = additional_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        started_at = d.pop("startedAt")

        status = d.pop("status")

        user_id = d.pop("userId")

        def _parse_ended_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))

        def _parse_duration_in_seconds(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        duration_in_seconds = _parse_duration_in_seconds(
            d.pop("durationInSeconds", UNSET)
        )

        def _parse_on_hold_reason_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        on_hold_reason_id = _parse_on_hold_reason_id(d.pop("onHoldReasonId", UNSET))

        def _parse_additional_info(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        additional_info = _parse_additional_info(d.pop("additionalInfo", UNSET))

        work_orders_elapsed_intervals_motor = cls(
            started_at=started_at,
            status=status,
            user_id=user_id,
            ended_at=ended_at,
            duration_in_seconds=duration_in_seconds,
            on_hold_reason_id=on_hold_reason_id,
            additional_info=additional_info,
        )

        work_orders_elapsed_intervals_motor.additional_properties = d
        return work_orders_elapsed_intervals_motor

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
