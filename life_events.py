def married(scott, result)
    buff = 0 
    if(self.focus == 'relationships')
        buff = 2

    Pass = [
    happiness = 2
    savings = -20000
    charisma = 1
    ]

    Suceed = [


    ]

    Fail = [


    ]

  
def married(sott):
    
    


def fail_married(scott):  
    pass  # TODO: implement  
  
def pass_get_sick(scott):  
    pass  # TODO: implement  
  
def fail_get_sick(scott):  
    pass  # TODO: implement  
  
  
life_events = [  
    {  
        'description': "Get married",  
        'optional': True,  
        'requires': 15,  
        'type': 'relationship'
        'pass_text': pass_married(False)
        'suceed_text': succeed_married(False)
        'fail_text': "-1 relationships"
        'bonus': 'relationship',  
        'pass_result': pass_married,  
        'succeed_result': succeed_married(True),
        'fail_result': fail_married(True),  
    }, 
    {  
        'description': "Run Half Marathon",  
        'optional': True,  
        'requires': 6,  
        'pass_text': "No effect"
        'suceed_text': "+2 happiness, +1 fitness, -10 time"
        'fail_text': "-1 fitness, gets injured"
        'bonus': 'fitness',  
        'pass_result': pass_halfmarathon,  
        'succeed_result': suceed_halfmarathon,
        'fail_result': fail_halfmarathon,  
    }, 


    {  
        'description': "Get sick",  
        'optional': False,  
        'requires': 0,  
        'bonus': 'health',  
        'pass_result': pass_get_sick,  
        'fail_result': fail_get_sick,  
    },  
]