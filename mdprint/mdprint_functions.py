import sys
from typing import Union
from mdprint.helper_functions import _get_table_line_string
import warnings


def mdprint(*objects: any, file=sys.stdout, heading: Union[bool, int] = False,
            bold: bool = False, italics: bool = False, strikethrough: bool = False,
            sep=' ', end='\n', flush=False) -> None:
    prepend_string = ''
    pre_and_post = ''

    if heading:

        if any([italics, bold, strikethrough]) is True:
            warnings.warn("Using italics, bold and strikethrough in conjunction with header will have no effect. "
                          "Header will be prioritized and other styles will be ignored. ")

        # set default heading size when heading is True
        if type(heading) is bool and heading is True:
            heading = 3

        # Fill no of hashes equal to heading count
        prepend_string = ''.join(['#' for _ in range(heading)])

    else:
        if italics:
            pre_and_post = f"_{pre_and_post}"
        if bold:
            pre_and_post = f"**{pre_and_post}"
        if strikethrough:
            pre_and_post = f"~~{pre_and_post}"

    print(pre_and_post, end='')
    print(prepend_string, end='')
    print(*objects, file=file, sep=sep, end='')
    print(pre_and_post[::-1], end=end, flush=flush)


def mdprint_dict(d: dict, file=sys.stdout, keys_as_headers: bool = True, sort_keys: bool = False) -> None:

    items = list(d.items())
    if sort_keys:
        items = sorted(items)

    if keys_as_headers:
        # make header row from dict keys
        header_row = [item[0] for item in items]

        # transpose columns to rows
        # https://stackoverflow.com/a/6473724/3125070
        column_values = [item[1] for item in items]
        rows = list(map(list, zip(*column_values)))

        mdprint_list([header_row, *rows], file=file, first_line_header=True)

    else:
        mdprint_list(items, file=file, first_line_header=False)


def mdprint_list(rows: list, file=sys.stdout, first_line_header: bool = True, sort_keys: bool = False) -> None:
    print("", file=file)

    if sort_keys:
        zipped = list(zip(*rows))
        zipped.sort()
        rows = list(zip(*zipped))

        # sort_indices = _argsort(rows[0])
        # for i in range(len(rows)):
        #     row = rows[i]
        #     rows[i] = [row[si] for si in sort_indices]

    # print first row as table header
    # if first_line_header is True
    if first_line_header:
        header_row = rows[0]
        print(_get_table_line_string(header_row), file=file)
        print(_get_table_line_string(header_row, line=True), file=file)

    value_rows = rows[1:] if first_line_header else rows

    # print row by row
    for row in value_rows:

        # make first column bold
        # if first line header is False
        row = list(row)
        if not first_line_header:
            row[0] = f'*{str(row[0])}*'

        # print as table
        print(_get_table_line_string(row), file=file)

    print("", file=file)


if __name__ == '__main__':
    a = [[3, 1, 2], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    b = {3: [4, 7], 1: [5, 8], 2: [6, 9]}

    mdprint_dict(b, keys_as_headers=False)
    mdprint_dict(b, keys_as_headers=False, sort_keys=True)
    mdprint_dict(b)
    mdprint_dict(b, sort_keys=True)

    mdprint("--------")
    mdprint_list(a)
    mdprint_list(a, sort_keys=True)

    print(list(zip(*a)))

    mdprint(*a, bold=True)
    mdprint(*a, bold=True, italics=True)
    mdprint(*a, bold=True, italics=True, strikethrough=True)
    mdprint(*a, heading=5)
    mdprint(*a, heading=True, bold=True, italics=True, strikethrough=True)
