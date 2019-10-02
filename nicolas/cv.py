"""Nicolas Harlem Eide's CV in glorious python"""
import shutil
from functools import partial

from tabulate import tabulate


name = "Nicolas Harlem Eide"

about = "Software developer with a passion for automation and simplicity.\n" \
        "Trying to help people achieve what they want with less effort."

experience = [
    {"Employer": "mnemonic",
     "Position": "Developer",
     "Period": "2018 - present"},

    {"Employer": "mnemonic",
     "Position": "Security Analyst",
     "Period": "2017 - 2018"},

    {"Employer": "UiO",
     "Position": "Student Recruiter",
     "Period": "2016 - 2017"},
]

education = [
    {"University": "UiO",
     "Type": "M.Sc.",
     "Name": "Programming and Networks",
     "Period": "2018 - 2020"},

    {"University": "UiO",
     "Type": "B.Sc.",
     "Name": "Programming and Networks",
     "Period": "2015 - 2018"},
]

contact = {
    "Phone": "+47 924 77 442",
    "E-mail": "nicolas@harlemeide.net",
}


def header(text: str, *,
           lines: int = 7,
           decorating_character: str = "="):
    """Returns the text as a header

    :param text: Text to display to the user
    :param lines: Amount of lines that the header will occupy
    :param decorating_character: The character that will be displayed around
                                 the specified text.
    :return: A string with the width of the users terminal with centered text.
    """
    line_length = shutil.get_terminal_size()[0]
    text_line_decorator_length = (line_length - len(text) - 2) // 2

    def centered_text(string):
        centered = "".join([decorating_character * text_line_decorator_length,
                            " " + string + " ",
                            decorating_character * text_line_decorator_length])
        centered += decorating_character * (line_length - len(centered))

        return centered

    output = []
    for line in range(lines):
        if line == lines // 2:
            output.append(centered_text(text))
        elif line == lines // 2 + 1 or line == lines // 2 - 1:
            output.append(centered_text(" " * len(text)))
        else:
            output.append(decorating_character * line_length)

    return "\n".join(output)


def tabbed(data: dict, spacing: int = 4):
    """Returns the dict with values aligned relative to the longest key

    :param data: The data to format
    :param spacing: Amount of spaces between the longest key and it's value.
    """
    longest_key_lenght = max(len(key) for key in data.keys())

    output = []
    for key, value in data.items():
        output.append("{key:<{width}}{value}".format(
            key=key + ":",
            value=value,
            width=longest_key_lenght + spacing + 1))

    return "\n".join(output)



# Wrapper around tabulate to get a cleaner appearance in the REPL
table = partial(tabulate, headers="keys", tablefmt="github")

