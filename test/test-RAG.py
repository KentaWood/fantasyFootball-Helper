import os
import weaviate

CLASS_NAME = "WebPage"

def query_weaviate(query_text):
    """
    Query the Weaviate database for a specific query text.

    Args:
        query_text (str): The text to query.

    Returns:
        list: A list of articles containing the query text.
    """
    # Connect to Weaviate
    client = weaviate.Client("http://localhost:1234")  # Ensure the correct port

    try:
        # Perform the query
        response = client.query.get(CLASS_NAME, ["url", "content"]) \
            .with_near_text({"concepts": [query_text]}) \
            .with_limit(2) \
            .do()

        # Extract the results
        result = response.get("data", {}).get("Get", {}).get(CLASS_NAME, [])
        return result
    except weaviate.exceptions.UnexpectedStatusCodeException as e:
        print(f"Query failed: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def test_rag_system():
    """
    Test the RAG system by querying each player and verifying the results.

    The test checks if the returned articles mention the player's name.
    """
    # Define the list of player files
    player_files = [
        "wev_db/player_urls/free_agent_urls/Christian_Watson_urls.txt",
        "wev_db/player_urls/free_agent_urls/Packers_D_ST_urls.txt",
        "wev_db/player_urls/free_agent_urls/Wil_Lutz_urls.txt",
        "wev_db/player_urls/players_woody/A.J._Brown_urls.txt",
        "wev_db/player_urls/players_woody/Alvin_Kamara_urls.txt",
        "wev_db/player_urls/players_woody/Calvin_Ridley_urls.txt",
        "wev_db/player_urls/players_woody/Chase_McLaughlin_urls.txt",
        "wev_db/player_urls/players_woody/Courtland_Sutton_urls.txt",
        "wev_db/player_urls/players_woody/Hunter_Henry_urls.txt",
        "wev_db/player_urls/players_woody/Jake_Ferguson_urls.txt",
        "wev_db/player_urls/players_woody/Keon_Coleman_urls.txt",
        "wev_db/player_urls/players_woody/Nico_Collins_urls.txt",
        "wev_db/player_urls/players_woody/Patrick_Mahomes_urls.txt",
        "wev_db/player_urls/players_woody/Sam_Darnold_urls.txt",
        "wev_db/player_urls/players_woody/Saquon_Barkley_urls.txt",
        "wev_db/player_urls/players_woody/Texans_D_ST_urls.txt",
        "wev_db/player_urls/players_woody/Tyrone_Tracy_Jr._urls.txt",
    ]

    total_results = 0
    players_with_matches = 0
    players_without_matches = 0

    for file_path in player_files:
        # Extract player name from the file name
        player_name = os.path.basename(file_path).replace("_urls.txt", "").replace("_", " ")
        print(f"Querying for player: {player_name}")

        # Query Weaviate
        results = query_weaviate(player_name)

        # Count the results that mention the player's name
        match_count = sum(1 for result in results if player_name.lower() in result.get("content", "").lower())

        print(f"Total articles retrieved: {len(results)}")
        print(f"Articles mentioning '{player_name}': {match_count}\n")
        total_results += match_count

        if match_count > 0:
            players_with_matches += 1
        else:
            players_without_matches += 1

    print(f"Overall matches across all players: {total_results}")
    print(f"Players with matched articles: {players_with_matches}")
    print(f"Players without matched articles: {players_without_matches}")

if __name__ == "__main__":
    test_rag_system()