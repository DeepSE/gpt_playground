
from datetime import datetime
from github import Github
import json
import logging

from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# does not raise an exception, but returns None
git_token = os.getenv('GITHUB_TOKEN')

if git_token is None:
    logger.error('Specify GITHUB_TOKEN as an environment variable.')
    exit(-1)

gh = Github(git_token)

def webhook(content):
    action =   content['action']
    if action != 'opened': 
      return -1 # Nothing to do

    repos_name = content['repository']['full_name']
    issue = content['issue']

    no = issue['number']
    user = issue['user']['login']

    title = issue['title']
    body = issue['body']
  
    start = time.time()
    n = index(title + "\n" + body, id=no, index_name=repos_name.replace('/', '_').lower())
    end = time.time()

    print(repos_name, no, user, title, body)

def write_comment(comment, repos_name, issueid):
    repo = gh.get_repo(repos_name)

    thread_issue = repo.get_issue(number=int(issueid))
    if thread_issue:
        res = thread_issue.create_comment(comment)
        logger.info("Comment on " + str(res))
        return


if __name__ == '__main__':
    write_comment("Test", 'hunkim/digital-human', 1)