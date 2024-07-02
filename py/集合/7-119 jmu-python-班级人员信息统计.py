a = set(str(input()))
b = set(map(str, input().split()))
join_acm = set(map(str, input().split()))
join_eng = set(map(str, input().split()))
trans_school = set(input())
print(f"Total: {len(a) + len(b)}")
print(f"Not in race: {sorted((a | b) - (join_acm | join_eng))}, num: {len((a | b) - (join_acm | join_eng))}")
print(f"All racers: {sorted(join_acm | join_eng)}, num: {len(join_acm | join_eng)}")
print(f"ACM + English: {sorted(join_acm & join_eng)}, num: {len(join_acm & join_eng)}")
print(f"Only ACM: {sorted(join_acm - join_eng)}")
print(f"Only English: {sorted(join_eng - join_acm)}")
print(f"ACM Or English: {sorted(join_acm ^ join_eng)}")
if not trans_school.isdisjoint(a):
    a.remove(*trans_school)
    print(sorted(a))
elif not trans_school.isdisjoint(b):
    b.remove(*trans_school)
    print(sorted(b))
else:
    pass
