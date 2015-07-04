def duplicates(array):
    d = {}
    _dups = []
    for i,e in enumerate(array):
        if e in d:
            if e not in _dups:
                _dups.append(e)
        else:
            d[e] = i
    return _dups

print duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5'])
