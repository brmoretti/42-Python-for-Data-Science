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
Each subfolder contains its own instructions and scripts, designed to be run and tested independently.

## Environment Setup

This project uses [uv](https://github.com/astral-sh/uv) for fast Python environment management and dependency installation.

### Prerequisites
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) installed (`pip install uv` or see uv documentation)

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
