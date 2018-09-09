#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b9),
    on Sun Sep  9 17:11:00 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'TBPMnBack'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/setegonz/MEGAsync/myPsychopyNback/TBPMnBack_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstructionsPractice"
InstructionsPracticeClock = core.Clock()
textPractice = visual.TextStim(win=win, name='textPractice',
    text='Você deve pressionar a tecla de espaço se a imagem na tela for a mesma da imagem imediatamente anterior.\nYou must press the space key if the image on the screen is the same as the immediately previous image.\nYou must press the M key to reset the clock each time one minute passes. \nTo find out how much time has passed since you started to see the images you can press the z key.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceTrial"
practiceTrialClock = core.Clock()
# Set a junk value for the first trial, as by definition we can't # have a one-back value there: 
one_back = 'Not applicable'
image = visual.ImageStim(
    win=win, name='image',units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
noise = visual.NoiseStim(
    win=win, name='noise',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(1, 1), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1, blendmode='avg', contrast=1.0,
    texRes=128,
    noiseType='Binary', noiseElementSize=0.0625, noiseBaseSf=8.0,
    noiseBW=1, noiseBWO=1, noiseFractalPower=0.0,noiseFilterLower=1.0, noiseFilterUpper=8.0, noiseFilterOrder=0.0, noiseClip=3.0, interpolate=False, depth=-3.0)
noise.buildNoise()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
msg='';

# Initialize components for Routine "InstructionsExperiment"
InstructionsExperimentClock = core.Clock()
textExperiment = visual.TextStim(win=win, name='textExperiment',
    text='Você deve pressionar a tecla de espaço se a imagem na tela for a mesma da imagem imediatamente anterior.\nYou must press the space key if the image on the screen is the same as the immediately previous image.\nYou must press the M key to reset the clock each time one minute passes. \nTo find out how much time has passed since you started to see the images you can press the z key.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "experimentTrial"
experimentTrialClock = core.Clock()

image_2 = visual.ImageStim(
    win=win, name='image_2',
    image=stimFile, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
noise_2 = visual.NoiseStim(
    win=win, name='noise_2',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1, blendmode='avg', contrast=1.0,
    texRes=128,
    noiseType='Binary', noiseElementSize=0.0625, noiseBaseSf=8.0,
    noiseBW=1, noiseBWO=1, noiseFractalPower=0.0,noiseFilterLower=1.0, noiseFilterUpper=8.0, noiseFilterOrder=0.0, noiseClip=3.0, interpolate=False, depth=-2.0)
noise_2.buildNoise()

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
textThanks = visual.TextStim(win=win, name='textThanks',
    text='Obrigado',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome_Screen"-------
t = 0
Welcome_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
text.setText('Bem vindo. \nLeia as instrucoes no papel.')
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
Welcome_ScreenComponents = [text, key_resp_2]
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['t'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructionsPractice"-------
t = 0
InstructionsPracticeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsPracticeComponents = [textPractice, key_resp_3]
for thisComponent in InstructionsPracticeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstructionsPractice"-------
while continueRoutine:
    # get current time
    t = InstructionsPracticeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textPractice* updates
    if t >= 0.0 and textPractice.status == NOT_STARTED:
        # keep track of start time/frame for later
        textPractice.tStart = t
        textPractice.frameNStart = frameN  # exact frame index
        textPractice.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['t'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionsPractice"-------
for thisComponent in InstructionsPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "InstructionsPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practiceBlock.csv'),
    seed=None, name='Practice')
thisExp.addLoop(Practice)  # add the loop to the experiment
thisPractice = Practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in Practice:
    currentLoop = Practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practiceTrial"-------
    t = 0
    practiceTrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    x = randint(low = 10, high = 20)
    myClock = core.Clock()  # Create the clock
    myClock.reset()  # At the relevant time, reset the clock to zero e.g., at beginning of a routine/trial
    myClock.getTime() 
    # set whatever keypress values are appropriate for this trial: 
    if stimFile == one_back:
        correct_response = 'y'
    else:
        correct_response = 'n'
    
    
    respPractice = event.BuilderKeyResponse()
    image.setImage(stimFile)
    # keep track of which components have finished
    practiceTrialComponents = [respPractice, image, noise]
    for thisComponent in practiceTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practiceTrial"-------
    while continueRoutine:
        # get current time
        t = practiceTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *respPractice* updates
        if t >= 0.0 and respPractice.status == NOT_STARTED:
            # keep track of start time/frame for later
            respPractice.tStart = t
            respPractice.frameNStart = frameN  # exact frame index
            respPractice.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(respPractice.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if respPractice.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                respPractice.keys = theseKeys[-1]  # just the last key pressed
                respPractice.rt = respPractice.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if t >= 0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *noise* updates
        if t >= 0.7 and noise.status == NOT_STARTED:
            # keep track of start time/frame for later
            noise.tStart = t
            noise.frameNStart = frameN  # exact frame index
            noise.setAutoDraw(True)
        frameRemains = 0.7 + x- win.monitorFramePeriod * 0.75  # most of one frame period left
        if noise.status == STARTED and t >= frameRemains:
            noise.setAutoDraw(False)
        if noise.status == STARTED:
            if noise._needBuild:
                noise.buildNoise()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceTrial"-------
    for thisComponent in practiceTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    one_back = stimFile
    # check responses
    if respPractice.keys in ['', [], None]:  # No response was made
        respPractice.keys=None
    Practice.addData('respPractice.keys',respPractice.keys)
    if respPractice.keys != None:  # we had a response
        Practice.addData('respPractice.rt', respPractice.rt)
    # the Routine "practiceTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if stimFile == one_back and respPractice = 'y' {
          msg="Correct! RT=" + resp.rt.toFixed(3);  }
     elif stimFile != one_back and respPractice = 'y' {
          msg="Correct! RT=" + resp.rt.toFixed(3);} 
    else      msg="Oops! That was wrong"; }
    # keep track of which components have finished
    FeedbackComponents = []
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practice'


# ------Prepare to start Routine "InstructionsExperiment"-------
t = 0
InstructionsExperimentClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsExperimentComponents = [textExperiment, key_resp_4]
for thisComponent in InstructionsExperimentComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstructionsExperiment"-------
while continueRoutine:
    # get current time
    t = InstructionsExperimentClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textExperiment* updates
    if t >= 0.0 and textExperiment.status == NOT_STARTED:
        # keep track of start time/frame for later
        textExperiment.tStart = t
        textExperiment.frameNStart = frameN  # exact frame index
        textExperiment.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['t'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionsExperiment"-------
for thisComponent in InstructionsExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "InstructionsExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ExperimentalBlocks = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('chooseBlock.csv'),
    seed=None, name='ExperimentalBlocks')
thisExp.addLoop(ExperimentalBlocks)  # add the loop to the experiment
thisExperimentalBlock = ExperimentalBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExperimentalBlock.rgb)
if thisExperimentalBlock != None:
    for paramName in thisExperimentalBlock:
        exec('{} = thisExperimentalBlock[paramName]'.format(paramName))

for thisExperimentalBlock in ExperimentalBlocks:
    currentLoop = ExperimentalBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisExperimentalBlock.rgb)
    if thisExperimentalBlock != None:
        for paramName in thisExperimentalBlock:
            exec('{} = thisExperimentalBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condsFile),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "experimentTrial"-------
        t = 0
        experimentTrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        x = randint(low = 10, high = 20)
        # keep track of which components have finished
        experimentTrialComponents = [image_2, noise_2]
        for thisComponent in experimentTrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "experimentTrial"-------
        while continueRoutine:
            # get current time
            t = experimentTrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            frameRemains = 0.0 + 0.7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_2.status == STARTED and t >= frameRemains:
                image_2.setAutoDraw(False)
            
            # *noise_2* updates
            if t >= 0.7 and noise_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                noise_2.tStart = t
                noise_2.frameNStart = frameN  # exact frame index
                noise_2.setAutoDraw(True)
            frameRemains = 0.7 + x- win.monitorFramePeriod * 0.75  # most of one frame period left
            if noise_2.status == STARTED and t >= frameRemains:
                noise_2.setAutoDraw(False)
            if noise_2.status == STARTED:
                if noise_2._needBuild:
                    noise_2.buildNoise()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experimentTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "experimentTrial"-------
        for thisComponent in experimentTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "experimentTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'ExperimentalBlocks'


# ------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = [textThanks]
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textThanks* updates
    if t >= 0.0 and textThanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        textThanks.tStart = t
        textThanks.frameNStart = frameN  # exact frame index
        textThanks.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textThanks.status == STARTED and t >= frameRemains:
        textThanks.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
