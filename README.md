# 42 Python for Data Science

This repository contains a collection of Python exercises designed to introduce and reinforce fundamental concepts and tools for data science, as part of the 42 school curriculum.

## Contents

- **0-Starting/**: A progressive set of exercises introducing Python and data science fundamentals:
   - **ex00/Hello.py**: Print a simple greeting to the screen, introducing basic script execution.
   - **ex01/format_ft_time.py**: Practice string formatting and working with time values.
   - **ex02/find_ft_type.py**: Identify and print the type of various Python objects, exploring dynamic typing.
   - **ex03/NULL_not_found.py**: Understand Python's `None` and how to handle null values.
   - **ex04/whatis.py**: Use command-line arguments and print information about them.
   - **ex05/building.py**: Analyze a text and print a summary of character types (upper, lower, digits, spaces, punctuation) from user input or command-line argument.
   - **ex06/filterstring.py & ft_filter.py**: Implement and use a custom filter function, reinforcing functional programming concepts.
   - **ex07/sos.py**: Encode a message in Morse code, practicing string manipulation and dictionaries.
   - **ex08/Loading.py**: Mimic the behavior of the `tqdm` progress bar by implementing a custom progress bar for iterables, without using external libraries.
   - **ex09/ft_package/**: Create a Python package, including modules, metadata, and distribution basics.

- **1-Array/**: Exercises focused on NumPy arrays and image processing:
   - **ex00/give_bmi.py**: Calculate Body Mass Index (BMI) from lists of heights and weights, and filter results by a specified limit.
   - **ex01/array2D.py**: Perform slicing operations on 2D arrays (matrices) and print shape information before and after slicing.
   - **ex02/load_image.py**: Load images from file paths using PIL and convert them to NumPy arrays, handling errors gracefully.
   - **ex03/zoom.py**: Zoom into images by cropping specific regions and displaying the cropped array data.
   - **ex04/rotate.py**: Rotate images by 90 degrees and display the transformed array data.
   - **ex05/pimp_image.py**: Apply image enhancement filters such as invert, blue-shift, magnitude, and cellshade effects to RGB images.

- **2-Datatable/**: Exercises focused on data analysis and visualization using pandas and matplotlib:
   - **ex00/load_csv.py**: Load CSV files into pandas DataFrames and print dataset dimensions.
   - **ex01/aff_life.py**: Visualize Brazil's life expectancy data over time using seaborn line plots and matplotlib for customization.
   - **ex02/aff_pop.py**: Visualize population data across countries, parsing population values with suffixes (M for millions, k for thousands), and creating bar charts.
   - **ex03/projection_life.py**: Compare income and life expectancy data by creating scatter plots for a specific year, exploring the relationship between economic indicators and quality of life.

- **3-OOP/**: Exercises focused on Object-Oriented Programming concepts:
   - **ex00/S1E9.py**: Define abstract base classes and understand inheritance hierarchies using Python's `ABC` module.
   - **ex01/S1E7.py**: Create concrete subclasses (Baratheon, Lannister) that inherit from an abstract Character class, implementing specific attributes and behaviors.
   - **ex02/DiamondTrap.py**: Implement multiple inheritance with a King class that inherits from both Baratheon and Lannister, demonstrating the diamond problem and method resolution order (MRO).
   - **ex03/ft_calculator.py**: Overload arithmetic operators (`__add__`, `__sub__`, `__mul__`, `__truediv__`) to perform in-place operations on lists of numbers.
   - **ex04/ft_calculator.py**: Use static methods to implement vector operations including dot product, element-wise addition, and element-wise subtraction.

- **4-Dod/**: Exercises focused on Data-Oriented Design and functional programming patterns:
   - **ex00/statistics.py**: Implement statistical functions to calculate mean, median, quartiles, variance, and standard deviation with error handling for various input cases.
   - **ex01/in_out.py**: Create closure-based functions that apply transformations iteratively using state management with `nonlocal` variables and cached results.
   - **ex02/callLimit.py**: Design decorators that limit function call counts and provide controlled access to functions with customizable call limits.
   - **ex03/new_student.py**: Use Python dataclasses with `field` and `default_factory` to manage complex object initialization and unique instance identifiers.

Each subfolder contains its own instructions and scripts, designed to be run and tested independently.

## Environment Setup

This project uses [uv](https://github.com/astral-sh/uv) for fast Python environment management and dependency installation.

### Prerequisites
- Python 3.10
- [uv](https://github.com/astral-sh/uv)

### Setting up the environment
1. **Install dependencies:**
   ```zsh
   uv sync
   ```
   This will create a `.venv` directory and install all dependencies.

2. **Activate the virtual environment:**
   ```zsh
   source .venv/bin/activate
   ```

3. **(Optional) Add aliases for tools:**
   For example, to alias `norminette` to `flake8`:
   ```zsh
   alias norminette='.venv/bin/flake8'
   ```
   Add this line to your `~/.zshrc` for persistence.

## Running Exercises

Navigate to the relevant exercise folder and run the Python scripts as needed. Example:
```zsh
cd 0-Starting/ex02
python find_ft_type.py
```

## Project Structure

- `pyproject.toml`: Project metadata and dependencies
- `README.md`: This file
- `0-Starting/`: Exercises and supporting files

## License

This project is for educational purposes as part of the 42 school curriculum.
