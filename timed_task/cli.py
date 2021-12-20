import datetime

import click

from .services import TimedTaskService
from .utils import load_config, build_duration
from .models import TimedTask
from .hook_utils import create_hooks




@click.command()
@click.option('--days', default=0.0)
@click.option('--seconds', default=0.0)
@click.option('--microseconds', default=0.0)
@click.option('--milliseconds', default=0.0)
@click.option('--minutes', default=0.0)
@click.option('--hours', default=0.0)
@click.option('--description', '-d', default='')
@click.option('--config', default='base_timed_task.yaml')
@click.option('--sleep')
def run_timed_task(days,
                seconds,
                microseconds,
                milliseconds,
                minutes,
                hours,
                description,
                config,
                sleep):
    duration = build_duration(days=days,
                              seconds=seconds,
                              microseconds=microseconds,
                              milliseconds=milliseconds,
                              minutes=minutes,
                              hours=hours)

    config = load_config(config)
    if 'duration' in config and datetime.timedelta() == duration:
        duration = build_duration(**config['duration'])
    sleep = sleep or config.get('sleep')
    start_hooks = create_hooks(config.get('start_hooks', []))
    loop_hooks = create_hooks(config.get('loop_hooks', []))
    exit_hooks = create_hooks(config.get('exit_hooks', []))

    timed_task = TimedTask(duration, description)
    timed_task_service = TimedTaskService(timed_task=timed_task,
                                          sleep=sleep,
                                          start_hooks=start_hooks,
                                          loop_hooks=loop_hooks,
                                          exit_hooks=exit_hooks)
    with timed_task_service:
        timed_task_service.run()



@click.command()
@click.option('--days', default=0.0)
@click.option('--seconds', default=0.0)
@click.option('--microseconds', default=0.0)
@click.option('--milliseconds', default=0.0)
@click.option('--minutes', default=0.0)
@click.option('--hours', default=0.0)
def run_command2(days,
                seconds,
                microseconds,
                milliseconds,
                minutes,
                hours):

    duration = build_duration(days,
                seconds,
                microseconds,
                milliseconds,
                minutes,
                hours)
    duration2 = datetime.timedelta(seconds=15.0)

    print(duration == duration2)


