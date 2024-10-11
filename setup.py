import os
import subprocess

# Get the SSH private and public key from the environment variable
SSH_PRIVATE_KEY = os.environ.get("SSH_PRIVATE_KEY")
SSH_PUBLIC_KEY = os.environ.get("SSH_PUBLIC_KEY")
GIT_REPOSITORY_SSH_ADDRESS = os.environ.get("GIT_REPOSITORY_SSH_ADDRESS")
GIT_USER_NAME = os.environ.get("GIT_USER_NAME")
GIT_USER_EMAIL = os.environ.get("GIT_USER_EMAIL")
APP_DIRECTORY = os.environ.get("APP_DIRECTORY")
APP_FILE_NAME = os.environ.get("APP_FILE_NAME")

# Define the file path where the private and public key will be saved
ssh_private_key_path = os.path.expanduser("~/.ssh/ssh_key")
ssh_public_key_path = os.path.expanduser("~/.ssh/ssh_key.pub")
ssh_config_path = os.path.expanduser("~/.ssh/config")


# Create the .ssh directory if it doesn't exist
os.makedirs(os.path.expanduser("~/.ssh"), exist_ok=True)

# Write the private key to the file
with open(ssh_private_key_path, "w") as file:
    file.write(SSH_PRIVATE_KEY)
    file.write("\n")

# Write the public key to the file
with open(ssh_public_key_path, "w") as file:
    file.write(SSH_PUBLIC_KEY)
    file.write("\n")


# Write the ssh config to the file
with open(ssh_config_path, "w") as file:
    file.write(f"Host *\n")
    file.write(f"    StrictHostKeyChecking no\n")
    file.write(f"    AddKeysToAgent yes\n")
    file.write(f"    IdentityFile {ssh_private_key_path}\n")

# Set appropriate permissions for the file (read/write for user only)
os.chmod(ssh_private_key_path, 0o600)
os.chmod(ssh_public_key_path, 0o600)
os.chmod(ssh_config_path, 0o600)

# execute the following bash command
"""
git config --global user.name GIT_USER_NAME
git config --global user.email GIT_USER_EMAIL
git config --global user.signingkey ~/.ssh/ssh_key.pub
git config --global gpg.format ssh
git config --global commit.gpgsign true
git config --global core.ignorecase false
"""

# Define the Git commands to configure
commands = [
    ["git", "config", "--global", "user.name", GIT_USER_NAME],
    ["git", "config", "--global", "user.email", GIT_USER_EMAIL],
    ["git", "config", "--global", "user.signingkey", ssh_public_key_path],
    ["git", "config", "--global", "gpg.format", "ssh"],
    ["git", "config", "--global", "commit.gpgsign", "true"],
    ["git", "config", "--global", "core.ignorecase", "false"],
]

# Run each Git command
for command in commands:
    result = subprocess.run(command, check=True)
    if result.returncode == 0:
        print(f"Successfully ran: {' '.join(command)}")
    else:
        print(f"Failed to run: {' '.join(command)}")

# Clone the repository
result = subprocess.run(
    ["git", "clone", GIT_REPOSITORY_SSH_ADDRESS, APP_DIRECTORY],
    check=True,
)

if result.returncode == 0:
    print(f"Successfully cloned the repository")
else:
    print(f"Failed to clone the repository")

# cd into the app directory
os.chdir(APP_DIRECTORY)


# run the app

# if the file is a python file
if APP_FILE_NAME.endswith(".py"):
    result = subprocess.run(
        ["python", f"{APP_FILE_NAME}"],
        check=True,
    )

# if the file is a ipynb file

elif APP_FILE_NAME.endswith(".ipynb"):
    result = subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--inplace",
            "--execute",
            f"{APP_FILE_NAME}",
        ],
        check=True,
    )

if result.returncode == 0:
    print(f"Successfully ran the app")
else:
    print(f"Failed to run the app")
