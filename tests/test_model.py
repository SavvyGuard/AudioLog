import boto3 as boto
from moto import mock_s3

import unittest

from audiolog import s3_model


def set_up_mock():
    mock = mock_s3()
    mock.start()
    client = boto.client("s3")
    client.create_bucket(Bucket = s3_model.S3Model.bucket_name)

    return mock, client

def tear_down_mock(mock):
    mock.stop()

class TestS3Model(unittest.TestCase):
    """
    """
    def setUp(self):
        self.mock, self.client = set_up_mock()
        self.test_user_id = "01"
        self.test_key_name = "2016-08-05T13:47:30Z"
        self.test_value = "My name is Michael Weston. I used to be a spy."
        self.test_bucket_name = s3_model.S3Model.bucket_name
        self.data_model = s3_model.S3Model(self.test_user_id)

    def tearDown(self):
        tear_down_mock(self.mock)

    def test_get_entry(self):
        self.data_model.save_entry(self.test_key_name, self.test_value)

        self.assertEqual(self.client.get_object(
                    Bucket=self.test_bucket_name,
                    Key=self.test_user_id + "/" + self.test_key_name)["Body"].read()
            , self.data_model.get_entry(self.test_key_name))

    def test_get_entry_nonexistent(self):
        with self.assertRaises(s3_model.MissingResource):
            self.data_model.get_entry(self.test_key_name)

    def test_save_entry(self):
        self.data_model.save_entry(self.test_key_name, self.test_value)
        self.assertEqual(self.data_model.get_entry(self.test_key_name), self.test_value)

    def test_remove_entry(self):
        self.data_model.save_entry(self.test_key_name, self.test_value)
        self.data_model.remove_entry(self.test_key_name)
        with self.assertRaises(s3_model.MissingResource):
            self.data_model.get_entry(self.test_key_name)

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

    def test_add_to_entry(self):
        test_addition = " I was that is."
        self.data_model.save_entry(self.test_key_name, self.test_value)
        self.data_model.add_to_entry(self.test_key_name, test_addition)
        self.assertEqual(self.data_model.get_entry(self.test_key_name
            ), self.test_value + test_addition)
