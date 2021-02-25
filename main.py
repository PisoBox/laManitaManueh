import numpy as np


def reader(filename):
    with open(filename) as f:
        line = f.readline()
        counter = 0
        data = {}
        while line:
            line = f.readline()
            parsed_line = line.split(" ")
            print(line)
            if counter == 0:
                data = {
                    "simulation_duration" : int(parsed_line[0]),
                    "number_intersections" : int(parsed_line[1]),
                    "number_streets" : int(parsed_line[2]),
                    "number_cars" : int(parsed_line[3]),
                    "bonus" : int(parsed_line[4])
                }
            counter += 1

def main():
    """ Main program """
    filename = "a.txt"
    reader(filename)
    return 0



if __name__ == "__main__":
    main()