from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["match_format", "batting_team", "bowling_team", "score", "overs", "wickets", "match_situation", "batsman_name", "bowler_name", "bowler_style", "delivery", "shot", "result"],
    template="""
Assume you are Aakash Chopra giving commentary in Hinglish.

Generate immersive, realistic, and emotionally engaging cricket commentary for a live match.

Context:
- Match Format: {match_format}
- Teams: {batting_team} vs {bowling_team}
- Score: {score}
- Overs: {overs}
- Wickets: {wickets}
- Match Situation: {match_situation}

Players:
- Striker: {batsman_name}
- Bowler: {bowler_name}
- Bowler Style: {bowler_style}

Ball Details:
- Delivery: {delivery}
- Shot: {shot}
- Result: {result}

Instructions:
- Write commentary like a live TV broadcaster.
- Keep it natural and exciting.
- Add crowd reaction and tension when appropriate.
- Use cricket terminology professionally.
- Increase intensity for wickets, boundaries, and close moments.
- Commentary should be 5-6 lines long.
- Avoid repetitive wording.
"""
)

match_format = input("What is the match format {T20 / ODI / Test}: ")
batting_team = input("Which team is batting: ")
bowling_team = input("Which team is bowling: ")
score= input("What is the score: ")
overs= input("What is the current over: ")
wickets= input("How many wickets: ")
match_situation= input("What is the situation of the match {powerplay / middle overs / death overs / chase pressure / collapse / partnership / last over thriller}: ")
batsman_name= input("Who is the batsman: ")
bowler_name= input("Who is the bowler: ")
bowler_style= input("What is the style of bowler {pace / swing / spin / leg-spin / off-spin / left-arm fast}: ")
delivery= input("In what style did bowler delivered the ball {yorker / bouncer / slower ball / googly / full length / short ball}: ")
shot= input("What shot did the batsman play {cover drive / pull / sweep / cut / flick / defense}: ")
result= input("What is the result {dot ball / single / double / FOUR / SIX / wicket}: ")

final_prompt = prompt.format(
    match_format = match_format,
    batting_team = batting_team,
    bowling_team = bowling_team,
    score = score,
    overs = overs,
    wickets = wickets, 
    match_situation = match_situation,
    batsman_name = batsman_name,
    bowler_name = bowler_name,
    bowler_style = bowler_style,
    delivery = delivery,
    shot = shot,
    result = result
)

response = llm.invoke(final_prompt)
print("")
print(response.content)