from nicolas import cv


def test_that_i_managed_to_spell_my_name_correctly():
    assert cv.name == "Nicolas Harlem Eide"


def test_that_i_say_something_about_myself():
    assert len(cv.about) > 1


def test_that_i_have_some_experience_with_programming_in_the_real_world():
    assert len(cv.experience) > 1


def test_that_i_actually_have_an_education():
    """Did you know that I've got a bachelor and a master degree?"""
    assert any("B.Sc." in degree["Type"] for degree in cv.education)
    assert any("M.Sc." in degree["Type"] for degree in cv.education)


def test_that_i_can_be_contacted_by_a_potential_employer():
    assert "Phone" in cv.contact
    assert "E-mail" in cv.contact
