#flanker test
#practice trail n=5
#one stimulus
#mask, directly before typing
#30/60 to type
#1 extra hour from email

import json
import os, random
import pandas as pd
from psychopy import core, gui, visual, event, data
import random
import numpy as np
path = r"stim_abridged.xlsx"
assert os.path.isfile(path)
with open(path, "r") as f:
    dataframe1 = pd.read_excel('stim_abridged.xlsx', sheet_name="Words")
    
my_directory = os.getcwd()
timetoprocess = 30

## make a data folder (if it does not yet exist)
directory_to_write_to = my_directory + "/Data" 
if not os.path.isdir(directory_to_write_to):
    os.mkdir(directory_to_write_to)

## present a dialog box with a 'unique' participant number
info = {"Nummer": random.randint(0, 99999), "Leeftijd": 18, "Geslacht": ["Man", "Vrouw", "Anders"], "Moedertaal": "Nederlands", "Proficiënt in Nederlands": ["Ja", "Nee"], "Handigheid": ["Rechts", "Links", "Ambidexter"]}
already_exists  = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Recall Task")
    file_name = str(directory_to_write_to + "/data_recall_" + "PPN_" + str(info["Nummer"]))
    ##verify whether file name exists
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
        f = open(file_name, "x")
        with open(file_name, "w") as f:
            f.write(json.dumps(info))
    ##ask for a new participant number if already in use
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Oops, this number is already in use! Choose a different number.")
        myDlg2.show()


Resp = []
rt_list = []
Direction = []
n_trials = 240
dataframe2 = pd.DataFrame(dataframe1).to_numpy()
#trials=len(dataframe2)
dataframe3 = pd.DataFrame(dataframe1).to_numpy()
trials=n_trials
trialdata = np.zeros((trials*2, 5), dtype=int, order="C")
np.random.shuffle(dataframe2)
np.random.shuffle(dataframe3)

dimensions = dataframe2.shape
rows, columns = dimensions
stim_list = []
con_list = []
for i in range(rows): 
    item = dataframe2[i]
    con_list.append(item[1])
    stim_list.append(item[0])
dimensions_c = dataframe2.shape
rows_c, columns_c = dimensions
for i in range(rows_c): 
    item = dataframe3[i]
    con_list.append(item[1])
    stim_list.append(item[0])
    

print(con_list, len(stim_list))


window = visual.Window(color = "white", fullscr = True)
message  = visual.TextStim(window, color="red", text = "Please type something.")
welcome = "Welkom tot het experiment. Als het nodig is om het experiment vroegtijdig geforceerd te stoppen, druk op Escape. Druk niet op Escape om gewoon te stoppen, het experiment stopt vanzelf. \n\n U zal steeds een niet-bestaande woord op het scherm zien. Probeer het zo goed mogelijk te onthouden, het wordt daarna vervangen door een masker (#####). Vanaf je dit masker ziet, kan je het woord overtypen. Wanneer u klaar bent met typen, druk op enter.\n\n Druk op spatie om te beginnen met de oefentrails."
mask = visual.TextStim(window, color="black", text = "#####")
typeinstr = "Typ hier het linkse woord."
typeinstr_alt = "Typ hier het rechtse woord."
asterisk = visual.TextStim(window, color="black", text = "+")
messagetext = visual.TextStim(window, color="black", text = message)
instructions = visual.TextStim(window, color ="black", text = welcome)
instructions.draw()
window.flip()
event.waitKeys(keyList=['space'])
timer=core.Clock()
counter = 0
practicelist=["xnevb", "vmaxj", "vkuvm", "zqovm", "vtuxn"] #none of these appear in the actual experiment


