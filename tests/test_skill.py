import unittest
import json

from audiolog import skill

class TestSkill(unittest.TestCase):

    def __init__(self):
        record_intent_filename = "test_requests/record_intent.json"
        with open(record_intent_filename) as f:
           record_intent = json.loads(f.read())
        self.record_intent = record_intent

    def setup(self):
        pass

    def record_new(self):
        pass

    def play_last(self):
        pass

    def play_all(self):
        pass
