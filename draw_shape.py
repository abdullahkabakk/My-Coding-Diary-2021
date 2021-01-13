import turtle
import time
def triangle(degree1=60,degree2=60,degree3=60,
             side_lengths1=10,side_lengths2=10,side_lengths3=10):
    turtle.fd(side_lengths1)
    turtle.lt(180-degree2)
    turtle.fd(side_lengths2)
    turtle.lt(180-degree1)
    turtle.fd(side_lengths3)
    turtle.lt(degree3)
    turtle.mainloop()
    


































def main():
    print('[1] TRIANGLE \t,[2] RECTANGLE \t,[3] SQUARE \t,[4] PENTAGON \t,'
          '[5] HEXAGON \t,[6] OCTAGON \t,[7] NONAGON \t,[8] DECAGON \t')
    print('WHICH SHAPE DO YOU WANT TO DRAW?')
    shape = input('>>>')
    shape = shape.lower()
    print('...')
    time.sleep(1)
    if shape == 'triangle' or shape == '1':
        while True:
            degrees1 = int(input('Input your triangle\'s FIRST degree(if you press enter '
                             'degree will be 60 automaticlly:'))
            degrees2 = int(input('Input your triangle\'s SECOND degree(if you press enter '
                             'degree will be 60 automaticlly:'))
            degrees3 = int(input('Input your triangle\'s THIRD degree(if you press enter '
                             'degree will be 60 automaticlly):'))
            side_length1 = int(input("Input your triangle's FIRST side's length"
                                     "(if you press enter side's length will be 10 automaticlly):"))
            side_length2 = int(input("Input your triangle's SECOND side's length"
                                     "(if you press enter side's length will be 10 automaticlly):"))
            side_length3 = int(input("Input your triangle's THIRD side's length"
                                     "(if you press enter side's length will be 10 automaticlly):"))
            if degrees1+degrees2+degrees3 == 180 and \
                    0 < degrees3 < 179 and \
                    0 < degrees1 < 179 and \
                    0 < degrees2 < 179 and \
                    abs(side_length1 - side_length2) < side_length3 <\
                    side_length1 + side_length2 and \
                    abs(side_length1 - side_length3) < side_length2 <\
                    side_length1 + side_length3 and \
                    abs(side_length3 - side_length2) < side_length1 <\
                    side_length2 + side_length3:
                        degree_list = [degrees1, degrees2, degrees3]
                        degree_list  = degree_list.sort()
                        side_length_list = [side_length1, side_length2, side_length3]
                        side_length_list = side_length_list.sort()
                        triangle(degree_list[2],degree_list[1],degree_list[0],
                                 side_length_list[1],side_length_list[0],side_length_list[2])
            else:
                print('INVALID DEGREES  OR SIDE LENGTH\'S. PLEASE TRY AGAIN!')




main()