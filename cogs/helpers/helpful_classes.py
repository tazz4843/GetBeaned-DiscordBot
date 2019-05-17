class LikeUser:
    def __init__(self, did, name, guild, discriminator='0000',
                 avatar_url="https://cdn.discordapp.com/embed/avatars/1.png", bot=False,
                 do_not_update=True):
        # Special users IDs:

        # 0 : Ban list import
        # 1 : Automod
        # 2 : Thresholds
        # 3 : Dehoister

        self.id = did
        self.name = name
        self.guild = guild
        self.discriminator = discriminator
        self.avatar_url = avatar_url
        self.default_avatar_url = avatar_url
        self.do_not_update = do_not_update
        self.bot = bot

    def avatar_url_as(self, *args, **kwargs):
        return self.avatar_url


class FakeMember:
    def __init__(self, user, guild):
        self._user = user
        self.guild = guild

    def __getattr__(self, item):
        return getattr(self._user, item)
