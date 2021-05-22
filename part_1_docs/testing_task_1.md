### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# card.value currently is assigning 1 instead of equality, should be ==
# missing : after else statement
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# dif should be def
# missing comma 
# indentation in the if/else statement is not correct
# where reads card should be card1
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# indentation of the function is not correct
# total needs to be "total = 0" as a placeholder
# return should have a space after "...total of "
# return should return a string
# return is should be in the same alignment as the for loop.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
