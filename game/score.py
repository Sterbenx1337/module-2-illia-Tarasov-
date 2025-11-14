# score.py
import json
import os
from .settings import *

class PlayerRecord:
    def __init__(self, name: str, difficulty: str, score: int):
        self.name = name
        self.difficulty = difficulty 
        self.score = score

    def __eq__(self, other):
        return (
            isinstance(other, PlayerRecord) and
            self.name == other.name and
            self.difficulty == other.difficulty
        )

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"{self.name} | {MODES[self.difficulty]} | {self.score}"

    def to_dict(self):
        return {
            "name": self.name,
            "difficulty": MODES[self.difficulty],
            "score": self.score
        }

    @staticmethod
    def from_dict(d):
        difficulty_key = None
        for k, v in MODES.items():
            if v == d["difficulty"]:
                difficulty_key = k
                break
        return PlayerRecord(
            d["name"],
            difficulty_key,
            d["score"]
        )


class GameRecord:
    def __init__(self):
        self.records = []

    def add_record(self, record: PlayerRecord):
        for i, existing in enumerate(self.records):
            if existing == record:
                if record.score > existing.score:
                    self.records[i] = record
                return
        self.records.append(record)

    def prepare_records(self, limit = MAX_RECORDS_NUMBER):
        self.records.sort(reverse=True)
        self.records = self.records[:limit]

class ScoreHandler:
    def __init__(self, filename="scores.json"):
        self.filename = filename
        self.game_record = GameRecord()
        self.read()

    def read(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for entry in data:
                    rec = PlayerRecord.from_dict(entry)
                    self.game_record.add_record(rec)
        except json.JSONDecodeError:
            pass

    def save(self, limit = MAX_RECORDS_NUMBER):
        self.game_record.prepare_records(limit)
        data = [rec.to_dict() for rec in self.game_record.records]

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def display(self):
        print("\n===== SCORE TABLE =====")
        for rec in self.game_record.records:
            print(rec)
        print("=======================\n")
