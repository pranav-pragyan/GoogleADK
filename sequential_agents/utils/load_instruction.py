from pathlib import Path


def load_instruction(current_file: str, instruction_file: str = "instruction.txt") -> str:
    """
    Load instruction text relative to the current Python file.

    Args:
        current_file: __file__ from the caller module
        instruction_file: instruction filename

    Returns:
        str: instruction content
    """

    instruction_path = Path(current_file).parent / instruction_file

    with open(instruction_path, "r", encoding="utf-8") as f:
        return f.read()