import threading
import time

import schedule

from commons.util import Logging


class Schedule:
    __build = False
    __loop_thread = None

    @staticmethod
    def start():
        if not Schedule.__build:
            Schedule.__loop_thread = threading.Thread(target=Schedule.__loop, name="schedule")
            Schedule.__loop_thread.start()
            Logging.info("Schedule working on a dedicated thread")

    @staticmethod
    def __loop():
        while Schedule.__build:
            schedule.run_pending()
            time.sleep(0.5)

    @staticmethod
    def cancel(job):
        if Schedule.__build:
            schedule.cancel_job(job)
            __build = False

    @staticmethod
    def schedule():
        return schedule
