import logging

def print_log(log1):
    logging.basicConfig(filename='../log/log.txt', level=logging.INFO, format='%(asctime)s %(message)s')
    file = logging.getLogger().handlers[0].stream

    print(log1, file=file)





