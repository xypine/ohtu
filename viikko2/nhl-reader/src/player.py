import requests

class Player:
    def __init__(self, dict):
        self.id = dict['id']
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team}  {self.goals:2} + {self.assists:2} = {self.points}"

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        # print("JSON-muotoinen vastaus:")
        # print(response)

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        self.players = players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players_nat = filter(lambda p: p.nationality == nationality, self.reader.players)
        players_nat = sorted(players_nat, key=lambda l: -l.points)
        return players_nat
