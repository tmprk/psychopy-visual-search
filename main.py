import os
import math
import numpy as np
from datetime import datetime
from psychopy import visual, core, data, event
from enum import Enum
from stim import Stimulus

# todo add a prompt to college participant name
global_clock = core.MonotonicClock() # initialize clock at the start of the experiment
filename = u'data/{0}_{1}'.format('test', datetime.today().strftime('%Y-%m-%d_%H-%M-%S'))
directory_path = os.getcwd()
expt = data.ExperimentHandler(name='Visual Search', version='1.0.0', originPath=directory_path, saveWideText=True,
    dataFileName=filename)
expt.addData('experiment_start', global_clock.getTime())

elements_per_stimulus = [12]
# elements_per_stimulus = [8, 12, 16, 20]
mainWindow = visual.Window(size=[1280, 800], monitor='testMonitor', fullscr=False, useRetina=True, pos=[0, 0], color='black', units='deg')


class trialtype(Enum):
    NO_DISTRACTOR = 0
    DISTRACTOR_MATCHED = 1
    DISTRACTOR_MISMATCHED = 2


def setattrs(_self, **kwargs):
    for k,v in kwargs.items():
        setattr(_self, k, v)


def create_distribution(size):
    distractors_matched = distractors_mismatched = int(size * 0.25)
    nondistractors = size - (distractors_matched + distractors_mismatched)
    # print('distractors:', distractors_matched)
    # print('distractors_mismatched:', distractors_mismatched)
    # print('nondistractors:', nondistractors)
    arr = np.array([0] * int(nondistractors) + [1] * int(distractors_matched) + [2] * int(distractors_mismatched))
    np.random.shuffle(arr)
    return arr


# https://stackoverflow.com/questions/23411688/drawing-polygon-with-n-number-of-sides-in-python-3-2
def polygon(sides, radius=6, rotation=0, translation=None):
    one_segment = math.pi * 2 / sides
    points = [
        (math.sin(one_segment * i + rotation) * radius,
         math.cos(one_segment * i + rotation) * radius)
        for i in range(sides)]
    if translation:
        points = [[sum(pair) for pair in zip(point, translation)] for point in points]
    return points


# function to run a single routine
def run_routine(trial_type):
    running = True
    correct_answer = None
    event.clearEvents(eventType='keyboard')
    expt.addData('routine_start', global_clock.getTime()) # or maybe use separate clock?

    number_of_elements = np.random.choice(elements_per_stimulus)
    stimulus_array = [Stimulus() for _ in range(number_of_elements)]
    coordinates_array = polygon(number_of_elements)
    # todo store the correct answer depending on the condition

    if trial_type == trialtype.NO_DISTRACTOR:
        print('no distractor, set all to green')
        # If the trial type is no distractor, all green and random orientation of target line
        # populate shape_array with number_of_elements, all green. One square as the target at a random location and the rest circles.

        # make all of the stimuli green for the first condition
        for element in stimulus_array:
            setattr(element, 'color', 'green')
        
        # randomize the location of the target
        setattrs(stimulus_array[np.random.randint(0, len(stimulus_array) - 1)], shape='square')
    else:
        print('distractor is present, one of two cases. set all to red\n')
        for element in stimulus_array:
            setattr(element, 'color', 'red')
        
        # creates distractor by setting to green
        setattrs(stimulus_array[np.random.randint(0, len(stimulus_array) - 1)], color='green', distractor=True)

        # create the target (a square) but make sure it's not the distractor
        np.random.choice([item for item in stimulus_array if item.distractor == False]).shape = 'square'

        itemToChange = [x for x in stimulus_array if x.distractor == True][0]
        targetItem = [x for x in stimulus_array if x.shape == 'square'][0]
        if trial_type == trialtype.DISTRACTOR_MATCHED:
            # If the trial type is a distractor matched, make all red and one green with same orientation as target line
            print('distractor matched\n')
            itemToChange.orientation = targetItem.orientation
        elif trial_type == trialtype.DISTRACTOR_MISMATCHED:
            # If the trial type is a distractor non-matched, make all red and one green with different orientations as target lines
            print('distractor mismatched')
            itemToChange.orientation = targetItem.orientation + 90
        correct_answer = 'horizontal' if (itemToChange.orientation == 45) else 'vertical'

    for index, element in enumerate(stimulus_array):
        element.position = coordinates_array[index]

    fixation_stimulus = visual.GratingStim(win=mainWindow, mask='cross', size=0.5, pos=[0,0], sf=0, color='white')
    fixation_stimulus.draw()
    print('number of shapes:', len(stimulus_array), '\n')
    
    for stimulus in stimulus_array:
        print(stimulus)
        if stimulus.shape == 'circle':
            circle = visual.Circle(win=mainWindow, lineColor=stimulus.color, pos=stimulus.position, lineWidth=4)
            circle.draw()
            line = visual.Line(win=mainWindow, pos=stimulus.position, ori=stimulus.orientation, lineColor='white', size=0.5, lineWidth=4)
            line.draw()
        else:
            square = visual.Rect(win=mainWindow, lineColor=stimulus.color, pos=stimulus.position, size=1, lineWidth=4)
            square.draw()
            line = visual.Line(win=mainWindow, pos=stimulus.position, ori=stimulus.orientation, lineColor='white', size=0.5, lineWidth=4)
            line.draw()
            
    mainWindow.flip()
    startTime = global_clock.getTime() # todo: get the time when stimuli are drawn
    expt.addData('stimuli_presented', startTime)

    while running:
        if event.getKeys(keyList=["escape"], timeStamped=False):
            print('quitting')
            mainWindow.close()
            core.quit()
        
        response = event.getKeys(keyList=['z', 'm'], timeStamped=global_clock)
        for key in response:
            print(key)
            letter = key[0]
            timestamp = key[1]
            if letter == 'z' or letter == 'm':
                print('z or m')
                expt.addData('key_press', letter)
                expt.addData('orientation', 'horizontal') # or vertical
                expt.addData('response_time', timestamp)
                running = False
        
    expt.addData('correct_answer', correct_answer)
    expt.nextEntry()
    # todo: RT = (time stimuli appear) - (time keystroke is detected)

# returns array of [0s, 1s, and 2s], 0 being no distractor, 1 being distractor with matching line, and 2 being distractor mismatching
# half have distractors, half of the distractors' target and distractor's are mismatched. 0.5, 0.25, 0.25 but shuffled
# sequence = create_distribution(4)
sequence = [0, 1]
print('sequence', sequence)

if __name__ == '__main__':
    for item in sequence:
        run_routine(trialtype(item))