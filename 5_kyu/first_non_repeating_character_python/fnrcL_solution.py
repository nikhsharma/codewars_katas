def first_non_repeating_letter(string):
    res = []
    for c in list(string.upper()): res.append(string.upper().count(c))
    if 1 in res: res = list(string)[res.index(1)]
    else: return ''
    return res[0]
