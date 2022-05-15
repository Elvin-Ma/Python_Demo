from python_log_looger import logger
'''
%(levelno)s : 打印日志级别的数值
%(levelname)s : 打印日志级别的名称
%(pathname)s : 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s : 打印当前执行程序名
%(funcName)s : 打印日志的当前函数
%(lineno)d : 打印日志的当前行号
%(asctime)s : 打印日志的时间
%(thread)d : 打印线程ID
%(threadName)s : 打印线程名称
%(process)d : 打印进程ID
%(message)s : 打印日志信息
'''
try:
    a = input("请输入一个数字：（请一定输入数字）")
    logger.debug('用户输入的第一个值是：%s' % a)
    a = int(a)
    b = input("请输入另外一个数字：")
    logger.debug('用户输入的第二个值是：%s' % b)
    b = int(b)
    c = a / b
    print("最后的结果是：%s" %c)
except Exception as ret:
    logger.error(ret)

