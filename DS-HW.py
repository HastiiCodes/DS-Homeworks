#HW 1:

class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0

    def enqueue(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item

    def front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[self.first]

    def is_empty(self):
        return self.num == 0

    def size(self):
        return self.num

    def is_full(self):
        return self.num >= self.max_size

    def get_ith(self, i):
        if i < 0 or i >= self.num:
            raise Exception("Index out of range")
        return self.Q[(self.first + i) % self.max_size]
    
    
# HW 2:


polynomials = [] # this is a list to save polynomials.

while True:
    user_input = input("Enter number according to the instructions given: Input: 1, Sum: 2, Multiplied: 3, Print: 4, Exit program: 5")
    if user_input == '1':
        get_and_store_polynomial()
        print("Polynomial is saved.", polynomials)

    elif user_input == '2':
        if len(polynomials) > 1:
            add_and_simplify_polynomials()
        else:
            print("You must enter at least two polynomials.")

    elif user_input == '3':
        if len(polynomials) > 1:
            multiply_and_simplify_polynomials()
        else:
            print("You must enter at least two polynomials.")

    elif user_input == '4':
        if polynomials:
            print_polynomial()
        else:
            print("There is no polynomial to print.")

    elif user_input == '5':
        print("End of program. Until next time.")
        break
    else:
        print("Number is out of range.")