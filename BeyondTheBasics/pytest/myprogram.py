import sys


def doubleit(x):
    if not isinstance(x, (int, float)):
        raise(TypeError)
    var = 2 * x
    return var


if __name__ == '__name__':
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)

    print 'the value is {} doubled {}'.format(input_val, doubled_val)
