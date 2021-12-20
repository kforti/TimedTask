import time


class TimedTaskService:
    def __init__(self, timed_task,
                       sleep=2,
                       start_hooks=[],
                       loop_hooks=[],
                       exit_hooks=[]):
        self.timed_task = timed_task
        self.sleep = sleep
        self.start_hooks = start_hooks
        self.loop_hooks = loop_hooks
        self.exit_hooks = exit_hooks

    def run(self):
        self._run_hooks(self.start_hooks)
        self.timed_task.start_task()
        while not self.timed_task.is_complete:
            time.sleep(self.sleep)
            self._run_hooks(self.loop_hooks)

    def exit(self):
        self.timed_task.end_task()
        self._run_hooks(self.exit_hooks)

    def _run_hooks(self, hooks):
        for hook in hooks:
            hook(self.timed_task)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.exit()


