import requests, json, random
from dotenv import load_dotenv
import os

load_dotenv('utils/.env')
LEETCODE_DOMAIN = os.getenv('LEETCODE_DOMAIN')
LEETCODE_PROBLEMS = os.getenv('LEETCODE_PROBLEMS')
LEETCODE_API = os.getenv('LEETCODE_API')

def random_problem_slug() -> str:
    response = requests.get(LEETCODE_PROBLEMS)
    data = response.json()
    problems = data['stat_status_pairs']
    random_slug = random.choice(problems)['stat']['question__title_slug']

    return random_slug

def get_problem_info() -> dict:
    slug = random_problem_slug()

    response = requests.post(
        LEETCODE_API,
        json = {
            'query': '''query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    title
                    titleSlug
                    isPaidOnly
                    difficulty
                    topicTags {
                        name
                        slug
                    }
                    stats
                }
            }''',
            'variables': {'titleSlug': slug}
        }
    )

    problem_data = response.json()['data']['question']
    problems_data_stats = json.loads(problem_data.get('stats', '{}'))

    problem_info = {
        'problem_id': problem_data['questionFrontendId'],
        'problem_title': problem_data['title'],
        'problem_title_slug': problem_data['titleSlug'],
        'problem_difficulty': problem_data['difficulty'],
        'problem_paid_only': 'Free' if problem_data['isPaidOnly'] is False else 'Premium',
        'problem_topic': ', '.join([topic['name'] for topic in problem_data['topicTags']]),
        'accepted': problems_data_stats['totalAccepted'],
        'submissions': problems_data_stats['totalSubmission'],
        'acceptance_rate': problems_data_stats['acRate'],
    }

    return problem_info