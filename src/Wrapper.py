def wrap(line: str, column: int) -> str:
    wrap_line: str = line
    if column < 0:
        raise Exception("Negative columns is not allowed")

    if not line or line == "":
        return ""

    if len(line) > column:
        wrap_line = line[0:column] + "\n" + wrap(line[column:], column)

    return wrap_line
