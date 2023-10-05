def profile_info(nick: str, profile_info: dict) -> str:
    return f'''
LeetCode profile stats: <a href='https://leetcode.com/{nick}'>{nick}</a>

<b>Solved Problems:</b>
Easy: <b>{profile_info['total_easy_problems_solved']}</b>/{profile_info['total_easy_problems']}
Medium: <b>{profile_info['total_medium_problems_solved']}</b>/{profile_info['total_medium_problems']}
Hard: <b>{profile_info['total_hard_problems_solved']}</b>/{profile_info['total_hard_problems']}
Total: <b>{profile_info['total_problems_solved']}</b>/{profile_info['total_problems']}

<b>{profile_info['submissions_last_year']}</b> submissions in the last year

Rank: <b>{profile_info['user_rank']}</b>
Reputation: <b>{profile_info['reputation']}</b>

Contribution Point: <b>{profile_info['contribution_point']}</b>'''

def problem_info(problem_info: dict) -> str:
    return f'''
<b>{problem_info['problem_id']}.</b> {problem_info['problem_title']}
<b>Topic:</b> {problem_info['problem_topic']}

<b>Difficulty:</b> {problem_info['problem_difficulty']}
<b>Status:</b> {problem_info['problem_paid_only']}

Accepted <b>{problem_info['accepted']}</b> | Submissions <b>{problem_info['submissions']}</b> | Acceptance Rate <b>{problem_info['acceptance_rate']}</b>'''