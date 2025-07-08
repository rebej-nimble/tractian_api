from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequestsTemplateIdentifiedAssetFailures")


@_attrs_define
class RequestsTemplateIdentifiedAssetFailures:
    asset_failure_id: str
    asset_failure_effect_id: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_failure_id = self.asset_failure_id

        asset_failure_effect_id: Union[None, str]
        asset_failure_effect_id = self.asset_failure_effect_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetFailureId": asset_failure_id,
                "assetFailureEffectId": asset_failure_effect_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_failure_id = d.pop("assetFailureId")

        def _parse_asset_failure_effect_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        asset_failure_effect_id = _parse_asset_failure_effect_id(
            d.pop("assetFailureEffectId")
        )

        requests_template_identified_asset_failures = cls(
            asset_failure_id=asset_failure_id,
            asset_failure_effect_id=asset_failure_effect_id,
        )

        requests_template_identified_asset_failures.additional_properties = d
        return requests_template_identified_asset_failures

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
