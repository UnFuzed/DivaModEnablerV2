import PyQt5
from  classes.mod import Mod

class DivaModEnabler:
    """
    A class to represent the program of DivaModEnabler

    Attributes
    ----------
    verison : str
        verison number written as a string of DivaModEnabler
    """

    def __init__(self, verison : str) -> None:
        self._verison: str = verison