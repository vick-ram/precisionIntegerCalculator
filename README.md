# Arbitrary Precision Integer Calculator
This project implements an arbitrary precision integer calculator. It's built from scratch, without relying on any external libraries for its core mathematical functions, providing a deep dive into the mechanics of arithmetic operations on arbitrarily large integers.

## Features
- **Arbitrary Precision:** Handles integers of any size, limited only by available memory.

- **Core Operations:**
    - Addition (`+`)
    - Subtraction (`-`)
    - Multiplication (`*`)
    - Division (`/`) (with integer quotient)
    - Modulo (`%`)
    - Exponentiation (`^`)
    - Factorial (`!`)

- **REPL (Read-Eval-Print Loop):** Interactive command-line interface for calculations.
- **Non-Decimal Bases (Bonus):** Supports input and output in bases from 2 to 36 (using digits 0-9 and letters A-Z).
- **Fractions (Bonus):** Limited basic fractional input/output support.
- **Logarithms (Bonus):** Integer base Logarithms.
- **Error Handling:** Provides clear error messages for invalid input or operations.

## How It Works
This calculator is built on the fundamental principles of elementary arithmetic operations. Here's a high-level overview of how the core features are implemented:

- **Arbitrary Precision Representation:** Integers are internally represented as a sequence (e.g., a list or array) of digits. This allows for numbers that far exceed the limits of built-in integer types.
- **Addition:** Implemented using the standard "carry-over" method taught in primary school.
- **Subtraction:** Implemented using the standard "borrow" method.
- **Multiplication:** Implemented using a digit-by-digit multiplication and accumulation process, similar to long multiplication.
- **Division and Modulo:** Implemented using long division algorithm.
- **Exponentiation:** Implemented using repeated multiplication (can be optimized using techniques like "exponentiation by squaring").
- **Factorial:** Implemented using iterative or recursive multiplication.
- **Base Conversion:** Conversion between decimal representation and the specified base is handled algorithmically.
- **REPL:** The REPL takes user input, parses it, performs the calculation, and prints the result.

## Usage
 ### 1. Running the Calculator:

   - Execute the script. The REPL should start.
      ```python
      python3 main.py
      ```
       ```bash
       calc> 12345678901234567890 + 98765432109876543210
       calc> BigInt("10").factorial()
       calc> to_base 255 16
       calc> from_base 16 FF
       calc> Fraction(4, 8)
       calc> factorial 5
       calc> 5!
       ```

 ### 2. Input Format:

   - **Integers:** Enter integers in the specified base (decimal by default).
   - **Operators:** Use +, -, *, /, %, ^ for addition, subtraction, multiplication, integer division, modulo, and exponentiation, respectively.
   - **Factorial:** Use ! after an integer.
   - **Base Specification:** To input a number in a specific base prefix the number with base_ e.g., 2_101. To output a number in a base use output base_ and all subsequent output will be in this base until another base output is set.
   - **Fractions:** To input a basic fraction a/b or a / b
   - **Logarithms:** To calculate the base b integer logarithm of a number a, type log_b(a) e.g. log_2(128) or log_5(200).
   - **Whitespace:** Whitespace between numbers and operators will be ignored, e.g. 2 + 2 or 2+2.
   - **Expressions:** The calculator evaluates expressions from left to right without precedence. Use parentheses as needed to dictate evaluation order.
   - **Output Base:** By default output will be in base 10, to change the output base use output base_N where N is the new output base.

### 3. Examples:

  - `12345 + 67890`
  - `100000000000000000000000000000000 * 2`
  - `10 ^ 5`
  - `5!`
  - `2_101 + 2_11 (Addition in base 2)`
  - `1000 / 3`
  - `1000 % 3`
  - `20/3 + 1/2`
  - `output base_16`
  - `log_2(16)`
  - `exit (to quit the REPL)`

### 4. Error Messages:
- Invalid input and operators will result in clear error messages.
- Attempting to divide by 0 will also result in a clear error message.

## Implementation Notes
- Language: Python

- No External Libraries: The core logic for arithmetic operations is implemented from scratch, not relying on external libraries for these tasks. (e.g., In Python we don't use int or decimal and in C++ we don't use BigInteger classes).

- Code Structure: The project is structured into functions or classes, with a separation of concerns. Typically:

  - A class to store a big integer using an array of int.

  - A class to deal with arbitrary precision fractions.

  - Arithmetic operations (addition, subtraction, multiplication, division, modulo, exponentiation, factorial) are implemented as separate functions.

  - Base conversion is implemented as a specific utility function.

  - The REPL is implemented as a loop that takes input, parses it, performs calculations and then prints the result.

## Bonus Features
- Non-Decimal Bases: The calculator can handle numbers in bases from 2 to 36.

- Fractions: The calculator supports basic operations on fractions.

- Logarithms: The calculator implements base b integer logarithms, log_b(a) e.g. the base 2 integer logarithm of 16 is 4.
