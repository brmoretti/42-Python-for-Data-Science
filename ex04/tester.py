import subprocess
import sys
import os

test_cases = [
    (['14'], "I'm Even.\n", 0),
    (['-5'], "I'm Odd.\n", 0),
    ([], '', 0),
    (['Hi!'], 'AssertionError: argument is not an integer\n', 1),
    (['13', '5'], 'AssertionError: more than one argument is provided\n', 1),
]

PYTHON = sys.executable
SCRIPT = os.path.join(os.path.dirname(__file__), 'whatis.py')

passed = 0
for i, (args, expected_out, expected_code) in enumerate(test_cases, 1):
    print(f"\033[1m\nTest {i}:\033[0m")
    print(f"  Args:            {args}")
    result = subprocess.run([PYTHON, SCRIPT, *args], capture_output=True, text=True)
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
