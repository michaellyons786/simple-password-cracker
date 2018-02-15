from password_cracker.cracker import *


def test_is_not_homogeneous():
    correct_pad = "......"
    incorrect_pad = "....?...."
    empty_pad = ""

    assert not is_not_homogeneous(correct_pad)
    assert is_not_homogeneous(incorrect_pad)
    assert not is_not_homogeneous(empty_pad)


def test_invalid_pad():
    pads = ['.', '?']
    correct_pad_period = "....."
    correct_pad_question = "??????????"
    incorrect_pad_length = "......................."
    incorrect_pad_comp = "....?...."
    incorrect_pad_not_in_list = "---------"
    empty_pad = ""

    assert not invalid_pad(correct_pad_period, pads)
    assert not invalid_pad(correct_pad_question, pads)
    assert invalid_pad(incorrect_pad_length, pads)
    assert invalid_pad(incorrect_pad_comp, pads)
    assert invalid_pad(incorrect_pad_not_in_list, pads)
    assert not invalid_pad(empty_pad, pads)


def test_get_random_pad():
    pads = ['.', ',', '?', '!', '@']

    pad_1 = get_random_pad(pads)
    pad_2 = get_random_pad(pads)
    pad_3 = get_random_pad(pads)

    assert not invalid_pad(pad_1, pads)
    assert not invalid_pad(pad_2, pads)
    assert not invalid_pad(pad_3, pads)


def test_PasswordCracker():
    pads = [',', '!', '.']
    passwords = ['password', 'readme', '123', 'setup', 'external', 'libraries']
    password = '!!!!!password,,,,,'

    cracker = PasswordCracker(password, passwords, pads)
    mean_time, mean_attempts, round_times = cracker.run_experiment(10, False)




