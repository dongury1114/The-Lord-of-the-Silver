a = 2
b = 3

a = int(bin(a)[2:])
b = int(bin(b)[2:])

tmp_a = list(str(a))
tmp_b = list(str(b))
if tmp_b[0] == "1" and tmp_a[0] == "1":
    ans = str(a | b)
    tmp = ("0b" + ans)
    answer = int(tmp, 2)
    print(answer << 1)
# else:
#     ans = str(a | b)
#     tmp = "0b" + ans
#     print(int(tmp, 2) << 1)

# print(type(tmp_a[0]), type(tmp_b[0]))
