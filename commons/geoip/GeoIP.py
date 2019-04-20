from geoip2 import database
from geoip2.errors import AddressNotFoundError

from commons.util.Enum.Language import Language


class GeoIP:
    __reader = None
    __languages = {}

    @staticmethod
    def build(geoip: str):
        GeoIP.__reader = database.Reader(geoip)
        GeoIP.__languages = {
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

    @staticmethod
    def get(address: str):
        try:
            response = GeoIP.__reader.country(address)
            iso_code = response.country.iso_code
            for language in GeoIP.__languages:
                if iso_code in GeoIP.__languages[language]:
                    return language
        except AddressNotFoundError:
            pass
        return Language.EN
