from enum import Enum
from player import Player
from player_reader import PlayerReader

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader: PlayerReader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many: int, sort_by: SortBy = SortBy.POINTS):
        def player_sorter(player: Player):
            match sort_by:
                case SortBy.GOALS:
                    return player.goals
                case SortBy.ASSISTS:
                    return player.assists
            return player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=player_sorter
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
