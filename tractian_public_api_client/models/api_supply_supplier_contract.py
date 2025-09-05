from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplySupplierContract")


@_attrs_define
class ApiSupplySupplierContract:
    id: str
    """ Unique identifier of the contract """
    company_id: str
    """ Unique identifier of the company the contract belongs to """
    created_at: Union[None, Unset, str] = UNSET
    """ The date and time when the contract was created """
    updated_at: Union[None, Unset, str] = UNSET
    """ The date and time when the contract was last updated """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who created the contract """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who last updated the contract """
    supplier_id: Union[None, Unset, str] = UNSET
    """ The supplier id associated with this contract """
    title: Union[None, Unset, str] = UNSET
    """ Title of the contract """
    is_in_effect: Union[None, Unset, bool] = UNSET
    """ Whether the contract is currently in effect """
    position: Union[None, Unset, int] = UNSET
    """ Position or order of the contract """
    attachment: Union[None, Unset, str] = UNSET
    """ Attachment associated with the contract """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        created_by_user_id: Union[None, Unset, str]
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        updated_by_user_id: Union[None, Unset, str]
        if isinstance(self.updated_by_user_id, Unset):
            updated_by_user_id = UNSET
        else:
            updated_by_user_id = self.updated_by_user_id

        supplier_id: Union[None, Unset, str]
        if isinstance(self.supplier_id, Unset):
            supplier_id = UNSET
        else:
            supplier_id = self.supplier_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        is_in_effect: Union[None, Unset, bool]
        if isinstance(self.is_in_effect, Unset):
            is_in_effect = UNSET
        else:
            is_in_effect = self.is_in_effect

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        attachment: Union[None, Unset, str]
        if isinstance(self.attachment, Unset):
            attachment = UNSET
        else:
            attachment = self.attachment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "companyId": company_id,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if supplier_id is not UNSET:
            field_dict["supplierId"] = supplier_id
        if title is not UNSET:
            field_dict["title"] = title
        if is_in_effect is not UNSET:
            field_dict["isInEffect"] = is_in_effect
        if position is not UNSET:
            field_dict["position"] = position
        if attachment is not UNSET:
            field_dict["attachment"] = attachment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("companyId")

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_created_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId", UNSET))

        def _parse_updated_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_user_id = _parse_updated_by_user_id(d.pop("updatedByUserId", UNSET))

        def _parse_supplier_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supplier_id = _parse_supplier_id(d.pop("supplierId", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_is_in_effect(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_in_effect = _parse_is_in_effect(d.pop("isInEffect", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_attachment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        attachment = _parse_attachment(d.pop("attachment", UNSET))

        api_supply_supplier_contract = cls(
            id=id,
            company_id=company_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            supplier_id=supplier_id,
            title=title,
            is_in_effect=is_in_effect,
            position=position,
            attachment=attachment,
        )

        api_supply_supplier_contract.additional_properties = d
        return api_supply_supplier_contract

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
