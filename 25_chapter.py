import re
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()



#
# stack = Stack()
# stack.push("hi")
# stack.push("hello")
# ze_popped_one = stack.pop()
# print(stack)
# print(ze_popped_one)
# ze_popped_one += stack.pop()
# print(stack.is_empty())
print(eval_postfix("56 47 + 2 *"))
print(eval_postfix("1 2 + 3 *"))
print(eval_postfix("2 3 * 1 +"))