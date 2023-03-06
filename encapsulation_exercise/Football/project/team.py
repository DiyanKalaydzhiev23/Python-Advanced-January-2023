from typing import List
from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)

        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str or Player:
        try:
            player = next(filter(lambda p: p.name == player_name, self.__players))
        except StopIteration:
            return f"Player {player_name} not found"

        self.__players.remove(player)

        return player
