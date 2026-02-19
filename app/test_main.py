import pytest
from typing import Any, Type
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("", False),
        ("Пароль@фadadf", False),
        ("Pass@word1", True),
        ("S234$67", False),
        ("S234$6789asdfgh11", False),
        ("pass@word1", False),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result


@pytest.mark.parametrize(
    "bad_password, expected_result_bad_password",
    [
        (123, TypeError),
        (None, TypeError),
        (object(), TypeError),
    ]
)
def test_check_password_type(bad_password: Any,
                             expected_result_bad_password: Type[Exception])\
        -> None:
    with pytest.raises(expected_result_bad_password):
        check_password(bad_password)
