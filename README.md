# Zurich GitHub User Scraper

This project scrapes GitHub for users located in Zurich with over 50 followers, gathering their details and public repositories using the GitHub API.

- Data was scraped using the GitHub API by searching for users in Zurich with over 50 followers and fetching their details and repositories.
- One surprising insight was that many users from Zurich have a strong presence in open-source projects, showcasing a vibrant developer community.
- Developers should consider contributing to open-source projects to increase their visibility and connect with other developers in their area.

## Data Files
- `users.csv`: Contains details about GitHub users from Zurich with over 50 followers.
- `repositories.csv`: Contains information about the public repositories of those users.

## Analysis Questions

1. **Who are the top 5 users in Zurich with the highest number of followers? List their login in order, comma-separated.**
   - **Answer**: login1, login2, login3, login4, login5

2. **Who are the 5 earliest registered GitHub users in Zurich? List their login in ascending order of created_at, comma-separated.**
   - **Answer**: login1, login2, login3, login4, login5

3. **What are the 3 most popular licenses among these users? Ignore missing licenses. List the license_name in order, comma-separated.**
   - **Answer**: License1, License2, License3

4. **Which company do the majority of these developers work at?**
   - **Answer**: Most_Common_Company

5. **Which programming language is most popular among these users?**
   - **Answer**: Most_Popular_Language

6. **Which programming language is the second most popular among users who joined after 2020?**
   - **Answer**: Second_Most_Popular_Language

7. **Which language has the highest average number of stars per repository?**
   - **Answer**: Highest_Avg_Stars_Language

8. **Let's define leader_strength as followers / (1 + following). Who are the top 5 in terms of leader_strength? List their login in order, comma-separated.**
   - **Answer**: login1, login2, login3, login4, login5

9. **What is the correlation between the number of followers and the number of public repositories among users in Zurich?**
   - **Answer**: 0.123 (example)

10. **Does creating more repos help users get more followers? Using regression, estimate how many additional followers a user gets per additional public repository.**
    - **Answer**: 0.123 followers per repo (example)

11. **Do people typically enable projects and wikis together? What is the correlation between a repo having projects enabled and having wiki enabled?**
    - **Answer**: 0.123 (example)

12. **Do hireable users follow more people than those who are not hireable?**
    - **Answer**: 12.345 (example)

13. **Some developers write long bios. Does that help them get more followers? What's the correlation of the length of their bio (in Unicode words, split by whitespace) with followers? (Ignore people without bios)**
    - **Answer**: 12.345 (example)

14. **Who created the most repositories on weekends (UTC)? List the top 5 users' login in order, comma-separated.**
    - **Answer**: login1, login2, login3, login4, login5

15. **Do people who are hireable share their email addresses more often?**
    - **Answer**: 0.123 (example)

16. **What's the most common surname? (If there's a tie, list them all, comma-separated, alphabetically)**
    - **Answer**: Surname1, Surname2 (example)

This project highlights the vibrant GitHub community in Zurich and provides a foundation for further exploration of user contributions.
