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
