from typing import Literal, cast

SupplyXyzClassification = Literal["X", "Y", "Z"]

SUPPLY_XYZ_CLASSIFICATION_VALUES: set[SupplyXyzClassification] = {
    "X",
    "Y",
    "Z",
}


def check_supply_xyz_classification(value: str) -> SupplyXyzClassification:
    if value in SUPPLY_XYZ_CLASSIFICATION_VALUES:
        return cast(SupplyXyzClassification, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLY_XYZ_CLASSIFICATION_VALUES!r}"
    )
