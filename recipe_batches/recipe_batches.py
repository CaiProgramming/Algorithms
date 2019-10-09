#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    try:
        total = [0] * len(recipe);
        overall = 0
        for i in range(0,len(recipe)):
            cRec = list(recipe.keys())[i]
            cIng = list(ingredients.keys())[i]
            while recipe[cRec] <= ingredients[cIng]:
                total[i] = total[i] + 1
                ingredients[cRec] = ingredients[cRec] - recipe[cRec]
        for i in range(0,len(total)):
            if i == 0:
                overall = total[i]
            else:
                if overall > total[i]:
                    overall = total[i]
        return overall
    except:
        return 0

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
