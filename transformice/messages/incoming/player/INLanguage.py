from commons.communication.Incoming import Incoming
from commons.communication.Rules import Rules
from commons.util.Enum.Language import Language


class INLanguage(Incoming):
    tokens = [8, 2]
    rule = Rules.session

    def dispatch(self, session, buffer_array):
        languageCode = buffer_array.readByte()
        session.language = Language(languageCode)