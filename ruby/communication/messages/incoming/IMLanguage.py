from ruby.communication.messages.Incoming import Incoming
from ruby.utils.Language import Language


class IMLanguage(Incoming):
    tokens = [8, 2]

    def dispatch(self, session, buffer_array):
        languageCode = buffer_array.readByte()
        session.language = Language(languageCode)