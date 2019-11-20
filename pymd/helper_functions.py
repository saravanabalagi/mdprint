from typing import Union


def _titleize(value):
    string = str(value)
    cleaned_string = string.replace("_", " ")
    cleaned_string = cleaned_string.replace("-", " ")
    return cleaned_string.title()


def _table_formatted_string(atomic_value, line=False):
    if line:
        return '|----'
    else:
        return '| {} '.format(atomic_value)


def _get_table_line_string(values: Union[list, tuple, any], line=False, original_call=True) -> str:
    if type(values) is not list and type(values) is not tuple:
        line_string = _table_formatted_string(values, line)
    else:
        line_string = ''.join([_table_formatted_string(v, line)
                               if type(v) is not list and type(values) is not tuple
                               else _get_table_line_string(v, line=line, original_call=False)
                               for v in values])
    if original_call:
        line_string += '|'
    return line_string


if __name__ == '__main__':
    assert(_get_table_line_string("something") == "| something |")
    assert(_get_table_line_string(["something", "else"]) == "| something | else |")
    assert(_get_table_line_string(["something", ["else"]]) == "| something | else |")
    assert(_get_table_line_string(["something", ["else", "else2"]]) == "| something | else | else2 |")
    assert(_get_table_line_string(["something", ["else", "else2"]], line=True) == "|----|----|----|")

    assert(_get_table_line_string(("something", "else")) == "| something | else |")
    assert(_get_table_line_string(("something", ["else"])) == "| something | else |")
    assert(_get_table_line_string(("something", ["else", "else2"])) == "| something | else | else2 |")
    assert(_get_table_line_string(("something", ["else", "else2"]), line=True) == "|----|----|----|")

    assert(_get_table_line_string(("something", "else", "else2")) == "| something | else | else2 |")
    assert(_get_table_line_string(("something", "else", "else2"), line=True) == "|----|----|----|")
