"""
--- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of
those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but
first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop)
and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase
the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction;
for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction
20 lines above to be executed next.

nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
For example, consider the following program:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
These instructions are visited in this order:

nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?
"""

from aoc.helpers import read_file_to_list
from dataclasses import dataclass


@dataclass
class SystemInstruction:
    direction: int
    magnitude: int
    command: int
    index: int = 0

    def get_movement_number(self):
        return self.direction * self.magnitude


class HandheldSystem:
    def __init__(self, datapath):
        self.commands_og = read_file_to_list(datapath)
        self.commands = read_file_to_list(datapath)
        self.commands_followed = set()
        self.accumulator = 0
        self.current_index = -1
        self.HALT = False
        self.COMPLETE = False
        self.swappable = [
            index for index, line in enumerate(self.commands_og) if "acc" not in line
        ]

    def parse_instruction(self, idx):
        self.current_index = idx
        try:
            line = self.commands[self.current_index]
            command, movement = line.split()
            return SystemInstruction(
                direction=1 if movement[0] == "+" else -1,
                magnitude=int(movement[1:]),
                command=command,
                index=idx,
            )
        except IndexError:
            self.HALT = True
            pass

    def run_command(self, command: SystemInstruction):
        # check if command has run before
        if not command:
            self.COMPLETE = True

        while not self.HALT and not self.COMPLETE:
            if command.index in self.commands_followed:
                self.HALT = True
                return

            self.commands_followed.add(command.index)

            if command.command == "acc":
                self.accumulator += command.get_movement_number()
            elif command.command == "nop":
                pass
            elif command.command == "jmp":
                next_line_index = command.index + command.get_movement_number()
                if next_line_index == len(self.commands):
                    self.COMPLETE = True
                else:
                    self.run_command(self.parse_instruction(next_line_index))

            if not self.COMPLETE and not self.HALT:
                self.run_command(self.parse_instruction(self.current_index + 1))

    def invert_command(self, command):
        if "jmp" in command:
            return command.replace("jmp", "nop")
        return command.replace("nop", "jmp")

    def invert_next_command(self):
        if not self.COMPLETE:
            commands = self.commands_og[:]
            swap_index = self.swappable.pop()
            commands[swap_index] = self.invert_command(commands[swap_index])
            self.commands = commands

    def reset(self):
        if not self.COMPLETE:
            self.HALT = False
            self.current_index = -1
            self.accumulator = 0
            self.commands_followed = set()

    def run_until_first_loop(self):
        self.run_command(self.parse_instruction(self.current_index + 1))
        return self.accumulator

    def run_to_completion(self):
        self.reset()
        while not self.COMPLETE:
            self.run_command(self.parse_instruction(self.current_index + 1))
            self.reset()
            self.invert_next_command()

        print("program finished!", self.accumulator)
        return self.accumulator


test_handheld = HandheldSystem("day8/test.txt")
assert test_handheld.run_until_first_loop() == 5
assert test_handheld.run_to_completion() == 8

live_handheld = HandheldSystem("day8/data.txt")
print("part 1:", live_handheld.run_until_first_loop())
print("part 2:", live_handheld.run_to_completion())