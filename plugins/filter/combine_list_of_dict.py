# -*- coding: utf-8 -*-
# 11.12.2019
# ----------------------------------------------------------------------------------------------------------------------
# Combine two lists from dictionaries by key.
# ----------------------------------------------------------------------------------------------------------------------
# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible import errors


class FilterModule(object):
    @staticmethod
    def filters():
        return {
            'combine_list_of_dict': combine_list_of_dict,
        }


def combine_list_of_dict(default_list, combine_list, key):
    """
    default_list <type 'list'>
    combine_list <type 'list'>
    key <type 'str'>
    """
    result = []
    # __________________________________________________________________________
    # default_list
    if not isinstance(default_list, list):
        raise errors.AnsibleFilterError("default_list is {} expected <type 'list'>".format(type(default_list)))
    for i, x in enumerate(default_list):
        if not isinstance(x, dict):
            raise errors.AnsibleFilterError(
                "default_list contains {} expected <type 'dict'> :: index: {}".format(type(x), i))
    flat_default_keys = list(map(lambda x: x['name'], default_list))
    if len(flat_default_keys) > len(set(flat_default_keys)):
        raise errors.AnsibleFilterError("default_list has duplicate keys")
    # combine_list
    if not isinstance(combine_list, list):
        raise errors.AnsibleFilterError("combine_list is {} expected <type 'list'>".format(type(combine_list)))
    for i, x in enumerate(combine_list):
        if not isinstance(x, dict):
            raise errors.AnsibleFilterError(
                "combine_list contains {} expected <type 'dict'> :: index: {}".format(type(x), i))
    flat_combine_keys = list(map(lambda x: x['name'], combine_list))
    if len(flat_combine_keys) > len(set(flat_combine_keys)):
        raise errors.AnsibleFilterError("flat_combine_keys has duplicate keys")
    # key
    if not isinstance(key, str):
        raise errors.AnsibleFilterError("key is {} expected <type 'str'>".format(type(key)))
    # ==================================================================================================================
    # ==================================================================================================================
    # Start of the work cycle
    # ==================================================================================================================
    for x in set(flat_default_keys + flat_combine_keys):
        if x in flat_combine_keys:
            result.append(combine_list[flat_combine_keys.index(x)])
        else:
            result.append(default_list[flat_default_keys.index(x)])
    # ==================================================================================================================
    # ==================================================================================================================
    # End of the work cycle
    # ==================================================================================================================
    # __________________________________________________________________________
    return result
