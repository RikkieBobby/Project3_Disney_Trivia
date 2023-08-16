import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("disney_trivia")
    leaderboard = SHEET.worksheet('leaderboard')


def get_user_name():
    """
    gets the name from the user for the trivia game,
    this function will run a while loop asking the user to input a name to the terminal
    the name must be at least 3 characters long and must not conatin numbers or syntax which
    is not letters, if the user inputs anything that isn't a letter, the loop will return an error and request
    the data again until the correct data is entered
    """
    while True:
        print("Welcome to the Disney Trivia game!")
        print("In this game you, the user, will answer a series of Disney based Trivia questions with a choice of answers")
        print("The game will calculate your score as you play and display the final score at the end, let's see if you can make it to the top 5!")
        print("First, let's start by entering your name\n")

        name = input("Enter your name here: ")
        if name.isalpha() and len(name) >= 3:
            return name
        else:
            print("Sorry, you must enter a name 3 letters long and only use letters, try again\n")
            continue
        


user_name = get_user_name()
print(f"Great! Your name for the game will be {user_name}.")


 questions = [
        {
            "question" : "What is the name of the toy store in Toy Story 2?",
            "options" : ["A) Joe's Toy Barn", "B) Al's Toy Barn", "C) John's Toy Barn", "D) Frank's Toy Barn"],
            "answer" : "B"
        },
        {
            "question" : "What are the names of Cinderella's stepsisters?",
            "options" : ["A) Anastasia and Drizella", "B) Stephanie and Audrey", "C) Philipina and Sarah", "D) Josephine and Rochelle"],
            "answer" : "A"
        },
        {
            "question" : "What does 'Hakuna Matata' mean?",
            "options" : ["A) No problem", "B) No regrets", "C) No Issues", "D) No worries"],
            "answer" : "D"
        },
        {
            "question" : "How many years was Genie stuck in the lamp before Aladdin found him?",
            "options" : ["A) 1000 years", "B) 100 years", "C) 10,000 years", "D) 100,000 years"],
            "answer" : "C"
        },
        {
            "question" : "Who is the fashion designer in The Incredibles?",
            "options" : ["A) Edna Style", "B) Edna Mode", "C) Edna Tone", "D) Edna Vein"],
            "answer" : "B"
        },
        {
            "question" : "Which Disney Princess attended Elsa's coronation day in Arendelle?",
            "options" : ["A) Sleeping Beauty", "B) Snow White", "C) Little Mermaid", "D) Rapunzel"],
            "answer" : "D"
        },
        {
            "question" : "What is the name of Belle's father in Beauty and the Beast?",
            "options" : ["A) Maurice", "B) Michael", "C) Marcel", "D) Marquis"],
            "answer" : "A"
        },
        {
            "question" : "What was the first Pixar movie?",
            "options" : ["A) Monster's Inc", "B) Toy Story", "C) Finding Nemo", "D) Wall-e"],
            "answer" : "B"
        },
        {
            "question" : " Emperor Kuzco turns into what animal in The Emperor's New Groove?",
            "options" : ["A) Cabybara", "B) Condor", "C) Llama", "D) Jaguar"],
            "answer" : "C"
        },
        {
            "question" : "Who said: 'Fish are friends, not food'?",
            "options" : ["A) Blake", "B) Benjamin", "C) Brian", "D) Bruce"],
            "answer" : "D"
        },
        {
            "question" : "What is Flynn Rider's real name in Tangled?",
            "options" : ["A) Constantine Sinclair", "B) Hugo Percival", "C) Edmund Balthazaar", "D) Eugene Fitzherbert"],
            "answer" : "D"
        },
        {
            "question" : "The Princess and the Frog is set in which city?",
            "options" : ["A) New Jersey", "B) Nashville", "C) New Orleans", "D) New York"],
            "answer" : "C"
        },
        {
            "question" : "Mowgli was raised by what animals in The Jungle Book?",
            "options" : ["A) Monkeys", "B) Wolves", "C) Bears", "D) Tigers"],
            "answer" : "B"
        },
        {
            "question" : "Quasimodo was the bell-ringer of which famous cathedral?",
            "options" : ["A) Notre Dame", "B) Duomo di Milano", "C) Westminster Abbey", "D) Catedral de Granada"],
            "answer" : "A"
        },
        {
            "question" : "Mike and Sulley joined which fraternity in Monsters University?",
            "options" : ["A) Beta Zed", "B) Oozma Kappa", "C) Delta Fy", "D) Sigma Kappa"],
            "answer" : "B"
        },
        {
            "question" : "Which character tells Buzz that he's his father?",
            "options" : ["A) Mr. Potato Head", "B) Slinky", "C) Zurg", "D) Dino"],
            "answer" : "C"
        },
        {
            "question" : "Russell belongs to which scouting organization in Up?",
            "options" : ["A) The wilderness Explorers", "B) The wild Pioneers", "C) The Outdoor Adventurers", "D) The Nature Investigators"],
            "answer" : "A"
        },
        {
            "question" : "Who said: 'The past can hurt. But the way I see it, you can either run from it or learn from it?'",
            "options" : ["A) Scar", "B) Zuzu", "C) Mufasa", "D) Rafiki"],
            "answer" : "D"
        },
        {
            "question" : "Which Monsters Inc. character is always watching?",
            "options" : ["A) Henry J Waternose", "B) Roz", "C) Randall", "D) Celia"],
            "answer" : "B"
        },
        {
            "question" : "Who is Miguel's idol in Coco?",
            "options" : ["A) Mama Imelda Riviera", "B) Hector", "C) Ernesto de la Cruz", "D) Juan Ortodoncia"],
            "answer" : "C"
        }
    ]