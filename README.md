# VGLUG


````markdown
# Electricity Tariff Calculator

## Description

This Python program calculates the electricity bill based on:

- Number of units consumed
- Connection type:
  - Non-Commercial
  - Commercial

The program uses `if`, `elif`, and `else` conditions to select the correct tariff slab.

## Tariff Rules

### Non-Commercial

| Units Consumed | Rate |
|---|---|
| 0 - 200 | Free |
| 201 - 500 | ₹4 per unit above 200 |
| 501 - 2000 | ₹8 per unit |
| Above 2000 | ₹10 per unit |

### Commercial

| Units Consumed | Rate |
|---|---|
| 0 - 500 | ₹6 per unit |
| 501 - 1000 | ₹9 per unit |
| 1001 - 5000 | ₹12 per unit |
| Above 5000 | ₹15 per unit |

## How It Works

1. The program asks the user to enter the number of units consumed.
2. The user enters the connection type.
3. The program checks whether the connection is Non-Commercial or Commercial.
4. It checks the number of units using `if` and `elif`.
5. The bill is calculated using arithmetic operators.
6. The total bill is displayed.

## Code

```python
units = int(input("Enter units consumed: "))
connection_type = input("Enter connection type: ")

if connection_type == "Non-Commercial":

    if units <= 200:
        bill = 0

    elif units <= 500:
        bill = (units - 200) * 4

    elif units <= 2000:
        bill = units * 8

    else:
        bill = units * 10

elif connection_type == "Commercial":

    if units <= 500:
        bill = units * 6

    elif units <= 1000:
        bill = units * 9

    elif units <= 5000:
        bill = units * 12

    else:
        bill = units * 15

else:
    bill = 0
    print("Invalid connection type")

print("Total Bill: ₹", bill)
````

## Example

### Example 1

**Input:**

```text
Enter units consumed: 350
Enter connection type: Non-Commercial
```

**Output:**

```text
Total Bill: ₹ 600
```

### Example 2

**Input:**

```text
Enter units consumed: 1200
Enter connection type: Commercial
```

**Output:**

```text
Total Bill: ₹ 14400
```

## Requirements

* Python 3.x
* No external libraries are required.

## Concepts Used

* `input()`
* `int()`
* `if`
* `elif`
* `else`
* Comparison operators
* Arithmetic operators
* `print()`

```
