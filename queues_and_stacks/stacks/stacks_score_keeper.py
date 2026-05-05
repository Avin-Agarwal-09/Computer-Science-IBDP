def score_keeper(operator):
    stack = []
    for op in operator:
        if op == "+":
            stack.append(stack[-1]+stack[-2])
        elif op == "D":
            stack.append(2*stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)

op = ["5","-2","4","C","D","9","+","+"]
print(score_keeper(op))