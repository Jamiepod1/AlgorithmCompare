import random
import time
import numpy as np


class Algorithm():

    def __init__(self):
        self.test_bank = {
            self.big_O_of_n_control: None,
            self.py_sort: None,
            self.bubble_sort: None,
            self.selection_sort: None,
            self.insertion_sort: None,
            self.hope_sort: None,
            self.merge_sort: None,
            self.heapSort: None
        }
        self.number_of_algorithms = len(self.test_bank)
        self.test_dict = {}

    def test(self, algorithm, number_of_tests, repeats):
        results = []
        for test in range(1, number_of_tests + 1):
            sum_of_tests = []
            for repeat in range(0, repeats):
                sum_of_tests.append(self.timer(algorithm, (self.test_dict[test])))
            results.append(sum(sum_of_tests) / len(sum_of_tests))
        x = [number for number in range(1, number_of_tests + 1)]
        y = results
        return (x, y)

    def generate_test_list(self, number_of_tests=2):
        for number in range(1, number_of_tests + 1):
            test_list = [value for value in range(1, number + 2)]
            random.shuffle(test_list)
            self.test_dict[number] = test_list

    def timer(self, algorithm, arr):
        start_time = time.time()
        algorithm(arr)
        end_time = time.time()
        return end_time - start_time

    def regression_equation(self, a, x, b):
        return a * np.exp(b * x)

    def extrapolate(self, x, y, intended_number_of_tests, number_of_tests):
        y = [y_val + 1 for y_val in y]
        x = np.array(x)
        y = np.array(y)
        a, b = np.polyfit(x, np.log(y), 1)
        for x_value in range(number_of_tests + 1, intended_number_of_tests + 1):
            x = np.append(x, x_value)
            y = np.append(y, self.regression_equation(a=a, x=x_value, b=b))
        A = np.exp(a)
        B = b
        print(f"y = {A:.2f} * exp({B:.2f} * x)")
        return x, y

    def hope_sort(self, arr):
        sorted = False
        while not sorted:
            input = [element for element in arr]
            output = []
            for _ in range(0, len(arr)):
                random_index = random.randint(0, len(input) - 1)
                random_element = input.pop(random_index)
                output.append(random_element)
            sorted = True
            for index, element in enumerate(output):
                if index != 0:
                    if output[index - 1] > output[index]:
                        sorted = False
        return output

    def py_sort(self, arr):
        output = sorted(arr)
        return output

    def bubble_sort(self, arr):
        n = len(arr)
        swapped = True
        while swapped:
            swapped = False
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            n -= 1
        return arr

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            current = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > current:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current
        return arr

    def merge(self, left, right):
        output = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        output.extend(left[i:])
        output.extend(right[j:])

        return output

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr


        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
        return 0

    def heapSort(self, arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return 0

    def big_O_of_n_control(self, arr):
        n_steps = [element for element in arr]
        return 0





