import unittest
from player_reader import PlayerReader
from statistics_service import SortBy, StatisticsService
from player import Player

class PlayerReaderStub(PlayerReader):
    def __init__(self):
        pass

    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        # Search should return players by name
        self.assertIsNotNone(self.stats.search("Kurri"))
        # But not by team
        self.assertIsNone(self.stats.search("EDM"))

    def test_team(self):
        # Should return all players in "EDM"
        players_in_edm = self.stats.team("EDM")
        self.assertGreater(len(players_in_edm), 0)
        player_names_edm = [player.name for player in players_in_edm]
        self.assertEqual(player_names_edm, ["Semenko", "Kurri", "Gretzky"])

    def test_top_ranges(self):
        # Invalid how_many
        self.assertEqual([player.name for player in self.stats.top(-2)], [])
        self.assertEqual([player.name for player in self.stats.top(-1)], [])
        # Only one
        self.assertEqual([player.name for player in self.stats.top(0)], ["Gretzky"])
        # More
        self.assertEqual([player.name for player in self.stats.top(2)], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_by_points(self):
        self.assertEqual([player.name for player in self.stats.top(2, SortBy.POINTS)], ["Gretzky", "Lemieux", "Yzerman"])
    def test_top_by_goals(self):
        self.assertEqual([player.name for player in self.stats.top(2, SortBy.GOALS)], ['Lemieux', 'Yzerman', 'Kurri'])
    def test_top_by_assists(self):
        self.assertEqual([player.name for player in self.stats.top(2, SortBy.ASSISTS)], ['Gretzky', 'Yzerman', 'Lemieux'])
