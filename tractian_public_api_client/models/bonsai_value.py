from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bonsai_child import BonsaiChild
    from ..models.bonsai_parent import BonsaiParent


T = TypeVar("T", bound="BonsaiValue")


@_attrs_define
class BonsaiValue:
    parents: Union[None, Unset, list["BonsaiParent"]] = UNSET
    children: Union[None, Unset, list["BonsaiChild"]] = UNSET
    name: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parents: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.parents, Unset):
            parents = UNSET
        elif isinstance(self.parents, list):
            parents = []
            for parents_type_0_item_data in self.parents:
                parents_type_0_item = parents_type_0_item_data.to_dict()
                parents.append(parents_type_0_item)

        else:
            parents = self.parents

        children: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)

        else:
            children = self.children

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parents is not UNSET:
            field_dict["parents"] = parents
        if children is not UNSET:
            field_dict["children"] = children
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bonsai_child import BonsaiChild
        from ..models.bonsai_parent import BonsaiParent

        d = dict(src_dict)

        def _parse_parents(data: object) -> Union[None, Unset, list["BonsaiParent"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parents_type_0 = []
                _parents_type_0 = data
                for parents_type_0_item_data in _parents_type_0:
                    parents_type_0_item = BonsaiParent.from_dict(
                        parents_type_0_item_data
                    )

                    parents_type_0.append(parents_type_0_item)

                return parents_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BonsaiParent"]], data)

        parents = _parse_parents(d.pop("parents", UNSET))

        def _parse_children(data: object) -> Union[None, Unset, list["BonsaiChild"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:
                    children_type_0_item = BonsaiChild.from_dict(
                        children_type_0_item_data
                    )

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BonsaiChild"]], data)

        children = _parse_children(d.pop("children", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        bonsai_value = cls(
            parents=parents,
            children=children,
            name=name,
            path=path,
            type_=type_,
        )

        bonsai_value.additional_properties = d
        return bonsai_value

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
