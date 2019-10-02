from unittest import mock

import nicolas.formatting


@mock.patch("shutil.get_terminal_size")
def test_that_header_returns_full_terminal_width(terminal_size_mock):
    expected_columns = 80
    test_text = "Test"

    terminal_size_mock.return_value = (expected_columns, 24)
    output = nicolas.formatting.header(test_text)

    assert test_text in output
    assert all(len(line) is expected_columns for line in output.splitlines())


@mock.patch("shutil.get_terminal_size")
def test_that_header_returns_full_terminal_width_with_odd_input(
        terminal_size_mock):
    expected_columns = 80
    test_text = "Testing"

    terminal_size_mock.return_value = (expected_columns, 24)
    output = nicolas.formatting.header(test_text)

    assert test_text in output
    assert all(len(line) is expected_columns for line in output.splitlines())


def test_that_tabbed_returns_with_values_alligned():
    data = {"x": "data", "yy": "data!!"}
    spaces = 4

    result = nicolas.formatting.tabbed(data, spacing=spaces)

    assert result.splitlines()[0].count(" ") is 5
    assert result.splitlines()[-1].count(" ") is 4
