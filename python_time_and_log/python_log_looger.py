# coding : utf-8
import logging

# step1 : build a logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# step2 : build a handle, use for write log
logfile = 'log.txt'
fh = logging.FileHandler(logfile, mode='a') # 追加写入
fh.setLevel(logging.DEBUG) # set log level

# step3 : build another handle, use for terminal print control
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING) # DEBUG INFO WARNING ERROR CRITICAL

# step4 : format control for file handle and terminal handle
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# step5 : 将logger添加到 handler 里面
logger.addHandler(fh)
logger.addHandler(ch)

