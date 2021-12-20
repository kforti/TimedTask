from importlib import import_module


def print_hook(main_loop):
    print('Its working!!!')


my_hooks = import_module('hooks.new_hooks')
my_hooks.print_hook(None)
