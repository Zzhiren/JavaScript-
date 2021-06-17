# Python 错误和异常
import sys

# try/except
# 异常捕捉可以使用 try/except 语句。

# while True:
#     try:
#         x = int(input('请输入一个数:'))
#         break
#     except ValueError:
#         print('您输入的不是数字，请再次尝试输入！')


# def fun2():
#     try:
#         f = open('myfile.txt')
#         s = f.readline()
#         i = int(s.strip())
#     except OSError as err:
#         print("OS error: {0}".format(err))
#     except ValueError:
#         print("Could not convert data to an integer.")
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         raise

# try/except...else
'''
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。
'''
print('---', sys.argv)
for arg in sys.argv[0:]:
    print('for')
    try:
        f = open(arg, 'r')
        print('f', f)
    except IOError:
        print('can not open', IOError)
    else:
        print('f.close')
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
