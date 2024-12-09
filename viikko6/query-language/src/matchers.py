from abc import ABC, abstractmethod
from player import Player

# Abstract class for common functionality of matchers
# In other languages this could be considered an "interface" or "trait"
class Matcher(ABC):
    @abstractmethod
    def test(self, player: Player) -> bool:
        pass

class And(Matcher):
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn(Matcher):
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast(Matcher):
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