#practicetrails
for i in range(5):
    if i == 0:
        countdown = visual.TextStim(window, color="black", text= "Starting in 3...")
        window.flip()
        countdown.draw()
        core.wait(1)
        countdown = visual.TextStim(window, color="black", text= "Starting in 2...")
        window.flip()
        countdown.draw()
        core.wait(1)
        countdown = visual.TextStim(window, color="black", text= "Starting in 1...")
        window.flip()
        countdown.draw()
        core.wait(1)
        countdown = visual.TextStim(window, color="black", text= "Starting in 0...")
        window.flip()
        countdown.draw()
        core.wait(0.5) #same time as fixation
        window.flip()
        
    practicestim = visual.TextStim(window, color="black", text= practicelist[i])
    practicestim.draw()
    window.flip()
    core.wait(0.1)
    mask.draw()
    window.flip()
    core.wait(0.1)
    typedText = ''
    textEntryCompleted = False
    showText = visual.TextStim(window, text=typedText, pos=(0,-.5), color=(-1,-1,-1), height=0.1)
    timer.reset()
    while not textEntryCompleted and not timer.getTime() >timetoprocess:
        keyPressed = event.waitKeys()
        if keyPressed != None and not timer.getTime() >timetoprocess:
            if 'return' in keyPressed:
                if not typedText == "":
                    textEntryCompleted = True
                else:
                    message.draw()
                    window.flip()
                    core.wait(0.3)
            elif 'space' in keyPressed:
                typedText = typedText + ' '
            elif 'backspace' in keyPressed:
                typedText = typedText[:-1]
            elif 'escape' in keyPressed:
                window.close()
            else:
                typedText = typedText + keyPressed[-1]
           
            showText.text = typedText
            showText.draw()
            window.flip()
        else:
            showText.text = typedText
            showText.draw()
            window.flip()
    asterisk.draw()
    window.flip()
    core.wait(0.5)

instr_experiment = visual.TextStim(window, color="black", text= "We beginnen nu met de echte trails. Druk op de spatieknop om door te gaan.")
instr_experiment.draw()
window.flip()
event.waitKeys(keyList=['space'])


for element in range(n_trials):
    if element == 0:
        countdown = visual.TextStim(window, color="black", text= "Starting in 3...")
        window.flip()
        countdown.draw()
        core.wait(1)
        countdown = visual.TextStim(window, color="black", text= "Starting in 2...")
        window.flip()
        countdown.draw()
        core.wait(1)
        countdown = visual.TextStim(window, color="black", text= "Starting in 1...")
        window.flip()
        countdown.draw()
        core.wait(1)
        countdown = visual.TextStim(window, color="black", text= "Starting in 0...")
        window.flip()
        countdown.draw()
        core.wait(0.5) #same time as fixation
        window.flip()
        
    if element == 60:
        block = visual.TextStim(window, color="black", text = "Dit is het einde van Block 1. Je kunt even pauze nemen. Druk op de spatie om met Block 2 te beginnen.")
        block.draw()
        window.flip()
        event.waitKeys(keyList=['space'])
    if element == 120:
        block = visual.TextStim(window, color="black", text = "Dit is het einde van Block 2. Je bent halverwege. Je kunt even pauze nemen. Druk op de spatie om met Block 3 te beginnen.")
        block.draw()
        window.flip()
        event.waitKeys(keyList=['space'])
    if element == 180:
        block = visual.TextStim(window, color="black", text = "Dit is het einde van Block 3. Je kunt even pauze nemen. Druk op de spatie om met de laatste block te beginnen.")
        block.draw()
        window.flip()
        event.waitKeys(keyList=['space'])

    expstim = visual.TextStim(window, text = stim_list[element], color="black")
    expstim.draw()
    window.flip()
    core.wait(0.1)
    mask.draw()
    window.flip()
    core.wait(0.1)
    typedText = ''
    textEntryCompleted = False
    showText = visual.TextStim(window, text=typedText, pos=(0,-.5), color=(-1,-1,-1), height=0.1)
    timer.reset()
    while not textEntryCompleted and not timer.getTime() >timetoprocess:
        keyPressed = event.waitKeys()
        if keyPressed != None and not timer.getTime() >timetoprocess:
            if 'return' in keyPressed:
                if not typedText == "":
                    textEntryCompleted = True
                else:
                    message.draw()
                    window.flip()
                    core.wait(0.3)
            elif 'space' in keyPressed:
                typedText = typedText + ' '
            elif 'backspace' in keyPressed:
                typedText = typedText[:-1]
            elif 'escape' in keyPressed:
                window.close()
            else:
                typedText = typedText + keyPressed[-1]
           
            showText.text = typedText
            showText.draw()
            window.flip()
        else:
            showText.text = typedText
            showText.draw()
            window.flip()
    Resp.append(typedText)
    rt_list.append(timer.getTime())
    asterisk.draw()
    window.flip()
    core.wait(0.5)
    


print(stim_list, con_list, Resp, rt_list)
fulldata = np.column_stack([stim_list, con_list, Resp, rt_list])        

fulldata_frame = pd.DataFrame(fulldata)
fulldata_frame.to_csv(str(info["Nummer"]) +"data")

end = "Je bent op het einde van het experiment!\n Bedankt om deel te nemen. Experiment eindigt automatisch."
endshow = visual.TextStim(window, color ="black", text = end)
endshow.draw()
window.flip()
core.wait(2)
window.close