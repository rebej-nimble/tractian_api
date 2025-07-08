from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.procedure_motor import ProcedureMotor


T = TypeVar("T", bound="InspectionMotor")


@_attrs_define
class InspectionMotor:
    company_id: str
    title: str
    status: str
    created_at: str
    id: str
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    asset_id: Union[None, Unset, str] = UNSET
    made_by: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    created_by_user_id: Union[None, Unset, str] = UNSET
    updated_by_user_id: Union[None, Unset, str] = UNSET
    number: Union[None, Unset, int] = UNSET
    procedures: Union[None, Unset, list["ProcedureMotor"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        title = self.title

        status = self.status

        created_at = self.created_at

        id = self.id

        assigned_user_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_user_ids, Unset):
            assigned_user_ids = UNSET
        elif isinstance(self.assigned_user_ids, list):
            assigned_user_ids = self.assigned_user_ids

        else:
            assigned_user_ids = self.assigned_user_ids

        assigned_team_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = UNSET
        elif isinstance(self.assigned_team_ids, list):
            assigned_team_ids = self.assigned_team_ids

        else:
            assigned_team_ids = self.assigned_team_ids

        asset_id: Union[None, Unset, str]
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        made_by: Union[None, Unset, str]
        if isinstance(self.made_by, Unset):
            made_by = UNSET
        else:
            made_by = self.made_by

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

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

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        procedures: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.procedures, Unset):
            procedures = UNSET
        elif isinstance(self.procedures, list):
            procedures = []
            for procedures_type_0_item_data in self.procedures:
                procedures_type_0_item = procedures_type_0_item_data.to_dict()
                procedures.append(procedures_type_0_item)

        else:
            procedures = self.procedures

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "title": title,
                "status": status,
                "createdAt": created_at,
                "id": id,
            }
        )
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if made_by is not UNSET:
            field_dict["madeBy"] = made_by
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if number is not UNSET:
            field_dict["number"] = number
        if procedures is not UNSET:
            field_dict["procedures"] = procedures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.procedure_motor import ProcedureMotor

        d = dict(src_dict)
        company_id = d.pop("companyId")

        title = d.pop("title")

        status = d.pop("status")

        created_at = d.pop("createdAt")

        id = d.pop("id")

        def _parse_assigned_user_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_user_ids_type_0 = cast(list[str], data)

                return assigned_user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_user_ids = _parse_assigned_user_ids(d.pop("assignedUserIds", UNSET))

        def _parse_assigned_team_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_team_ids_type_0 = cast(list[str], data)

                return assigned_team_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_team_ids = _parse_assigned_team_ids(d.pop("assignedTeamIds", UNSET))

        def _parse_asset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_id = _parse_asset_id(d.pop("assetId", UNSET))

        def _parse_made_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        made_by = _parse_made_by(d.pop("madeBy", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

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

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_procedures(
            data: object,
        ) -> Union[None, Unset, list["ProcedureMotor"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                procedures_type_0 = []
                _procedures_type_0 = data
                for procedures_type_0_item_data in _procedures_type_0:
                    procedures_type_0_item = ProcedureMotor.from_dict(
                        procedures_type_0_item_data
                    )

                    procedures_type_0.append(procedures_type_0_item)

                return procedures_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ProcedureMotor"]], data)

        procedures = _parse_procedures(d.pop("procedures", UNSET))

        inspection_motor = cls(
            company_id=company_id,
            title=title,
            status=status,
            created_at=created_at,
            id=id,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            asset_id=asset_id,
            made_by=made_by,
            parent_id=parent_id,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            number=number,
            procedures=procedures,
        )

        inspection_motor.additional_properties = d
        return inspection_motor

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
