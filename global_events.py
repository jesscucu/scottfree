def pass_married(scott):  
    scott.happiness += 2  
    scott.savings -= 20000  
    scott.charisma += 1  
  
def fail_married(scott):  
    pass  # TODO: implement  
  
def pass_get_sick(scott):  
    pass  # TODO: implement  
  
def fail_get_sick(scott):  
    pass  # TODO: implement  
  
  
life_events = [  
    {  
        'event': "Get married",  
        'optional': True,  
        'requires': 15,  
        'bonus': 'relationship',  
        'pass_result': pass_married,  
        'fail_result': fail_married,  
    },  
    {  
        'event': "Get sick",  
        'optional': False,  
        'requires': 0,  
        'bonus': 'health',  
        'pass_result': pass_get_sick,  
        'fail_result': fail_get_sick,  
    },  
]