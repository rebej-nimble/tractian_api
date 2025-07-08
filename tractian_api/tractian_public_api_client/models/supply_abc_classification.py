from typing import Literal, cast

SupplyAbcClassification = Literal["A", "B", "C"]

SUPPLY_ABC_CLASSIFICATION_VALUES: set[SupplyAbcClassification] = {
    "A",
    "B",
    "C",
}


def check_supply_abc_classification(value: str) -> SupplyAbcClassification:
    if value in SUPPLY_ABC_CLASSIFICATION_VALUES:
        return cast(SupplyAbcClassification, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLY_ABC_CLASSIFICATION_VALUES!r}"
    )
