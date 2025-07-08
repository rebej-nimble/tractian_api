from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhaseValues")


@_attrs_define
class PhaseValues:
    a: Union[Unset, list[float]] = UNSET
    """ List of values for phase A, each value represents a sample. """
    b: Union[Unset, list[float]] = UNSET
    """ List of values for phase B, each value represents a sample. """
    c: Union[Unset, list[float]] = UNSET
    """ List of values for phase C, each value represents a sample. """
    ab: Union[Unset, list[float]] = UNSET
    """ List of values for phase-phase AB, each value represents a sample. Only available for voltage. """
    bc: Union[Unset, list[float]] = UNSET
    """ List of values for phase-phase BC, each value represents a sample. Only available for voltage. """
    ac: Union[Unset, list[float]] = UNSET
    """ List of values for phase-phase AC, each value represents a sample. Only available for voltage. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a: Union[Unset, list[float]] = UNSET
        if not isinstance(self.a, Unset):
            a = self.a

        b: Union[Unset, list[float]] = UNSET
        if not isinstance(self.b, Unset):
            b = self.b

        c: Union[Unset, list[float]] = UNSET
        if not isinstance(self.c, Unset):
            c = self.c

        ab: Union[Unset, list[float]] = UNSET
        if not isinstance(self.ab, Unset):
            ab = self.ab

        bc: Union[Unset, list[float]] = UNSET
        if not isinstance(self.bc, Unset):
            bc = self.bc

        ac: Union[Unset, list[float]] = UNSET
        if not isinstance(self.ac, Unset):
            ac = self.ac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["a"] = a
        if b is not UNSET:
            field_dict["b"] = b
        if c is not UNSET:
            field_dict["c"] = c
        if ab is not UNSET:
            field_dict["ab"] = ab
        if bc is not UNSET:
            field_dict["bc"] = bc
        if ac is not UNSET:
            field_dict["ac"] = ac

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        a = cast(list[float], d.pop("a", UNSET))

        b = cast(list[float], d.pop("b", UNSET))

        c = cast(list[float], d.pop("c", UNSET))

        ab = cast(list[float], d.pop("ab", UNSET))

        bc = cast(list[float], d.pop("bc", UNSET))

        ac = cast(list[float], d.pop("ac", UNSET))

        phase_values = cls(
            a=a,
            b=b,
            c=c,
            ab=ab,
            bc=bc,
            ac=ac,
        )

        phase_values.additional_properties = d
        return phase_values

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
