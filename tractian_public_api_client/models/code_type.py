from typing import Literal, cast

CodeType = Literal["code128", "code39", "eanCode", "qrCode", "sku", "upcCode"]

CODE_TYPE_VALUES: set[CodeType] = {
    "code128",
    "code39",
    "eanCode",
    "qrCode",
    "sku",
    "upcCode",
}


def check_code_type(value: str) -> CodeType:
    if value in CODE_TYPE_VALUES:
        return cast(CodeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_TYPE_VALUES!r}")
