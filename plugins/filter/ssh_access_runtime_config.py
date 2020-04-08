# -*- coding: utf-8 -*-
# 06.04.2020
# ----------------------------------------------------------------------------------------------------------------------
# Runtime user configuration generator.
# Special for 'ssh-access' role.
# ----------------------------------------------------------------------------------------------------------------------
# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import sys
from itertools import chain

from ansible import errors
from ansible.parsing.yaml.objects import AnsibleUnicode

if sys.version[0] == "2":
    __str = unicode
else:
    __str = str


class FilterModule(object):
    @staticmethod
    def filters():
        return {
            'ssh_access_runtime_config': ssh_access,
        }


def ssh_access(hostname, user_roles, user_enabled, user_disabled, group_names):
    """
    hostname <type 'unicode'>
    user_roles <type 'list'> (to <type 'dict'>)
    user_enabled <type 'list'> (to <type 'dict'>)
    user_disabled <type 'list'>
    group_names <type 'list'>
    """
    result = []
    # __________________________________________________________________________
    # hostname
    # print(hostname)  #### TEST
    # print(type(hostname))  #### TEST
    if not isinstance(hostname, (AnsibleUnicode, __str)):
        raise errors.AnsibleFilterError("hostname is {} expected <type 'str'>".format(type(hostname)))
    # __________________________________________________________________________
    # user_roles
    if not isinstance(user_roles, list):
        raise errors.AnsibleFilterError("user_roles is {} expected <type 'list'>".format(type(user_roles)))
    for i, r in enumerate(user_roles):
        if not isinstance(r, dict):
            raise errors.AnsibleFilterError(
                "user_roles contains item {} expected <type 'dict'> :: index: {}".format(type(r), i))
        if not (isinstance(r.get('name'), (AnsibleUnicode, __str)) and r.get(u'name')):
            raise errors.AnsibleFilterError("user_roles contains item without name :: index: {}".format(i))
        if not isinstance(r.get('user_groups', []), list):
            raise errors.AnsibleFilterError(
                "user_groups is {} expected <type 'list'> :: user role: {}".format(
                    type(r.get('user_groups')), r['name']))
        if not isinstance(r.get('user_hosts', []), list):
            raise errors.AnsibleFilterError(
                "user_hosts is {} expected <type 'list'> :: user role: {}".format(
                    type(r.get('user_hosts')), r['name']))
    # flat user roles list
    flat_user_roles = list(map(lambda x: x['name'], user_roles))
    # check role name uniqueness
    for r in flat_user_roles:
        if flat_user_roles.count(r) > 1:
            raise errors.AnsibleFilterError("duplicate user role :: {}".format(r))
    # list() to dict()
    user_roles = dict((x['name'], x) for x in user_roles)
    # __________________________________________________________________________
    # user_enabled
    if not isinstance(user_enabled, list):
        raise errors.AnsibleFilterError("user_enabled is {} expected <type 'list'>".format(type(user_enabled)))
    for i, u in enumerate(user_enabled):
        if not isinstance(u, dict):
            raise errors.AnsibleFilterError(
                "user_enabled contains item {} expected <type 'dict'> :: index: {}".format(type(u), i))
        if not (isinstance(u.get('name'), (AnsibleUnicode, __str)) and u.get('name')):
            raise errors.AnsibleFilterError("user_enabled contains item without name :: index: {}".format(i))
        if not isinstance(u.get('user_hosts', []), list):
            raise errors.AnsibleFilterError(
                "user_hosts is {} expected <type 'list'> :: user enabled: {}".format(
                    type(u.get('user_hosts')), u['name']))
        if not isinstance(u.get('user_roles', []), list):
            raise errors.AnsibleFilterError(
                "user_roles is {} expected <type 'list'> :: user enabled: {}".format(
                    type(u.get('user_roles')), u['name']))
    # flat user enabled list
    flat_users_enabled = list(map(lambda x: x['name'], user_enabled))
    # check username uniqueness
    for u in flat_users_enabled:
        if flat_users_enabled.count(u) > 1:
            raise errors.AnsibleFilterError("duplicate user enabled :: {}".format(u))
    # list() to dict()
    user_enabled = dict((x['name'], x) for x in user_enabled)
    # __________________________________________________________________________
    # user_disabled
    if not isinstance(user_disabled, list):
        raise errors.AnsibleFilterError("user_disabled is {} expected <type 'list'>".format(type(user_disabled)))
    for i, x in enumerate(user_disabled):
        if not (isinstance(x, (AnsibleUnicode, __str)) and x):
            raise errors.AnsibleFilterError(
                "user_disabled contains item {} expected <type 'str'> :: index: {}".format(type(x), i))
        # check username uniqueness
    for x in user_disabled:
        if user_disabled.count(x) > 1:
            raise errors.AnsibleFilterError("duplicate user disabled :: {}".format(x))
    # __________________________________________________________________________
    # group_names
    if not isinstance(group_names, list):
        raise errors.AnsibleFilterError("group_names is {} expected <type 'list'>".format(type(group_names)))
    # __________________________________________________________________________
    # check conflict between enabled and disabled user list
    if len(set(flat_users_enabled) & set(user_disabled)) > 0:
        raise errors.AnsibleFilterError("duplicate username between enabled and disabled user list")
    # verify user role existence
    flat_used_roles = set(chain(*map(lambda x: user_enabled[x].get('user_roles', []), user_enabled)))
    for x in flat_used_roles:
        if x not in user_roles:
            raise errors.AnsibleFilterError("user role does not exist :: name: {}".format(x))
    # set default user groups
    default_user_groups = user_roles.get('default', {}).get('user_groups', [])
    user_roles.pop("default", None)
    # ==================================================================================================================
    # ==================================================================================================================
    # Start of the work cycle
    # ==================================================================================================================
    for u_name in user_enabled:
        # print(u_name)  #### TEST
        u_config = {u'name': u_name, u'enable': None}
        result.append(u_config)
        # ______________________________________________________________________
        # groups from user.user_hosts
        for h in user_enabled[u_name].get('user_hosts', []):
            # print("host >", h)  #### TEST
            if isinstance(h, (AnsibleUnicode, __str)):
                h = {u'name': h, u'user_groups': default_user_groups}
            elif isinstance(h, dict):
                if not (isinstance(h.get('name'), (AnsibleUnicode, __str)) and h.get('name')):
                    raise errors.AnsibleFilterError(
                        "user_hosts configuration failed :: user enabled: {}".format(u_name))
                if not (isinstance(h.get('enable', True), bool)):
                    raise errors.AnsibleFilterError(
                        "user enable flag is {} expected <type 'bool'> :: user enabled: {}".format(
                            type(h.get('enable')), u_name))
            else:
                raise errors.AnsibleFilterError(
                    "user.hosts is {} expected <type 'str' || 'dict'> :: user enabled: {}".format(type(h), u_name))
            #
            h_name = h.get('name')
            if h_name == hostname or h_name in group_names or h_name == u'all':
                # ansible host/group
                u_config['user_groups'] = h.get('user_groups', default_user_groups)
                u_config['enable'] = h.get('enable', True)
                break
        # ______________________________________________________________________
        if u_config['enable'] is not None:
            continue
        # ______________________________________________________________________
        # groups from user.user_roles
        for r in user_enabled[u_name].get('user_roles', []):
            # print("role >", r)  #### TEST
            if not isinstance(r, (AnsibleUnicode, __str)):
                raise errors.AnsibleFilterError(
                    "user_roles is {} expected <type 'str'> :: user enabled: {}".format(type(r), u_name))
            #
            for h_name in user_roles[r].get('user_hosts', []):
                # print("     host >", h_name)  #### TEST
                if h_name == hostname or h_name in group_names or h_name == u'all':
                    # ansible host/group
                    u_config['user_groups'] = user_roles[r].get('user_groups', default_user_groups)
                    u_config['enable'] = True
                    break
            # __________________________________________________________________
            if u_config['enable'] is True:
                break
        # ______________________________________________________________________
        if u_config['enable'] is None:
            u_config['enable'] = False
    # ==================================================================================================================
    # ==================================================================================================================
    # End of the work cycle
    # ==================================================================================================================
    for x in result:
        # unique groups
        _tmp = list(set(x.get('user_groups', [])))
        x['user_groups'] = _tmp
    for x in user_disabled:
        result.append({u'name': x, u'enable': False, u'user_groups': []})
    # print(result)  #### TEST
    # __________________________________________________________________________
    return result
