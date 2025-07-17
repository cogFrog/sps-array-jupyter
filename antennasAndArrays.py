import numpy as np

class AntennaArray:
    """Basic array of identical antennas, minimal assumptions
    """    
    def __init__(self, positions, excitations=None):
        """Initialize antenna array with N antenna positions and excitations

        Args:
            positions (nparray(N, 3)): 2D array representing position of all antennas in wavelengths. Each row is an antenna position [x, y, z]
            excitations (nparray(N)): Array of complex #s representing excitation of each antenna. If None, defaults to all 1's
        """

        if len(positions.shape) != 2:
            raise ValueError(f'Expected 2D nparray, found {len(positions.shape)}D nparray')
        if positions.shape[1] != 3:
            raise ValueError(f'Expected 3 column nparray, found {positions.shape[1]} columns')
        self.positions = positions

        if excitations is None:
            excitations = np.ones(positions.shape[0])
        elif positions.shape[0] != excitations.shape[0]:
            raise ValueError(f'Expected positions and excitations to have same number of rows (antennas), found {positions.shape[0]} and {excitations.shape[0]} rows')
        self.excitations = excitations

        # TODO add an antenna object that can describe the antenna properties such as antenna rad pattern?
    
    @classmethod
    def empty(self):
        """Initialize an empty antenna array
        """
        return self(np.array((0,3)))
    
    def append(self, position, excitation=None):
        """Append a single antenna's position and excitation

        Args:
            position (nparray(n,3)): Array represention position [x, y, z] in wavelengths (can be any number of rows)
            excitation (nparray, optional): Complex number representing the excitation of the antenna. Defaults to None.
        """
        self.positions = np.vstack((self.positions, position))

        # TODO update this so it can handle appending multiple antennas at the same time
        if excitation is None:
            excitation = np.array([1])
        self.excitations = np.hstack((self.excitations, np.array(excitation)))

    def __repr__(self):
        return str(self.antennas)

    def arrayFactor(self, azimuth, elevation):
        """The most general form of the array factor calculation. No assumptions about the array or
           the range of azimuth/elevations is made.

           AF()

        Args:
            azimuth (float): _description_
            elevation (float): _description_

        Returns:
            nparray: _description_
        """
        # TODO all of this is completely wrong, fix it
        azimuth_grid, elevation_grid = np.meshgrid(azimuth, elevation)
        u_grid = np.sin(azimuth_grid / 180 * np.pi)
        v_grid = np.sin(elevation_grid/180*np.pi)

        AF = np.zeros(np.shape(u_grid), dtype=complex)

        for antenna in self.antennas:
            AF = AF + np.exp(-1j * 2 * np.pi * (antenna.x()*u_grid + antenna.y()*v_grid))

        return np.transpose(AF)

# TODO add more array variants (rectanglular array, circular array, sparce arrays, different simplifications)
