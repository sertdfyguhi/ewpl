from sys import argv

def run(text):
    cell = 0
    toprint = ''
    e = False
    for idx, letter in enumerate(text):
        if letter == '>':
            toprint += chr(cell)
        elif letter == '<':
            toprint += (chr(cell) + '\n')
        elif letter == '+':
            cell += 1
        elif letter == '-':
            cell -= 1
        elif letter == '~':
            cell += 10
        elif letter == '=':
            cell -= 10
        elif letter == '/':
            toprint += str(cell)
        elif letter == '\\':
            toprint += (str(cell) + '\n')
        elif letter == '_':
            cell = 0
        else:
            print(f'{str(idx + 1)}: error')
            e = True
            break
    if e == False:
        print(toprint)

if len(argv) > 1:
    with open(argv[1], 'r') as f:
        text = f.read()
    run(text)
else:
    while True:
        text = input('> ')
        run(text)