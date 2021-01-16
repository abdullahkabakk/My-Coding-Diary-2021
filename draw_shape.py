import turtle
import time


def triangle(degree1=60, degree2=60, degree3=60,
             side_lengths1=10, side_lengths2=10, side_lengths3=10):
    degree_list = [degree2, degree1, degree3]
    side_length_list = [side_lengths1, side_lengths2, side_lengths3]
    for i in range(3):
        turtle.fd(side_length_list[i])
        turtle.lt(180-degree_list[i])
    turtle.mainloop()


def triangle_rules():
    while True:
        try:
            degrees1 = int(input('Input your triangle\'s FIRST degree(if you press enter '
                                 'degree will be 60 automatically:'))
            if degrees1 == '':
                degrees1 = 60
            degrees2 = int(input('Input your triangle\'s SECOND degree(if you press enter '
                                 'degree will be 60 automatically:'))
            if degrees2 == '':
                degrees2 = 60
            degrees3 = int(input('Input your triangle\'s THIRD degree(if you press enter '
                                 'degree will be 60 automatically):'))
            if degrees3 == '':
                degrees3 = 60
            side_length1 = int(input("Input your triangle's FIRST side's length"
                                     "(if you press enter side's length will be 10 automatically):"))
            if side_length1 == '':
                side_length1 = 10
            side_length2 = int(input("Input your triangle's SECOND side's length"
                                     "(if you press enter side's length will be 10 automatically):"))
            if side_length2 == '':
                side_length2 = 10
            side_length3 = int(input("Input your triangle's THIRD side's length"
                                     "(if you press enter side's length will be 10 automatically):"))
            if side_length3 == '':
                side_length3 = 60
            if degrees1 + degrees2 + degrees3 == 180 and \
                    0 < degrees3 < 179 and \
                    0 < degrees1 < 179 and \
                    0 < degrees2 < 179 and \
                    abs(side_length1 - side_length2) < side_length3 < \
                    side_length1 + side_length2 and \
                    abs(side_length1 - side_length3) < side_length2 < \
                    side_length1 + side_length3 and \
                    abs(side_length3 - side_length2) < side_length1 < \
                    side_length2 + side_length3:

                degree_list = [degrees1, degrees2, degrees3]
                degree_list = sorted(degree_list, reverse=False)
                side_length_list = [side_length1, side_length2, side_length3]
                side_length_list = sorted(side_length_list, reverse=False)
                triangle(degree_list[2], degree_list[1], degree_list[0],
                         side_length_list[1], side_length_list[0], side_length_list[2])
        except ValueError:
            print('Hit')
        else:
            print('INVALID DEGREES  OR SIDE LENGTH\'S. PLEASE TRY AGAIN!')


def rectangle():
    try:
        short_side = int(input('>>> INPUT SHORT SIDE\'S LENGTH:'))
        long_side = int(input('>>> INPUT LONG SIDE\'S LENGTH:'))
        for i in range(2):
            turtle.fd(short_side)
            turtle.lt(90)
            turtle.fd(long_side)
            turtle.lt(90)
        turtle.mainloop()
    except ValueError:
        print('Please input "NUMBER". TRY AGAIN!')


def square():
    try:
        side_length = int(input('>>> INPUT SIDE\'S LENGTH:'))
        for i in range(4):
            turtle.fd(side_length)
            turtle.lt(90)
            turtle.mainloop()
            time.sleep(10)
    except ValueError:
        print('Please input "NUMBER". TRY AGAIN!')


def pentagon():
    try:
        side_length = int(input('>>> INPUT SIDE\'S LENGTH:'))
        for i in range(5):
            turtle.fd(side_length)
            turtle.lt(72)
        turtle.mainloop()
    except ValueError:
        print('Please input "NUMBER". TRY AGAIN!')


def hexagon():
    try:
        side_length = int(input('>>> INPUT SIDE\'S LENGTH:'))
        for i in range(6):
            turtle.fd(side_length)
            turtle.lt(60)
        turtle.mainloop()
    except ValueError:
        print('Please input "NUMBER". TRY AGAIN!')


def octagon():
    try:
        side_length = int(input('>>> INPUT SIDE\'S LENGTH:'))
        for i in range(8):
            turtle.fd(side_length)
            turtle.lt(45)
        turtle.mainloop()
    except ValueError:
        print('Please input "NUMBER". TRY AGAIN!')


def nonagon():
    try:
        side_length = int(input('>>> INPUT SIDE\'S LENGTH:'))
        for i in range(9):
            turtle.fd(side_length)
            turtle.lt(40)
        turtle.mainloop()
    except ValueError:
        print('Please input "NUMBER". TRY AGAIN!')


def decagon():
    try:
        side_length = int(input('>>> INPUT SIDE\'S LENGTH:'))
        for i in range(10):
            turtle.fd(side_length)
            turtle.lt(36)
        turtle.mainloop()
    except ValueError:
        print('Please input "NUMBER". TRY AGAIN!')


def main():
    print('[1] TRIANGLE \t [2] RECTANGLE \t [3] SQUARE \t [4] PENTAGON \t \n'
          '[5] HEXAGON \t [6] OCTAGON \t [7] NONAGON \t [8] DECAGON \t')
    print('WHICH SHAPE DO YOU WANT TO DRAW? (YOU EITHER CAN WRITE THE NUMBER OR THE WORD)')
    shape = input('>>>')
    shape = shape.lower()
    print('...')
    time.sleep(1)
    if shape == 'triangle' or shape == '1':
        triangle_rules()
    elif shape == 'rectangle' or shape == '2':
        rectangle()
    elif shape == 'square' or shape == '3':
        square()
    elif shape == 'pentagon' or shape == '4':
        pentagon()
    elif shape == 'hexagon' or shape == '5':
        hexagon()
    elif shape == 'octagon' or shape == '6':
        octagon()
    elif shape == 'nonagon' or shape == '7':
        nonagon()
    elif shape == 'decagon' or shape == '8':
        decagon()
    else:
        print('PLEASE WRITE INVALID NUMBER OR WORD!')


main()
