from assertpy import assert_that
from unittest import TestCase

from src.Wrapper import wrap
""" TODO
"" ó null, n -> "" - ok
"hello", -3 -> error - ok

hello, 5 -> "hello" - ok
hello, 2 -> "he\nll\no -
hello, 3 -> "hel\nlo -

hello world, 8 -> "hello\nworld" -
hello world, 5 -> "hello\n world" -
hello world, 2 -> "he\nll\no\nwo\nrl\nd" -
"""


class TestIsNarcissisticNumber(TestCase):
    def test_return_emtpy_for_null_or_empty_line(self):
        assert_that(wrap("", 5)).is_equal_to("")
        assert_that(wrap(None, 5)).is_equal_to("")

    def test_return_error_for_negative_column(self):
        with self.assertRaises(Exception):
            wrap("hello", -3)

    def test_return_same_line_width_high_column(self):
        assert_that(wrap("hello", 5)).is_equal_to("hello")

    def test_return_wrap_line(self):
        assert_that(wrap("hello", 2)).is_equal_to("he\nll\no")
        assert_that(wrap("hello", 3)).is_equal_to("hel\nlo")



