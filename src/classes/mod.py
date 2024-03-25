class Mod:
    """
    A class to describe a single mod for Hatsune Miku: Project DIVA Megamix+
    
    Attributes
    ----------
    name : str
        first name of the person
    author : str
        author of the mod
    verison : str
        verison number written as a string of the mod
    enabled : bool
        mod is enabled or disabled
    path : str
        path to the mod folder
    """

    def __init__(self, name : str, author: str, verison: str, enabled : bool, path : str) -> None:
        self._name : str = name
        self._author : str = author
        self._verison : str = verison
        self._enabled: bool = enabled
        self._path: str = path


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        self._name = value


    @property
    def author(self) -> str:
        return self._author
    
    @author.setter
    def author(self, value : str) -> None:
        self._author = value

    
    @property
    def verison(self) -> str:
        return self._verison
    
    @verison.setter
    def verison(self, value : str) -> None:
        self._verison = value
    

    @property
    def enabled(self) -> str:
        return self._enabled

    @enabled.setter
    def enabled(self, value) -> None:
        self._enabled = value


    @property
    def path(self) -> str:
        return self._path
    
    @enabled.setter
    def path(self, value) -> None:
        self._path = value
