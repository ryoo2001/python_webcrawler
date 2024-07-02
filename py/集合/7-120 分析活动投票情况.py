l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
team_1 = set(map(str, l1))
team_2 = set(map(str, l2))
get_ticket = set(map(str, input().split(",")))
if not get_ticket.isdisjoint(team_2):
    no_get = team_2 - get_ticket
    print(*sorted(map(int, no_get)))
else:
    pass

