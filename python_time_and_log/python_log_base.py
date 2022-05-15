import logging

# level : 开发的时候调低，交付的时候调低
logging.basicConfig(level = logging.DEBUG,
                    filename = './log.txt',
                    filemode = 'a', # 以追加方式写入
                    format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

try:
    a = input("请输入一个数字：（请一定输入数字）")
    logging.debug('用户输入的第一个值是：%s' % a)
    a = int(a)
    b = input("请输入另外一个数字：")
    logging.debug('用户输入的第二个值是：%s' % b)
    b = int(b)
    c = a / b
    print("最后的结果是：%s" %c)
except Exception as ret:
    logging.error(ret)
