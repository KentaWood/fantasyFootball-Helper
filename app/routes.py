from flask import Blueprint, render_template, jsonify, request
from app.wev_RAG_query import query_weaviate
# from app.espn_api improt
from app.openAI_api import ask_openai  
from app.espn_api_helper import *
from config import ESPN_2, SWID,LEAGUE_ID


# Define a blueprint for modular routing
main_bp = Blueprint('main', __name__)

# Espn Fantasy info
YEAR = 2024
WOODY_ID = 9
woody = MyTeam(LEAGUE_ID, YEAR, ESPN_2, SWID, WOODY_ID)



# Define the home route
@main_bp.route("/")
def home():
    
    return render_template("home.html", players=woody.player_names + ["Christian Watson", "Packers D/ST", "Wil Lutz"])

# Define an API route for processing user input
@main_bp.route("/process", methods=["POST"])
def process():
    # Get data from the POST request
    data = request.json
    action = data.get("action")  # Action: "ask" or "compare"
    player1 = data.get("player1")  # First player
    player2 = data.get("player2")  # Second player (optional for "compare")
    prompt_user_input = data.get("prompt")  # User's additional prompt (if provided)

    # Process the action
    if action == "compare":
        # Fetch context for each player
        player1_RAG = query_weaviate(player1)
        player2_RAG = query_weaviate(player2)

        # Get projections for each player
        player1_proj = woody.get_player_projection(player1)
        player2_proj = woody.get_player_projection(player2)

        # Build the prompt for OpenAI
        full_prompt = (
            prompt_user_input
            + "Who Should I Start?"
            + "\n\nPlayer Projections:\n"
            + f"{player1}: {player1_proj}\n"
            + f"{player2}: {player2_proj}\n\n"
            + f"Context for {player1}:\n{player1_RAG}\n\n"
            + f"Context for {player2}:\n{player2_RAG}"
        )

        
        response = ask_openai(full_prompt)
        
    elif action == "ask":
        
        # Fetch context for player1
        player1_RAG = query_weaviate(player1)

        # Get projection for player1
        player1_proj = woody.get_player_projection(player1)

        # Build the prompt for OpenAI
        full_prompt = (
            prompt_user_input
            + "\n\nPlayer Projection:\n"
            + f"{player1}: {player1_proj}\n\n"
            + f"Context for {player1}:\n{player1_RAG}"
        )

        response = ask_openai(full_prompt)
    else:
        response = "Invalid action. Please try again."
        
        
    # Return the response as JSON
    return jsonify({"output": response})
