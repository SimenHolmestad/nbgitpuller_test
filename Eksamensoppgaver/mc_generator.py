import ipywidgets as widgets
import sys
from IPython.display import display
from IPython.display import clear_output


def generate_mc(answers,question,answer,custom_feedback=[]):
    out = widgets.Output()
    radio_options = []
    for i in range(len(answers)):
        radio_options.append((answers[i],i+1))
    
    alternativ = widgets.RadioButtons(
    options=radio_options,
    description='',
    layout=widgets.Layout(width='1500px'),
    disabled=False)
    
    print('\033[1m',question,'\033[0m')
    button = widgets.Button(description="Sjekk svaret")
    display(alternativ)
    display(button)
    def check_answer(b):
        a = int(alternativ.value)
        if(a==answer):
            color = '\x1b[6;30;42m' + "Riktig." + '\x1b[0m' +"\n" #fargen blir da grønn
        else:
            color = '\x1b[5;30;41m' + "Feil. " + '\x1b[0m' +"\n" #ellers blir fargen rød
        with out:
            clear_output()
        with out:
            print(color)
            if(len(custom_feedback)!=0):
                print(custom_feedback[a])
      
    display(out)
    button.on_click(check_answer)