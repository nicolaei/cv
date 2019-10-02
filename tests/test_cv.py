from unittest import mock

from nicolas import cv


def test_that_i_managed_to_spell_my_name_correctly():
    assert cv.name == "Nicolas Harlem Eide"


def test_that_i_say_something_about_myself():
    assert len(cv.about) > 1


def test_that_i_have_some_experience_with_programming_in_the_real_world():
    assert len(cv.experience) > 1


def test_that_i_actually_have_an_education():
    """Did you know that I've got a bachelor and a master degree?"""
    assert any("b.sc." in degree["type"] for degree in cv.education)
    assert any("m.sc." in degree["type"] for degree in cv.education)


def test_that_i_can_be_contacted_by_a_potential_employer():
    assert "phone" in cv.contact
    assert "e-mail" in cv.contact


@mock.patch("shutil.get_terminal_size")
def test_that_header_prints_full_terminal_width(terminal_size_mock):
    expected_columns = 80
    test_text = "Test"

    terminal_size_mock.return_value = (expected_columns, 24)
    output = cv.header(test_text)

    assert test_text in output
    assert all(len(line) is expected_columns for line in output.splitlines())


@mock.patch("shutil.get_terminal_size")
def test_that_header_prints_full_terminal_width_with_odd_input(
        terminal_size_mock):
    expected_columns = 80
    test_text = "Testing"

    terminal_size_mock.return_value = (expected_columns, 24)
    output = cv.header(test_text)

    assert test_text in output
    assert all(len(line) is expected_columns for line in output.splitlines())
