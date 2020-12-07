import pathlib

PATH = pathlib.Path(__file__).parent.absolute()


def read_lines(datapath):
    with open(f"{PATH}/data/{datapath}") as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()
