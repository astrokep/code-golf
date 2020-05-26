# CHALLENGE: Calculate the first 50 prime numbers

# GOLF ENTRY:
print(*filter(lambda i: {i % v : 0 for v in range(2,i)}.get(0,1), range(1,228)), sep='\n')