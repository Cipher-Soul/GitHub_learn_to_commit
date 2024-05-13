import os
import subprocess
import random
from datetime import datetime, timedelta

# Configure these variables
GIT_REPO_PATH = "C:/Users/user/Desktop/GitHub_learn_to_commit"  # Your local git repo path
YEAR = 2024                          # The year in which random commits will be made
MIN_COMMITS_PER_DAY = 1               # Minimum commits on a selected day
MAX_COMMITS_PER_DAY = 8               # Maximum commits on a selected day
TOTAL_COMMIT_DAYS = 39                # Total random days to make commits in the year

# Change the current directory to your git repository
os.chdir(GIT_REPO_PATH)

# Function to run shell commands
def run_command(command):
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

# Function to create a commit on a specific date
def commit_on_date(commit_date, commit_message):
    # Set the GIT_COMMITTER_DATE and commit using the current date
    env = os.environ.copy()
    env['GIT_COMMITTER_DATE'] = commit_date
    run_command(f'git add .')
    run_command(f'git commit --date="{commit_date}" -m "{commit_message}"')

# Function to generate random commit days in a year
def generate_random_days(year, total_days):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    # Generate random days within the year
    commit_days = random.sample(range((end_date - start_date).days + 1), total_days)
    return [start_date + timedelta(days=day) for day in commit_days]

# Function to generate commits for the random days
def generate_commits_on_random_days(commit_days, min_commits_per_day, max_commits_per_day):
    for commit_day in commit_days:
        # Random number of commits for the selected day
        commits_per_day = random.randint(min_commits_per_day, max_commits_per_day)

        for _ in range(commits_per_day):
            # Set the commit time within the current day
            commit_time = commit_day + timedelta(
                hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59)
            )
            commit_date_str = commit_time.strftime('%Y-%m-%dT%H:%M:%S')
            commit_message = f"Auto commit on {commit_time.strftime('%Y-%m-%d')}"

            # Make a simple file change (e.g., appending to a file)
            with open(os.path.join(GIT_REPO_PATH, 'contribution.txt'), 'a') as f:
                f.write(f"Commit on {commit_date_str}\n")

            # Make a commit on that date
            commit_on_date(commit_date_str, commit_message)

# Generate random commit days
commit_days = generate_random_days(YEAR, TOTAL_COMMIT_DAYS)

# Generate the commits on random days
generate_commits_on_random_days(commit_days, MIN_COMMITS_PER_DAY, MAX_COMMITS_PER_DAY)

# Push the commits to the remote repository
run_command("git push")
print(f'\033')
