from espn_api import football
from espn_api.football import League
from config import ESPN_2, SWID,LEAGUE_ID

def get_all_players(league, week):
    """
    Fetch all players in the league, including those on rosters and free agents.

    Args:
        league (League): An instance of the League class.
        week (int): The week for which to fetch free agents.

    Returns:
        List[Player]: A list of all Player objects.
    """
    all_players = []

    # Get all players currently on team rosters
    for team in league.teams:
        all_players.extend(team.roster)  # Team rosters contain Player objects

    # Get all free agents for the given week
    free_agents = league.free_agents(week=week)
    all_players.extend(free_agents)

    return [player.name for player in all_players]


# Replace with your actual league_id and year
YEAR = 2024

WOODY_ID = 9

LEAGUE = League(
            league_id=LEAGUE_ID,
            year=YEAR,
            espn_s2=ESPN_2,
            swid=SWID
        )

def get_team(league, team_id):
    """
    Fetch a specific team from the league by team ID.
    
    Args:
        league (League): The league object.
        team_id (int): The ID of the team to fetch.

    Returns:
        Team: The matching team object, or None if not found.
    >>> get_team(LEAGUE,9)
    Team(Woody)
    """
    for team in league.teams:
        if team.team_id == team_id:
            return team
    return None


def get_player_names(team):
    """
    Get the names of all players on a team.
    
    Args:
        team (Team): The team object.

    Returns:
        list: A list of player names.
    """
    if team and hasattr(team, 'roster'):
        return [player.name for player in team.roster]
    return []

def get_player_proj(league, player_name, current_week, myTeam=None):
    """
    >>> test = MyTeam(LEAGUE_ID, YEAR, ESPN_2, SWID, WOODY_ID)
    >>> get_player_proj(LEAGUE,"Christian Watson",15)
    10.63
    >>> get_player_proj(LEAGUE,"Patrick Mahomes",15,myTeam=test)
    18.6
    """
    if myTeam:
        for box_score in myTeam.league.box_scores(myTeam.curr_week):
                # Combine home and away lineups
                all_players = box_score.home_lineup + box_score.away_lineup
                for player in all_players:
                    if player.name == player_name:
                        return player.projected_points
    
    # Get the list of free agents for the current week
    free_agents = league.free_agents(week=current_week)
    
    #look through free agents
    for free_agent in free_agents:
        # Check if the free agent's name matches the input
        if free_agent.name == player_name:
            # Return the projected points for the specified week
            return free_agent.stats.get(current_week, {}).get('projected_points', 0)
    
    
    # If the player is not found, return a message or None
    return f"{player_name} not found."

    



    


class MyTeam:
    def __init__(self, league_id, year, espn_s2, swid, team_id):
        """
        Initialize the MyTeam object and create a League instance.
        
        Args:
            league_id (int): The ESPN League ID.
            year (int): The year of the league.
            espn_s2 (str): The ESPN S2 authentication token.
            swid (str): The SWID authentication token.
            team_id (int): The ID of the team to associate with this object.
        """
        # Initialize the League object
        self.league = League(
            league_id=league_id,
            year=year,
            espn_s2=espn_s2,
            swid=swid
        )

        # Get the specific team
        self.team = get_team(self.league, team_id)
        if not self.team:
            raise ValueError(f"Team with ID {team_id} not found in the league.")

        # Set team attributes
        self.roster = self.team.roster  # List of players on the team
        self.player_names = get_player_names(self.team) # List of player names
        self.curr_week = self.league.scoringPeriodId # Current week in the league
        
        
    





# Create the League object

if __name__ == "__main__":
   
#    # Fetch the box scores for the current week
#    week = league.scoringPeriodId  # Or specify a different week
#    box_scores = league.box_scores(week=week)
   player_name = "Patrick Mahomes"  # Replace with the desired player's name
   
   
   woody = MyTeam(LEAGUE_ID, YEAR, ESPN_2, SWID, WOODY_ID)
   
#    print(get_free_player_proj(LEAGUE,"Christian Watson",15))