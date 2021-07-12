N = int(input())
expr = list(input())

dic = {}
for i in range(N):
    dic[chr(65+i)] = int(input())

for i in range(len(expr)):
    if 65 <= ord(expr[i]) <= 90:
        expr[i] = dic[expr[i]]

expr.reverse()
stack = []
while len(expr) != 0:
    stack.append(expr.pop())
    if len(stack) != 0 and stack[-1] in ['+', '-', '/', '*']:
        otr = stack.pop()
        op2 = stack.pop()
        op1 = stack.pop()
        if otr == '+':
            stack.append(op1+op2)
        elif otr == '-':
            stack.append(op1-op2)
        elif otr == '/':
            stack.append(op1/op2)
        elif otr == '*':
            stack.append(op1*op2)

print(format(stack[-1], ".2f"))