# s = "8" * 125
#
# while ("333" in s) or ("888" in s):
#     if "333" in s:
#         s.replace("333", "8", 1)
#     if "888" in s:
#         s.replace("888", "3", 1)
#
# print(s)

n1 = 125 % 8
n2 = n1 // 3
print(n1, n2)
print(n1 - (n2 * 3))
print("Ответ:", "3" * n2 + "8" * (n1 - (n2 * 3)))