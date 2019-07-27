import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    log_filter = logging.Filter('A')

    logger1 = logging.getLogger('A')
    logger1.addFilter(log_filter)
    logger1.debug('This is written to log output')

    logger2 = logging.getLogger('A.B')
    logger2.addFilter(log_filter)
    logger2.debug('This is written to log output')

    logger3 = logging.getLogger('B')
    logger3.addFilter(log_filter)
    logger3.debug('This is NOT written to log output, because only names start with "A" are allowed by filter')

