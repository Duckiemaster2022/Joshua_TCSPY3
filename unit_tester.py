import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "test at line {0} OK.".format(linenum)
    else:
        msg = ("test at line {0} FAILED".format(linenum))
    print(msg)
