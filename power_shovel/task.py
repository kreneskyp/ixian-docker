import functools

import shovel
#task = shovel.task
shovel_task = shovel.task


TARGETS = {}


def decorate_task(func, target=None, depends=None, check=None, clean=None):
    power_shovel_task = Task(
        func=func,
        depends=depends,
        check=check,
        clean=clean)

    # TODO: targets
    """
    if target:
        try:
            target_task = TARGETS[target]
        except:
            target_task = Task()
        target_task.add_dependency(power_shovel_task)
    """

    # Register with shovel. Shovel expects a function so create another wrapper
    # function around the power_shovel_task.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return power_shovel_task(*args, **kwargs)
    shovel_task(wrapper)

    # return the Task object so the module receives the task.
    return power_shovel_task


def task(func=None, **kwargs):
    if func is None:
        def decorator(func):
            return decorate_task(func, **kwargs)
        return decorator
    else:
        return decorate_task(func)


class AlreadyComplete(Exception):
    """
    Exception thrown when a Task executes but it's checks indicate complete.
    """


class Task(object):
    """
    A task is a wrapper around functions that adds in various functionality
    such as dependencies and check functions.
    """

    def __init__(self, func=None, depends=None, check=None, clean=None):
        self.func = func
        self.depends = depends or []
        if check:
            if isinstance(check, (list, tuple)):
                self.checkers = check
            else:
                self.checkers = [check]
        else:
            self.checkers = None
        self.clean = clean

    def __call__(self, *args, **kwargs):
        try:
            self.execute(*args, **kwargs)
        except AlreadyComplete:
            print('Already complete. Override with --force or --force-all')

    def execute(self, *args, **kwargs):
        clean = kwargs.pop('clean', False)
        clean_all = kwargs.pop('clean-all', False)
        force = kwargs.pop('force', False)
        force_all = kwargs.pop('force-all', False)

        if clean:
            force = True
        if clean_all:
            clean = True
            force_all = True
        if force_all:
            force = True

        if self.clean and clean:
            self.clean()

        # execute dependencies. Ignore completed.
        dependency_kwargs = {
            'clean-all': clean_all,
            'force-all': force_all
        }
        try:
            for dependency in self.depends:
                dependency.execute(**dependency_kwargs)
        except AlreadyComplete:
            pass

        # Execute function if there is one. Targets may not have a function.
        if self.func:
            checkers = None
            passes = False
            if self.checkers:
                if force:
                    passes = False
                elif self.checkers:
                    checkers = [checker.clone() for checker in self.checkers]
                    checks = [checker.check() for checker in checkers]
                    passes = all(checks)

            if passes:
                raise AlreadyComplete()

            else:
                return_value = self.func(*args, **kwargs)
                # save checker only after function has completed successfully
                if checkers:
                    for checker in checkers:
                        checker.save()
                return return_value

    def add_dependency(self, power_shovel_task):
        self.depends.append(power_shovel_task)
