from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    count = Counter(dice)
    items = list(count.items())

    if len(count) == 1:
        return 1111 * items[0][0]
    elif len(count) == 2:
        if items[0][1] == 3 or items[1][1] == 3:
            p = items[0][0] if items[0][1] == 3 else items[1][0]
            q = items[1][0] if items[0][1] == 3 else items[0][0]
            return (10 * p + q) ** 2
        else:
            p, q = items[0][0], items[1][0]
            return (p + q) * abs(p - q)
    elif len(count) == 3:
        for item in items:
            if item[1] == 2:
                p = item[0]
                break
        q, r = [item[0] for item in items if item[0] != p]
        return q * r
    else:
        return min(dice)