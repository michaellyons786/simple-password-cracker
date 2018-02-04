# Written by Michael Lyons
# CS 356
# 12/4/17

import time
import random
import matplotlib.pyplot as plt


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

        mean_time = mean(round_times)
        mean_attempts = mean(round_attempts)

        return mean_time, mean_attempts, round_times

    def crack_haystack(self, password):
        guess = ''
        guesses_made = 0
        start = time.time()

        while password != guess:
            front_pad = get_random_pad(self.pad_list)
            back_pad = get_random_pad(self.pad_list)

            guess = front_pad + get_random_password(self.password_list) + back_pad
            print(guess)
            time.sleep(1)
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


def mean(collection):
    sum_of_elements = 0
    for element in collection:
        sum_of_elements += element

    return sum_of_elements / len(collection)


def write_data(round_times, mean_time, mean_attempts, password):
    file_object = open('data.csv', 'w')

    file_object.write("password, " + password + '\n')
    file_object.write("mean_time, " + "{0:.2f}".format(mean_time) + '\n')
    file_object.write("mean_attempts, " + str(mean_attempts) + '\n')


    index = 1
    for round in round_times:
        file_object.write(str(index) + ', ' + "{0:.2f}".format(round) + '\n')
        index += 1

    file_object.close()


def plot_experiment(number_of_rounds, crack_times, crack_attempts):
    rounds = range(1, int(number_of_rounds) + 1)
    plt.plot(rounds, crack_times, '-')
    plt.xlabel("Round")
    plt.ylabel("Time (s)")
    plt.grid(True)
    plt.title("Time to crack")
    plt.savefig("time")
    plt.clf()

    plt.plot(rounds, crack_attempts, '-')
    plt.xlabel("Round")
    plt.ylabel("Attempts to crack (s)")
    plt.grid(True)
    plt.title("Attempts to crack")
    plt.savefig("attempts")


if __name__ == "__main__":
    words = load_list("words.txt")
    a = []
    for _ in range(6):
        a.append(random.choice(words))

    print(len(words))
    print(a)



# References
# Password lists, https://github.com/danielmiessler/SecLists
