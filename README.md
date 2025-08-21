# ThoughtfulAI
Thoughtful AI Technical Screen

# Package Sorting Project
This project implements a Python-based package sorting system that categorizes packages into three stacks (STANDARD, SPECIAL, or REJECTED) based on their dimensions (width, height, length in centimeters) and mass (in kilograms). The system includes a core sorting function and an interactive script for testing custom inputs.
Project Overview
The project consists of two Python scripts:


sort_package.py: Contains the sort function, which implements the sorting logic and includes built-in test cases.


run_custom_sort.py: Provides an interactive interface to input custom package dimensions and mass, using the sort function to display results.

# Sorting Rules

**Stacks:**


STANDARD: Packages that are neither bulky nor heavy.


SPECIAL: Packages that are either bulky or heavy (but not both).


REJECTED: Packages that are both bulky and heavy, or have invalid inputs (non-numeric, negative, or zero values).


**Special characteristics**


Bulky: A package is bulky if its volume is ≥ 1,000,000 cm³ or any dimension (width, height, or length) is ≥ 150 cm.


Heavy: A package is heavy if its mass is ≥ 20 kg.



# Prerequisites
To run this project from the command prompt, ensure you have:

Python: Version 3.6 or higher installed. Download from python.org.


Verify installation by running:python --version


Command Prompt: Access to Command Prompt (Windows), Terminal (macOS/Linux), or equivalent.


No external libraries are required; the project uses only standard Python.

# Setup Instructions
Setup Instructions

Follow these steps to clone the ThoughtfulAI repository and run the project from the command prompt.

Step 1: Clone the Repository

Open your command prompt or terminal:

Clone the ThoughtfulAI repository:

git clone https://github.com/BobHocraffer/ThoughtfulAI.git
Navigate to the project directory
Check that sort_package.py and run_custom_sort.py are present
If the files are missing, ensure the repository was cloned correctly or create them manually.

Step 3: Run the Project from Command Prompt

Run Test Cases (Optional):

To verify the sort function:

python sort_package.py

Expected Output:

All tests passed!



Run with Custom Inputs:

Execute the interactive script:

python run_custom_sort.py



**Files included:**

sort_package.py:

Contains the sort function, which uses a ternary operator because I used an LLM to create the code.

Includes test cases covering all scenarios (standard, special, rejected, invalid inputs).

Run directly to execute tests: python sort_package.py.


run_custom_sort.py:

Provides an interactive interface to input custom package dimensions and mass.

Validates user inputs to ensure they are positive numbers.


Run to test custom values: python run_custom_sort.py.



Invalid Input Handling:

run_custom_sort.py handles non-numeric or negative inputs by prompting again.

The sort function returns "REJECTED" for invalid inputs.
Alternative Execution:
Run at Repl.it by uploading both files and running run_custom_sort.py.
