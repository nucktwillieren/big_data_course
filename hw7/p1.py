from random import random
from psychopy import data


def stim_setup():
    stim_list = []
    for pitch in ['A', 'G']:
        for secs in [0.5, 2.0]:
            for volume in [0.5, 1.0]:
                stim_list.append(
                    {'pitch': pitch, 'secs': secs, "volume": volume})

    return stim_list[:]


def main():
    stim_list = stim_setup()
    trials = data.TrialHandler(stim_list, 20, extraInfo={
                               'participant': "Nobody", 'session': '001'})

    for index, trial in enumerate(trials):
        random_rt = random() + float(trial['secs'])
        random_choice = round(random())
        trials.data.add('RT', random_rt)
        trials.data.add('choice', random_choice)

        print(
            f"Trial {index+1} ({trials.thisIndex} in the list) (pitch={trial['pitch']}, secs={trial['secs']}, volume={trial['volume']})")

    trials.saveAsText(fileName='testData',
                      stimOut=['pitch', 'secs', 'volume'],
                      dataOut=['RT_mean', 'RT_std', 'choice_raw'])


if __name__ == '__main__':
    main()
