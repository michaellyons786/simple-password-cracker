# Written by Michael Lyons
# CS 356
# 12/4/17

import time
import random
import numpy as np

class PasswordCracker:
    def __init__(self, password, password_list, pad_list):
        self.password_list = password_list
        self.pad_list = pad_list
        self.password = password

    def run_experiment(self, iterations):
        round_times = []
        round_attempts = []

        for i in range(iterations):
            time_elapsed, attempts_made = self.crack_haystack(self.password)
            round_times.append(time_elapsed)
            round_attempts.append(attempts_made)
            print("**********\nCracked. Round " + str(i + 1))
            print("Time: ", time_elapsed)
            print("Attempts: ", attempts_made)

        mean_time = np.mean(round_times)
        mean_attempts = np.mean(round_attempts)

        return mean_time, mean_attempts, round_times

    def crack_haystack(self, password):
        guess = ''
        guesses_made = 0
        start = time.time()

        while password != guess:
            front_pad = get_random_pad(self.pad_list)
            back_pad = get_random_pad(self.pad_list)

            guess = front_pad + get_random_password(self.password_list) + back_pad
            if guesses_made % 100000 is 0:
                print("Guess " + str(guesses_made) + ": " + guess)
            guesses_made += 1

        stop = time.time()

        return (stop - start), guesses_made

    def change_password(self, password):
        self.password = password


def get_random_password(passwords):
    return random.choice(passwords)


def load_list(file_name):
    loaded_list = []
    text_file = open(file_name, 'r')

    for line in text_file:
        loaded_list.append(line.strip())

    return loaded_list


def get_random_pad(pads):
    pad_character = random.choice(pads)
    pad = ''
    size = random.randint(0, 10)

    for _ in range(size):
        pad += pad_character

    return pad


def password_in_file(password, passwords):
    return password in passwords


def invalid_pad(pad, pad_list):
    return is_not_homogeneous(pad) or len(pad) > 10 or pad[0] not in pad_list


def is_not_homogeneous(pad):
    if len(pad) > 0:
        initial_pad = pad[0]
    else:
        return False

    for p in pad:
        if p != initial_pad:
            return True

    return False

def get_pad(pads):
    correct_pad = False
    while not correct_pad:
        print("Available pads: " + str(pads))
        print("Pad length should be between 0 and 10")
        print("Pads should be homogeneous (all of the same character), but left and right pads can differ")
        left_pad = input("Please enter left pad\n")
        right_pad = input("Please enter right pad\n")

        if invalid_pad(left_pad, pads) or invalid_pad(right_pad, pads):
            print("Invalid pad, please reenter valid pads.")
        else:
            correct_pad = True

    return left_pad, right_pad


if __name__ == "__main__":
    print("Please note that if the password list or pad list is too long, then the program may not finish in your "
          "lifetime. This is a toy cracker!")
    password = input("Please enter password\n")
    iterations = input("Please enter how many times you'd like to run the cracker\n")

    passwords_file = input("Please enter location of password list\n")
    passwords = load_list(passwords_file)

    if password_in_file(password, passwords):
        pads_file = input("Please enter location of pad list\n")
        pads = load_list(pads_file)

        left_pad, right_pad = get_pad(pads)
        full_password = left_pad + password + right_pad

        cracker = PasswordCracker(full_password, passwords, pads)
        cracker.run_experiment(int(iterations))
    else:
        print("Error: Password " + password + " not in password list, program will *never* crack password!")


# References
# Password lists, https://github.com/danielmiessler/SecLists
