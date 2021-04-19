def solution(N, trust) -> int:
    if not trust:
        return N
    res = {}
    tmp = []
    for t in trust:
        tmp.append(t[0])
        if t[1] not in res:
            res[t[1]] = 1
        else:
            res[t[1]] += 1
    for k in res:
        if res[k] == N - 1 and k not in tmp:
            return k
    return -1
