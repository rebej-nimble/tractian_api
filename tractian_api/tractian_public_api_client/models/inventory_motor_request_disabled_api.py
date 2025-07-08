from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryMotorRequestDisabledAPI")


@_attrs_define
class InventoryMotorRequestDisabledAPI:
    value: Union[Unset, bool] = False
    """ Indicates whether the inventory item is disabled. """

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        inventory_motor_request_disabled_api = cls(
            value=value,
        )

        return inventory_motor_request_disabled_api
