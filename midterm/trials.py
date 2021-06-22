

from base import BaseTrial
from mixins import SequenceMemoryMixin, ChimpTestMixin, VirtualMemoryMixin


class TrialWrapper(object):
    def __init__(self, *args):
        self._list = []

    def register(self, trial_list):
        self._list = trial_list

    def start(self):
        for trial in self._list:
            if isinstance(trial, BaseTrial):
                trial.start()
                del trial


class SequenceMemoryTrial(SequenceMemoryMixin, BaseTrial):
    pass


class ChimpTestTrial(ChimpTestMixin, BaseTrial):
    pass


class VirtualMemoryTrial(VirtualMemoryMixin, BaseTrial):
    pass
