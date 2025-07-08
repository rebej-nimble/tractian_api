from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentifiedAssetFailures")


@_attrs_define
class IdentifiedAssetFailures:
    id: str
    name: Union[None, Unset, str] = UNSET
    asset_failure_effect_id: Union[None, Unset, str] = UNSET
    asset_failure_cause_id: Union[None, Unset, str] = UNSET
    asset_failure_action_id: Union[None, Unset, str] = UNSET
    asset_failure_id: Union[None, Unset, str] = UNSET
    asset_component_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        asset_failure_effect_id: Union[None, Unset, str]
        if isinstance(self.asset_failure_effect_id, Unset):
            asset_failure_effect_id = UNSET
        else:
            asset_failure_effect_id = self.asset_failure_effect_id

        asset_failure_cause_id: Union[None, Unset, str]
        if isinstance(self.asset_failure_cause_id, Unset):
            asset_failure_cause_id = UNSET
        else:
            asset_failure_cause_id = self.asset_failure_cause_id

        asset_failure_action_id: Union[None, Unset, str]
        if isinstance(self.asset_failure_action_id, Unset):
            asset_failure_action_id = UNSET
        else:
            asset_failure_action_id = self.asset_failure_action_id

        asset_failure_id: Union[None, Unset, str]
        if isinstance(self.asset_failure_id, Unset):
            asset_failure_id = UNSET
        else:
            asset_failure_id = self.asset_failure_id

        asset_component_id: Union[None, Unset, str]
        if isinstance(self.asset_component_id, Unset):
            asset_component_id = UNSET
        else:
            asset_component_id = self.asset_component_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if asset_failure_effect_id is not UNSET:
            field_dict["assetFailureEffectId"] = asset_failure_effect_id
        if asset_failure_cause_id is not UNSET:
            field_dict["assetFailureCauseId"] = asset_failure_cause_id
        if asset_failure_action_id is not UNSET:
            field_dict["assetFailureActionId"] = asset_failure_action_id
        if asset_failure_id is not UNSET:
            field_dict["assetFailureId"] = asset_failure_id
        if asset_component_id is not UNSET:
            field_dict["assetComponentId"] = asset_component_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_asset_failure_effect_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_failure_effect_id = _parse_asset_failure_effect_id(
            d.pop("assetFailureEffectId", UNSET)
        )

        def _parse_asset_failure_cause_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_failure_cause_id = _parse_asset_failure_cause_id(
            d.pop("assetFailureCauseId", UNSET)
        )

        def _parse_asset_failure_action_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_failure_action_id = _parse_asset_failure_action_id(
            d.pop("assetFailureActionId", UNSET)
        )

        def _parse_asset_failure_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_failure_id = _parse_asset_failure_id(d.pop("assetFailureId", UNSET))

        def _parse_asset_component_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_component_id = _parse_asset_component_id(d.pop("assetComponentId", UNSET))

        identified_asset_failures = cls(
            id=id,
            name=name,
            asset_failure_effect_id=asset_failure_effect_id,
            asset_failure_cause_id=asset_failure_cause_id,
            asset_failure_action_id=asset_failure_action_id,
            asset_failure_id=asset_failure_id,
            asset_component_id=asset_component_id,
        )

        identified_asset_failures.additional_properties = d
        return identified_asset_failures

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
