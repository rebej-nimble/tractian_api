from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bonsai_value import BonsaiValue


T = TypeVar("T", bound="BonsaiAssetTree")


@_attrs_define
class BonsaiAssetTree:
    key: str
    company_id: str
    value: "BonsaiValue"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        company_id = self.company_id

        value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "companyId": company_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bonsai_value import BonsaiValue

        d = dict(src_dict)
        key = d.pop("key")

        company_id = d.pop("companyId")

        value = BonsaiValue.from_dict(d.pop("value"))

        bonsai_asset_tree = cls(
            key=key,
            company_id=company_id,
            value=value,
        )

        bonsai_asset_tree.additional_properties = d
        return bonsai_asset_tree

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
