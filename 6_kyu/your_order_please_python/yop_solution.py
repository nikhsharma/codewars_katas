def order(sentence):
    res = []
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word: res.append(word)
    return " ".join(res)
