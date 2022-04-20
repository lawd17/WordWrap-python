def wrap(line: str, column: int) -> str:
    if not line or line == "":
        return ""

    if column < 0:
        raise Exception("Negative columns is not allowed")

    return line
