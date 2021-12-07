import pathlib

PATH = pathlib.Path(__file__).parent.absolute()


def read_lines(datapath):
    with open(f"{PATH}/data/{datapath}") as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()


def read_file_to_list(datapath, strip=True):
    file = open(f"{PATH}/data/{datapath}")
    file_list = file.readlines()
    if strip:
        return [line.strip() for line in file_list]
    return file_list