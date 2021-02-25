import numpy as np
import random

class InfoGen:
    dur = 0

    def __init__(self):
        self.dur = 0

class Coche:
    str_no = 0
    ruta = []

    def __init__(self):
        self.str_no = 0
        self.ruta = []

class Calle:
    ID = ""
    entry = ""
    exit = ""
    L = 0
    rent = 0
    num_coches = 0

    def __init__(self):
        self.ID = ""
        self.entry = ""
        self.exit = ""
        self.L = 0
        self.rent = 0
        self.num_coches = 0
        self.total_time_coches = 0
        self.min = 10000000000
        self.max = -1000000000

class Interesc:
    streets = []
    id = 0 
    
    def __init__(self):
        self.streets = []


def reader(filename):
    calles = {}
    coches = []
    with open(filename) as f:
        counter = 0
        data = InfoGen()
        line = f.readline()
        # Obtener informacion general
        parsed_line = line.split(" ")
        data.dur = int(parsed_line[0])
        data.inter_no = int(parsed_line[1])
        data.streets_no = int(parsed_line[2])
        data.cars_no = int(parsed_line[3])
        data.bonus = int(parsed_line[4])


        inters =  [Interesc() for i in range(data.inter_no)]
        # Calle parser
        counter = 0
        while counter < data.streets_no:
            line = f.readline()
            parsed_line = line.split(" ")
            calle = Calle()
            calle.entry = int(parsed_line[0])
            calle.exit = int(parsed_line[1])
            calle.ID = parsed_line[2]
            calle.L = int(parsed_line[3])
            calles[calle.ID] = calle
            if inters[calle.exit].streets is []:
                inters[calle.exit].streets = [calle]
            else:
                inters[calle.exit].streets.append(calle)
            inters[calle.exit].id = calle.exit
            counter += 1

        # Coches parser
        counter = 0
        while counter < data.cars_no:
            line = f.readline()
            parsed_line = line.split(" ")
            coche = Coche()
            coche.str_no = int(parsed_line[0])
            parsed_line[-1] = parsed_line[-1][:-1]
            coche.ruta = parsed_line[1:]
            coches.append(coche)
            total_time = 0
            for ruta in coche.ruta:
                calles[ruta].num_coches += 1
                total_time += calles[ruta].L

            for ruta in coche.ruta:
                calles[ruta].total_time_coches += total_time
                calles[ruta].min = min(calles[ruta].min, total_time)
                calles[ruta].max = max(calles[ruta].max, total_time)

            counter += 1
    return data, calles, coches, inters

def main():
    """ Main program """

    times = [10, 10, 10, 10, 10, 10]
    filenames = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]
    times_index = 0
    for filename in filenames:
        tiempo_interseccion = times[times_index]
        print(filename)
        data, calles, coches, inters = reader(filename)

        inters_write = []
        counter = 0
        for inter in inters:
            coches_total = 0
            inter_write = {}
            coches_total_L = 0
            max_todas = 0
            for calle in inter.streets:
                coches_total += calle.num_coches
                coches_total_L += calle.total_time_coches
                max_todas = max(max_todas, calle.max)
            for calle in inter.streets:
                if coches_total != 0 and calle.total_time_coches != 0:
                    #rent = float(calle.num_coches) / float(coches_total)
                    #rent = (float(calle.num_coches) / float(coches_total))/float(calle.total_time_coches)
                    #rent = (float(calle.num_coches) / float(coches_total)) / (float(calle.total_time_coches) / data.dur)
                    #rent = float(calle.num_coches) / float(coches_total) * float(calle.total_time_coches/coches_total_L)
                    rent = float(calle.num_coches) / float(coches_total) * float(float(calle.min + calle.max)/2.0 / float(max_todas))
                    if rent > 0.0:
                        time_semaforo = int(rent * tiempo_interseccion)
                        #time_semaforo = int(random.randint(1, 15))
                        if time_semaforo == 0:
                            time_semaforo += 1
                        inter_write[calle.ID] = time_semaforo

            if (len(inter_write.keys()) > 0):
                inters_write.append((inter.id,inter_write))

        with open("result_" + filename, "w") as f:
            f.write(str(len(inters_write)) + '\n')
            for id, inter in inters_write:
                if(len(inter.keys()) > 0):
                    f.write(str(id) + '\n')
                    f.write(str(len(inter.keys())) + '\n')
                    for calle in inter.keys():
                        f.write(calle + " " + str(inter[calle]) + '\n')
        times_index += 1
    return 0



if __name__ == "__main__":
    main()