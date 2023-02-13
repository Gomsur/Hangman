![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Gomsur,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!


# Hangman

Hangman is a nostalgic game created for the user who likes clever games.
In the beginning of the game, the user will be able to select a word category of their choice.
Based on their choice, they will get an animal word, a country or some kind of food word.

## Site Owner Goals

- Providing the user with a fun nostalgic game
- Giving the user different word categories to choose from
- Give the end user a game functionality that lets them play the game again

## User Stories
- ### First Time User
- As a first time user I want the user to easily choose different categories
- As a first time user I want the user to get a hint of how many letters is in the word
- As a first time user I want the user to be given a play again option

- ### Returning User
