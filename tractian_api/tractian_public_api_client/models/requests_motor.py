from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feedback_requests_motor import FeedbackRequestsMotor
    from ..models.generated_workorder import GeneratedWorkorder
    from ..models.parent_info_request_motor import ParentInfoRequestMotor
    from ..models.template_request_motor import TemplateRequestMotor


T = TypeVar("T", bound="RequestsMotor")


@_attrs_define
class RequestsMotor:
    template: "TemplateRequestMotor"
    created_at: str
    created_by_user_id: str
    company_id: str
    target: str
    id: str
    status: str
    number: int
    target_id: Union[None, Unset, str] = UNSET
    made_by: Union[None, Unset, str] = UNSET
    parent_info: Union["ParentInfoRequestMotor", None, Unset] = UNSET
    feedback: Union["FeedbackRequestsMotor", None, Unset] = UNSET
    work_order: Union["GeneratedWorkorder", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.feedback_requests_motor import FeedbackRequestsMotor
        from ..models.generated_workorder import GeneratedWorkorder
        from ..models.parent_info_request_motor import ParentInfoRequestMotor

        template = self.template.to_dict()

        created_at = self.created_at

        created_by_user_id = self.created_by_user_id

        company_id = self.company_id

        target = self.target

        id = self.id

        status = self.status

        number = self.number

        target_id: Union[None, Unset, str]
        if isinstance(self.target_id, Unset):
            target_id = UNSET
        else:
            target_id = self.target_id

        made_by: Union[None, Unset, str]
        if isinstance(self.made_by, Unset):
            made_by = UNSET
        else:
            made_by = self.made_by

        parent_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent_info, Unset):
            parent_info = UNSET
        elif isinstance(self.parent_info, ParentInfoRequestMotor):
            parent_info = self.parent_info.to_dict()
        else:
            parent_info = self.parent_info

        feedback: Union[None, Unset, dict[str, Any]]
        if isinstance(self.feedback, Unset):
            feedback = UNSET
        elif isinstance(self.feedback, FeedbackRequestsMotor):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

        work_order: Union[None, Unset, dict[str, Any]]
        if isinstance(self.work_order, Unset):
            work_order = UNSET
        elif isinstance(self.work_order, GeneratedWorkorder):
            work_order = self.work_order.to_dict()
        else:
            work_order = self.work_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template": template,
                "createdAt": created_at,
                "createdByUserId": created_by_user_id,
                "companyId": company_id,
                "target": target,
                "id": id,
                "status": status,
                "number": number,
            }
        )
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if made_by is not UNSET:
            field_dict["madeBy"] = made_by
        if parent_info is not UNSET:
            field_dict["parentInfo"] = parent_info
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if work_order is not UNSET:
            field_dict["workOrder"] = work_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_requests_motor import FeedbackRequestsMotor
        from ..models.generated_workorder import GeneratedWorkorder
        from ..models.parent_info_request_motor import ParentInfoRequestMotor
        from ..models.template_request_motor import TemplateRequestMotor

        d = dict(src_dict)
        template = TemplateRequestMotor.from_dict(d.pop("template"))

        created_at = d.pop("createdAt")

        created_by_user_id = d.pop("createdByUserId")

        company_id = d.pop("companyId")

        target = d.pop("target")

        id = d.pop("id")

        status = d.pop("status")

        number = d.pop("number")

        def _parse_target_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        target_id = _parse_target_id(d.pop("targetId", UNSET))

        def _parse_made_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        made_by = _parse_made_by(d.pop("madeBy", UNSET))

        def _parse_parent_info(
            data: object,
        ) -> Union["ParentInfoRequestMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_info_type_0 = ParentInfoRequestMotor.from_dict(data)

                return parent_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ParentInfoRequestMotor", None, Unset], data)

        parent_info = _parse_parent_info(d.pop("parentInfo", UNSET))

        def _parse_feedback(
            data: object,
        ) -> Union["FeedbackRequestsMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_0 = FeedbackRequestsMotor.from_dict(data)

                return feedback_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FeedbackRequestsMotor", None, Unset], data)

        feedback = _parse_feedback(d.pop("feedback", UNSET))

        def _parse_work_order(data: object) -> Union["GeneratedWorkorder", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                work_order_type_0 = GeneratedWorkorder.from_dict(data)

                return work_order_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GeneratedWorkorder", None, Unset], data)

        work_order = _parse_work_order(d.pop("workOrder", UNSET))

        requests_motor = cls(
            template=template,
            created_at=created_at,
            created_by_user_id=created_by_user_id,
            company_id=company_id,
            target=target,
            id=id,
            status=status,
            number=number,
            target_id=target_id,
            made_by=made_by,
            parent_info=parent_info,
            feedback=feedback,
            work_order=work_order,
        )

        requests_motor.additional_properties = d
        return requests_motor

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
