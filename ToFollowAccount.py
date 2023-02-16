from helpers.tweepyClient import getTweepyClient

client = getTweepyClient()


class ToFollowAccount:
    def __init__(self, username) -> None:
        self.username = username

    # Get user object for bio etc
    def getUserObject(self):
        return client.get_user(
            username=self.username, user_fields="entities,description"
        )

    # Substack trim

    # Nft trim

    # Update ToFollowList so that all checks are done and unneeded elements are removed
