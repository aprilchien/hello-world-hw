#Assignment 1

#object 1
myFavoriteColorIsOrange = True
print (myFavoriteColorIsOrange)

#object 2
numBooks = 10
print (numBooks)

#object 3
myFavoriteAnimals = ["narwhal", "dog", "panda"]
print (myFavoriteAnimals)

#object 4
hasAdidasShoes = 2
print (hasAdidasShoes)

print ("-----------------")

#Assignment 2
{
    "name": "Eve Coupe Glass",
    "location": "CB2",
    "material": "glass",
    "height": 4,
    "count": 8,
    "fragile": True,
    "opaque": False
}


#Assignment3

#tell the user what's happening
name = input("Hi! What's your name? ")

print (" \n"
    "Welcome, Chef " + name + "! \n" 
    "We're so excited that you're here to share your newest dish with us. \n" \
    "We've created a smart bot that will hopefully make it easier for you to write down your recipe! " \
    "Just answer the following prompts and it'll put everything together for you. \n")

#make a variable for the user input
play = input("If you're good to go say 'Ready!' (case sensitive!) ")

#boolean variable
condition = (play == "Ready!")

#if the user input indicates that they want to play the game, start the game
if condition:

    print ("-----------------------------------")

    #variables for recipe information
    
    #string valuables
    dishName = input("Name of the dish: ")
    mealType = input("What kind of meal is this, breakfast, lunch, or dinner: ")
    cuisine = input("Cuisine type: ")
    textureWrong = input("What texture should the food NOT be: ")
    textureRight =input("What texture should be food be?: ")
    ingredients = input("What ingredients are needed? Enter them as a list with a comma in between each ingredient (no spaces): ")
    ingredientsList = ingredients.split(",")
    action1 = input("Name an action needed in this recipe: ")
    action2 = input("Name another action: ")

    #integer variable
    myNum = 4
    #change number into a string so it can be concatenated
    numString = str(myNum)

    #this is the recipe. it is made up of strings and variables.
    #including "\"s to break up the paragraph 

    intro = "A recipe for " + dishName + " by Chef " + name + ": \n" \
    "This dish is the perfect addition to your " + mealType + " spread! " \
    "Filled with rich " + cuisine + " flavors, " \
    "it'll be a big hit with your friends and family."

    recipeIngredients = "Ingredients: " + ingredients
    
    recipe = "First, " + action1 + " the " + ingredientsList[1] + \
    " together with the " + ingredientsList[2] + ". The mixture " \
    "shouldn't be too " + textureWrong + " but if it is, just " \
    "add more " + ingredientsList[1] + ". Then, take the mixture and " \
    + action2 + " it with the rest of the ingredients." \
    " Repeat this step " + numString + " times until the mixure " \
    "looks " + textureRight + ". Then bake and your creation is ready." \
    "Bon Appetit!"\

    #print the story
    print (intro)
    print (recipeIngredients)
    print ("------------------")
    print (recipe)

else:
    print ("Aw man, see you later!")
