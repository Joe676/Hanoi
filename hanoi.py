def counter():
    x = 0
    while True:
        yield x
        x += 1

c = counter()

def move(fr, to):
    print('Move a disc from {} to {}'.format(fr, to))
    next(c)

def move_through(fr, th, to):
    move(fr, th)
    move(th, to)

def hanoi(n, fr, he, to):
    if n==0:
        pass
    else:
        hanoi(n-1, fr, to, he)
        move(fr, to)
        hanoi(n-1, he, fr, to)

if __name__ == "__main__":
    ok = False
    while not ok:
        ok = True
        try:
            number = int(input('How many discs would you like to move?'))
        except ValueError:
            print('Only whole numbers are valid!')
            ok = False
    hanoi(number, 'A', 'B', 'C')
    print("That's been {} moves!".format(next(c)))