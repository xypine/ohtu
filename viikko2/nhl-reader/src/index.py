import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)


    players_fin = filter(lambda p: p.nationality == "FIN", players)
    players_fin = sorted(players_fin, key=lambda l: -l.points)

    print("Players from FIN\n")
    for player in players_fin:
        print(player)

if __name__ == "__main__":
    main()
