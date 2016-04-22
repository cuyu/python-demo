'''_
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 4/22/16
'''
import logging

# The meaning of each format string can refer to the official doc.
_LOG_FORMAT = '[%(asctime)s] %(levelname)s - %(name)s: %(message)s'


def test():
    result = 0
    logger.debug("This is `debug` log")
    logger.info("This is `info` log")
    logger.warning("This is `warning` log")
    try:
        result = 1 / 0
    except Exception, e:
        # Set exc_info=True will also print the trace back info!
        logger.error("Some exception occurs.", exc_info=True)

    return result


class TestClass(object):
    def __init__(self):
        # A typical naming way is using the class name.
        self.logger = logging.getLogger(self.__class__.__name__)

    def test(self):
        self.logger.debug("This is `debug` log")
        self.logger.info("This is `info` log")
        self.logger.warning("This is `warning` log")
        self.logger.critical("This is `critical` log")


if __name__ == "__main__":
    # The level set here will only change the Logger.level of the root node;
    # The default Logging level of root node is logging.WARNING.
    # If not set the filename, the logs will print on terminal. filemode='w' will clear the file content each time.
    logging.basicConfig(filename="demo_logging.log", filemode='w', level=logging.DEBUG, format=_LOG_FORMAT)
    # logging.getLogger() actually called Logger.manager.getLogger();
    # Logger.manager is a property of class {Logger}, and is a instance of {Manager} class;
    # This call will search a internal dict of {Manager} objects and return a new {Logger} instance if not found;
    # The new {Logger} instance's default logging level is logging.NOTSET, which means all level logs will be recorded.
    logger = logging.getLogger(__name__)
    # Set the logging level of this specific logger. If not set, it will use the settings of its father node.
    logger.setLevel(logging.INFO)

    test()

    TestClass().test()
