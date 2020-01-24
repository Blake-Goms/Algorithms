
def recipe_batches(recipe, ingredients):
  # recipe is what is need 
  # ingredients is what we have 
  total_batches = []
  if set(ingredients) >= set(recipe): # could have used len() instead. Wasn't aware that would work on dictionaries
    for x in recipe:
      # if we don't have enough of an ingredient, add 0 to list
      if recipe.get(x) > ingredients.get(x):
        total_batches.append(0)
      else:
        # if we have more than the recipe, divide evenly total batches made
        total_batches.append((ingredients[x] // recipe[x]))
    return min(total_batches)
  # if we have less than the recipe, return 0
  else:
    return 0

#print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))
print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))

'''if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
'''