class Book:

    def __init__(self, name, price, hight=10, width=20, weight=30):
        self.n = name
        self.p = price
        self.h = hight
        self.width= width
        self.weight = weight


a_input = int (input('please input a number:'))
if a_input == 1:
    print('this is a good one')
elif a_input ==2:
    print('See u next time')
else:
    print('good luck')

