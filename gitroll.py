import subprocess 
from pathlib import Path 
from github import Github, GithubException

def createLocal(file_name): 
    try: 
        file_path = Path(file_name)
        file_path.mkdir(parents=True, exist_ok=True) 
        print(f"Parent directory {file_name} created")
    except Exception as e: 
        print(f"Error creating directory: {e}") 

    try: 
        subprocess.run(f"cd {file_name} ; python3 -m venv {file_name}", shell=True, check=True) 
        print(f"Python virtual environment {file_name} created")
    except subprocess.CalledProcessError as e: 
        print(f"Failed to create virtual environment") 

def createGitRepo(file_name): 
	try: 
		token = ""
		github_auth = Github(token) 
		user =  github_auth.get_user()
		print(f"{user} initialized") 
		repo = user.create_repo(file_name)
		print(f"{repo} created") 
	except GithubException as e:
		print(f"Failed to create repo {e}") 
	try: 
		subprocess.run("pwd", shell=True, check=True)
		subprocess.run(f"git clone https://github.com/WillStephensonxyz/{file_name}.git", shell=True, check=True)
		print(f"Github repo {file_name} cloned to host") 
	except FileNotFoundError as e: 
		print(f"Parent directory {file_name} not found: {e}") 

if __name__ == "__main__": 

	# token = ""
	# github_auth = Github(token) 
	# user =  github_auth.get_user()

	file_name = input("Enter repo parent directory: ") 
	# createLocal(file_name)
	createGitRepo(file_name) 
