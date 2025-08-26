from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Supplier")


@_attrs_define
class Supplier:
    company_id: str
    """ Unique identifier of the company the supplier contact belongs to """
    name: str
    """ Name of the supplier contact """
    email: str
    """ Email of the supplier contact """
    supplier_id: str
    """ Unique identifier of the supplier the supplier contact belongs to """
    phone: str
    """ Phone number of the supplier contact """
    identifier_code: Union[None, Unset, str] = UNSET
    """ Identifier code for external system integration """
    role: Union[None, Unset, str] = UNSET
    """ Role of the supplier contact """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        name = self.name

        email = self.email

        supplier_id = self.supplier_id

        phone = self.phone

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "name": name,
                "email": email,
                "supplierId": supplier_id,
                "phone": phone,
            }
        )
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId")

        name = d.pop("name")

        email = d.pop("email")

        supplier_id = d.pop("supplierId")

        phone = d.pop("phone")

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))

        supplier = cls(
            company_id=company_id,
            name=name,
            email=email,
            supplier_id=supplier_id,
            phone=phone,
            identifier_code=identifier_code,
            role=role,
        )

        supplier.additional_properties = d
        return supplier

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
