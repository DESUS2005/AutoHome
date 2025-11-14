import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# --- Tests для capitalize ---
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123abc", "123abc"),  # число как строка
    ("", ""),  # пустая строка
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str", [None, 123, [], {}])
def test_capitalize_negative(input_str):
    with pytest.raises(TypeError):
        string_utils.capitalize(input_str)

# --- Tests для trim ---
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("      hello", "hello"),
    ("no_space", "no_space"),
    (" ", ""),  # одна пробельная строка
    ("    ", ""),  # только пробелы
    ("", ""),  # пустая строка
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str", [None, 123, [], {}])
def test_trim_negative(input_str):
    with pytest.raises(TypeError):
        string_utils.trim(input_str)

# --- Тесты для contains ---

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "P", True),
    ("SkyPro", "U", False),
    ("hello world", "o", True),
    ("hello world", "z", False),
])
def test_contains_positive_and_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
    ("hello", None),
    (123, "a"),
    ("hello", 5),
])
def test_contains_negative_cases(string, symbol):
    with pytest.raises(TypeError):
        string_utils.contains(string, symbol)

# --- Тесты для delete_symbol ---

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", "o", "hell wrld"),
    ("abcabc", "a", "bcbc"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
    ("hello", None),
    (123, "a"),
    ("hello", 5),
])
def test_delete_symbol_negative_cases(string, symbol):
    with pytest.raises(TypeError):
        string_utils.delete_symbol(string, symbol)