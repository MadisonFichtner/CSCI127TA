def possible_scores(numPlayed, ptsEarned):
    # determine initial number of w-t-l
    wins = ptsEarned // 3
    ties = ptsEarned - wins * 3
    losses = numPlayed - wins - ties

    print(wins,"-",ties,"-",losses)

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    possible_scores(games_played, points_earned)
    print()

def process_seasons(seasons):
    for i in range(len(seasons)):
        process_season(i+1, seasons[i][0], seasons[i][1])

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]
    process_seasons(soccer_seasons)

main()
