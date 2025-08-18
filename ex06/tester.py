import subprocess
import sys
import os

ERR_ARGS_ARE_BAD = "AssertionError: the arguments are bad"
ERR_SPECIAL_CHARACTERS = (
    "AssertionError: the argument contains a special character"
)

test_cases = [
    (["Hello the World", "4"], "['Hello', 'World']\n", 0),
    (["Hello the World", "99"], "[]\n", 0),
    (["3",  "Hello the World"], f"{ERR_ARGS_ARE_BAD}\n", 0),
    ([], f"{ERR_ARGS_ARE_BAD}\n", 0),
    (["He\nllo!", "2"], f"{ERR_SPECIAL_CHARACTERS}\n", 0),
]

PYTHON = sys.executable
SCRIPT = os.path.join(os.path.dirname(__file__), 'filterstring.py')

passed = 0
for i, (args, expected_out, expected_code) in enumerate(test_cases, 1):
    print(f"\033[1m\nTest {i}:\033[0m")
    print(f"  Args:            {args}")
    result = subprocess.run([PYTHON, SCRIPT, *args], capture_output=True,
                            text=True)
    out = result.stdout
    err = result.stderr
    code = result.returncode
    print(f"  Expected output: {expected_out!r}")
    print(f"  Actual output:   {out!r}")
    if out == expected_out and code == expected_code:
        print("\033[92mPASS\033[0m")
        passed += 1
    else:
        print("\033[91mFAIL\033[0m")
        print(f"  Expected code:   {expected_code}")
        print(f"  Actual code:     {code}")

print(f"\n{passed}/{len(test_cases)} tests passed.")
