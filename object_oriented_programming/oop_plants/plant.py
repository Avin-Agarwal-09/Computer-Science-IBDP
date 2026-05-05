# Name of file: Plant.py

class Plant:

    def __init__(self, scientificName, scientificFamily, distribution, bloom):
        # private instance variables
        self.__scientificName = scientificName
        self.__scientificFamily = scientificFamily
        self.__distribution = distribution
        self.__bloom = bloom

    # getters
    def getScientificName(self):
        return self.__scientificName

    def getScientificFamily(self):
        return self.__scientificFamily

    def getDistribution(self):
        return self.__distribution

    def getBloom(self):
        return self.__bloom

    # string method (like toString in Java)
    def __str__(self):
        return (
            f"Scientific Name: {self.__scientificName}, "
            f"Scientific Family: {self.__scientificFamily}"
        )
