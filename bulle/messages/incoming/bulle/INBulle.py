from bulle.rpc.RpcManager import RpcManager
from commons.communication.Output import Output
from commons.communication.Rules import Rules


class INBulle(Output):
    tokens = [44, 1]
    rule = Rules.session

    def dispatch(self, session, buffer_array):
        code = buffer_array.readInt()
        print(RpcManager.proxy().getPlayerDataByCode(code))
        print(code)
