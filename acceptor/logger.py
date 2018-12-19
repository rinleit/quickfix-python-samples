import logging

def setup_logger(logger_name, log_file, level=logging.DEBUG):
    lz = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    lz.setLevel(level)
    lz.addHandler(fileHandler)
    lz.addHandler(streamHandler) 