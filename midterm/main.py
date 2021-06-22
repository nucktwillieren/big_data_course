from trials import TrialWrapper, SequenceMemoryTrial, ChimpTestTrial, VirtualMemoryTrial
from psychopy import visual
from win32api import GetSystemMetrics


def main():
    # win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(
    #    1)), units="pix", fullscr=True, color=[-0.656, 0.08, 0.672])
    #wrapper = TrialWrapper()
    # wrapper.register([
    #    SequenceMemoryTrial(turns=3, win=win),
    #    ChimpTestTrial(turns=1, win=win),
    #    VirtualMemoryTrial(turns=3, win=win)
    # ])
    # wrapper.register([VirtualMemoryTrial(turns=3, win=win)])
    # wrapper.register([ChimpTestTrial(turns=3, win=win)])
    # wrapper.start()
    VirtualMemoryTrial(turns=3).start()
    ChimpTestTrial(turns=3).start()
    SequenceMemoryTrial(turns=3).start()


if __name__ == '__main__':
    main()
