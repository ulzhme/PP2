# 4. Расширение метода (super + своя логика)
class Logger:
    def log(self, msg):
        print(f"Log: {msg}")

class VerboseLogger(Logger):
    def log(self, msg):
        super().log(msg)
        print("Timestamp added.")