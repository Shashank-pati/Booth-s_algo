# Booth's Algorithm Simulator

## Overview
This is a Python-based graphical user interface (GUI) application that simulates Booth's Multiplication Algorithm using Tkinter. It allows users to enter a multiplicand and a multiplier, and it provides a step-by-step breakdown of the Booth multiplication process, including binary representations and intermediate calculations.

## Features
- Converts decimal inputs into binary using two's complement representation.
- Implements Booth's Algorithm for signed integer multiplication.
- Displays each step of the multiplication process.
- Provides both binary and decimal results.
- Simple and interactive Tkinter-based UI.

## Requirements
- Python 3.x
- Tkinter (included in standard Python installation)

## How to Run
1. Download or copy the `booth_multiplication.py` script.
2. Open a terminal or command prompt and navigate to the script location.
3. Run the script using the command:
   ```sh
   python booth_multiplication.py
   ```
4. Enter the multiplicand and multiplier in the input fields.
5. Click the "Calculate" button to execute Booth's Algorithm.
6. View the step-by-step results in the output box.

## Code Explanation
- **decimal_to_binary(n, bits=8)**: Converts a decimal number to its binary representation using two's complement.
- **booth_multiplication(multiplicand, multiplier, bits=8)**: Implements Booth's Algorithm for signed multiplication.
  - Initializes registers: Accumulator (A), Multiplier (Q), and Q-1.
  - Iterates for `bits` cycles, performing operations based on Q and Q-1 values.
  - Performs arithmetic right shifts to update A, Q, and Q-1.
  - Outputs step-by-step results in binary and decimal forms.
- **calculate()**: Retrieves user input, computes multiplication, and displays the results in the Tkinter text box.
- **Tkinter GUI**: Provides input fields, a calculation button, and a text area for displaying results.

## Example
### Input:
```
Multiplicand (M) = 5
Multiplier (Q) = -3
```
### Output (Simplified Example):
```
Step 1:
A: 00000000  Q: 11111101  Q-1: 0
-> Subtract M: A = 11111011
...
Final result (Binary): 11111001
Final result (Decimal): -15
```

## Author
Shashank Pati Tripathi

## License
This project is open-source and available for educational purposes.

