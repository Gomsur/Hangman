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

## Introduction
Hangman is a classic game that puts your brain to work.
In this nostalgic game the user decides which category they would like to play.
When the user chose a category the game begins and the user gets 8 tries of guessing the correct word.
If the user guess a word incorrect, the stickman starts getting filled out.
The game ends with either a full stickman which would be a loss, or if the user guesses the correct word before the stickman gets hung.

## Planning stage
### Target Audience
- A game for all ages
- English speaking/writing users
- Users who want a nostalgic touch of gaming

### User Stories
- As a user I want to choose between different word categories
- As a user I want to see how many letters are in the word.
- As a user I want the game to be re-playable if lost
- As a user I want to get an introduction of how many lives I have
- As a user I want to count the hangman parts to calculate how many tries I have left

### Site aims
- Providing a nostalgic runnable game
- Giving the user a choice of categories based on their interest
- Give the user a re-playable game

### Page Layout
Page is on a mock terminal deployed on [Heroku] and connected through [GitHub]
The user provides a letter and press enter to submit.

## Game walkthrough
- The start of the game is kept simple with instructions on how to choose a word category, logo to catch the attention of the user which was built with [patorjk]

- The game is asking you to choose between 3 different categories
- Animals = A
- Food = F
- Countries = C

- The user starts by entering a letter of their choice/guess.
The game then tells the user if the letter is correct or not and will tell the user how many letters are in the full word.
If the letter is correct, it will add it to the word, if not it will tell you to try again.

- If a user guesses a letter that have already been guessed, a life will not be taken but a message will tell them that this letter already have been guessed.

-

## Testing phase
- The code was tested through [pep8ci](https://pep8ci.herokuapp.com/#) where a couple of problems showed up.

### Manual Testing
- When you choose a category, the only words that are allowed to use are A, F and C.
If a user enters any other letters, the game should not start as it requires a category to be chosen.

- When a user guesses a word that have already been guessed, the player should not lose a life.


### Bugs
- Line 63 have a bug where I need to have a space after the letter for the logo to look good without errors.

- Line 271 have the same bug as mentioned above and needs a space after to be shown correctly.

- Invalid escape sequence, this error is due to my logos and cant be fixed.

## Technologies
### Languages
- Everything is made out of Python, except the README file

### Developing eviroment
- [GitHub]
- [Heroku]

### Packages 
- [pep8ci] for code validation & errors

### Other
- [patrojk] Used for logo design

## Deployment
- Everything is git pushed as much as possible.
- Created account on Heroku
- Added credits to my Heroku account to set up account
- Created a new app on Heroku
- Chose the name Hangman for my project and selected Europe as region
- Went to settings to sort out the buildpacks and node parts.
- Deployed my project and link to GitHub repository
- Heroku searched through my code and uploaded it
- Enable automatic deployes
- Opened the game in Heroku to check that everything runs as intended.

## Credits
- A big shoutout to a good friend of mine, Fredrik who is a student on Code Institute and have been a good helping hand on this project.
- A big shoutout to Bethieieio who I took inspiration from for this project [Bethieieio] (https://github.com/Bethieieio/project-three-console-hangman/blob/main/run.py)
- A big shoutout to gibbio101 who I got the color inspiration from to my Hangman game [gibbi101] (https://github.com/gibbo101/hangman/blob/main/run.py)
- A big shoutout to my mentor Antonio for always being there for me whenever I got stuck on parts, providing me with tips and tricks throughout everything.
