from python_log_looger import logger

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

