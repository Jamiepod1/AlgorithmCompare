from tkinter import ttk

from algorithms import Algorithm
import tkinter as tk
import tkinter.ttk as ttk
import plotly.express as px


def main():
    algorithm = Algorithm()
    root = tk.Tk()
    root.title("Algorithm comparison")
    root.geometry("340x330")
    number_of_tests = tk.StringVar(value="100")
    repeats = tk.StringVar(value="5")
    frame = ttk.Frame(root)
    frame.pack()
    label1 = ttk.Label(frame, text="List length limit:")
    test_number_input_box = ttk.Entry(frame, textvariable=number_of_tests)
    label2 = ttk.Label(frame, text="Number of repeats:")
    repeats_input_box = ttk.Entry(frame, textvariable=repeats)
    label1.grid(row=0, column=0)
    test_number_input_box.grid(row=0, column=1)
    label2.grid(row=1, column=0)
    repeats_input_box.grid(row=1, column=1)
    create_checkboxes(root, algorithm, frame)
    button = ttk.Button(root, text="Run Tests",
                       command=lambda: run(int(number_of_tests.get()), int(repeats.get()), algorithm, progress, root))
    button.pack()
    progress = ttk.Progressbar(root, orient="horizontal",
                           length=100, mode='determinate')
    progress.pack()
    root.mainloop()


def create_checkboxes(root, algorithm, frame):
    checkboxes = []
    row = 2
    for test in algorithm.test_bank:
        checkbox_name = test.__name__
        checkbox_var = tk.BooleanVar()
        algorithm.test_bank[test] = checkbox_var
        checkbox = ttk.Checkbutton(
            frame,
            text=checkbox_name,
            variable=checkbox_var,
        )
        checkbox.grid(row=row, column=0, sticky="w")
        row += 1
        checkboxes.append(checkbox_var)


def run(number_of_tests, repeats, algorithm, progress, root):
    algorithm.generate_test_list(number_of_tests)
    total_test_number = 0
    for test in algorithm.test_bank:
        if algorithm.test_bank[test].get():
            total_test_number += 1
    results = {}
    current_test_number = 0
    tests_to_run = (test for test in algorithm.test_bank if algorithm.test_bank[test].get())
    root.after(100, run_test, number_of_tests, repeats, algorithm, progress, root, tests_to_run, results,
               current_test_number, total_test_number)


def run_test(number_of_tests, repeats, algorithm, progress, root, tests_to_run, results, current_test_number,
             total_test_number):
    try:
        test = next(tests_to_run)
        test_name = test.__name__
        x, y = algorithm.test(algorithm=test, number_of_tests=number_of_tests, repeats=repeats)
        results[test_name] = [x, y]
        current_test_number += 1
        progress["value"] = current_test_number / total_test_number * 100
        root.after(100, run_test, number_of_tests, repeats, algorithm, progress, root, tests_to_run, results,
                   current_test_number, total_test_number)
    except StopIteration:
        fig = px.scatter()
        for result in results.keys():
            fig.add_scatter(x=results[result][0], y=results[result][1], name=result, mode='markers')
        fig.update_xaxes(title_text="List length")
        fig.update_yaxes(title_text="Average time to sort (s)")
        fig.show()
        progress.stop()


if __name__ == "__main__":
    main()
