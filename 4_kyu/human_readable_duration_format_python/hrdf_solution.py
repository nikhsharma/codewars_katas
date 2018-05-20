def format_duration(seconds):
    res = []
    for value in 31536000, 86400, 3600, 60:
        x = (seconds//value)
        res.append(x)
        seconds -= x*value

    times = [str(res[0]) +" years",
    str(res[1]) + " days",
    str(res[2]) + " hours",
    str(res[3]) + " minutes",
    str(seconds) + " seconds"]

    results = []
    for result in times:
        if result[0] is "0":
            continue
        if result[0] is "1" and result[1] is " ":
            results.append(result[:-1])
        else: results.append(result)

    if len(results) is 1: return results[0]
    elif len(results) is 0: return "now"
    else: return ", ".join(results[:-1]) + " and " + results[-1]
