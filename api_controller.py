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
        f"Pushed {counters['push_by_repo'][event['repo']['name']]} times to {event['repo']['name']}"
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

    counters["push_by_repo"] = {}

    for event in events_json:
        event_type = event.get("type")
        info = mapping.get(event_type)

        if info is None:
            continue

        key = info["key"]
        counters[key] += 1

        if key == "push":
            repo_name = event["repo"]["name"]
            if repo_name not in counters["push_by_repo"]:
                counters["push_by_repo"][repo_name] = 0
            counters["push_by_repo"][repo_name] += 1

    return counters


def activit_treatment(events, counters):

    for event in events:
        event_type = event["type"]

        if event_type not in mapping:
            continue

        info = mapping[event_type]

        description_fn = info["description"]

        if callable(description_fn):
            desc = description_fn(event,counters)

        elif isinstance(description_fn, str):
            desc = description_fn

        else:
            desc = f"Did {info['key']} activity."

        print(desc)