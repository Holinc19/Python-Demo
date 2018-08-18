class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    # 1 / 0
    raise Networkerror("Bad hostname")

except Networkerror as err:
    print("自定义异常")
    print(err.args)
except Exception as e:
    '''异常的父类，可以捕获所有的异常'''
    print("0不能被除")
else:
    '''保护不抛出异常的代码'''
    print("没有异常")
finally:
    print("最后总是要执行我")
