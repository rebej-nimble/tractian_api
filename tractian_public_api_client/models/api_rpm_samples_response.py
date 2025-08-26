from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiRpmSamplesResponse")


@_attrs_define
class ApiRpmSamplesResponse:
    """API response model for RPM samples that includes companyId for proper authorization."""

    company_id: str
    """ Company ID associated with the asset. """
    id: list[str]
    """ Sample ID (UUID). """
    rpm: list[Union[None, float]]
    """ RPM data. """
    sampled_at: list[str]
    """ Sample date in ISO 8601 format. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        id = self.id

        rpm = []
        for rpm_item_data in self.rpm:
            rpm_item: Union[None, float]
            rpm_item = rpm_item_data
            rpm.append(rpm_item)

        sampled_at = self.sampled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "id": id,
                "rpm": rpm,
                "sampledAt": sampled_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId")

        id = cast(list[str], d.pop("id"))

        rpm = []
        _rpm = d.pop("rpm")
        for rpm_item_data in _rpm:

            def _parse_rpm_item(data: object) -> Union[None, float]:
                if data is None:
                    return data
                return cast(Union[None, float], data)

            rpm_item = _parse_rpm_item(rpm_item_data)

            rpm.append(rpm_item)

        sampled_at = cast(list[str], d.pop("sampledAt"))

        api_rpm_samples_response = cls(
            company_id=company_id,
            id=id,
            rpm=rpm,
            sampled_at=sampled_at,
        )

        api_rpm_samples_response.additional_properties = d
        return api_rpm_samples_response

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
