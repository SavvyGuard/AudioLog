import boto
from moto import mock_s3
from mymodule import MyModel
import unittest

class TestS3Model(unittest.TestCase):
	"""
	"""
	@mock_s3
	def setUp(self):
		self.test_key_name = "2016-08-05T13:47:30Z"
		self.test_value = "My name is Michael Weston. I used to be a spy."
		self.conn = boto.connect_s3()
		self.conn.create_bucket(test_bucket_name)
		self.data_model = s3_model.S3Model()
		self.test_bucket_name = self.data_model.bucket_name

    @mock_s3
    def test_get_entry(self)
        self.data_model.save_entry(self.test_key_name, self.test_value)
		self.assertEqual(self.conn.get_bucket(self.test_bucket_name
            ).get_key(self.test_key_name
            ).get_contents_as_string(), self.data_model.get_entry(self.test_key_name))

	@mock_s3
	def test_save_entry(self):
		self.data_model.save_entry(self.test_key_name, self.test_value)
		self.assertEqual(self.data_model.get_entry(self.test_key_name), log_entry)

	@mock_s3
	def test_remove_entry(self):
		self.data_model.save_entry(self.test_key_name, self.test_value)
		self.data_model.remove_entry(self.test_key_name, self.test_value)
        self.assertEqual(self.data_model.get_entry(self.test_key_name), None)

	@mock_s3
	def test_get_entry_list(self):
        """
            Should return higher values first
        """
		test_entry_names = ["1", "40", "5", "6", "4", "30"]
		for test_name in test_entry_names:
			self.data_model.save_entry(test_name, self.test_value)
		entry_list = self.data_model.get_entry_list()
        sorted_entry_names = sorted(test_entry_names, reverse = True)
		for ii in xrange(len(test_entry_names)):
            self.assertEqual(entry_list[ii],sorted_entry_names[ii])

    @mock_s3
    def test_add_to_entry(self):
        test_addition = " I was that is."
        self.data_model.save_entry(self.test_key_name, self.test_value)
        self.data_model.add_to_entry(self.test_key_name, test_addition)
        self.assertEqual(self.data_model.get_entry(self.test_key_name
            ), self.test_value + test_addition)

class TestJournalClass(unittest.TestCase):

    def setUp(self):
        self.test_user_id = "001"
        self.journal = journal.Journal(self.test_user_id)
        self.today_datetime = datetime.datetime.today()
        self.test_entry = "My name is Michael Weston."

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
        with self.assertRaises JournalEntryEmpty as e:
            self.journal.record_entry(
                self.today_datetime, "")

    def test_record_entry_dupe(self):
        """
            Raises error when duplicate time stamps
            entered
        """
        with self.assertRaises JournalEntryDupe as e:
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
        self.assertEqual(read_value, self.test_entry)
        with self.assertRaises JournalEntryNotFound as e:
            self.journal.read_entry(
                self.today_datetime + datetime.timedelta(days=1))

    def test_append_entry(self):
        """
            Raises JournalEntryNotFound if append
            attempted
        """
        appended_text = " appended text"
        with self.assertRaises JournalEntryNotFound as e:
            self.journal.append_entry(
                self.today_datetime, appended_text)
        self.journal.record_entry(
            self.today_datetime, self.test_entry)
        self.assertEqual(
            self.journal.read_entry(self.today_datetime),
            self.test_entry)
        self.journal.append_entry(
            self.today_datetime, appended_text)
        self.assertEqual(
            self.journal.read_entry(self.today_datetime),
            self.test_entry + self.appended_text)

    def test_remove_entry(self):
        """
            Remove entry. Throw up error if not found
        """
        self.journal.record_entry(
            self.today_datetime, self.test_entry)
        self.assertEqual(
            self.journal.read_entry(self.today_datetime),
            self.test_entry)
        self.journal.remove_entry(self.today_datetime)
        with self.assertRaises JournalEntryNotFound as e:
            self.journal.read_entry(self.today_datetime)
        with self.assertRaises JournalEntryNotFound as e:
            self.journal.remove_entry(self.today_datetime)

    def test_get_latest_entry(self):
        yester_datetime = self.today_datetime - datetime.timedelta(days = 1),
        self.journal.record_entry(
            yester_datetime,
            self.test_entry)
        self.assertEqual(self.get_latest_entry(),
            (yester_datetime, self.test_entry))
        self.journal.record_entry(
            self.today_datetime,
            "today's entry")
        self.assertEqual(self.get_latest_entry(),
            (self.today_datetime, "today's entry"))

    def test_get_day_entries(self):
        """
            Return the entries from a given day
            by local time
        """
        pass
    def test_get_today_entries(self):
        """
            Return the entries from today by local time
        """
        pass

    def test_get_last_week_entries(self):
        """
            Return the entries from last 7 days in order of
            latest first
        """
        for ii in xrange(7)
            ii_datetime = self.today_datetime - datetime.timedelta(days = ii)
            self.journal.record_entry(
                yester_datetime,
                str(ii))
        current_datetime = self.today_datetime
        days_prev = 0
        for entry_datetime, entry in self.get_last_week_entries():
            self.assertEqual(entry_datetime, current_datetime)
            self.assertEqual(entry, str(days_prev))
            days_prev += 1
            current_datetime += datetime.timedelta(days = 1)

    def test_get_last_month_entries(self):
        pass

    def test_remove_all_entries(self):
        pass
