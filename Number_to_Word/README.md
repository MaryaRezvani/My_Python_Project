# Number to Word Converter
this project presents a Python script that convert a positive integer input from a user into its equivalent words.

for instance, if a user inputs "12345", the program will output "Twelve thousand three hundred forty five.". Keep in mind that this program is designed to handle numbers with a maximum of 12 digits.

```
Input: 257
Output: Two Hundred Fifty Seven

Input: 600000
Output: Six Hundred Thousand

Input: 1000000
Output: One Million

```
## Project Structure

The project comprises two main components:

- `README.md` file: This documentation file provides a comprehensive information about the project, its structure, requirements, as well as useful tips to successfully run the program.

- The Python Script (`src` directory): This is where the main Python script for the number-to-word conversion is located. 

```
.
├── README.md
└── src
    └── main.py
```

## Requirements

The program does not rely on any third-party libraries or dependencies. It is purely written in Python 3 and does not need any additional modules for its functionality.

## How To Run

To run the program, you need to navigate to the `src` directory and run the `main.py` script using Python. You can do this by opening your terminal and typing the following commands:

```bash
cd src
python main.py
```

The program will then ask you to enter a number to convert into words. You can enter any positive integer number with a maximum of 12 digits. The program will then output the equivalent words for the number you entered.

## Hints
- you may use loops and conditionals to break down the number into smaller units which can be individually converted to words.
- Python's dictionaries can map numbers to their word equivallents for easier conversion
- adding and exception to handle incorrect input is also a good idea.
- Keep in mind, this program is set up to support numbers with a maximum of 12 digits, but feel free to modify the program to handle larger numbers.
---
you can look into this python package: [num2words](https://github.com/savoirfairelinux/num2words)  for more advanced number-to-word conversion capabilities.