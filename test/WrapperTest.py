from assertpy import assert_that
from unittest import TestCase

from src.Wrapper import wrap
""" TODO
"" ó null, n -> "" -
"hola", -3 -> error -

hola, 5 -> "hola" -
hola, 2 -> "ho\nla -
hola, 3 -> "hol\na -

hola mundo, 7 -> "hola\nmundo" -
hola mundo, 4 -> "hola\nmundo" -
hola mundo, 2 -> "ho\nla\nmu\nnd\no" -
"""


class TestIsNarcissisticNumber(TestCase):
    def test_return_same_line_width_high_column(self):
        line: str = "hola"
        assert_that(wrap(line, len(line)+1)).is_equal_to(line)

    def test_return_emtpy_for_null_or_empty_line(self):
        assert_that(wrap("", 5)).is_equal_to("")
        assert_that(wrap(None, 5)).is_equal_to("")
