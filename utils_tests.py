import utils

def test_reversed(input):
    if type(input) != int:
        print("Error data type")
    else:
        result = utils.reversed(input)
        print("Success, input reversed as ", result)


def test_format(input):
    if type(input) != int:
        print("Error data type")
    else:
        bin_res, oct_res = utils.formatter(input)
        print("Success, input formatted as binary ", bin_res, " octal ", oct_res)

if __name__=='__main__':
    my_str="adcbe"
    my_int=12345
    my_float=1.2345
    test_reversed(my_str)
    test_reversed(my_int)
    test_reversed(my_float)
    test_format(my_str)
    test_format(my_int)
    test_format(my_float)