from player_domain.entity.playerdomain import Player_Domain
from player_domain.repository.playerdomain_repository import PlayerDomain_Repo


class PlayerDomain_Repo_Impl(PlayerDomain_Repo):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__nickname = None
            return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def get_playerid_and_nickname(self, pid):
        pd = Player_Domain()
        flag = pd.checkid(pid)
        try:
            self.__nickname = pd.getnickname(pid, flag)[0]
            return pid, self.__nickname
        except Exception as e:
            pass