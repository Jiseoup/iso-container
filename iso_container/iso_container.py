"""ISO Container 6346 package.

Functions:
    - get_container_info(code: str):
        Retrieves container information by code.
    - validate_container(container_number: str):
        Validates a container number using ISO 6346 standards.
"""
from __future__ import annotations

import json
from pathlib import Path

# Get ISO Container 6346 datasets.
BASE_DIR = Path(__file__).resolve().parent
DATASETS_PATH = BASE_DIR / 'datasets.json'
with open(DATASETS_PATH, 'r', encoding='utf-8') as json_file:
    DATASETS = json.load(json_file)

# Set constants for validate container.
WEIGHTS = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17,
    'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25,
    'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32,
    'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38,
}
FACTORS = [2 ** i for i in range(10)]


def get_container_info(code: str) -> dict | None:
    """Retrieves container information by code.

    Args:
        code (str): ISO Container code (case-insensitive).

    Returns:
        dict | None: Container information if found, otherwise None.
    """
    return DATASETS.get(code.upper())


def validate_container(container_number: str) -> bool:
    """Validates a container number using ISO 6346 standards.

    Args:
        container_number (str): Container Number.

    Returns:
        bool: Validation Status.
    """
    if len(container_number) != 11:
        return False

    letters = container_number[:4].upper()
    digits = container_number[4:-1]
    check_digit = container_number[-1]

    if not (letters.isascii() and letters.isalpha()):
        return False
    if not (digits.isascii() and digits.isdigit()):
        return False
    if not (check_digit.isascii() and check_digit.isdigit()):
        return False

    total = 0
    for idx, char in enumerate(letters + digits):
        if char.isdigit():
            value = int(char)
        else:
            value = WEIGHTS[char]
        total += value * FACTORS[idx]

    return total % 11 == int(check_digit)
