import math
import matplotlib.pyplot as plt

class Gaussian():
    """
    Create Gaussian class for calculation and visualization of a Gaussian distribution.

    Attributes
        mean : float
            The mean value of the distribution data.
        std : float
            The standard deviation of the distribution data.
        data : list of float
            List of float numbers extracted from the data file.
    """

    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.std = sigma
        self.data = []

    def calculate_mean(self):
        """Function to calculate the mean of the data set.

        Returns:
            float: mean of the data set
        """
        avg = 1 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def read_data_file(self, filename, sample=True):
        """Read text file into a list.

        The file should contain one number (float) per line. The numbers are stored in the attribute data.
        Then the standard deviation and mean are calculated and stored in their attributes.

        Args:
            filename (string): The file path and name.

        Returns:
            None
        """
        with open(filename, 'r') as file:
            numbers = file.read().strip().split('\n')
            numbers = list(map(int, numbers))
        file.close()

        self.data = numbers
        self.mean = self.calculate_mean()