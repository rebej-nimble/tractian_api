from typing import Literal, cast

CategoryOtherCosts = Literal[
    "accommodation",
    "displacement",
    "food",
    "labor",
    "material",
    "other",
    "outsource",
    "travel",
]

CATEGORY_OTHER_COSTS_VALUES: set[CategoryOtherCosts] = {
    "accommodation",
    "displacement",
    "food",
    "labor",
    "material",
    "other",
    "outsource",
    "travel",
}


def check_category_other_costs(value: str) -> CategoryOtherCosts:
    if value in CATEGORY_OTHER_COSTS_VALUES:
        return cast(CategoryOtherCosts, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATEGORY_OTHER_COSTS_VALUES!r}"
    )
