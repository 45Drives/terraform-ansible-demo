import ansible.utils as utils
import ansible.errors as errors
from ansible.plugins.lookup import LookupBase
import random

class LookupModule(LookupBase):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, variables=None, **kwargs):

        items = terms[0]
        excluded_items = terms[1]

        if not isinstance(items, list) or len(items) < 1:
            raise errors.AnsibleError("randomlist lookup expects a populated list (items)")

        if not isinstance(items, list):
            raise errors.AnsibleError("randomlist lookup expects a list (excluded_items)")

        item = None

        if len(items) == 1 or len(items) <= len(excluded_items):
            item = random.choice(items)
        else:
            while item == None:
                opt = random.choice(items)

                if opt not in excluded_items:
                    item = opt

        return [item]