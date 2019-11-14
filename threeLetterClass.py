# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:19:44 2019

@author: Keith
"""

import actr

actr.load_act_r_model("ACT-R:tutorial;unit2;dummy.lisp")

def respond_to_key_press(model, key):
    t1.response[-1] = key
    if t1.response[-1].lower() == t1.letterDict["target"].lower():
        t1.result.append(True)
    else:
        t1.result.append(False)
         
    #t1.generate_three_letters()           
    #actr.clear_exp_window()
    #t1.display_three_letters()
    #actr.modify_line_for_exp_window(t1.textIdDict[0],text="MyText")   <--not working, can we output the remote call log in actr lisp interp to see the arguments?
    #actr.schedule_event(3,"modify-text-for-exp-window",[None,*list(t1.textIdDict.values())])
               
               
    #if t1.isHuman == True:
        #t1.remove_three_letters()
        #t1.generate_three_letters()
        #t1.display_three_letters()
    
class TaskVars:
    def __init__(self):
        self.response = []
        self.result = []
        self.window = None
        self.isHuman = None
        self.trialCount = 0
        self.letterDict = {
                "t1": '',
                "t2": '',
                "t3": '',
                "target": '',
                "focus": '+',
                "shock": "TOO SLOW!"
                }
        self.textIdDict = {
                "textid1": None,
                "textid2": None,
                "textid3": None,
                #"focusid": '',
                #"shockid": ''
                }
        self.eventId = []
        
    def experiment_initialization(self):
        actr.reset()
        actr.add_command("unit2-key-press",respond_to_key_press,
                         "Assignment 2 task output-key monitor")
        actr.monitor_command("output-key","unit2-key-press")
        self.window = actr.open_exp_window("Leter difference task")
        
    def generate_three_letters(self):
        items = actr.permute_list(["B","C","D","F","G","H","J","K","L",
                                   "M","N","P","Q","R","S","T","V","W",
                                   "X","Y","Z"])
        self.letterDict["target"] = items[0]
        foil = items[1]
        self.letterDict["t1"] = foil
        self.letterDict["t2"] = foil
        self.letterDict["t3"] = foil
        index = actr.random(3)
        
        #assign a letter unique to the other two, based on a random value generated by actr
        if index == 0:
            self.letterDict["t1"] = self.letterDict["target"]
        elif index == 1:
            self.letterDict["t2"] = self.letterDict["target"]
        else:
            self.letterDict["t3"] = self.letterDict["target"]
            
    def display_three_letters(self):
        self.textIdDict["textid1"] = actr.add_text_to_exp_window(self.window, self.letterDict["t1"], x=125, y=75)
        self.textIdDict["textid2"] = actr.add_text_to_exp_window(self.window, self.letterDict["t2"], x=75, y=175)
        self.textIdDict["textid3"] = actr.add_text_to_exp_window(self.window, self.letterDict["t3"], x=175, y=175)
        #self.generate_three_letters()
        #actr.schedule_event(3,"remove-items-from-exp-window",[None,*list(self.textIdDict.values())])
        
   # def schedule_no_response():
        
    
    def experiment_cleanup(self):
        actr.remove_command_monitor("output-key","unit2-key-press")
        actr.remove_command("unit2-key-press")
    
    def remove_three_letters(self):
        actr.remove_items_from_exp_window(self.window,*list(self.textIdDict.values()))

    #def schedule_letter_deletion(self):
            #actr.schedule_event(3,"remove-items-from-exp-window",[None,*list(self.textIdDict.values())])
    
def experiment(human=False):
    t1.isHuman = human
    
    t1.experiment_initialization()
    
    
    t1.generate_three_letters()
    
    #you can pass optional parameters as a list of sublists, or as a dictionary.
    #print("schedule_event=",actr.schedule_event(.1,"add-text-to-exp-window",[None,'+',{"x": 150,"y":150}]))
    #print("schedule_event=",actr.schedule_event(.1,"add-text-to-exp-window",[None,'+',[["x",150],["y",150]]]))
    t1.display_three_letters()
    #t1.eventId.append(actr.schedule_event(1.5,"clear-exp-window"))
    #t1.eventId.append(actr.schedule_event(1.5))
    
    print("modify_text_for_exp_window=",actr.schedule_event(3,"modify-text-for-exp-window",[t1.textIdDict["textid1"],{"text":"TEST"}]))
    actr.mp_show_queue()
    t1.response.append('')
    
    if human == True:
        while t1.response[-1] == '':
            actr.process_events()   #<-- process_events() doesn't block
    else:
        actr.install_device(t1.window)
        actr.run(1,True)            #<-- run() blocks
        
    #if t1.response[-1].lower() == t1.letterDict["target"].lower():
    #    t1.result.append(True)
    #else:
    #    t1.result.append(False)
    
    #print(str([t1.window,' ','+',' ',150,' ',150]))
    #print(*list(t1.textIdDict.values()))
    
    #t1.remove_three_letters()
    
    t1.experiment_cleanup()
    
    return t1.result

t1 = TaskVars()


