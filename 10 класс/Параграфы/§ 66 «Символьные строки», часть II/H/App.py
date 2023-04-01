N = int(input())
players = []
m_goals = 0
for i in range(N):
    surname, name, birth_year, goals = input().split()
    birth_year = int(birth_year)
    goals = int(goals)
    if goals > m_goals:
        m_goals = goals
        players = []
    if goals == m_goals:
        players.append((surname, name, goals))


for player in players:
    print(player[0], player[1])

print(players[0][2])
