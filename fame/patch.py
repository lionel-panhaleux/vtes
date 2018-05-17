"""Unified diff patcher using a line + line number reference.
"""
import re


class PatchError(Exception):
    pass


def patch(source, diff, target, reference):
    """Apply unified diff (TWDA.diff) to TWDA.html.

    It uses a (line, line_number) reference to compute the offset for the patch.
    This ensures the patch continues to be valid when TWDA is updated.
    TWDA updates from 2016 on are consistent with Fame parsing and do not
    need patching.
    """
    diff, source = iter(diff), iter(source)
    start = 0
    line_num = 0
    try:
        # offset
        while not line_num:
            s_line = next(source)
            if s_line != reference[0]:
                target.write(s_line)
                continue
            line_num = reference[1]
        while True:
            d_line = next(diff)
            if not start and d_line[:3] == b'---':
                continue
            if not start and d_line[:3] == b'+++':
                continue
            if d_line[:2] == b'@@':
                start = int(
                    re.match(b'^@@ -(\d+),\d+ \+\d+,\d+ @@$', d_line).group(1)
                )
                continue
            while line_num < start:
                target.write(s_line)
                s_line = next(source)
                line_num += 1
            if d_line[0] == ord('+'):
                target.write(d_line[1:])
                continue
            if d_line[1:] != s_line:
                raise PatchError(
                    "failed to apply patch @{}, hunk @@{}."
                    .format(line_num, start)
                )
            if d_line[0] == ord(' '):
                target.write(s_line)
            elif d_line[0] != ord('-'):
                raise PatchError(
                    "bad diff format, hunk @@{}."
                    .format(start)
                )
            s_line = next(source)
            line_num += 1

    except StopIteration:
        pass
