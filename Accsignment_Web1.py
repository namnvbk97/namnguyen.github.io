# create two dictionaries
from random import choice

questions={
    "strong":"Do ye like yer drinks strong?",
    "salty":"Do ye like it with a salty tang?",
    "bitter":"Are ye a lubber who likes it bitter?",
    "sweet":"Would ye like a bit of sweetness with yer poison?",
    "fruity":"Are ye one for a fruity finish?",
    }
ingredients={
    "strong":["glug of rum ","slug of whisky","splash of gin"],
    "salty":["olive on stick","salt-dusted rim","rasher of bacon"],
    "bitter":["shake of bitters","splash of tonic","twist of lemon peel"],
    "sweet":["sugar cube","spoonful of honey","spash of cola"],
    "fruily":["slice of orange","dash of cassis","cherry on top"],
    }
# input states
def input_():
    states=input("Please entering thier states :")
    return states
def output_():
    states=input_()
    while True:
        c=0;
        for menu,ques in questions.items():
            if states == menu:
                c=1;
                list_ingre=ingredients[menu]
                newques=questions[menu].replace("?"," ")+ choice(list_ingre)+"  ?"
                print(newques)
        # check states input have in menu of questions?
        if c==0:
            states=input("Entering is wrong,please again :")
        else:
            break
while True:
    output_()

            
        
