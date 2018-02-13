from password_cracker.cracker import *

def test_is_not_homogeneous():
    correct_pad = "......"
    incorrect_pad = "....?...."
    empty_pad = ""

    assert not is_not_homogeneous(correct_pad)
    assert is_not_homogeneous(incorrect_pad)
    assert not is_not_homogeneous(empty_pad)
