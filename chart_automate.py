import os
import subprocess
import random
from datetime import datetime, timedelta

# Configure these variables
GIT_REPO_PATH = "C:/Users/user/Desktop/chart"  # Your local repo path
START_DATE = "2024-03-05"  # Start date (YYYY-MM-DD)
END_DATE = "2024-05-24"    # End date (YYYY-MM-DD)
MIN_COMMITS_PER_DAY = 1    # Minimum commits per day
MAX_COMMITS_PER_DAY = 8    # Maximum commits per day

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

# Generate commits between two dates
def generate_commits(start_date, end_date, min_commits_per_day, max_commits_per_day):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end - start

    for i in range(delta.days + 1):
        commit_day = start + timedelta(days=i)
        
        # Generate a random number of commits for the current day
        commits_per_day = random.randint(min_commits_per_day, max_commits_per_day)

        for _ in range(commits_per_day):
            # Set the commit time for the current day
            commit_time = commit_day + timedelta(
                hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59)
            )
            commit_date_str = commit_time.strftime('%Y-%m-%dT%H:%M:%S')
            commit_message = f"Auto commit on {commit_time.strftime('%Y-%m-%d')}"

            # Create a random change (e.g., append to a file)
            with open(os.path.join(GIT_REPO_PATH, 'contribution.txt'), 'a') as f:
                f.write(f"Commit on {commit_date_str}\n")

            # Make a commit on that date
            commit_on_date(commit_date_str, commit_message)

# Generate the commits
generate_commits(START_DATE, END_DATE, MIN_COMMITS_PER_DAY, MAX_COMMITS_PER_DAY)

# Push the commits to the remote repository
run_command("git push")