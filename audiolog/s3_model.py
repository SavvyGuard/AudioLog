import boto3 as boto

import unittest
import s3_model

class S3Model(object):

    bucket_name = "meiji.software.alexa.audiolog"

    def __init__(self, user_id):
        self.s3_client = boto.client("s3")
        self.s3_folder = user_id + "/"

        self.entry_list = self.get_entry_list()

    def get_entry(self, key):
        pass

    def save_entry(self, key, value):
        pass

    def remove_entry(self, key):
        pass

    def get_entry_list(self):
        """
            Returns a list of entry keys
        """
        paginator = self.s3_client.get_paginator("list_objects_v2")
        response_iterator = paginator.paginate(
            Bucket=self.bucket_name,
            Delimiter="/",
            Prefix=self.s3_folder
        )
        entry_list = []
        prefix_len = len(self.s3_folder)
        for page in response_iterator:
            if not "Contents" in page:
                continue
            contents = page["Contents"]
            for content in contents:
                entry_list.append(content["key"][prefix_len:])
        return entry_list

    def add_to_entry(self, key, addition):
        pass
