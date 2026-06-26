import cupy as cp
import numpy as np

class AntennaArray:
    """Basic array of identical antennas, minimal assumptions
    """    
    def __init__(self, positions, excitations=None):
        """Initialize antenna array with N antenna positions and excitations

        Args:
            positions (cparray(N, 3)): 2D array representing position of all antennas in wavelengths. Each row is an antenna position [x, y, z]
            excitations (cparray(N)): Array of complex #s representing excitation of each antenna. If None, defaults to all 1's
        """
        positions = cp.atleast_2d(positions)

        if len(positions.shape) != 2:
            raise ValueError(f'Expected 2D cparray, found {len(positions.shape)}D cparray')
        if positions.shape[1] != 3:
            raise ValueError(f'Expected 3 column cparray, found {positions.shape[1]} columns')
        self.positions = positions

        if excitations is None:
            self.excitations = cp.ones(positions.shape[0])
        else:
            self.excitations = cp.atleast_1d(excitations)
        
        if positions.shape[0] != self.excitations.shape[0]:
            print(f'{positions.shape} and {self.excitations.shape}')
            raise ValueError(f'Expected positions and excitations to have same number of rows (antennas), found {positions.shape[0]} and {excitations.shape[0]} rows')
    
    @classmethod
    def empty(self):
        """Initialize an empty antenna array
        """
        return self(cp.empty([0,3]))

    @classmethod
    def uniformRectArray(self, xSize, ySize, spacing):
        """Initialize a rectangular antenna array
        """
        xVals = cp.arange(xSize) * spacing
        yVals = cp.arange(ySize) * spacing
        x, y = cp.meshgrid(xVals, yVals)
        array = cp.vstack([x.ravel(), y.ravel(), cp.zeros(xSize*ySize)])
        return self(array.T)

    def append(self, positions, excitations=None):
        """Append a single antenna's position and excitation

        Args:
            positions (cparray(n,3)): 1D or 2D array representing antenna positions to add. Each row is an antenna position [x, y, z]
            excitations (cparray, optional): Array of complex numbers representing the excitation of the antennas. Defaults to all 1's.
        """
        positions = cp.atleast_2d(positions)

        self.positions = cp.vstack((self.positions, positions))

        if excitations is None:
            excitations = cp.ones(positions.shape[0])
        else:
            excitations = cp.atleast_1d(excitations)

        if positions.shape[0] != excitations.shape[0]:
            print(f'{positions.shape} and {excitations.shape}')
            raise ValueError(f'Expected positions and excitations to have same number of rows (antennas), found {positions.shape[0]} and {excitations.shape[0]} rows')
        self.excitations = cp.hstack((self.excitations, excitations))

    # TODO make something that looks pretty
    #def __repr__(self):

    def arrayFactor(self, theta, phi):
        """The most general form of the array factor calculation. No assumptions about the array or
           the range of thetas/phis is made.

        Args:
            theta (cparray): Array of theta angles to test in degrees
            phi (float): Array of phi angles to test in degrees

        Returns:
            cparray: _description_
        """
        if type(theta) == np.ndarray:
            theta = cp.array(theta)
        if type(phi) == np.ndarray:
            phi = cp.array(phi)

        # create pairs of every theta/phi combination
        theta_grid, phi_grid = cp.meshgrid(cp.radians(theta), cp.radians(phi))
        
        # Calculate wavenumber (in 3D) for every theta/phi combination
        k = 2*cp.pi*cp.array([cp.sin(phi_grid)*cp.cos(theta_grid),
                              cp.sin(phi_grid)*cp.sin(theta_grid),
                              cp.cos(phi_grid)])
        k = cp.transpose(k, axes=[1,2,0])

        # Calculate the AF itself (one big operation, using dot product to perform sum of products)
        af = cp.dot(cp.exp(-1j * cp.dot(k, self.positions.T)), self.excitations)

        return af

# TODO add more array variants (rectanglular array, circular array, sparce arrays, different simplifications)
