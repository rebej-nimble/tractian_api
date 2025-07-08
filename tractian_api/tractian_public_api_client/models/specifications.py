from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_components_motor import AssetComponentsMotor


T = TypeVar("T", bound="Specifications")


@_attrs_define
class Specifications:
    filled_percentage: Union[None, Unset, float] = UNSET
    missing_essential_fields: Union[None, Unset, list[str]] = UNSET
    missing_non_essential_fields: Union[None, Unset, list[str]] = UNSET
    components: Union["AssetComponentsMotor", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_components_motor import AssetComponentsMotor

        filled_percentage: Union[None, Unset, float]
        if isinstance(self.filled_percentage, Unset):
            filled_percentage = UNSET
        else:
            filled_percentage = self.filled_percentage

        missing_essential_fields: Union[None, Unset, list[str]]
        if isinstance(self.missing_essential_fields, Unset):
            missing_essential_fields = UNSET
        elif isinstance(self.missing_essential_fields, list):
            missing_essential_fields = self.missing_essential_fields

        else:
            missing_essential_fields = self.missing_essential_fields

        missing_non_essential_fields: Union[None, Unset, list[str]]
        if isinstance(self.missing_non_essential_fields, Unset):
            missing_non_essential_fields = UNSET
        elif isinstance(self.missing_non_essential_fields, list):
            missing_non_essential_fields = self.missing_non_essential_fields

        else:
            missing_non_essential_fields = self.missing_non_essential_fields

        components: Union[None, Unset, dict[str, Any]]
        if isinstance(self.components, Unset):
            components = UNSET
        elif isinstance(self.components, AssetComponentsMotor):
            components = self.components.to_dict()
        else:
            components = self.components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filled_percentage is not UNSET:
            field_dict["filledPercentage"] = filled_percentage
        if missing_essential_fields is not UNSET:
            field_dict["missingEssentialFields"] = missing_essential_fields
        if missing_non_essential_fields is not UNSET:
            field_dict["missingNonEssentialFields"] = missing_non_essential_fields
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_components_motor import AssetComponentsMotor

        d = dict(src_dict)

        def _parse_filled_percentage(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        filled_percentage = _parse_filled_percentage(d.pop("filledPercentage", UNSET))

        def _parse_missing_essential_fields(
            data: object,
        ) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_essential_fields_type_0 = cast(list[str], data)

                return missing_essential_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        missing_essential_fields = _parse_missing_essential_fields(
            d.pop("missingEssentialFields", UNSET)
        )

        def _parse_missing_non_essential_fields(
            data: object,
        ) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_non_essential_fields_type_0 = cast(list[str], data)

                return missing_non_essential_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        missing_non_essential_fields = _parse_missing_non_essential_fields(
            d.pop("missingNonEssentialFields", UNSET)
        )

        def _parse_components(
            data: object,
        ) -> Union["AssetComponentsMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                components_type_0 = AssetComponentsMotor.from_dict(data)

                return components_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AssetComponentsMotor", None, Unset], data)

        components = _parse_components(d.pop("components", UNSET))

        specifications = cls(
            filled_percentage=filled_percentage,
            missing_essential_fields=missing_essential_fields,
            missing_non_essential_fields=missing_non_essential_fields,
            components=components,
        )

        specifications.additional_properties = d
        return specifications

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
