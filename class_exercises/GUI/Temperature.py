class Temperature:
    def __init__(self,celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, celsius: float):
        if celsius < -273.15:
            raise ValueError("Celsius must be >= -273.15")
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit: float):
        if self.fahrenheit < -459.67:
            raise ValueError("Fahrenheit must be greater than absolute 0")
        self._celsius = (fahrenheit - 32) * 5/9

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, kelvin: float):
        if kelvin < 0:
            raise ValueError("Kelvin must be >= 0")
        self._celsius = kelvin - 273.15

    @property
    def rankine(self) -> float:
        return self._celsius * 1.8 + 491.67

    @rankine.setter
    def rankine(self, rankine: float):
        if rankine < 0:
            raise ValueError("Rankine must be >= 0")
        self._celsius = (rankine - 491.67) * 5/9

    @property
    def romer(self) -> float:
        return self._celsius * 21/40 + 7.5

    @romer.setter
    def romer(self, romer: float):
        if romer < 0:
            raise ValueError("Romer must be >= 0")
        self._celsius = (romer - 7.5) * 40/21


if __name__ == "__main__":
    temp = Temperature(celsius=55)
    print(temp.celsius)
    print(temp.fahrenheit)
    print(temp.kelvin)
    print(temp.rankine)
    print(temp.romer)
    temp.fahrenheit = 72
    print(temp.celsius)
    print(temp.fahrenheit)
    print(temp.kelvin)
    print(temp.rankine)
    print(temp.romer)