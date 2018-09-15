#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b9),
    on Sat Sep 15 15:32:26 2018
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

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
import pandas as pd  
files = ['pos.xlsx', 'neg.xlsx', 'neutral.xlsx']
 # 9 images per condition 
# 3 repeats per condition  
# First, select repeating stim at random and indicate they repeat with a 1 
newStimList = pd.DataFrame() 
for f in files:
     temp = pd.read_excel(f)
     randomLocs = np.random.choice(range(temp.shape[0]), size=3, replace=False)
     temp['repeat'].iloc[randomLocs] = 1
     newStimList = newStimList.append(temp)  # Append all stim to a new dataframe, so all in one place  
# Shuffle new dataframe 
newStimList = newStimList.sample(frac=1).reset_index(drop=True) 
# Add new index to keep track of order 
newStimList = newStimList.reset_index() 
# Duplicate repeating rows 
repeats = newStimList[newStimList['repeat']==1] 
newStimList = pd.concat([repeats, newStimList], ignore_index=True).sort_values('index') 
# Save new stim list to csv ready for trial handler 
newStimList.to_csv('newStimList.csv', index=False)
textWS = visual.TextStim(win=win, name='textWS',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "InstructionsPractice"
InstructionsPracticeClock = core.Clock()
textPractice = visual.TextStim(win=win, name='textPractice',
    text='Practice\nVocê deve pressionar a tecla de espaço se a imagem na tela for a mesma da imagem imediatamente anterior.\nYou must press the space key if the image on the screen is the same as the immediately previous image.\nYou must press the M key to reset the clock each time one minute passes. \nTo find out how much time has passed since you started to see the images you can press the z key.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeRoutine"
PracticeRoutineClock = core.Clock()
imageprobando = visual.ImageStim(
    win=win, name='imageprobando',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
# Begin Experiment 
msg = ''
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "InstructionsExperiment"
InstructionsExperimentClock = core.Clock()
textExperiment = visual.TextStim(win=win, name='textExperiment',
    text='Experiment\nVocê deve pressionar a tecla de espaço se a imagem na tela for a mesma da imagem imediatamente anterior.\nYou must press the space key if the image on the screen is the same as the immediately previous image.\nYou must press the M key to reset the clock each time one minute passes. \nTo find out how much time has passed since you started to see the images you can press the z key.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "readyMessage"
readyMessageClock = core.Clock()
textTask = visual.TextStim(win=win, name='textTask',
    text='Bloque nuevo',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "valencedTrial"
valencedTrialClock = core.Clock()

image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
noise = visual.NoiseStim(
    win=win, name='noise',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1, blendmode='avg', contrast=1.0,
    texRes=128,
    noiseType='Binary', noiseElementSize=0.0625, noiseBaseSf=8.0,
    noiseBW=1, noiseBWO=1, noiseFractalPower=0.0,noiseFilterLower=1.0, noiseFilterUpper=8.0, noiseFilterOrder=0.0, noiseClip=3.0, interpolate=False, depth=-2.0)
noise.buildNoise()

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

# ------Prepare to start Routine "WelcomeScreen"-------
t = 0
WelcomeScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

textWS.setText('Bem vindo. \nLeia as instrucoes no papel.')
respWS = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeScreenComponents = [textWS, respWS]
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *textWS* updates
    if t >= 0.0 and textWS.status == NOT_STARTED:
        # keep track of start time/frame for later
        textWS.tStart = t
        textWS.frameNStart = frameN  # exact frame index
        textWS.setAutoDraw(True)
    
    # *respWS* updates
    if t >= 0.0 and respWS.status == NOT_STARTED:
        # keep track of start time/frame for later
        respWS.tStart = t
        respWS.frameNStart = frameN  # exact frame index
        respWS.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(respWS.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if respWS.status == STARTED:
        theseKeys = event.getKeys(keyList=['t'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            respWS.keys = theseKeys[-1]  # just the last key pressed
            respWS.rt = respWS.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if respWS.keys in ['', [], None]:  # No response was made
    respWS.keys=None
thisExp.addData('respWS.keys',respWS.keys)
if respWS.keys != None:  # we had a response
    thisExp.addData('respWS.rt', respWS.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructionsPractice"-------
t = 0
InstructionsPracticeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
respPract = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsPracticeComponents = [textPractice, respPract]
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
    
    # *respPract* updates
    if t >= 0.0 and respPract.status == NOT_STARTED:
        # keep track of start time/frame for later
        respPract.tStart = t
        respPract.frameNStart = frameN  # exact frame index
        respPract.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(respPract.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if respPract.status == STARTED:
        theseKeys = event.getKeys(keyList=['t'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            respPract.keys = theseKeys[-1]  # just the last key pressed
            respPract.rt = respPract.clock.getTime()
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
if respPract.keys in ['', [], None]:  # No response was made
    respPract.keys=None
thisExp.addData('respPract.keys',respPract.keys)
if respPract.keys != None:  # we had a response
    thisExp.addData('respPract.rt', respPract.rt)
thisExp.nextEntry()
# the Routine "InstructionsPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsPractice = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('newStimList.csv'),
    seed=None, name='trialsPractice')
thisExp.addLoop(trialsPractice)  # add the loop to the experiment
thisTrialsPractice = trialsPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice.rgb)
if thisTrialsPractice != None:
    for paramName in thisTrialsPractice:
        exec('{} = thisTrialsPractice[paramName]'.format(paramName))

for thisTrialsPractice in trialsPractice:
    currentLoop = trialsPractice
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice.rgb)
    if thisTrialsPractice != None:
        for paramName in thisTrialsPractice:
            exec('{} = thisTrialsPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PracticeRoutine"-------
    t = 0
    PracticeRoutineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    imageprobando.setImage(stim)
    respPrac = event.BuilderKeyResponse()
    # keep track of which components have finished
    PracticeRoutineComponents = [imageprobando, respPrac]
    for thisComponent in PracticeRoutineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "PracticeRoutine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeRoutineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageprobando* updates
        if t >= 0.0 and imageprobando.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageprobando.tStart = t
            imageprobando.frameNStart = frameN  # exact frame index
            imageprobando.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if imageprobando.status == STARTED and t >= frameRemains:
            imageprobando.setAutoDraw(False)
        
        # *respPrac* updates
        if t >= 0.0 and respPrac.status == NOT_STARTED:
            # keep track of start time/frame for later
            respPrac.tStart = t
            respPrac.frameNStart = frameN  # exact frame index
            respPrac.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(respPrac.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 1.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if respPrac.status == STARTED and t >= frameRemains:
            respPrac.status = STOPPED
        if respPrac.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                respPrac.keys = theseKeys[-1]  # just the last key pressed
                respPrac.rt = respPrac.clock.getTime()
                # was this 'correct'?
                if (respPrac.keys == str('')) or (respPrac.keys == ''):
                    respPrac.corr = 1
                else:
                    respPrac.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeRoutine"-------
    for thisComponent in PracticeRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respPrac.keys in ['', [], None]:  # No response was made
        respPrac.keys=None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           respPrac.corr = 1;  # correct non-response
        else:
           respPrac.corr = 0;  # failed to respond (incorrectly)
    # store data for trialsPractice (TrialHandler)
    trialsPractice.addData('respPrac.keys',respPrac.keys)
    trialsPractice.addData('respPrac.corr', respPrac.corr)
    if respPrac.keys != None:  # we had a response
        trialsPractice.addData('respPrac.rt', respPrac.rt)
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # Begin Routine 
    if trialsPractice.thisN == 0:
         one_back = 'Not applicable'
    text.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [text]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # End Routine
    if stim == one_back and respPrac.keys == 'space':
         msg= "Correct! RT=%.3f" %(respPrac.rt)
    elif stim != one_back and not respPrac.keys:
          msg= "Correct!" 
    elif stim != one_back and respPrac.keys == 'space':
         msg="Incorrect" 
    elif stim == one_back and not respPrac.keys:
         msg="You miss that one" 
    one_back = stim
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialsPractice'


# ------Prepare to start Routine "InstructionsExperiment"-------
t = 0
InstructionsExperimentClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
respExpText = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsExperimentComponents = [textExperiment, respExpText]
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
    
    # *respExpText* updates
    if t >= 0.0 and respExpText.status == NOT_STARTED:
        # keep track of start time/frame for later
        respExpText.tStart = t
        respExpText.frameNStart = frameN  # exact frame index
        respExpText.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(respExpText.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if respExpText.status == STARTED:
        theseKeys = event.getKeys(keyList=['t'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            respExpText.keys = theseKeys[-1]  # just the last key pressed
            respExpText.rt = respExpText.clock.getTime()
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
if respExpText.keys in ['', [], None]:  # No response was made
    respExpText.keys=None
thisExp.addData('respExpText.keys',respExpText.keys)
if respExpText.keys != None:  # we had a response
    thisExp.addData('respExpText.rt', respExpText.rt)
thisExp.nextEntry()
# the Routine "InstructionsExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
conditionsLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('chooseBlock.csv', selection='0:2'),
    seed=None, name='conditionsLoop')
thisExp.addLoop(conditionsLoop)  # add the loop to the experiment
thisConditionsLoop = conditionsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConditionsLoop.rgb)
if thisConditionsLoop != None:
    for paramName in thisConditionsLoop:
        exec('{} = thisConditionsLoop[paramName]'.format(paramName))

for thisConditionsLoop in conditionsLoop:
    currentLoop = conditionsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisConditionsLoop.rgb)
    if thisConditionsLoop != None:
        for paramName in thisConditionsLoop:
            exec('{} = thisConditionsLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "readyMessage"-------
    t = 0
    readyMessageClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    respTask = event.BuilderKeyResponse()
    # keep track of which components have finished
    readyMessageComponents = [textTask, respTask]
    for thisComponent in readyMessageComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "readyMessage"-------
    while continueRoutine:
        # get current time
        t = readyMessageClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textTask* updates
        if t >= 0.0 and textTask.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTask.tStart = t
            textTask.frameNStart = frameN  # exact frame index
            textTask.setAutoDraw(True)
        
        # *respTask* updates
        if t >= 0.0 and respTask.status == NOT_STARTED:
            # keep track of start time/frame for later
            respTask.tStart = t
            respTask.frameNStart = frameN  # exact frame index
            respTask.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(respTask.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if respTask.status == STARTED:
            theseKeys = event.getKeys(keyList=['t'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                respTask.keys = theseKeys[-1]  # just the last key pressed
                respTask.rt = respTask.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in readyMessageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "readyMessage"-------
    for thisComponent in readyMessageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respTask.keys in ['', [], None]:  # No response was made
        respTask.keys=None
    conditionsLoop.addData('respTask.keys',respTask.keys)
    if respTask.keys != None:  # we had a response
        conditionsLoop.addData('respTask.rt', respTask.rt)
    # the Routine "readyMessage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    experimentalLoop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condsFile),
        seed=None, name='experimentalLoop')
    thisExp.addLoop(experimentalLoop)  # add the loop to the experiment
    thisExperimentalLoop = experimentalLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExperimentalLoop.rgb)
    if thisExperimentalLoop != None:
        for paramName in thisExperimentalLoop:
            exec('{} = thisExperimentalLoop[paramName]'.format(paramName))
    
    for thisExperimentalLoop in experimentalLoop:
        currentLoop = experimentalLoop
        # abbreviate parameter names if possible (e.g. rgb = thisExperimentalLoop.rgb)
        if thisExperimentalLoop != None:
            for paramName in thisExperimentalLoop:
                exec('{} = thisExperimentalLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "valencedTrial"-------
        t = 0
        valencedTrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        x = randint(low = 1, high = 5)
        image_2.setImage(stimFile)
        # keep track of which components have finished
        valencedTrialComponents = [image_2, noise]
        for thisComponent in valencedTrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "valencedTrial"-------
        while continueRoutine:
            # get current time
            t = valencedTrialClock.getTime()
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
            for thisComponent in valencedTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "valencedTrial"-------
        for thisComponent in valencedTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "valencedTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'experimentalLoop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'conditionsLoop'


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
