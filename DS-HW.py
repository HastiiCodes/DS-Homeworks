#سلام و عرض ادب استاد. من همورک های شماره 1 و 2 رو سر تایم خودش اپلود کرده بودم و ریپازیتوری اون ها توی پروفایلم جدا هست
#اما چون فرموده بودید همه رو توی یک ریپازیتوری اپلود کنیم من این ریپازیتوری را جدا ساختم
# و مجددا همورک هارو آپلود کردم




#HW 1: گرفتن عنصر i ام.

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

#HW3: مرتب سازی هرمی


def heapify(arr, n, i):
	largest = i 
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2
    
	if l < n and arr[i] < arr[l]:
		largest = l
	elif r < n and arr[largest] < arr[r]:
		largest = r
        
	elif largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i])
		heapify(arr, n, largest)
        
def heapSort(arr):
	n = len(arr)
	for i in range(n // 2, -1, -1):
		heapify(arr, n, i)
        
        for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		heapify(arr, i, 0)
            
arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
	print(arr[i])
