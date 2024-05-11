import re


class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = e
        else:
            raise Exception("Stack overflow")

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            raise Exception("Stack underflow")

    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        else:
            return None


def remove_strings_and_comments(code):
    pattern = r'''
        (\"\"\"|\'\'\')  
        .*?             
        (\"\"\"|\'\'\')  
        |               
        (\"|\')         
        .*?             
        (\2)            
        |               
        \#[^\n]*        
    '''
    return re.sub(pattern, "", code, flags=re.VERBOSE | re.DOTALL)


def check_bracket(statement):
    statement = remove_strings_and_comments(statement)

    stack = ArrayStack(len(statement))
    line_counter = 0
    for line in statement.split('\n'):
        line_counter += 1
        char_counter = 0
        for ch in line:
            char_counter += 1
            if ch in "{[(":
                stack.push((ch, line_counter, char_counter))

            elif ch in "}])":
                if stack.is_empty():
                    return (1, line_counter, char_counter)
                else:
                    left, l_line, l_char = stack.pop()
                    if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "("):
                        return (2, line_counter, char_counter)

    if not stack.is_empty():
        _, l_line, l_char = stack.peek()
        return (1, l_line, l_char)
    return (0, 0, 0)


def check_file_brackets(filename):
    error_code_dict = {
        0: "괄호 매칭이 성공적.",
        1: "왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 다름.",
        2: "같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 함을 위반.",
        3: "서로 다른 타입의 괄호 쌍이 서로를 교차함."
    }

    with open(filename, 'r') as file:
        content = file.read()
        error_code, line, char = check_bracket(content)
        if error_code != 0:
            print(f"에러 : {error_code_dict[error_code]}, 라인수 : {line}, 문자수 : {char}")
        else:
            print("에러 없음.")
