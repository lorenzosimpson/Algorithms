#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  ## recipe = what you need
  ## ingredients = what you have
  recipe_length = len(recipe)
  ingredients_length = len(ingredients)
  # initialize an array that will contain (inventory/required) for each item
  minimums = [0] * recipe_length
  # append each item at index x to the array of minimums
  x = 0
  # if there are more required ingredients than inventory, automatic fail
  if recipe_length > ingredients_length:
    return 0
  else:
    for i in ingredients:
        # recipe[r] is value, ingredients[r] is value
        if ingredients[i] == 0 or recipe[i] == 0:
          return 0
        elif ingredients[i] // recipe[i] < 1:
          # not enough of an ingredient
          return 0
        else:
          # minimums.append(ingredients[i] // recipe[i]) <-- easy way
          minimums[x] = ingredients[i] // recipe[i]
          x += 1
  
  # manually find the lowest value of minimums
  result = minimums[0]
  for m in range(1, len(minimums)):
    if minimums[m] < minimums[m - 1]:
      result = minimums[m]
  
  return result
        



  # return max number of whole batches we can make


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 58, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))