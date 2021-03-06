def tribonacci(signature, n):
    if n <= 3: return signature[:n]

    for _ in range(n-3):
        signature.append(sum(signature[-3:]))
    return signature
