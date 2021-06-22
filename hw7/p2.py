from random import random
from psychopy import data
from p1 import stim_setup
from models import HighLowTrial


def main():
    stim_list = stim_setup()
    trial_handler = data.TrialHandler(stim_list, 20, extraInfo={
        'participant': "Nobody", 'session': '001'})

    trial = HighLowTrial(trial_handler)
    trial.start()

    trial_handler.saveAsText(fileName='testData',
                             stimOut=['pitch', 'secs', 'volume'],
                             dataOut=['RT_mean', 'RT_std', 'choice_raw'])


if __name__ == '__main__':
    main()
