from typing import Literal, cast

MeasurementUnit = Literal[
    "cubicMeters",
    "gallons",
    "inches",
    "kilograms",
    "liters",
    "meters",
    "milliliters",
    "millimeters",
    "pairs",
    "pieces",
    "services",
    "squareMeters",
    "tons",
    "units",
]

MEASUREMENT_UNIT_VALUES: set[MeasurementUnit] = {
    "cubicMeters",
    "gallons",
    "inches",
    "kilograms",
    "liters",
    "meters",
    "milliliters",
    "millimeters",
    "pairs",
    "pieces",
    "services",
    "squareMeters",
    "tons",
    "units",
}


def check_measurement_unit(value: str) -> MeasurementUnit:
    if value in MEASUREMENT_UNIT_VALUES:
        return cast(MeasurementUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEASUREMENT_UNIT_VALUES!r}"
    )
