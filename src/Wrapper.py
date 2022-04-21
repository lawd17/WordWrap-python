def wrap(line: str, column: int) -> str:
    wrap_line: str = line
    if column < 0:
        raise Exception("Negative columns is not allowed")

    if not line or line == "":
        return ""

    if len(line) > column:
        wrap_line = line[0:change_column_to_space(line, column)] + "\n" + wrap(line[change_column_to_space(line, column):], column)

    return wrap_line


def change_column_to_space(line: str, column: int) -> int:
    if " " in line and line.find(" ") != 0:
        space_index = line.find(" ")
        if space_index < column:
            return space_index

    return column
