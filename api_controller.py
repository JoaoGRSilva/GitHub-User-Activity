import requests


mapping = {
    "CommitCommentEvent": {
        "key": "commit_comment",
        "description": lambda event, counters: f"Commented in a commit: {event['repo']['name']}"
    },

    "CreateEvent": {
        "key": "create",
        "description": lambda event, counters: "Created a tag or branch."
    },

    "DeleteEvent": {
        "key": "delete_branch",
        "description": lambda event, counters: "Deleted a tag or branch."
    },

    "DiscussionEvent": {
        "key": "discussion",
        "description": None
    },

    "ForkEvent": {
        "key": "fork",
        "description": None
    },

    "GollumEvent": {
        "key": "wiki",
        "description": None
    },

    "IssueCommentEvent": {
        "key": "issue_comment",
        "description": None
    },

    "IssuesEvent": {
        "key": "issue",
        "description": None
    },

    "MemberEvent": {
        "key": "member",
        "description": None
    },

    "PublicEvent": {
        "key": "public",
        "description": None
    },

    "PullRequestEvent": {
        "key": "pull_request",
        "description": None
    },

    "PullRequestReviewEvent": {
        "key": "pullrequest_review",
        "description": None
    },

    "PullRequestReviewCommentEvent": {
        "key": "pullrequest_review_comment",
        "description": None
    },

    "PushEvent": {
        "key": "push",
        "description": lambda event, counters: (
            f"Pushed {counters['push']} times to {event['repo']['name']}"
        )
    },

    "ReleaseEvent": {
        "key": "release",
        "description": None
    },

    "WatchEvent": {
        "key": "watch",
        "description": None
    }
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

    counters = {mapping[event]["key"]: 0 for event in mapping}

    for event in events_json:
        event_type = event.get("type")

        key = mapping.get(event_type)

        if key is not None:
            counters[key] += 1

    return counters

def activit_treatment(activity_list):

    for event in activity_list:
        pass