# BaekJoon 07/30 2022
# 2800 괄호 제거

from itertools import combinations
import copy

equation = list(input())
res = []

stack = []
bracket = []
for i in range(len(equation)):
    if equation[i] == "(":
        stack.append([i, "("])
    elif equation[i] == ")":
        bracket.append([stack.pop()[0], i])

combi = []
for i in range(1, len(bracket)+1):
    combi.extend(list(combinations(bracket, i)))

for c in combi:
    equation_copy = copy.deepcopy(equation)
    for i in range(len(c)):
        equation_copy[c[i][0]] = ""
        equation_copy[c[i][1]] = ""
    res.append("".join(equation_copy))

for r in sorted(list(set(res))):
    print(r)