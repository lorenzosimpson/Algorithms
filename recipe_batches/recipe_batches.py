#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  ## recipe = what you need
  ## ingredients = what you have
  recipe_length = len(recipe)
  ingredients_length = len(ingredients)
  minimums = []

  # if there are more required ingredients than inventory, automatic fail
  if recipe_length is not ingredients_length:
    return 0
  else:
    for i in ingredients:
        # recipe[r] is value, ingredients[r] is value
        if ingredients[i] // recipe[i] < 1:
          # not enough of an ingredient
          print('not enough')
        else:
          minimums.append(ingredients[i] // recipe[i])

        
  
  
  
  return min(minimums)
        


print(recipe_batches({'milk': 1, 'flour': 2}, {'milk': 15, 'flour': 4} ))
  # return max number of whole batches we can make


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))