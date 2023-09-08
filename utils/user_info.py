from dotenv import load_dotenv
import os
import requests

load_dotenv('utils/.env')

LEETCODE_DOMAIN = os.getenv('LEETCODE_DOMAIN')
LEETCODE_PROFILE = os.getenv('LEETCODE_PROFILE')

def check_profile_existence(NICKNAME: str) -> bool:
    LEETCODE_USER_PROFILE = f'{LEETCODE_DOMAIN}/{NICKNAME}'
    response = requests.get(LEETCODE_USER_PROFILE)

    return response.status_code == 200

def get_user_info(NICKNAME: str):
    if check_profile_existence(NICKNAME):
        API_USER = LEETCODE_PROFILE + NICKNAME

        try:
            response = requests.get(API_USER, timeout=5)
            problem_data = response.json()

            user_stat = {
                'total_problems_solved': problem_data['totalSolved'],
                'total_problems': problem_data['totalQuestions'],
                'total_easy_problems_solved': problem_data['easySolved'],
                'total_easy_problems': problem_data['totalEasy'],
                'total_medium_problems_solved': problem_data['mediumSolved'],
                'total_medium_problems': problem_data['totalMedium'],
                'total_hard_problems_solved': problem_data['hardSolved'],
                'total_hard_problems': problem_data['totalHard'],
                'user_rank': format_num(problem_data['ranking']),
                'contribution_point': problem_data['contributionPoint'],
                'reputation': problem_data['reputation'],
                'submissions_last_year': problem_data['totalSubmissions'][0]['submissions']
            }

            return user_stat
        except Exception:
            return 'Error while getting data from the site'
    return f'Profile {NICKNAME} does not exist'

def format_num(num: str) -> str:
    return '{:,}'.format(num)