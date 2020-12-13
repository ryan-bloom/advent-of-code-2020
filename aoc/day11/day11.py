import copy

from collections import Counter
from itertools import chain
from aoc.helpers import read_lines


def get_num_adjacent_full_seats(seat_data, row_num, seat_num):
    num_seats = len(seat_data[0])
    num_rows = len(seat_data)

    check_prev_row = row_num > 0
    check_next_row = row_num < num_rows - 1
    check_prev_seat = seat_num > 0
    check_next_seat = seat_num < num_seats - 1

    adjacent_full = 0

    start_row = row_num - 1 if check_prev_row else row_num
    end_row = row_num + 2 if check_next_row else row_num + 1
    start_seat = seat_num - 1 if check_prev_seat else seat_num
    end_seat = seat_num + 2 if check_next_seat else seat_num + 1

    for row in range(start_row, end_row):
        for seat in range(start_seat, end_seat):

            if seat_data[row][seat] == "#" and not (
                (row == row_num) and (seat == seat_num)
            ):
                adjacent_full += 1

    return adjacent_full


def by_adjacency(seat_data):
    num_changes = 0
    new_arrangement = copy.deepcopy(seat_data)
    for row_num, row in enumerate(seat_data):
        for seat_num, seat in enumerate(row):
            if (
                seat == "L"
                and get_num_adjacent_full_seats(seat_data, row_num, seat_num) == 0
            ):
                new_arrangement[row_num][seat_num] = "#"
                num_changes += 1
            if seat == "#":
                if get_num_adjacent_full_seats(seat_data, row_num, seat_num) >= 4:
                    new_arrangement[row_num][seat_num] = "L"
                    num_changes += 1

    return num_changes, new_arrangement


def get_final_arrangement(seat_data, seat_selection_method):
    changes = 1

    while changes:
        changes, seat_data = seat_selection_method(seat_data)

    return seat_data


def get_num_occupied_seats(seat_data):
    return Counter(chain.from_iterable(seat_data)).get("#")


def run(datapath, seat_selection_method):
    data = [list(seats.strip()) for seats in read_lines(datapath)]
    final = get_final_arrangement(data, seat_selection_method)
    return get_num_occupied_seats(final)


assert run("day11/test.txt", by_adjacency) == 37
print("part 1", run("day11/data.txt", by_adjacency))


def get_occupied_seat_in_line_of_sight(seat_data, slope, row_num, seat_num):
    num_rows = len(seat_data)
    num_seats = len(seat_data[0])
    row_move, seat_move = slope
    stop = False

    while not stop:
        next_row = row_num + row_move
        next_seat = seat_num + seat_move

        if (next_row == -1) or (next_seat == -1):
            return False

        stop = (
            (0 > next_row)
            or (next_row >= num_rows)
            or (0 > next_seat)
            or (next_seat >= num_seats)
        )

        try:
            next_visbile = seat_data[row_num + row_move][seat_num + seat_move]
        except IndexError:
            return False

        if next_visbile == "#":
            return True
        elif next_visbile == "L":
            return False

        row_num = next_row
        seat_num = next_seat

    return False


def get_num_visible_full_seats(seat_data, row_num, seat_num):
    # slopes for line of sight:
    line_of_sight_slopes = [
        (-1, 0),  # up
        (-1, -1),  # up and backward
        (0, -1),  # backward
        (1, -1),  # down and backward
        (1, 0),  # down
        (1, 1),  # down and forward
        (0, 1),  # forward
        (-1, 1),  # up and forward
    ]

    visible_full_seats = 0
    for slope in line_of_sight_slopes:
        if get_occupied_seat_in_line_of_sight(seat_data, slope, row_num, seat_num):
            visible_full_seats += 1

    return visible_full_seats


def by_visibility(seat_data):
    num_changes = 0
    new_arrangement = copy.deepcopy(seat_data)
    for row_num, row in enumerate(seat_data):
        for seat_num, seat in enumerate(row):
            if (
                seat == "L"
                and get_num_visible_full_seats(seat_data, row_num, seat_num) == 0
            ):
                new_arrangement[row_num][seat_num] = "#"
                num_changes += 1
            if seat == "#":
                if get_num_visible_full_seats(seat_data, row_num, seat_num) >= 5:
                    new_arrangement[row_num][seat_num] = "L"
                    num_changes += 1

    return num_changes, new_arrangement


assert run("day11/test.txt", by_visibility) == 26
print("part 2", run("day11/data.txt", by_visibility))