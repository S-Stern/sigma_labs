def digitize(n):
    if not n:
        return [0]
    
    res = []
    while n:
        res.append(n % 10)
        n = n // 10
    return res