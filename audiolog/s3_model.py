import boto3 as boto
import botocore

import unittest
import s3_model

class S3Model(object):

    bucket_name = "meiji.software.alexa.audiolog"

    def __init__(self, user_id):
        self.s3_client = boto.client("s3")
        self.s3_folder = user_id + "/"
        self.key_format = "{0}{1}".format(self.s3_folder, "{0}")
        self.entry_list = self.get_entry_list()


    def get_entry(self, key):
        try:
            entry = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=self.key_format.format(key)
                )["Body"].read()
        except botocore.exceptions.ClientError as e:
            raise MissingResource(key, str(e))
        return entry

    def save_entry(self, key, value):
        self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=self.key_format.format(key),
                Body=value)

    def remove_entry(self, key):
        try:
            result = self.s3_client.delete_object(
                Bucket=self.bucket_name,
                Key=self.key_format.format(key))["DeleteMarker"]
        except KeyError as e:
            return False
        return result

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
                entry_list.append(content["Key"][prefix_len:])
        entry_list.sort(reverse=True)
        return entry_list

    def add_to_entry(self, key, addition):
        old_value = self.get_entry(key)
        self.save_entry(key, old_value + addition)

class MissingResource(Exception):
   def __init__(self, value, underlying = None):
       self.value = value
       self.underlying = underlying
   def __str__(self):
       return "Could not find resource: {0}; {1}".format(self.value, self.underlying)
