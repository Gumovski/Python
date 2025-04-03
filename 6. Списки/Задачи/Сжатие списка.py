print(*sorted(list(map(int, input().split())), key=lambda x: x if x == 0 else float('inf'), reverse=True))
