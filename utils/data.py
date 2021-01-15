import json, os


class Data:
    @classmethod
    def get_json_data(cls, file):
        with open("./data" + os.sep + file, "r", encoding="utf-8")as f:
            return json.load(f)
