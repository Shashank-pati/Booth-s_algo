import tkinter as tk
from tkinter import messagebox

def decimal_to_binary(n, bits=8):
    """Converts a decimal number to a binary string with two's complement representation."""
    if n < 0:
        return format((1 << bits) + n, f'0{bits}b')
    return format(n, f'0{bits}b')

def booth_multiplication(multiplicand, multiplier, bits=8):
    """Performs Booth's multiplication algorithm step by step."""
    A = 0  # Accumulator
    Q = multiplier  # Multiplier
    M = multiplicand  # Multiplicand
    Q_1 = 0  # Q-1 (initialized to 0)
    count = bits  # Number of bits for processing
    
    steps = []
    steps.append(f"Multiplicand (M): {decimal_to_binary(M, bits)} ({M})")
    steps.append(f"Multiplier (Q):   {decimal_to_binary(Q, bits)} ({Q})")
    steps.append("\nStep-by-step process:")
    
    while count > 0:
        step_text = f"\nStep {bits - count + 1}:\n"
        step_text += f"A: {decimal_to_binary(A, bits)}  Q: {decimal_to_binary(Q, bits)}  Q-1: {Q_1}\n"
        
        if (Q & 1 == 1 and Q_1 == 0):
            A = A - M  # A = A - M
            step_text += f"  -> Subtract M: A = {decimal_to_binary(A, bits)}\n"
        elif (Q & 1 == 0 and Q_1 == 1):
            A = A + M  # A = A + M
            step_text += f"  -> Add M: A = {decimal_to_binary(A, bits)}\n"
        
        # Arithmetic Right Shift (ARS)
        combined = (A << (bits + 1)) | (Q << 1) | Q_1  # Merge A, Q, and Q-1
        combined >>= 1  # Shift Right
        
        A = (combined >> (bits + 1)) & ((1 << bits) - 1)  # Extract new A
        Q = (combined >> 1) & ((1 << bits) - 1)  # Extract new Q
        Q_1 = combined & 1  # Extract new Q-1
        
        steps.append(step_text)
        count -= 1
    
    steps.append(f"\nFinal Result: A: {decimal_to_binary(A, bits)}  Q: {decimal_to_binary(Q, bits)}")
    result = (A << bits) | Q
    if result >= (1 << (2 * bits - 1)):
        result -= (1 << (2 * bits))  # Convert from two's complement
    
    steps.append(f"Final result (Binary): {decimal_to_binary(result, bits * 2)}")
    steps.append(f"Final result (Decimal): {result}")
    return "\n".join(steps)

def calculate():
    try:
        multiplicand = int(entry_m.get())
        multiplier = int(entry_q.get())
        max_bits = max(multiplicand.bit_length(), multiplier.bit_length()) + 1
        result = booth_multiplication(multiplicand, multiplier, max_bits)
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers")

# Create UI
root = tk.Tk()
root.title("Booth's Algorithm Simulator")

tk.Label(root, text="Enter Multiplicand (M):").grid(row=0, column=0)
entry_m = tk.Entry(root)
entry_m.grid(row=0, column=1)

tk.Label(root, text="Enter Multiplier (Q):").grid(row=1, column=0)
entry_q = tk.Entry(root)
entry_q.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2)

text_output = tk.Text(root, height=20, width=50)
text_output.grid(row=3, column=0, columnspan=2)

root.mainloop()
