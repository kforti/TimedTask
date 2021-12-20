from pathlib import Path
import yaml
import datetime


PACKAGE_CONFIGS = Path(__file__).parent.parent.joinpath('configs')
USER_CONFIGS = Path.home().joinpath('.timed_task', 'configs')

def load_config(path, package_configs=PACKAGE_CONFIGS, user_configs=USER_CONFIGS):

    if '/' not in path:
        if user_configs.joinpath(path).exists():
            path = user_configs.joinpath(path)
        elif package_configs.joinpath().exists():
            path = package_configs.joinpath(path)

    with open(path) as f:
        config = yaml.safe_load(f)
    return config


def build_duration(days=0.0,
                   seconds=0.0,
                   microseconds=0.0,
                   milliseconds=0.0,
                   minutes=0.0,
                   hours=0.0):
    data = dict(days=days,
                seconds=seconds,
                microseconds=microseconds,
                milliseconds=milliseconds,
                minutes=minutes,
                hours=hours)
    final_data = {k: v for k, v in data.items() if v}
    duration = datetime.timedelta(**final_data)
    return duration