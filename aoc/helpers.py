import pathlib


def read_lines(path):
    current_path = pathlib.Path(__file__).parent.absolute()
    with open(f"{current_path}/{path}") as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()
