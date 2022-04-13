from github import Github


def main():
    # First create a Github instance:

    # using an access token
    g = Github("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")
    g.get_user()

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)
        


main()