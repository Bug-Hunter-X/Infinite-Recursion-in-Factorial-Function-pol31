This repository demonstrates a common error in Python: infinite recursion. The `factorial_bug.py` file contains a recursive function to calculate the factorial.  However, it does not handle the case for negative input causing a `RecursionError`. The solution (`factorial_solution.py`) demonstrates how to correctly handle negative input or invalid inputs by adding input validation and returning an error message.