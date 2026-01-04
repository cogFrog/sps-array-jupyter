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
        positions = np.atleast_2d(positions)

        if len(positions.shape) != 2:
            raise ValueError(f'Expected 2D nparray, found {len(positions.shape)}D nparray')
        if positions.shape[1] != 3:
            raise ValueError(f'Expected 3 column nparray, found {positions.shape[1]} columns')
        self.positions = positions

        if excitations is None:
            excitations = np.ones(positions.shape[0])
        else:
            excitations = np.atleast_1d(excitations)
        
        if positions.shape[0] != excitations.shape[0]:
            print(f'{positions.shape} and {excitations.shape}')
            raise ValueError(f'Expected positions and excitations to have same number of rows (antennas), found {positions.shape[0]} and {excitations.shape[0]} rows')
        self.excitations = excitations

        # TODO add an antenna object that can describe the antenna properties such as antenna rad pattern?
    
    @classmethod
    def empty(self):
        """Initialize an empty antenna array
        """
        return self(np.empty([0,3]))
    
    def append(self, positions, excitations=None):
        """Append a single antenna's position and excitation

        Args:
            positions (nparray(n,3)): 1D or 2D array representing antenna positions to add. Each row is an antenna position [x, y, z]
            excitations (nparray, optional): Array of complex numbers representing the excitation of the antennas. Defaults to all 1's.
        """
        positions = np.atleast_2d(positions)

        self.positions = np.vstack((self.positions, positions))

        if excitations is None:
            excitations = np.ones(positions.shape[0])
        else:
            excitations = np.atleast_1d(excitations)

        if positions.shape[0] != excitations.shape[0]:
            print(f'{positions.shape} and {excitations.shape}')
            raise ValueError(f'Expected positions and excitations to have same number of rows (antennas), found {positions.shape[0]} and {excitations.shape[0]} rows')
        self.excitations = np.hstack((self.excitations, excitations))

    # TODO make something that looks pretty
    #def __repr__(self):

    def arrayFactor(self, theta, phi):
        """The most general form of the array factor calculation. No assumptions about the array or
           the range of thetas/phis is made.

        Args:
            theta (nparray): Array of theta angles to test in degrees
            phi (float): Array of phi angles to test in degrees

        Returns:
            nparray: _description_
        """
        # TODO all of this is completely wrong, fix it
        theta_grid, phi_grid = np.meshgrid(np.radians(theta), np.radians(phi))
        
        # ignoring this for now. try it later
        k = 2*np.pi*np.array([np.sin(theta_grid)*np.cos(phi_grid), np.sin(theta_grid)*np.sin(phi_grid), np.cos(theta_grid)])

        AF = np.zeros(np.shape(u_grid), dtype=complex)

        return np.transpose(AF)

# TODO add more array variants (rectanglular array, circular array, sparce arrays, different simplifications)
