"""
--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
"""

from collections import defaultdict
from dataclasses import dataclass
from operator import add, sub
from aoc.helpers import read_file_to_list

DIRECTONS = {
    "N": 0,
    "E": 90,
    "S": 180,
    "W": 270,
}

DEGREE_DIRECTIONS = dict(map(reversed, DIRECTONS.items()))
ROTATE_ACTIONS = ["R", "L"]


@dataclass
class WayPoint:
    N: int = 1
    S: int = 0
    E: int = 10
    W: int = 0

    def get_coords(self):
        return {"N": self.N, "S": self.S, "E": self.E, "W": self.W}

    def initialize(self, N=0, S=0, E=0, W=0):
        self.N = N
        self.S = S
        self.E = E
        self.W = W

    def rotate_90(self, action):

        # The waypoint stays 10 units east and 4 units north of the ship.
        # R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship.

        # I hate this and want to refactor it to use a single cardinal direction,
        # but im mostly just happy its over.
        QUAD_RULES = {
            "E": {"R": {"E": "S"}, "L": {"E": "N"}},
            "S": {"R": {"S": "W"}, "L": {"S": "E"}},
            "W": {"R": {"W": "N"}, "L": {"W": "S"}},
            "N": {"R": {"N": "E"}, "L": {"N": "W"}},
            "EN": {"R": {"N": "E", "E": "S"}, "L": {"N": "W", "E": "N"}},
            "ES": {"R": {"E": "S", "S": "W"}, "L": {"E": "N", "S": "E"}},
            "SW": {"R": {"S": "W", "W": "N"}, "L": {"S": "E", "W": "S"}},
            "NW": {"R": {"W": "N", "N": "E"}, "L": {"W": "S", "N": "W"}},
        }

        current_quad = "".join(
            sorted(
                [direction for direction, val in self.get_coords().items() if val > 0]
            )
        )
        rule = QUAD_RULES.get(current_quad, {}).get(action)
        if rule:
            new_values = defaultdict(int)
            for old, new in rule.items():
                new_values[new] = getattr(self, old)

            self.initialize(**new_values)

    def rotate(self, action, degrees):
        num_moves = degrees // 90
        for _ in range(num_moves):
            self.rotate_90(action)

    def move(self, move_dir, magnitude):
        INVERSE_DIRECTIONS = {"N": "S", "S": "N", "E": "W", "W": "E"}

        # calculate new coords
        if getattr(self, INVERSE_DIRECTIONS.get(move_dir)) > 0:
            if (
                new_val := getattr(self, INVERSE_DIRECTIONS.get(move_dir)) - magnitude
            ) > 0:
                setattr(self, INVERSE_DIRECTIONS.get(move_dir), new_val)
            else:
                setattr(self, move_dir, abs(new_val))
                setattr(self, INVERSE_DIRECTIONS.get(move_dir), 0)
        else:
            setattr(self, move_dir, getattr(self, move_dir) + magnitude)


class Ship:
    def __init__(self, waypoint=None):
        # origin position
        self.N = 0
        self.S = 0
        self.E = 0
        self.W = 0
        self.facing_direction = "E"
        self.waypoint = waypoint

    def get_coords(self):
        return {"N": self.N, "S": self.S, "E": self.E, "W": self.W}

    def get_rotation_op(self, action):
        if action == "R":
            return add
        return sub

    def rotate(self, action, degrees):
        # if following a waypoint rotate it
        if self.waypoint:
            self.waypoint.rotate(action, degrees)
            return

        # get current directions - start with 360 if facing N and clockwise
        current_degrees = (
            360
            if (self.facing_direction == "N" and action == "R")
            else DIRECTONS.get(self.facing_direction)
        )

        post_rotation_degrees = self.get_rotation_op(action)(current_degrees, degrees)

        if post_rotation_degrees < 0:
            post_rotation_degrees += 360
        elif post_rotation_degrees >= 360:
            post_rotation_degrees -= 360

        self.facing_direction = DEGREE_DIRECTIONS.get(post_rotation_degrees)

    def move(self, action, magnitude):
        # if following a waypoint, move towards it N times.
        if self.waypoint:
            if action == "F":
                moves = {
                    direction: amount
                    for direction, amount in self.waypoint.get_coords().items()
                    if amount > 0
                }
                for direction, amount in moves.items():
                    setattr(
                        self, direction, getattr(self, direction) + (magnitude * amount)
                    )
            else:
                self.waypoint.move(action, magnitude)
            return

        move_dir = self.facing_direction if action == "F" else action
        setattr(self, move_dir, getattr(self, move_dir) + magnitude)

    def follow_command(self, command):
        action, magnitude = command[0], int(command[1:])
        if action in ROTATE_ACTIONS:
            self.rotate(action, magnitude)
        else:
            self.move(action, magnitude)

    def get_manhattan_distance(self):
        return abs(self.E - self.W) + abs(self.N - self.S)


def run(datapath, with_waypoint=False):
    # instantiate ship
    ship = Ship(waypoint=WayPoint()) if with_waypoint else Ship()
    data = read_file_to_list(datapath)
    for command in data:
        ship.follow_command(command)

    return ship.get_manhattan_distance()


assert run("day12/test.txt") == 25
print("part 1", run("day12/data.txt"))

assert run("day12/test.txt", with_waypoint=True) == 286
print("part 2", run("day12/data.txt", with_waypoint=True))
