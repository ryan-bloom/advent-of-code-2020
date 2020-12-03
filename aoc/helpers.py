import os


def read_lines(path):
    with open(f"{os.getcwd()}/{path}") as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()
