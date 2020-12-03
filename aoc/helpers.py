import pathlib


def read_lines(datapath):
    current_path = pathlib.Path(__file__).parent.absolute()
    with open(f"{current_path}/data/{datapath}") as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()
