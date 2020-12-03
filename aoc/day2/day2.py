"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

from aoc.helpers import read_lines


def check_password_string(password_string, pw_validator):
    """ Check a password string w/ a given validator callable """
    [rule, letter, password] = password_string.split()
    return pw_validator(rule, letter[:-1], password)


def is_password_valid_count(rule, letter, password):
    """ Part 1 - pw is valid if letter appears N times within range """
    if not letter in password:
        return False

    letter_count = sum(1 for char in password if char == letter)
    letter_range = rule.split("-")
    letter_min, letter_max = [int(letter_range[0]), int(letter_range[-1])]

    if letter_count >= letter_min and letter_count <= letter_max:
        return True

    return False


assert check_password_string("1-3 a: abcde", is_password_valid_count) is True
assert check_password_string("1-3 b: cdefg", is_password_valid_count) is False
assert check_password_string("2-9 c: ccccccccc", is_password_valid_count) is True


def get_num_valid_passwords(pw_validator):
    num_valid = 0
    for line in read_lines("aoc/day2/input1.txt"):
        if check_password_string(line, pw_validator):
            num_valid += 1
    print(num_valid)


print("getting number of valid passwords by rule: count")
get_num_valid_passwords(is_password_valid_count)

# part 2

"""
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""


def is_password_valid_position(rule, letter, password):
    """ Part 2 - pw is valid if letter appears at exactly 1 of the given indices """
    if not letter in password:
        return False

    letter_positions = rule.split("-")
    p1, p2 = [int(letter_positions[0]), int(letter_positions[-1])]

    p1_match_term = 1 if password[p1 - 1] == letter else 0
    p2_match_term = 1 if password[p2 - 1] == letter else 0

    return p1_match_term + p2_match_term == 1


assert check_password_string("1-3 a: abcde", is_password_valid_position) is True
assert check_password_string("1-3 b: cdefg", is_password_valid_position) is False
assert check_password_string("2-9 c: ccccccccc", is_password_valid_position) is False

print("getting number of valid passwords by rule: position")
get_num_valid_passwords(is_password_valid_position)
