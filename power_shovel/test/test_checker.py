from unittest.mock import Mock

from power_shovel.check.checker import Checker


class MockChecker(Checker):

    def __init__(self, *args, **kwargs):
        self.save = Mock()
        self.check = Mock(return_value=True)
        self.mocked_state = 1

    def state(self):
        return {'mock': self.mocked_state}

    def file_path(self):
        return '/mock/'

    def clone(self):
        instance = type(self)()
        instance.save = self.save
        return instance


class FailingCheck(MockChecker):
    """A checker that always fails the check"""

    def __init__(self, *args, **kwargs):
        super(FailingCheck, self).__init__(*args, **kwargs)
        self.check = Mock(return_value=False)


class PassingCheck(MockChecker):
    """A checker that always passes the check"""

    pass
