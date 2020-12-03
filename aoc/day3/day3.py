from aoc.helpers import read_lines
from functools import reduce
from operator import mul


class MapTraversal:

    TREE_CHAR = "#"
    SAFE_CHAR = "."

    num_trees = 0

    def __init__(self, tree_map, move_down, move_right):
        self.tree_map = tree_map
        self.move_down = move_down
        self.move_right = move_right
        self.map_height = len(self.tree_map)
        self.map_width = len(self.tree_map[0])

    def run(self):
        """ until at the bottom of the map, move and determine if a tree was encountered """
        row_num = 0
        col_num = 0

        while row_num < self.map_height:
            if self.tree_map[row_num][col_num] == self.TREE_CHAR:
                self.num_trees += 1
            row_num += self.move_down
            col_num = (col_num + self.move_right) % self.map_width

        return self.num_trees


multiply_slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

test_map_panel = []
for line in read_lines("day3/test.txt"):
    test_map_panel.append([space for space in line.strip()])

test_traversal = MapTraversal(test_map_panel, 1, 3)
assert test_traversal.run() == 7

test_results = [MapTraversal(test_map_panel, x, y).run() for [x, y] in multiply_slopes]
assert reduce(mul, test_results) == 336


part_1_map_panel = []
for line in read_lines("day3/day3.txt"):
    part_1_map_panel.append([space for space in line.strip()])

part_1_traversal = MapTraversal(part_1_map_panel, 1, 3)
print("part 1 num trees", part_1_traversal.run())

part_2_results = [
    MapTraversal(part_1_map_panel, x, y).run() for [x, y] in multiply_slopes
]
print("part 2 multiplied trees", reduce(mul, part_2_results))
