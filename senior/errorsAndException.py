# 语法错误和异常

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise  # raise 语句抛出一个指定的异常

# else 子句将在try子句没有发生任何异常的时候执行
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
    finally:
        print("executing finally clause")

# TRY WITH RESOURCE
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
