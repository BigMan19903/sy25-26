def get_team_names():
    num_teams = int(input("Enter the number of teams: "))
    return [input(f"Enter name for team {i+1}: ").strip() for i in range(num_teams)]

def select_team(team_names):
    print("\nTeams:")
    for idx, name in enumerate(team_names, 1):
        print(f"{idx}. {name}")
    selection = int(input("\nSelect a team by number: "))
    return team_names[selection - 1]

def main():
    team_names = get_team_names()
    selected_team = select_team(team_names)
    winning_team = input("\nEnter the name of the winning team: ").strip()

    if selected_team == winning_team:
        print(f"\nCinderella Alert! {selected_team} pulls the upset!")
    else:
        print(f"\n{selected_team} did not win this time.")

if __name__ == "__main__":
    main()