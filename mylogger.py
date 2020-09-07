from MySQLConnector.mysqlconnector import MySqlConnector
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class LogLevel:
    info = 1
    warn = 2
    error = 3
    fatal = 4
    debug = 5


class MyLogger:

    def __init__(self, func=''):
        self.db = MySqlConnector()
        self.func = func

    def putLog(self, logLv, subject, detail):
        print(subject, detail)
        try:
            self.db.cur.execute(
                "INSERT INTO Logs (logFrom, level, subject, detail)"
                " VALUES (%(func)s, %(level)s, %(subject)s, %(detail)s)",
                {
                    'func': self.func,
                    'level': logLv,
                    'subject': subject,
                    'detail': detail
                }
            )
            self.db.conn.commit()
        except:
            raise

    def info(self, subject, detail):
        self.putLog(LogLevel.info, subject, detail)

    def warn(self, subject, detail):
        self.putLog(LogLevel.warn, subject, detail)

    def error(self, subject, detail):
        self.putLog(LogLevel.error, subject, detail)

    def fatal(self, subject, detail):
        self.putLog(LogLevel.fatal, subject, detail)

    def debug(self, subject, detail):
        self.putLog(LogLevel.debug, subject, detail)

    def close(self):
        self.db.close()
