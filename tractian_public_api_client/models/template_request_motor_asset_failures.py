from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateRequestMotorAssetFailures")


@_attrs_define
class TemplateRequestMotorAssetFailures:
    asset_failure_id: str
    asset_failure_effect_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_failure_id = self.asset_failure_id

        asset_failure_effect_id: Union[None, Unset, str]
        if isinstance(self.asset_failure_effect_id, Unset):
            asset_failure_effect_id = UNSET
        else:
            asset_failure_effect_id = self.asset_failure_effect_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetFailureId": asset_failure_id,
            }
        )
        if asset_failure_effect_id is not UNSET:
            field_dict["assetFailureEffectId"] = asset_failure_effect_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_failure_id = d.pop("assetFailureId")

        def _parse_asset_failure_effect_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_failure_effect_id = _parse_asset_failure_effect_id(
            d.pop("assetFailureEffectId", UNSET)
        )

        template_request_motor_asset_failures = cls(
            asset_failure_id=asset_failure_id,
            asset_failure_effect_id=asset_failure_effect_id,
        )

        template_request_motor_asset_failures.additional_properties = d
        return template_request_motor_asset_failures

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
