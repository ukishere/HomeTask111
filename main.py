class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

def check_stack(test_string):

    stack.stack = []
    for string in test_string:
        if stack.size() == 0:
            stack.push(string)
        else:
            if stack.peek() == '(' and string  == ')':
                stack.pop()
            elif stack.peek() == '[' and string  == ']':
                stack.pop()
            elif stack.peek() == '{' and string == '}':
                stack.pop()
            else:
                stack.push(string)

    if stack.isEmpty():
        return 'сбалансирован'
    else:
        return 'несбалансирован'

if __name__ == '__main__':

    stack = Stack()

    # Примеры из домашнего задания
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

    # Пример для полноты картины
    test_string = '[(])'
    print(f'Стек {test_string} {check_stack(test_string)}')