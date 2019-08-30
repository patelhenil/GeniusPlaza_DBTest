# GeniusPlaza_DBTest
Genius Plaza Back End Developer (Python and Django) initial Test.


#Project_requirements:


You will be designing REST APIs using Django REST Framework Models:

  1) Design the User Model with username(unique field), email(unique field), first_name, last_name,m password. (You can use the Django inbuilt user model)

  2) Design A Step Model with step_text(string field, not null), Many to One relationship with Recipe

  3) Design An Ingredient Model with text(not null, string), Many to One relationship with Recipe

  4) Design A Recipe Model with the name(string, not null), Foreign Key to User table(one to one relationship), One to Many relationships with Step and Ingredient Model
  
 
API: You need to create API’s to create a new recipe, get recipes by a particular user, get all the recipes, update a recipe, delete a particular recipe You need to create the project and add it to your GitHub and Email us your GitHub username and we can take it from there.


Notes:


All the project requirements specified above has been completed.

Instructions:

1) Please navigate to GeniusPlaza_DBTest/worldFoodiesOrg/ for manage.py file. (RecipesREST is the project and RecipesAPI is the app)

2) pyhton manage.py runserver will boot up the server.

3) Navigate to your local host.

4) Permissions have been set to "IsAuthenticatedOrReadOnly" thus you would need to log in with following admin credentials to manipulate data:

Username: geniusplazateam Password: Teamdb123

or 

using user: genius1 Password: Teamdb123


Some API specifications:


1) One "Foodie" can only add one recipe.
2) For each recipe, you can add many ingredients and many steps.
3) You can also create DELETE and PUT steps, ingredients.
4) HyperlinkedModelSerializer is enabled so that the user can see the URLs.
5) All these functionalities are available using other API tools such as Postman as well.



    
