import boto3 as boto
from moto import mock_s3

import unittest

from audiolog import s3_model

class TestS3Model(unittest.TestCase):
    """
    """

    @mock_s3
    def setUp(self):
        self.test_bucket_name = "01"
        self.test_key_name = "2016-08-05T13:47:30Z"
        self.test_value = "My name is Michael Weston. I used to be a spy."
        self.conn = boto.resouce("s3")
        self.conn.create_bucket(Bucket = test_bucket_name)
        self.data_model = s3_model.S3Model()
        self.test_bucket_name = self.data_model.bucket_name

    @mock_s3
    def test_get_entry(self):
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
