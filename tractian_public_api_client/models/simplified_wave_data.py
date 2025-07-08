from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.axis_data import AxisData


T = TypeVar("T", bound="SimplifiedWaveData")


@_attrs_define
class SimplifiedWaveData:
    crest_factor: Union[Unset, "AxisData"] = UNSET
    crest_factor_db: Union[Unset, "AxisData"] = UNSET
    peak: Union[Unset, "AxisData"] = UNSET
    peak_to_peak: Union[Unset, "AxisData"] = UNSET
    rms: Union[Unset, "AxisData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crest_factor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.crest_factor, Unset):
            crest_factor = self.crest_factor.to_dict()

        crest_factor_db: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.crest_factor_db, Unset):
            crest_factor_db = self.crest_factor_db.to_dict()

        peak: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.peak, Unset):
            peak = self.peak.to_dict()

        peak_to_peak: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.peak_to_peak, Unset):
            peak_to_peak = self.peak_to_peak.to_dict()

        rms: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rms, Unset):
            rms = self.rms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crest_factor is not UNSET:
            field_dict["crestFactor"] = crest_factor
        if crest_factor_db is not UNSET:
            field_dict["crestFactorDb"] = crest_factor_db
        if peak is not UNSET:
            field_dict["peak"] = peak
        if peak_to_peak is not UNSET:
            field_dict["peakToPeak"] = peak_to_peak
        if rms is not UNSET:
            field_dict["rms"] = rms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.axis_data import AxisData

        d = dict(src_dict)
        _crest_factor = d.pop("crestFactor", UNSET)
        crest_factor: Union[Unset, AxisData]
        if isinstance(_crest_factor, Unset):
            crest_factor = UNSET
        else:
            crest_factor = AxisData.from_dict(_crest_factor)

        _crest_factor_db = d.pop("crestFactorDb", UNSET)
        crest_factor_db: Union[Unset, AxisData]
        if isinstance(_crest_factor_db, Unset):
            crest_factor_db = UNSET
        else:
            crest_factor_db = AxisData.from_dict(_crest_factor_db)

        _peak = d.pop("peak", UNSET)
        peak: Union[Unset, AxisData]
        if isinstance(_peak, Unset):
            peak = UNSET
        else:
            peak = AxisData.from_dict(_peak)

        _peak_to_peak = d.pop("peakToPeak", UNSET)
        peak_to_peak: Union[Unset, AxisData]
        if isinstance(_peak_to_peak, Unset):
            peak_to_peak = UNSET
        else:
            peak_to_peak = AxisData.from_dict(_peak_to_peak)

        _rms = d.pop("rms", UNSET)
        rms: Union[Unset, AxisData]
        if isinstance(_rms, Unset):
            rms = UNSET
        else:
            rms = AxisData.from_dict(_rms)

        simplified_wave_data = cls(
            crest_factor=crest_factor,
            crest_factor_db=crest_factor_db,
            peak=peak,
            peak_to_peak=peak_to_peak,
            rms=rms,
        )

        simplified_wave_data.additional_properties = d
        return simplified_wave_data

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
