def goodVsEvil(good, evil):
    goodworth = [1,2,3,3,4,10]
    evilworth = [1,2,2,2,3,5,10]
    goodres = []
    evilres = []
    for i in range(0, 6): goodres.append(int(good.split()[i]) * goodworth[i])
    for i in range(0, 7): evilres.append(int(evil.split()[i]) * evilworth[i])
    if sum(goodres) > sum(evilres): return 'Battle Result: Good triumphs over Evil'
    elif sum(evilres) > sum(goodres): return 'Battle Result: Evil eradicates all trace of Good'
    else: return 'Battle Result: No victor on this battle field'
