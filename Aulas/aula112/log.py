class LogMixin:

    @staticmethod
    def write(msg):
        with open('log.txt', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'WARN: {msg}')
