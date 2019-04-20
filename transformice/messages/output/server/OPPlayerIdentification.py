from commons.communication.Output import Output


class OPPlayerIdentification(Output):
    tokens = [26, 2]

    def __init__(self, player_id: int, player_name: str, player_time: int, language_code: int, player_code: int,
                 guest: bool, privilege_level: int, lua_dev: bool, map_crew: bool, fun_corp: bool, fashion_squad: bool):
        super().__init__()
        count = 0
        permCount = 0
        ranks = []
        self.bufferArray.writeInt(player_id)
        self.bufferArray.writeUTF(player_name)
        self.bufferArray.writeInt(player_time)
        self.bufferArray.writeByte(language_code)
        self.bufferArray.writeInt(player_code)
        self.bufferArray.writeBool(not guest)
        permList = [False, False, False, privilege_level >= 3, False, privilege_level >= 5, False, False, False, False,
                    privilege_level == 10, map_crew, lua_dev, fun_corp, False, fashion_squad]
        while len(permList) > count:
            if permList[permCount]:
                ranks.append(permCount == permCount + 1)
            count += 1
        self.bufferArray.writeByte(permCount)
        for rank in ranks:
            self.bufferArray.writeByte(rank)
        self.bufferArray.writeBool(lua_dev or fashion_squad)
