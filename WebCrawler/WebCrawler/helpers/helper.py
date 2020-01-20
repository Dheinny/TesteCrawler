from datetime import datetime

class Helper:

    @staticmethod
    def build_date(day, month, year="2012"):
        map_month = {"jan": "01", "fev": "02", "mar": "03", "abr": "04",
                     "mai": "05", "jun": "06", "jul": "07", "ago": "08",
                     "set": "09", "out": "10", "nov": "11", "dez": "12"}
        return "{}-{}-{}".format(year, map_month[month.lower()], day)

    @staticmethod
    def get_weekday(date):
        map_week = {0: "Seg", 1: "Ter", 2: "Qua", 3: "Qui", 4: "Sex", 5: "Sab", 6: "Dom"}
        weedkay_dig = datetime.strptime(date, "%Y-%m-%d").weekday()
        return map_week[weedkay_dig]

    @staticmethod
    def get_local(local):
        local = local.split("-")
        size = len(local)
        nome_local = "-".join(local[0:(size-1)]).strip()
        cidade = "" if size <= 1 else local[size-1].strip()
        return {"nome_local": nome_local, "cidade": cidade}
