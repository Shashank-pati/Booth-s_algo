import tkinter as tk
from tkinter import messagebox

def decimal_to_binary(n, bits=8):
    if n < 0:
        n = (1 << bits) + n  # Two's complement
    return format(n, f'0{bits}b')

def binary_to_decimal(b):
    if b[0] == '1':  # Negative number in two's complement
        return -((1 << len(b)) - int(b, 2))
    return int(b, 2)

def add_binary(a, b, bits):
    result = bin(int(a, 2) + int(b, 2))[2:].zfill(bits + 1)
    return result[-bits:]  # Truncate to required bits

def booth_algorithm(multiplicand, multiplier, bits=8):
    M = decimal_to_binary(multiplicand, bits)
    Q = decimal_to_binary(multiplier, bits)
    A = '0' * bits
    Q_1 = '0'
    count = bits

    steps = []  # List to store step-wise process
    steps.append(f"Initial Values: A={A}, Q={Q}, Q-1={Q_1}, M={M}\n")

    while count > 0:
        steps.append(f"Step {bits - count + 1}: A={A}, Q={Q}, Q-1={Q_1}")
        if Q[-1] + Q_1 == '10':
            A = add_binary(A, decimal_to_binary(-multiplicand, bits), bits)
            steps.append(f"  - Subtract M: A={A}")
        elif Q[-1] + Q_1 == '01':
            A = add_binary(A, decimal_to_binary(multiplicand, bits), bits)
            steps.append(f"  - Add M: A={A}")
        
        # Arithmetic right shift
        A_Q_Q1 = A + Q + Q_1
        A_Q_Q1 = A_Q_Q1[0] + A_Q_Q1[: -1]  # Preserve sign bit
        A, Q, Q_1 = A_Q_Q1[:bits], A_Q_Q1[bits:-1], A_Q_Q1[-1]
        steps.append(f"  - Arithmetic Right Shift: A={A}, Q={Q}, Q-1={Q_1}\n")
        count -= 1
    
    result = binary_to_decimal(A + Q)
    steps.append(f"Final Result: A={A}, Q={Q}, Decimal={result}")
    return result, '\n'.join(steps)

def calculate():
    try:
        multiplicand = int(entry_multiplicand.get())
        multiplier = int(entry_multiplier.get())
        bits = max(len(bin(abs(multiplicand))) - 2, len(bin(abs(multiplier))) - 2, 8)
        result, steps = booth_algorithm(multiplicand, multiplier, bits)
        label_result.config(text=f"Result: {result}")
        text_steps.delete("1.0", tk.END)
        text_steps.insert(tk.END, steps)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers")

# GUI Setup
root = tk.Tk()
root.title("Booth's Algorithm Multiplier")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Multiplicand:").grid(row=0, column=0)
entry_multiplicand = tk.Entry(frame)
entry_multiplicand.grid(row=0, column=1)

tk.Label(frame, text="Multiplier:").grid(row=1, column=0)
entry_multiplier = tk.Entry(frame)
entry_multiplier.grid(row=1, column=1)

tk.Button(frame, text="Calculate", command=calculate).grid(row=2, columnspan=2)
label_result = tk.Label(frame, text="Result:")
label_result.grid(row=3, columnspan=2)

text_steps = tk.Text(frame, height=10, width=50)
text_steps.grid(row=4, columnspan=2)

root.mainloop()
