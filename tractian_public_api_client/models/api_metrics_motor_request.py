from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.offline_metric import OfflineMetric, check_offline_metric
from ..models.online_metric import OnlineMetric, check_online_metric
from ..models.sensor_metric import SensorMetric, check_sensor_metric
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frequency_model_request import FrequencyModelRequest


T = TypeVar("T", bound="ApiMetricsMotorRequest")


@_attrs_define
class ApiMetricsMotorRequest:
    name: str
    """ Name of the metric """
    company_id: str
    """ ID of the company this metric belongs to """
    measurement_unit: Union[OfflineMetric, OnlineMetric, SensorMetric]
    """ Unit of measurement for the metric. OnlineMetric for real-time measurements, OfflineMetric for manual
    measurements, SensorMetric for sensor-based measurements """
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    """ List of user IDs responsible for this metric """
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    """ List of team IDs responsible for this metric """
    frequency: Union["FrequencyModelRequest", None, Unset] = UNSET
    """ Frequency configuration for how often this metric should be measured """
    location_id: Union[None, Unset, str] = UNSET
    """ ID of the location where this metric applies """
    default: Union[Unset, bool] = False
    """ Whether this is a default metric for the company """
    number: Union[None, Unset, int] = UNSET
    """ Numeric identifier or order number for the metric """
    is_cumulative: Union[Unset, bool] = False
    """ Whether the metric values are cumulative (each reading adds to the total) """
    asset_id: Union[None, Unset, str] = UNSET
    """ ID of the asset this metric is associated with """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.frequency_model_request import FrequencyModelRequest

        name = self.name

        company_id = self.company_id

        measurement_unit: str
        if isinstance(self.measurement_unit, str):
            measurement_unit = self.measurement_unit
        elif isinstance(self.measurement_unit, str):
            measurement_unit = self.measurement_unit
        else:
            measurement_unit = self.measurement_unit

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

        frequency: Union[None, Unset, dict[str, Any]]
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        elif isinstance(self.frequency, FrequencyModelRequest):
            frequency = self.frequency.to_dict()
        else:
            frequency = self.frequency

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        default = self.default

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        is_cumulative = self.is_cumulative

        asset_id: Union[None, Unset, str]
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "companyId": company_id,
                "measurementUnit": measurement_unit,
            }
        )
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if default is not UNSET:
            field_dict["default"] = default
        if number is not UNSET:
            field_dict["number"] = number
        if is_cumulative is not UNSET:
            field_dict["isCumulative"] = is_cumulative
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frequency_model_request import FrequencyModelRequest

        d = dict(src_dict)
        name = d.pop("name")

        company_id = d.pop("companyId")

        def _parse_measurement_unit(
            data: object,
        ) -> Union[OfflineMetric, OnlineMetric, SensorMetric]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                measurement_unit_type_0 = check_online_metric(data)

                return measurement_unit_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                measurement_unit_type_1 = check_offline_metric(data)

                return measurement_unit_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            measurement_unit_type_2 = check_sensor_metric(data)

            return measurement_unit_type_2

        measurement_unit = _parse_measurement_unit(d.pop("measurementUnit"))

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

        def _parse_frequency(
            data: object,
        ) -> Union["FrequencyModelRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                frequency_type_0 = FrequencyModelRequest.from_dict(data)

                return frequency_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FrequencyModelRequest", None, Unset], data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        default = d.pop("default", UNSET)

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

        is_cumulative = d.pop("isCumulative", UNSET)

        def _parse_asset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_id = _parse_asset_id(d.pop("assetId", UNSET))

        api_metrics_motor_request = cls(
            name=name,
            company_id=company_id,
            measurement_unit=measurement_unit,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            frequency=frequency,
            location_id=location_id,
            default=default,
            number=number,
            is_cumulative=is_cumulative,
            asset_id=asset_id,
        )

        api_metrics_motor_request.additional_properties = d
        return api_metrics_motor_request

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
