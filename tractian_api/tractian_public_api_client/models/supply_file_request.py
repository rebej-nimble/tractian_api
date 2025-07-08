from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.supply_file_conversion import SupplyFileConversion


T = TypeVar("T", bound="SupplyFileRequest")


@_attrs_define
class SupplyFileRequest:
    filename: str
    content_type: str
    size: int
    url: str
    key: str
    favorite: Union[None, bool]
    uploaded: Union[None, bool]
    internal: Union[None, bool]
    conversion: Union["SupplyFileConversion", None]
    upload_url: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.supply_file_conversion import SupplyFileConversion

        filename = self.filename

        content_type = self.content_type

        size = self.size

        url = self.url

        key = self.key

        favorite: Union[None, bool]
        favorite = self.favorite

        uploaded: Union[None, bool]
        uploaded = self.uploaded

        internal: Union[None, bool]
        internal = self.internal

        conversion: Union[None, dict[str, Any]]
        if isinstance(self.conversion, SupplyFileConversion):
            conversion = self.conversion.to_dict()
        else:
            conversion = self.conversion

        upload_url: Union[None, str]
        upload_url = self.upload_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "contentType": content_type,
                "size": size,
                "url": url,
                "key": key,
                "favorite": favorite,
                "uploaded": uploaded,
                "internal": internal,
                "conversion": conversion,
                "uploadURL": upload_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supply_file_conversion import SupplyFileConversion

        d = dict(src_dict)
        filename = d.pop("filename")

        content_type = d.pop("contentType")

        size = d.pop("size")

        url = d.pop("url")

        key = d.pop("key")

        def _parse_favorite(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        favorite = _parse_favorite(d.pop("favorite"))

        def _parse_uploaded(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        uploaded = _parse_uploaded(d.pop("uploaded"))

        def _parse_internal(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        internal = _parse_internal(d.pop("internal"))

        def _parse_conversion(data: object) -> Union["SupplyFileConversion", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conversion_type_0 = SupplyFileConversion.from_dict(data)

                return conversion_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SupplyFileConversion", None], data)

        conversion = _parse_conversion(d.pop("conversion"))

        def _parse_upload_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        upload_url = _parse_upload_url(d.pop("uploadURL"))

        supply_file_request = cls(
            filename=filename,
            content_type=content_type,
            size=size,
            url=url,
            key=key,
            favorite=favorite,
            uploaded=uploaded,
            internal=internal,
            conversion=conversion,
            upload_url=upload_url,
        )

        supply_file_request.additional_properties = d
        return supply_file_request

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
