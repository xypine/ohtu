from abc import ABC, abstractmethod
from player import Player

# Abstract class for common functionality of matchers
# In other languages this could be considered an "interface" or "trait"
class Matcher(ABC):
    @abstractmethod
    def test(self, player: Player) -> bool:
        pass


class All(Matcher):
    def test(self, player: Player) -> bool:
        return True

class And(Matcher):
    def __init__(self, *matchers: Matcher):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Not(Matcher):
    def __init__(self, matcher: Matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)

class PlaysIn(Matcher):
    def __init__(self, team: str):
        self._team = team

    def test(self, player):
        return player.team == self._team

class HasAtLeast(Matcher):
    def __init__(self, value: int, attr: str):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan(Matcher):
    def __init__(self, value: int, attr: str):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
