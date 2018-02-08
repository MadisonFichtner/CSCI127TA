def possible_scores(gp, earned):
    # determine initial combination of w-t-l
    wins = earned // 3
    ties = earned - wins * 3
    losses = gp - wins - ties

    while losses > -1:
        print(str(wins) + "-" + str(ties) + "-" + str(losses))

        # see if another combination is possible
        wins -= 1
        ties += 3
        losses = gp - wins - ties

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
