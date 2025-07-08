from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_image_motor import AssetImageMotor


T = TypeVar("T", bound="AssetUserMotor")


@_attrs_define
class AssetUserMotor:
    id: str
    name: str
    email: str
    company_id: str
    image: Union["AssetImageMotor", None, Unset] = UNSET
    number: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_image_motor import AssetImageMotor

        id = self.id

        name = self.name

        email = self.email

        company_id = self.company_id

        image: Union[None, Unset, dict[str, Any]]
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, AssetImageMotor):
            image = self.image.to_dict()
        else:
            image = self.image

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "email": email,
                "companyId": company_id,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_image_motor import AssetImageMotor

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        email = d.pop("email")

        company_id = d.pop("companyId")

        def _parse_image(data: object) -> Union["AssetImageMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = AssetImageMotor.from_dict(data)

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AssetImageMotor", None, Unset], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

        asset_user_motor = cls(
            id=id,
            name=name,
            email=email,
            company_id=company_id,
            image=image,
            number=number,
        )

        asset_user_motor.additional_properties = d
        return asset_user_motor

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
