import boto3 as boto

import unittest
import s3_model

class S3Model(object):

    def __init__(self, user_id):
		self.s3 = boto.resource("s3")
        self.bucket_name = "meiji.software.alexa.audiolog." + user_id
        self.key_prefix = user_id

    def get_entry(self, key):
        pass

    def save_entry(self, key, value):
        pass

    def remove_entry(self, key):
        pass

    def get_entry_list(self):
        pass

    def add_to_entry(self, key):
        pass
