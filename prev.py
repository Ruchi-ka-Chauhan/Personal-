
def get_choices():
 player_choice = input("Enter a choice (rock,paper,sciccors:")
 computer_choice="paper"
 choices = {"player":player_choice ,"computer": computer_choice}
 return choices
 #functio is a set of code which only run when it is called
 return player_choice

choices = get_choices()
print(choices)   
