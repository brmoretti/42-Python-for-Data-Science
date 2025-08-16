#!/usr/bin/env python3

# fun fact: tqdm means "progress" in Arabic (taqadum, تقدّم) and is an
# abbreviation for "I love you so much" in Spanish (te quiero demasiado).
# source: https://tqdm.github.io/ on Aug 15 2025

def _ttyCursor(active: bool):
    """
    Enables or disables the terminal cursor visibility using ANSI escape codes.

    Args:
        active (bool): If True, shows the cursor; if False, hides the cursor.

    Note:
        This function is intended for use in terminals that support ANSI
        escape codes.
    """
    if active:
        print("\033[?25h", end="", flush=True)
        return
    print("\033[?25l", end="", flush=True)


def _progressBar(progress: float | int) -> str:
    """
    Generates a textual progress bar representation based on the given
    progress value.

    Args:
        progress (float | int): The progress value, expected to be between
        0 and 100.

    Returns:
        str: A string representing the progress bar, where completed progress
        is shown with '█' characters and remaining progress with spaces,
        enclosed within '|'.
    """
    nb = int(progress)
    return "|" + "█" * nb + " " * (100 - nb) + "|"


def _printProgressLine(progress: float | int, ops_elapsed: int,
                       total_ops: int):
    """
    Prints a progress bar line to the terminal, clearing the current line
    first.

    Args:
        progress (float | int): The current progress percentage.
        ops_elapsed (int): The number of operations completed.
        total_ops (int): The total number of operations.
    """
    bar = _progressBar(progress)
    line = f"{progress:3.0f}%{bar} {ops_elapsed}/{total_ops}"
    # \r moves the cursor to the beginning of the line, \033[K clears the line.
    print(f"\r\033[K{line}", end="", flush=True)


def ft_tqdm(lst: range) -> None:
    """
    Generator that yields items from lst while displaying a progress bar.
    """
    _ttyCursor(False)
    count = 0
    length = len(lst)
    try:
        for i in lst:
            progress = round(count * 100 / length, 0)
            _printProgressLine(progress, count, length)
            count += 1
            yield i
        _printProgressLine(100, count, length)
    finally:
        _ttyCursor(True)
