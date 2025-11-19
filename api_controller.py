import requests


mapping = {
    "CommitCommentEvent": "commit_comment",
    "CreateEvent": "create",
    "DeleteEvent": "delete_branch",
    "DiscussionEvent": "discussion",
    "ForkEvent": "fork",
    "GollumEvent": "wiki",
    "IssueCommentEvent": "issue_comment",
    "IssuesEvent": "issue",
    "MemberEvent": "member",
    "PublicEvent": "public",
    "PullRequestEvent": "pull_resquest",
    "PullRequestReviewEvent": "pullrequest_review",
    "PullRequestReviewCommentEvent": "pullrequest_review_comment",
    "PushEvent": "push",
    "ReleaseEvent": "realease",
    "WatchEvent": "watch"
}

def fetch_user_activity(username):
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-Github-Api-Version': '2022-11-28',
    }

    response = requests.get(f'https://api.github.com/users/{username}/events', headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro ao buscar eventos. Status code: {response.status_code}")
        return []

def count_user_activit(events_json):

    counters = {key: 0 for key in mapping.values()}

    for event in events_json:
        event_type = event.get("type")

        key = mapping.get(event_type)

        if key is not None:
            counters[key] += 1

    return counters