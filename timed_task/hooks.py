from pathlib import Path

from playsound import playsound
from plyer import notification
import pandas as pd


class CompletionNotification:
    def __init__(self,
                 title="Time Completed!",
                 timeout=2):
        self.title = title
        self.timeout = timeout

    def __call__(self, timed_task):
        if timed_task.is_complete:
            notification.notify(
                title=self.title,
                message=f"You just completed a {timed_task.duration} minute work session",

                # displaying time
                timeout=self.timeout
            )


class SoundEffect:
    def __init__(self,
                 sound='default',
                 repeat=3):
        self.repeat = repeat
        self.sound = sound
        if self.sound == 'default':
            self.sound = Path(__file__).parent.parent.joinpath('sounds', 'chime.mp3')

    def __call__(self, timed_task):
        if not timed_task.is_complete:
            return None
        for i in range(self.repeat):
            playsound(self.sound)
        return None


class TaskWriter:
    def __init__(self, file_name):
        self.path = Path().home().joinpath('.timed_task', file_name)

    def __call__(self, timed_task):
        row = timed_task.to_dict()

        if self.path.exists():
            rows = pd.read_csv(self.path).to_dict(orient='records')
        else:
            rows = []
        rows.append(row)

        df = pd.DataFrame(rows)
        df.to_csv(self.path, index=False)

