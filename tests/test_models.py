import datetime
import time

from timed_task.models import TimedTask


def test_timed_task_should_complete():
    duration = datetime.time(microsecond=10)
    task = TimedTask(duration)
    task.start_task()
    time.sleep(.15)
    assert task.is_complete


def test_timed_task_should_not_complete():
    duration = datetime.time(minute=10)
    task = TimedTask(duration)
    task.start_task()
    assert not task.is_complete
