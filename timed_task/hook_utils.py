from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, Path().home().joinpath('.timed_task'))
sys.path.insert(0, Path(__file__).parent)


hook_schemas = [
    {'module': 'hooks',
     'name': 'CompletionNotification',
     'args': {}}
]

def create_hooks(hook_schemas):
    hooks = []
    for schema in hook_schemas:
        module = import_module(schema['module'])
        hook_cls = getattr(module, schema['name'])
        hook = hook_cls(**schema['args'])
        hooks.append(hook)
    return hooks


# hooks = create_hooks(hook_schemas)
# print(hooks)

