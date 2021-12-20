from dataclasses import dataclass
import datetime
import uuid


@dataclass
class TimedTask:
    duration: datetime.timedelta
    description: str
    _start: datetime.datetime = None
    _end: datetime.datetime = None
    id: str = uuid.uuid4()

    @property
    def elapsed_time(self):
        now = datetime.datetime.now()
        time_ = (now - self.start)
        return time_

    @property
    def is_complete(self):
        return self.elapsed_time >= self.duration

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def start_task(self):
        self._start = datetime.datetime.now()
        self._end = self._start + self.duration
        return None

    def end_task(self):
        self._end = datetime.datetime.now()
        return None

    def to_dict(self):
        data = {'id': self.id,
                'description': self.description,
                'duration': self.duration,
                'start': self.start,
                'end': self.end,
                'is_complete': self.is_complete,
                'elapsed_time': self.elapsed_time}
        return data

