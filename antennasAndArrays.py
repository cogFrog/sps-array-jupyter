import numpy as np

class AntennaArray:
    def __init__(self, *args):

        if len(args) == 0:
            self.antennas = []
        elif len(args) == 1:
            # TODO type checking
            self.antennas = antennaList
    
    def append(self, antenna):
        self.antennas.append(antenna)

    def __repr__(self):
        return str(self.antennas)


class rectangularArray(AntennaArray):
    def __init__(self, x, y, spacing):
        self.array = AntennaArray()
        for i in range(x):
            for j in range(y):
                self.array.append(Antenna([i*spacing, j*spacing, 0]))

        print(self.array)


class Antenna:
    # TODO add antenna radiation patterns
    def __init__(self, position):
        # TODO type checking
        self.pos = np.array(position[0:3])
    
    def x(self):
        return self.pos[0]
    
    def y(self):
        return self.pos[1]
    
    def z(self):
        return self.pos[2]
    
    def __repr__(self):
        return f"Antenna ({self.pos[0]}, {self.pos[1]}, {self.pos[2]})"