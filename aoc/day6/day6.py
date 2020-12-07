"""
--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

"""

from aoc.helpers import read_lines
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class AnswerGroup:
    group_input: list

    def count_yes_answers(self):
        yes_answers = set()

        for person_answers in self.group_input:
            for answer in person_answers:
                yes_answers.add(answer)

        return len(yes_answers)

    def count_all_yes_questions(self):
        question_count = defaultdict(int)
        num_people = len(self.group_input)

        for person_answers in self.group_input:
            for answer in person_answers:
                question_count[answer] += 1

        return len(
            [
                num_answered
                for _, num_answered in question_count.items()
                if num_answered == num_people
            ]
        )


assert AnswerGroup(["abc"]).count_yes_answers() == 3
assert AnswerGroup(["a", "b", "c"]).count_yes_answers() == 3
assert AnswerGroup(["ab", "ac"]).count_yes_answers() == 3
assert AnswerGroup(["a", "a", "a", "a"]).count_yes_answers() == 1
assert AnswerGroup(["b"]).count_yes_answers() == 1

assert AnswerGroup(["abc"]).count_all_yes_questions() == 3
assert AnswerGroup(["a", "b", "c"]).count_all_yes_questions() == 0
assert AnswerGroup(["ab", "ac"]).count_all_yes_questions() == 1
assert AnswerGroup(["a", "a", "a", "a"]).count_all_yes_questions() == 1
assert AnswerGroup(["b"]).count_all_yes_questions() == 1


def parse_data_into_groups(data_path):
    answer_groups = []
    current_group = []
    for line in read_lines(data_path):
        if line != "\n":
            current_group.append(line.strip())
        else:
            answer_groups.append(AnswerGroup(current_group))
            current_group = []
    answer_groups.append(AnswerGroup(current_group))
    return answer_groups


def parse_data_return_sum_yes(data_path):
    answer_groups = parse_data_into_groups(data_path)
    return sum(group.count_yes_answers() for group in answer_groups)


assert parse_data_return_sum_yes("day6/test.txt") == 11
print("total yes:", parse_data_return_sum_yes("day6/data.txt"))


def parse_data_return_sum_all_yes_questions(data_path):
    answer_groups = parse_data_into_groups(data_path)
    return sum(group.count_all_yes_questions() for group in answer_groups)


assert parse_data_return_sum_all_yes_questions("day6/test.txt") == 6
print("total all yes:", parse_data_return_sum_all_yes_questions("day6/data.txt"))