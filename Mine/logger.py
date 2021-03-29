import logging,os

dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
log_dir=os.path.join(dir,'Results/')

class MyLog:

    def my_log(self, message, level):
        # 1，定义一个日志收集器
        my_logger = logging.getLogger("python")

        # 2，设定级别,如果不给定参数就默认收集warning以上的，不指定级别就默认收集warning以上的
        my_logger.setLevel('DEBUG')

        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        # 3.创建一个我们自己的输出渠道
        # 3.1输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        # 3.2 输出到文本
        fh = logging.FileHandler(log_dir + "/a.txt", encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 4.两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 5，收集日志
        if level == "DEBUG":
            my_logger.debug(message)
        elif level == "INFO":
            my_logger.info(message)
        elif level == "WARNING":
            my_logger.warning(message)
        elif level == "ERROR":
            my_logger.error(message)
        elif level == "CRITICLE":
            my_logger.critical(message)

        # 关闭日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def error(self, msg):
        self.my_log(msg, 'ERROR')
