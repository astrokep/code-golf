# BASIC ATTEMPT
# Initial Conditions:
# s = [0, 2, 3]

# for N in range(3,30):
#     print((s[N-2] + s[N-1])*(N%2^1) + (s[N-1] * 2 + s[N-2])*(N%2))
#     if N%2 == 0:
#         s.append(s[N-2] + s[N-1])
#     else:
#         s.append(s[N-1] * 2 + s[N-2])
# l = zip(list(range(len(s))), s)
# print(*l, sep='\n')

# NON-BRANCHING LOGIC 
# s = [0, 2, 3]
# for N in range(3, 30):
#     a=s[N-1]
#     b=s[N-2]
#     s.append(b+(a*(N%2^1)+a*2*(N%2))) 
# print(*s, sep='\n')


# GOLF ENTRY:
s = [0, 2, 3]
for N in range(3,30):a=s[N-1];b=s[N-2];s.append(b+(a*(N%2^1)+a*2*(N%2)))
print(*s,sep="\n")