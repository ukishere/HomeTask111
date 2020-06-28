class Stack:

    def __init__(self):
        self.stack = ''

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        self.stack = self.stack + str(new_element)

    def pop(self):
        last_element = self.stack[len(self.stack)-1]
        self.stack = self.stack[0:len(self.stack)-1]
        return last_element

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

def check_stack(test_string):

    for string in test_string:
        stack.push(string)

    if stack.size()%2 != 0:
        return 'несбалонсирован'

    type1 = 0
    type2 = 0
    type3 = 0

    while stack.isEmpty() != True:
        test_item = stack.pop()
        if test_item == '(': type1 += 1
        elif test_item == ')': type1 -= 1
        elif test_item == '[': type2 += 1
        elif test_item == ']': type2 -= 1
        elif test_item == '{': type3 += 1
        elif test_item == '}': type3 -= 1

    if not type1 and not type2 and not type3:
        return 'сбалонсирован'
    else:
        return 'несбалонсирован'

if __name__ == '__main__':

    stack = Stack()
    test_string = '(((([{}]))))'
    print(f'Стек {test_string} {check_stack(test_string)}')
    test_string = '[([])((([[[]]])))]{()}'
    print(f'Стек {test_string} {check_stack(test_string)}')
    test_string = '{{[()]}}'
    print(f'Стек {test_string} {check_stack(test_string)}')
    test_string = '}{}'
    print(f'Стек {test_string} {check_stack(test_string)}')
    test_string = '{{[(])]}}'
    print(f'Стек {test_string} {check_stack(test_string)}')
    test_string = '[[{())}]'
    print(f'Стек {test_string} {check_stack(test_string)}')






