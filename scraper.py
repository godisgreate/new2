# import requests
# import csv
# import time

# # Replace 'YOUR_TOKEN' with your actual token from Step 2
# headers = {"Authorization": "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"}

# # Base URL to search for users in Zurich with more than 50 followers
# # Base URL to search for users in Zurich with more than 50 followers, requesting 100 results per page
# url = "https://api.github.com/search/users?q=location:Zurich+followers:>50"


# # Send the request to GitHub API
# response = requests.get(url, headers=headers)
# data = response.json()

# # Extract user logins (usernames) from the results
# users = [user['login'] for user in data.get('items', [])]

# print("Found users:", users)  # This will display the list of usernames
# # Prepare to save user data
# users_data = []

# for user_login in users:
#     user_url = f"https://api.github.com/users/{user_login}"
#     user_response = requests.get(user_url, headers=headers)
#     user_info = user_response.json()
    
#     # Clean up company name as instructed
#     company = user_info.get('company', '')
#     if company:
#         company = company.strip().lstrip('@').upper()
    
#     # Add user info to users_data
#     users_data.append([
#         user_info.get('login', ''),
#         user_info.get('name', ''),
#         company,
#         user_info.get('location', ''),
#         user_info.get('email', ''),
#         user_info.get('hireable', ''),
#         user_info.get('bio', ''),
#         user_info.get('public_repos', 0),
#         user_info.get('followers', 0),
#         user_info.get('following', 0),
#         user_info.get('created_at', '')
#     ])
    
#     time.sleep(1)  # Avoid hitting rate limits

# # Save to users.csv
# with open("users.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["login", "name", "company", "location", "email", "hireable", "bio", 
#                      "public_repos", "followers", "following", "created_at"])
#     writer.writerows(users_data)

# print("Saved user data to users.csv")
# repos_data = []

# for user_login in users:
#     repos_url = f"https://api.github.com/users/{user_login}/repos?sort=pushed&per_page=100"
#     repos_response = requests.get(repos_url, headers=headers)
#     repos_info = repos_response.json()
    
#     for repo in repos_info:
#         repos_data.append([
#             user_login,
#             repo.get('full_name', ''),
#             repo.get('created_at', ''),
#             repo.get('stargazers_count', 0),
#             repo.get('watchers_count', 0),
#             repo.get('language', ''),
#             repo.get('has_projects', False),
#             repo.get('has_wiki', False),
#             repo.get('license', {}).get('key', '')
#         ])
    
#     time.sleep(1)  # Avoid rate limits

# # Save to repositories.csv
# with open("repositories.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["login", "full_name", "created_at", "stargazers_count", "watchers_count", 
#                      "language", "has_projects", "has_wiki", "license_name"])
#     writer.writerows(repos_data)

# print("Saved repository data to repositories.csv")
import requests
import csv
import time

headers = {"Authorization": "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"}

# Base URL to search for users in Zurich with more than 50 followers
base_url = "https://api.github.com/search/users"
query = "location:Zurich followers:>50"
page = 1
users = []

while True:
    url = f"{base_url}?q={query}&per_page=100&page={page}"
    response = requests.get(url, headers=headers)
    data = response.json()

    # Check if there are items in the response
    if 'items' not in data or len(data['items']) == 0:
        break

    users.extend(data['items'])
    page += 1
    time.sleep(1)  # Avoid hitting rate limits

print("Found users:", [user['login'] for user in users])

# Prepare to save user data
users_data = []

for user in users:
    user_login = user['login']
    user_url = f"https://api.github.com/users/{user_login}"
    user_response = requests.get(user_url, headers=headers)
    user_info = user_response.json()
    
    # Clean up company name as instructed
    company = user_info.get('company', '')
    if company:
        company = company.strip().lstrip('@').upper()
    
    # Add user info to users_data
    users_data.append([
        user_info.get('login', ''),
        user_info.get('name', ''),
        company,
        user_info.get('location', ''),
        user_info.get('email', ''),
        user_info.get('hireable', ''),
        user_info.get('bio', ''),
        user_info.get('public_repos', 0),
        user_info.get('followers', 0),
        user_info.get('following', 0),
        user_info.get('created_at', '')
    ])
    
    time.sleep(1)  # Avoid hitting rate limits

# Save to users.csv
with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["login", "name", "company", "location", "email", "hireable", "bio", 
                     "public_repos", "followers", "following", "created_at"])
    writer.writerows(users_data)

print("Saved user data to users.csv")
