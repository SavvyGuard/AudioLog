import datetime
import unittest

from moto import mock_s3
import test_model

from audiolog import journal

class TestJournalClass(unittest.TestCase):

    def setUp(self):
        # Required for mocking the s3 model
        self.mock, _ = test_model.set_up_mock()
        self.test_user_id = "001"
        self.journal = journal.Journal(self.test_user_id)
        self.today_datetime = datetime.datetime.today()
        self.test_entry = "My name is Michael Weston."

    def tearDown(self):
        # Required for mocking the s3 model
        test_model.tear_down_mock(self.mock)

    def test_get_user_id(self):
        self.assertEqual(self.journal.get_user_id(), self.test_user_id)

    def test_record_entry(self):
        """
            Accepts datetime object and a value
        """
        self.journal.record_entry(
            self.today_datetime, self.test_entry)

        # test that latest entry can be read
        pass

    def test_record_entry_empty(self):
        """
            When provided an empty entry do not record
        """
        with self.assertRaises(journal.JournalEntryEmpty):
            self.journal.record_entry(
                self.today_datetime, "")

    def test_record_entry_dupe(self):
        """
            Raises error when duplicate time stamps
            entered
        """
        with self.assertRaises(journal.JournalEntryDupe):
            self.journal.record_entry(
                self.today_datetime, self.test_entry)
            self.journal.record_entry(
                self.today_datetime, self.test_entry)

    def test_read_entry(self):
        """
            Reads an entry when provided a datetime

            Raise JournalEntryNotFound error if entry
            missing
        """
        self.journal.record_entry(
            self.today_datetime, self.test_entry)
        read_value = self.journal.read_entry(self.today_datetime)
