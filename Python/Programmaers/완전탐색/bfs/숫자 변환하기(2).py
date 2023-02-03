from collections import defaultdict, deque

def solution(x, y, n):
    if x == y: return 0
    queue = deque([[x, 0]])
    duplication = defaultdict(lambda: 0)

    while queue:
        x, cnt = queue.popleft()
        cnt += 1
        
        if duplication[x] == 1:
            continue
        else:
            duplication[x] = 1

        if x + n < y:
            queue.append([x + n, cnt])
        elif x + n == y:
            return cnt

        if 2 * x < y:
            queue.append([2 * x, cnt])
        elif 2 * x == y:
            return cnt

        if 3 * x < y:
            queue.append([3 * x, cnt])
        elif 3 * x == y:
            return cnt

    return -1