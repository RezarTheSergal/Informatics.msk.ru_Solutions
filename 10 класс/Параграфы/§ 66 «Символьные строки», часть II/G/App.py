K, M, B = map(int, input().split())
N = int(input())
players = []

for i in range(N):
    surname, name, birth_year, goals = input().split()
    birth_year = int(birth_year)
    goals = int(goals)
    if K <= birth_year <= M and goals == B:
        players.append((surname, name))

for player in players:
    print(player[0], player[1])

print(len(players))
