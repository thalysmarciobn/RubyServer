from controller.bulle.BulleManager import BulleManager


class RpcFunctions:

    @staticmethod
    def updateBulle(address: str):
        BulleManager.update(address)


    @staticmethod
    def enterRoom(language_code: str, code: int, name: str):
        print("aaaaaaaaaaaa")

    @staticmethod
    def getPlayerDataByCode(code: int):
        print("asasasa")
        print(BulleManager.getSession(code).data())
        session = BulleManager.getSession(code)
        if session is not None:
            return session.data()
        return None