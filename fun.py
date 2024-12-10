from espn_api.football import League

# Replace with your actual league_id and year
league_id = 1959023854
year = 2024

# Use the provided credentials
espn_s2 = "AECLb9C9J8G%2BrJ5YgcH4d%2B%2FFqPgnJoGrowRSv%2FPiLrWKeeVWfRb%2BDl4KWrPBdHjIlICn0bClz1cb14ZCO0F2zwA8XVX008xU%2BAnYmFW9IlMw23mcUXg1sq8npOc1GFAnPhRykl5YXnW9r3GjYZpXxPcVOdIc1aVZd6ZF1z5qgegHZqjsEv%2B8AK0WHrdXvaSh0gQ%2FM6YlaERKeZSvyPjtdNPEeFMhHqQc7MK9m1v7e7AfGKxHeuSrEWHkKS%2FMTiEQ4sYw75crnGcD9RB2S81nNQ%2B95AcexF34Y99Q1p68kqWLUw%3D%3D"

swid = "{7207909F-4307-499B-AEE8-C3C0806E7D61}"

WOODY_ID = 9

# Create the League object

if __name__ == "__main__":
   league = League(
    league_id=league_id,
    year=year,
    espn_s2=espn_s2,
    swid=swid
    )
   # Define the player name or ID
   player_name = "Saquon Barkley"  # Replace with the desired player's name

   # Fetch the box scores for the current week
   week = league.scoringPeriodId  # Or specify a different week
   box_scores = league.box_scores(week=14)

   # Search for the player's projected points
   player_projection = None
   for box_score in box_scores:
      for player in box_score.home_lineup + box_score.away_lineup:
         if player.name == player_name:
               player_projection = player.projected_points
               break
      if player_projection is not None:
         break

   # if player_projection is not None:
   #    print(f"{player_name}'s projected points for Week {week}: {player_projection}")
   # else:
   #    print(f"Player {player_name} not found in the box scores for Week {week}.")
   
   # # Get player information by name
   # player_name = "Saquon Barkley"  # Replace with the player you want
   # player = league.player_info(name=player_name)

   # if player:
   #    print(f"Player: {player.name}")
   #    print(f"Projected Points: {player.projected_points}")
   # else:
   #    print(f"Player {player_name} not found.")
   
   print(box_score.home_lineup )