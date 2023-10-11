# Інкапсуляція
class Kettle:
    def enable(self):
        self.__power_on()
        self.__enable_ten()
        self.__check_temperature()
        self._power_off()

PUBLIC
PRIVATE #приватні методи які видно лише в середині def __enable...
PROTECTED #
    def enable_ten(self):


    pass
    def check_temperature(self):
    def power_off(self):