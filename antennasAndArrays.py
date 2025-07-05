import numpy as np
import matplotlib.pyplot as plt

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
    

    def getPattern(self, azimuth, elevation):
        # TODO all of this is completely wrong, fix it
        azimuth_grid, elevation_grid = np.meshgrid(azimuth, elevation)
        u_grid = np.sin(azimuth_grid / 180 * np.pi)
        v_grid = np.sin(elevation_grid/180*np.pi)

        AF = np.zeros(np.shape(u_grid), dtype=complex)

        for antenna in self.antennas:
            AF = AF + np.exp(-1j * 2 * np.pi * (antenna.x()*u_grid + antenna.y()*v_grid))

        return np.transpose(AF)


class rectangularArray(AntennaArray):
    def __init__(self, x, y, spacing):
        super().__init__()

        for i in range(x):
            for j in range(y):
                self.antennas.append(Antenna([i*spacing, j*spacing, 0]))


class Antenna:
    # TODO add antenna radiation patterns
    # position defaults to value in terms of wavelength
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
