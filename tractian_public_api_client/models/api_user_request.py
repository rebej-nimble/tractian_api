from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_user_deleted import ApiUserDeleted


T = TypeVar("T", bound="ApiUserRequest")


@_attrs_define
class ApiUserRequest:
    name: str
    """ Full name of the user """
    email: str
    """ Email address of the user (must be unique) """
    company_id: str
    """ Unique identifier of the company the user belongs to """
    language: str
    """ User's preferred language """
    profile_id: str
    """ Profile/role identifier that determines user permissions and access levels """
    external_id: Union[None, Unset, str] = UNSET
    """ External system identifier for integration purposes """
    phone: Union[None, Unset, str] = UNSET
    """ User's phone number """
    hourly_rate: Union[None, Unset, str] = UNSET
    """ User's hourly rate for cost calculations and time tracking """
    deleted: Union[Unset, "ApiUserDeleted"] = UNSET
    job_role: Union[None, Unset, str] = UNSET
    """ User's job role or position title """
    projects: Union[None, Unset, list[int]] = UNSET
    """ List of project IDs the user is associated with """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        company_id = self.company_id

        language = self.language

        profile_id = self.profile_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        hourly_rate: Union[None, Unset, str]
        if isinstance(self.hourly_rate, Unset):
            hourly_rate = UNSET
        else:
            hourly_rate = self.hourly_rate

        deleted: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deleted, Unset):
            deleted = self.deleted.to_dict()

        job_role: Union[None, Unset, str]
        if isinstance(self.job_role, Unset):
            job_role = UNSET
        else:
            job_role = self.job_role

        projects: Union[None, Unset, list[int]]
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = self.projects

        else:
            projects = self.projects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
                "companyId": company_id,
                "language": language,
                "profileId": profile_id,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if hourly_rate is not UNSET:
            field_dict["hourlyRate"] = hourly_rate
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if job_role is not UNSET:
            field_dict["job_role"] = job_role
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_user_deleted import ApiUserDeleted

        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        company_id = d.pop("companyId")

        language = d.pop("language")

        profile_id = d.pop("profileId")

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_hourly_rate(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hourly_rate = _parse_hourly_rate(d.pop("hourlyRate", UNSET))

        _deleted = d.pop("deleted", UNSET)
        deleted: Union[Unset, ApiUserDeleted]
        if isinstance(_deleted, Unset):
            deleted = UNSET
        else:
            deleted = ApiUserDeleted.from_dict(_deleted)

        def _parse_job_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_role = _parse_job_role(d.pop("job_role", UNSET))

        def _parse_projects(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_type_0 = cast(list[int], data)

                return projects_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        projects = _parse_projects(d.pop("projects", UNSET))

        api_user_request = cls(
            name=name,
            email=email,
            company_id=company_id,
            language=language,
            profile_id=profile_id,
            external_id=external_id,
            phone=phone,
            hourly_rate=hourly_rate,
            deleted=deleted,
            job_role=job_role,
            projects=projects,
        )

        api_user_request.additional_properties = d
        return api_user_request

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
