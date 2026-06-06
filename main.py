# TODO: add your imports here, e.g.:  
# import random  
  
from life_events import life_events  
from global_events import global_events
  
  
class Scott:  
  
    def __init__(self):  
        self.age = 30  
        self.focus = "relationships"
        self.scores = {  
            'networth': 
            'relationships': 0,  
            'career': 0,  
            'happiness': 0,  
            'health': 0,  
        }  
        self.stats = {  
            'income': 80000,  
            'savings'
            'luck': 4,  
            'charisma': 2,  
            'fitness': 2,  
            'time': 3,  
            'intelligence': 4,  
        }  
        
        self.investments = [
            initial_fund = 0
            interest_rate = 0.02
            years = 0;
            current_value = 0;
        ]
            
        }

    def print_stats(self):
        print("Age: ", self.age)

        current_score = self.networth + 

        print("Current Score: ")
        print("  Net Worth: ", self.networth)
        print("       Savings      : " self.scores.savings)
        print("     + Income       : " self.stats.income)
        print("     + Investments  : ")
        coutner = 1
        for funds in investents:
            print("       (", counter, ")  Current Value: $", current_value, " at ", interest_rate, "% annual")

        print("  Relationships: ", self.networth)
       
        print("    ", self.savings)

  
    def next_age(self):  
        self.age += 1  
        self.scores.savings = self.scores.savings + self.scores.income  

        print("Age: ", self.age)
        print("Current Stats:")
        print("Savings: ")

        self.earn()  
        self.buy_sell()  
        self.process_life_events()  
        self.process_global_events()  


    def print_event(self, event):
        print("Event: " event.description)
        print("Requires: ", event.requires)
        print("Buff: Dice Roll + " event.buff)

       
        if(event.optional == True):
            print("Optional")
        else:
            print("Mandetory")
        
        print("If Pass: ", event.pass_text)  # Don't take optional event
        print("If Succeed: ", event.suceed_text) # Roll at or above required
        print("If Fail: ", event.fail_text) # Roll below required 


    def print_rules(self):
        print("SCOTT FREE")
        print("How to play...")
        print("Each turn is one year of your life. Each year so get to preform 3 actions.")
        print("1. Buy or sell investments, real estate etc.")
        print("2. Choose at least 1 and up to 3 life events to improve your scores")
        self.print_event(life_events[1])
        print("3. Randomly draw 1 life event and 1 global events")
        self.print_event(global_evenst[1])

        print("Every event requires a dice roll for pass or fail. Each event will be bufferd by a specific stat")
        print("Final score is: ")
        print("Net worth + [(relationships + career + happiness + health) * 1000]")    
        print("Focus doubles the score from that cateogry") 
  
    def choose_focus(self):

        print("Please choose your life focus: ")

        #Get input from user. Can be any of these options 
        1. Relationship
        - charisma = +2
        - more likely to receive relationship life_events
        - doubles relationships score
        2. Career
        - greater base salary
        - more likely to receive promotions
        - less time 
        - doubles career score
        3. Pursuits. 
        - time = 2
        - intellignce = 2
        - doubles happiness score
        - get 4 life options to choose from each turn

        # Accept user input and repeat back response

        # Print current stats here before beggining: 


    def earn(self):
        self.scores.savings = self.scores.savings + self.scores.income  

        for funds in investments (
            self.current_value = self.initial_value * years * interest_rate
        )

        self.investments = 
        self.networth = 
  
    def buy_sell(self): 

        # Randomly generate an interest rate between 0.1-0.6% 
        
        if input 

        pass  # TODO: implement  
  
    def process_life_events(self):  
        pass  # TODO: implement  
  
    def process_global_events(self):  
        pass  # TODO: implement  
  
  
if __name__ == "__main__":  
    scott = Scott()  
    scott.choose_focus()

    for i in range(30,60):
        scott.next_age()