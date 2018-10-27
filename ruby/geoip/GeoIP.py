from geoip2 import database

from ruby.utils import Logging
from ruby.utils.Language import Language


class GeoIP:

    def __init__(self):
        Logging.info("Loading geoip.")
        self.__reader = database.Reader('files/GeoLite2-Country.mmdb')
        self.__languages = {
            Language.PT: {
                "PT"
            },
            Language.BR: {
                "BR"
            },
            Language.EN: {
                "US",
                "AG",
                "CA",
                "AU",
                "BS",
                "BB",
                "BZ"
            },
            Language.ES: {
                "AR",
                "PY",
                "UY",
                "CO",
                "PE",
                "CL",
                "EC",
                "BO",
                "VE",
                "SV",
                "NI",
                "GT",
                "CR",
                "CU",
                "GQ",
                "HN",
                "PA",
                "DO",
                "MX",
                "ES"
            }
        }

    def get(self, address):
        try:
            response = self.__reader.country(address)
            iso_code = response.country.iso_code
            for language in self.__languages:
                if iso_code in self.__languages[language]:
                    return language
        except:
            pass
        return Language.EN
