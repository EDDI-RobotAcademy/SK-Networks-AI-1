from initializer.domain_initializer import DomainInitializer
from player_domain.repository.playerdomain_repository_impl import PlayerDomain_Repo_Impl

DomainInitializer.initPlayerDomain()

if __name__ == "__main__":
    pdri = PlayerDomain_Repo_Impl.getInstance()
    ppid = int(input("ID:"))
    try:
        pid, nick = pdri.get_playerid_and_nickname(ppid)
        print(f"player {pid}'s nickname is {nick}")
    except Exception as e:
            print("Bye.")