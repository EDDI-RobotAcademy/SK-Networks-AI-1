from player_domain.entity.players import Players


class Player_Domain():
    def checkid(self, playerid):
        if (len(Players.playerlist) < playerid) | (0 >= playerid):
            print("id doesn't exist")
            return False
        else:
            print("id exists. loading nickname...")
            return True

    def getnickname(self, playerid, flag):
        if flag == True:
            return list(Players.playerlist[playerid - 1].values())
        if flag == None:
            return None
