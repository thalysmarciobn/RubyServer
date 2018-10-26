from ruby.communication.messages.Incoming import Incoming

class IM_Test(Incoming):

    tokens = [8, 2]

    def dispatch(self, Session, BufferArray):
        langueCode = BufferArray.readByte()
        Session.langueCode = langueCode