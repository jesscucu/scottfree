import random  
from life_events import life_events, format_result, apply_result  
# from global_events import global_events  
  
SEP  = "-" * 52  
WIDE = "=" * 52  
  
  
class Scott:  
  
    def __init__(self):  
        self.age     = 30  
        self.focus   = None  
        self.savings = 100000  
  
        self.scores = {  
            "relationships": 0,  
            "career":        0,  
            "happiness":     0,  
            "health":        0,  
        }  
  
        self.stats = {  
            "income":       20000,  
            "luck":         4,  
            "charisma":     2,  
            "fitness":      2,  
            "time":         3,  
            "intelligence": 4,  
        }  
  
        # Each investment: {"initial_value": int, "interest_rate": float, "years": int, "current_year": int}  
        self.investments = []  
  
    @property  
    def networth(self):  
        investment_value = sum(  
            inv["initial_value"] * ((1 + inv["interest_rate"]) ** inv["current_year"])  
            for inv in self.investments  
        )  
        return self.savings + investment_value 
  
    # ------------------------------------------------------------------ #  
    #  Display                                                             #  
    # ------------------------------------------------------------------ #  
  
    def print_stats(self):  
        print(WIDE)  
        print(f"  AGE: {self.age}  |  FOCUS: {self.focus or 'None'}")  
        print(WIDE)  
        print(f"  NET WORTH:      ${self.networth:>12,.0f}")  
        print(f"    Savings:      ${self.savings:>12,.0f}")  
        print(f"    Income/yr:    ${self.stats['income']:>12,.0f}")  
        if self.investments:  
            print("    Investments:")  
            for i, inv in enumerate(self.investments, 1):  
                current = inv["initial_value"] * ((1 + inv["interest_rate"]) ** inv["current_year"])  
                print(f"      ({i}) ${current:>10,.0f}  at {inv['interest_rate']*100:.1f}% annual")  
        print(SEP)  
        print("  LIFE SCORES:")  
        for score, value in self.scores.items():  
            print(f"    {score.capitalize():<16} {value:>4}")  
        print(SEP)  
        print("  STATS:")  
        for stat, value in self.stats.items():  
            print(f"    {stat.capitalize():<16} {value:>4}")  
        print(WIDE)  
  
    def print_event(self, event):  
        print(SEP)  
        tag = "[OPTIONAL]" if event["optional"] else "[MANDATORY]"  
        print(f"  {tag}  {event['description']}")  
        buff_stat  = event.get("buff_stat", "")  
        buff_value = self.stats.get(buff_stat, 0)  
        focus_bonus = 2 if self.focus == event.get("type") else 0  
        bonus_str = f"  |  Focus bonus: +{focus_bonus}" if focus_bonus else ""  
        print(f"  Requires: {event['requires']}  |  Buff: +{buff_value} ({buff_stat}){bonus_str}")  
        results = event.get("results", {})  
        if event["optional"]:  
            print(f"  Skip:     {format_result(results.get('pass', {}))}")  
        print(f"  Succeed:  {format_result(results.get('succeed', {}))}")  
        print(f"  Fail:     {format_result(results.get('fail', {}))}")  
        print(SEP)  
  
    def print_rules(self):  
        print(WIDE)  
        print("  SCOTT FREE  -  HOW TO PLAY")  
        print(WIDE)  
        print("  Each turn = one year of your life.\n")  
        print("  Each year you:")  
        print("  1. Buy or sell investments")  
        print("  2. Choose 1-3 life events to attempt")  
        print("  3. Randomly draw 2 mandetory events\n")  
        
        
        print("  Investment interest rates are generated randomly every turn")
        print()
        print("  Every event you roll a D20 + buffered stat to determine success or failure")
        print("  Sucess: (roll + buff) >= required;    Fail: (roll + buff) < required")  
        print()
        print("  At the start of the game you get to choose your life focus")
        print("  Focus increases the probability of receiving those events and changes your starting buffs")
        
        print()  
        print("  STARTING BUFFS:")  
        for key, value in self.stats.items():  
            print("    ", key, value)  

        print()  
        print("  SCORE CATEGORIES:")  
        for key, value in self.scores.items():  
            print("    ", key, value)

        print()
        print("  FINAL SCORE:")  
        print("  Net Worth + [(relationships + career + happiness + health) x 1000]")  
        print("  Your focus doubles the score from that category.\n")  
        print("  EXAMPLE EVENTS:")  
        for event in life_events[:2]:  
            self.print_event(event)  
        print(WIDE)  
  
    # ------------------------------------------------------------------ #  
    #  Setup                                                               #  
    # ------------------------------------------------------------------ #  
  
    def choose_focus(self):  
        print(WIDE)  
        print("  CHOOSE YOUR LIFE FOCUS")  
        print(WIDE)  
        print("  1. Relationships")  
        print("     +2 charisma | more relationship events | doubles relationships score\n")  
        print("  2. Career")  
        print("     +$20,000 income | more career events | doubles career score | -1 time\n")  
        print("  3. Pursuits")  
        print("     +2 time, +2 intelligence | doubles happiness score | 4 event choices/turn\n")  
  
        while True:  
            choice = input("  Enter 1, 2, or 3: ").strip()  
            if choice == "1":  
                self.focus = "relationships"  
                self.stats["charisma"] += 2  
                break  
            elif choice == "2":  
                self.focus = "career"  
                self.stats["income"] += 20000  
                self.stats["time"] -= 1  
                break  
            elif choice == "3":  
                self.focus = "pursuits"  
                self.stats["time"] += 2  
                self.stats["intelligence"] += 2  
                break  
            else:  
                print("  Please enter 1, 2, or 3.")  
  
        print(f"\n  Focus set to: {self.focus.capitalize()}\n")  
        self.print_stats()  
  
    # ------------------------------------------------------------------ #  
    #  Event resolution                                                    #  
    # ------------------------------------------------------------------ #  
  
    def roll_for_event(self, event):  
        """Roll 1d20 + buff stat + focus bonus. Return breakdown and total."""  
        roll        = random.randint(1, 20)  
        buff_stat   = event.get("buff_stat", "")  
        buff        = self.stats.get(buff_stat, 0)  
        focus_bonus = 2 if self.focus == event.get("type") else 0  
        total       = roll + buff + focus_bonus  
        return roll, buff, buff_stat, focus_bonus, total  
  
    def resolve_event(self, event):  
        roll, buff, buff_stat, focus_bonus, total = self.roll_for_event(event)  
        print(f"\n  Rolling for: {event['description']}")  
        focus_str = f" + {focus_bonus} (focus)" if focus_bonus else ""  
        print(f"  Roll: {roll} + {buff} ({buff_stat}){focus_str} = {total}  (need {event['requires']})")  
  
        results = event.get("results", {})  
        if total >= event["requires"]:  
            outcome = results.get("succeed", {})  
            print(f"  SUCCESS!  {format_result(outcome)}")  
            apply_result(self, outcome)  
        else:  
            outcome = results.get("fail", {})  
            print(f"  FAILED.   {format_result(outcome)}")  
            apply_result(self, outcome)  
  
    # ------------------------------------------------------------------ #  
    #  Turn phases                                                         #  
    # ------------------------------------------------------------------ #  
  
    def earn(self):  
        self.savings += self.stats["income"]  
        for inv in self.investments:  
            inv["current_year"] += 1  
            # Variable investments: fluctuate rate each year  
            if inv["type"] == "variable":  
                inv["interest_rate"] = round(random.uniform(0.01, 0.06), 3)
  
    def buy_sell(self):
        print(WIDE)  
        print("  INVESTMENTS")  
        print(WIDE)  

        # Mature fixed investments before the turn begins  
        matured = [  
            inv for inv in self.investments  
            if inv["type"] == "fixed" and inv["current_year"] >= inv["lock_in_years"]  
        ]  
        for inv in matured:  
            payout = inv["initial_value"] * ((1 + inv["interest_rate"]) ** inv["current_year"])  
            self.savings += payout  
            self.investments.remove(inv)  
            print(f"  Fixed investment matured! +${payout:,.0f} returned to savings.")  

        print(f"  Savings: ${self.savings:,.0f}")  

        # Display current investments  
        if self.investments:  
            print("  Current investments:")  
            for i, inv in enumerate(self.investments, 1):  
                current = inv["initial_value"] * ((1 + inv["interest_rate"]) ** inv["current_year"])  
                if inv["type"] == "fixed":  
                    years_left = inv["lock_in_years"] - inv["current_year"]  
                    print(f"    ({i}) [FIXED]    ${current:>10,.0f}  at {inv['interest_rate']*100:.1f}%  |  {years_left} yr(s) left")  
                else:  
                    print(f"    ({i}) [VARIABLE] ${current:>10,.0f}  at {inv['interest_rate']*100:.1f}% (this year)")  

        # Generate available rates for new investments  
        fixed_rate  = round(random.uniform(0.03, 0.07), 3)   # slightly higher reward for locking in  
        fixed_years = random.randint(3, 10)  
        var_rate    = round(random.uniform(0.01, 0.06), 3)  

        print(f"\n  Available investments:")  
        print(f"  [1] Fixed:    {fixed_rate*100:.1f}% locked for {fixed_years} years (cannot sell early)")  
        print(f"  [2] Variable: ~{var_rate*100:.1f}% this year (rate fluctuates, sell any turn)")  
        print(f"  [3] Sell a variable investment")  
        print(f"  [0] Skip")  

        choice = input("  Choice: ").strip()  

        if choice == "1":  
            try:  
                amount = int(input(f"  Amount to invest (savings: ${self.savings:,.0f}): $").strip())  
                if amount <= 0 or amount > self.savings:  
                    print("  Invalid amount.")  
                else:  
                    self.investments.append({  
                        "type":          "fixed",  
                        "initial_value": amount,  
                        "interest_rate": fixed_rate,  
                        "lock_in_years": fixed_years,  
                        "current_year":  0,  
                    })  
                    self.savings -= amount  
                    print(f"  Invested ${amount:,} at {fixed_rate*100:.1f}% for {fixed_years} years.")  
            except ValueError:  
                print("  Invalid input.")  

        elif choice == "2":  
            try:  
                amount = int(input(f"  Amount to invest (savings: ${self.savings:,.0f}): $").strip())  
                if amount <= 0 or amount > self.savings:  
                    print("  Invalid amount.")  
                else:  
                    self.investments.append({  
                        "type":          "variable",  
                        "initial_value": amount,  
                        "interest_rate": var_rate,  
                        "current_year":  0,  
                    })  
                    self.savings -= amount  
                    print(f"  Invested ${amount:,} at ~{var_rate*100:.1f}% (variable).")  
            except ValueError:  
                print("  Invalid input.")  

        elif choice == "3":  
            variable = [(i, inv) for i, inv in enumerate(self.investments) if inv["type"] == "variable"]  
            if not variable:  
                print("  No variable investments to sell. Fixed investments are locked in.")  
            else:  
                print("  Variable investments:")  
                for display_i, (_, inv) in enumerate(variable, 1):  
                    current = inv["initial_value"] * ((1 + inv["interest_rate"]) ** inv["current_year"])  
                    print(f"    ({display_i}) ${current:>10,.0f}  at {inv['interest_rate']*100:.1f}%")  
                try:  
                    idx = int(input("  Which to sell? ").strip()) - 1  
                    if 0 <= idx < len(variable):  
                        real_idx = variable[idx][0]  
                        inv      = self.investments.pop(real_idx)  
                        payout   = inv["initial_value"] * ((1 + inv["interest_rate"]) ** inv["current_year"])  
                        self.savings += payout  
                        print(f"  Sold for ${payout:,.0f}.")  
                    else:  
                        print("  Invalid choice.")  
                except (ValueError, IndexError):  
                    print("  Invalid choice.")
  
    def process_life_events(self):  
        print(WIDE)  
        print("  LIFE EVENTS")  
        print(WIDE)  
  
        optional  = [e for e in life_events if e["optional"]]  
        mandatory = [e for e in life_events if not e["optional"]]  
  
        max_choices = self.stats["time"] + (1 if self.focus == "pursuits" else 0)  
        print(f"\n  You have {max_choices} time slot(s) this year.")  
        print("  Optional events available:\n")  
        for i, event in enumerate(optional, 1):  
            print(f"  [{i}]", end=" ")  
            self.print_event(event)  
        print("  [0] Done choosing\n")  
  
        chosen = []  
        while len(chosen) < max_choices:  
            slots_left = max_choices - len(chosen)  
            choice = input(f"  Choose event ({slots_left} slot(s) left, 0 to stop): ").strip()  
            if choice == "0":  
                break  
            try:  
                idx = int(choice) - 1  
                if not (0 <= idx < len(optional)):  
                    print("  Invalid number.")  
                elif optional[idx] in chosen:  
                    print("  Already chosen.")  
                else:  
                    chosen.append(optional[idx])  
                    print(f"  Added: {optional[idx]['description']}")  
            except ValueError:  
                print("  Invalid input.")  
  
        for event in chosen:  
            self.resolve_event(event)  
  
        if mandatory:  
            print("\n  Drawing mandatory event...")  
            event = random.choice(mandatory)  
            print(f"  You drew: {event['description']}")  
            self.resolve_event(event)  
  
    def process_global_events(self):  
        pass  # TODO: implement  
  
    def next_age(self):  
        self.age += 1  
        self.earn()  
        self.buy_sell()  
        self.process_life_events()  
        self.process_global_events()  
        self.print_stats()  
  
    # ------------------------------------------------------------------ #  
    #  Final score                                                         #  
    # ------------------------------------------------------------------ #  
  
    def final_score(self):  
        life_score  = sum(self.scores.values()) * 1000  
        focus_bonus = 0  
        if self.focus == "relationships":  
            focus_bonus = self.scores["relationships"] * 1000  
        elif self.focus == "career":  
            focus_bonus = self.scores["career"] * 1000  
        elif self.focus == "pursuits":  
            focus_bonus = self.scores["happiness"] * 1000  
        total = self.networth + life_score + focus_bonus  
  
        print(WIDE)  
        print("  GAME OVER  -  FINAL SCORE")  
        print(WIDE)  
        print(f"  Net Worth:    ${self.networth:>12,.0f}")  
        print(f"  Life Score:   ${life_score:>12,.0f}")  
        print(f"  Focus Bonus:  ${focus_bonus:>12,.0f}")  
        print(SEP)  
        print(f"  TOTAL:        ${total:>12,.0f}")  
        print(WIDE)  
  
  
if __name__ == "__main__":  
    scott = Scott()  
    scott.print_rules()  
    scott.choose_focus()  
  
    for age in range(31, 61):  
        input(f"\n  Press Enter to advance to age {age}...")  
        scott.next_age()  
  
    scott.final_score()