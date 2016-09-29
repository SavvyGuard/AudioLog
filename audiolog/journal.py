import datetime

import s3_model

class Journal(object):

    def __init__(self, user_id):
        self.model = s3_model.S3Model(user_id)
        self.user_id = user_id
        self.entries = self.model.get_entry_list()

    def get_user_id(self):
        return self.user_id

    def record_current_entry(self, entry):
        dt = datetime.datetime.today()
        return record_entry(self, dt, entry)

    def record_entry(self, dt, entry):
        if dt in self.entries:
            raise JournalEntryDupe(dt)
        if entry is not None and len(entry) > 0:
            result = self.model.save_entry(dt, entry)
            self.entries.append(dt)
            self.entries.sort(reverse=True)
        else:
            raise JournalEntryEmpty(dt)

    def read_entry(self, dt):
        pass

class JournalEntryEmpty(Exception):
    def __init__(self, dt):
        self.dt = dt
    def __str__(self):
        return "Cannot record empty entry for {0}".format(self.dt)

class JournalEntryDupe(Exception):
    def __init__(self, dt):
        self.dt = dt
    def __str__(self):
        return "Cannot record duplicate entry for {0}".format(self.dt)
