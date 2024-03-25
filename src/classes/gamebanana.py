import requests

class GameBanana:


    _START_ENDPOINT : str = "https://api.gamebanana.com/docs/endpoints/"
    _GAME_ID : int = "16522"

    @staticmethod
    def get_new_mods() -> list[int]:
        """
        returns all new mods on the Gamebanana page for the game ID in a list of type int

        Returns
        -------
        type: list[int]
        """
        return [1, 2, 3]