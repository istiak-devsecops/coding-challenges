

class Logger:
    def log(self, message):
        return f"[LOG] {message}"

class Notifier:
    def notify(self, message):
        return f"[Notify] {message}"

class Service:
    def __init__(self, logger, notifier):
        self.logger = logger
        self.notifier = notifier

    def run(self):
        self.logger.log("Service started")
        self.notifier.notify("Service is live")

logger = Logger()
notifier = Notifier()
service = Service(logger, notifier)
service.run()
