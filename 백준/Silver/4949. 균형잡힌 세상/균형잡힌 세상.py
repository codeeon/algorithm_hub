pair = {
    ')' : '(',
    ']' : '[',
}
opener = '(['
closer = ')]'

while True:
    case = input()
    if case and case == '.':
        break

    stack = []
    result = True

    for char in case:
        if char in opener:
            stack.append(char)
        elif char in closer:
            if not stack:
                result = False
                break
            top = stack.pop()
            if pair[char] != top:
                result = False
            
    if result == False or len(stack) > 0:
        print('no')
    else:
        print('yes')