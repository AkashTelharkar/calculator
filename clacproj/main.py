import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the input and output
        entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 20), justify='right')
        entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 16),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear button
        tk.Button(self.master, text="C", padx=20, pady=20, font=('Arial', 16), command=self.clear_entry).grid(row=row_val, column=col_val)

    def on_button_click(self, value):
        current = self.result_var.get()
        if value == '=':
            try:
                result = eval(current)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current + value)

    def clear_entry(self):
        self.result_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
