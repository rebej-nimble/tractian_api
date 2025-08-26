from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.axis_data import AxisData


T = TypeVar("T", bound="WaveData")


@_attrs_define
class WaveData:
    """Wave data measurements for vibration analysis."""

    crest_factor: "AxisData"
    """ Axis data for vibration measurements (X, Y, Z coordinates). """
    crest_factor_db: "AxisData"
    """ Axis data for vibration measurements (X, Y, Z coordinates). """
    peak: "AxisData"
    """ Axis data for vibration measurements (X, Y, Z coordinates). """
    peak_to_peak: "AxisData"
    """ Axis data for vibration measurements (X, Y, Z coordinates). """
    rms: "AxisData"
    """ Axis data for vibration measurements (X, Y, Z coordinates). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crest_factor = self.crest_factor.to_dict()

        crest_factor_db = self.crest_factor_db.to_dict()

        peak = self.peak.to_dict()

        peak_to_peak = self.peak_to_peak.to_dict()

        rms = self.rms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crestFactor": crest_factor,
                "crestFactorDb": crest_factor_db,
                "peak": peak,
                "peakToPeak": peak_to_peak,
                "rms": rms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.axis_data import AxisData

        d = dict(src_dict)
        crest_factor = AxisData.from_dict(d.pop("crestFactor"))

        crest_factor_db = AxisData.from_dict(d.pop("crestFactorDb"))

        peak = AxisData.from_dict(d.pop("peak"))

        peak_to_peak = AxisData.from_dict(d.pop("peakToPeak"))

        rms = AxisData.from_dict(d.pop("rms"))

        wave_data = cls(
            crest_factor=crest_factor,
            crest_factor_db=crest_factor_db,
            peak=peak,
            peak_to_peak=peak_to_peak,
            rms=rms,
        )

        wave_data.additional_properties = d
        return wave_data

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
