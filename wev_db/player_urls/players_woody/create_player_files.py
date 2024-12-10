import os

# List of player names
player_names = [
    'A.J. Brown', 'Saquon Barkley', 'Nico Collins', 'Alvin Kamara', 'Patrick Mahomes',
    'Calvin Ridley', 'Courtland Sutton', 'Hunter Henry', 'Sam Darnold', 'Bears D/ST',
    'Tyrone Tracy Jr.', 'Keon Coleman', 'Chase McLaughlin', 'Jake Ferguson', 'Texans D/ST'
]

\

# Create a file for each player
for player_name in player_names:
    # Sanitize player name for filename (remove spaces and special characters)
    filename = f"{player_name.replace(' ', '_').replace('/', '_')}_urls.txt"
    filepath = os.path.join(filename)
    
    # Write URLs or placeholder content
    with open(filepath, 'w') as file:
        file.write(f"{player_name}_urls = []\n")
    
    print(f"Created file: {filepath}")
