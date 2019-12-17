# -*- coding: utf-8 -*-
# 11.12.2019
# ----------------------------------------------------------------------------------------------------------------------
# Runtime user configuration generator.
# Special for 'ssh-access' role.
# ----------------------------------------------------------------------------------------------------------------------
# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from itertools import chain

from ansible import errors
from ansible.parsing.yaml.objects import AnsibleUnicode


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
    # print(hostname) #### TEST
    if not isinstance(hostname, (AnsibleUnicode, unicode)):
        raise errors.AnsibleFilterError("hostname is {} expected <type 'unicode'>".format(type(hostname)))
    # __________________________________________________________________________
    # user_roles
    if not isinstance(user_roles, list):
        raise errors.AnsibleFilterError("user_roles is {} expected <type 'list'>".format(type(user_roles)))
    for i, r in enumerate(user_roles):
        if not isinstance(r, dict):
            raise errors.AnsibleFilterError(
                "user_roles contains {}  expected <type 'dict'> :: index: {}".format(type(r), i))
        if not (isinstance(r.get('name'), (AnsibleUnicode, unicode)) and r.get(u'name')):
            raise errors.AnsibleFilterError("user role without name :: index: {}".format(i))
        if not isinstance(r.get('groups', []), list):
            raise errors.AnsibleFilterError(
                "role.groups is {} expected <type 'list'> :: role: {}".format(type(r.get('groups')), r['name']))
        if not isinstance(r.get('hosts', []), list):
            raise errors.AnsibleFilterError(
                "role.hosts is {} expected <type 'list'> :: role: {}".format(type(r.get('hosts')), r['name']))
    # flat user roles list
    flat_user_roles = list(map(lambda x: x['name'], user_roles))
    # check role name uniqueness
    for r in flat_user_roles:
        if flat_user_roles.count(r) > 1:
            raise errors.AnsibleFilterError("duplicate user role :: role: {}".format(r))
    # list() to dict()
    user_roles = dict((x['name'], x) for x in user_roles)
    # __________________________________________________________________________
    # user_enabled
    if not isinstance(user_enabled, list):
        raise errors.AnsibleFilterError("user_enabled is {} expected <type 'list'>".format(type(user_enabled)))
    for i, u in enumerate(user_enabled):
        if not isinstance(u, dict):
            raise errors.AnsibleFilterError(
                "user_enabled contains {}  expected <type 'dict'> :: index: {}".format(type(u), i))
        if not (isinstance(u.get('name'), (AnsibleUnicode, unicode)) and u.get('name')):
            raise errors.AnsibleFilterError("user enabled without name :: index: {}".format(i))
        if not isinstance(u.get('hosts', []), list):
            raise errors.AnsibleFilterError(
                "user.hosts is {} expected <type 'list'> :: user: {}".format(type(u.get('hosts')), u['name']))
        if not isinstance(u.get('roles', []), list):
            raise errors.AnsibleFilterError(
                "user.roles is {} expected <type 'list'> :: user: {}".format(type(u.get('roles')), u['name']))
    # flat user enabled list
    flat_users_enabled = list(map(lambda x: x['name'], user_enabled))
    # check username uniqueness
    for u in flat_users_enabled:
        if flat_users_enabled.count(u) > 1:
            raise errors.AnsibleFilterError("duplicate user enabled :: user: {}".format(u))
    # list() to dict()
    user_enabled = dict((x['name'], x) for x in user_enabled)
    # __________________________________________________________________________
    # user_disabled
    if not isinstance(user_disabled, list):
        raise errors.AnsibleFilterError("user_disabled is {} expected <type 'list'>".format(type(user_disabled)))
    for i, x in enumerate(user_disabled):
        if not (isinstance(x, (AnsibleUnicode, unicode)) and x):
            raise errors.AnsibleFilterError("user disabled without name :: index: {}".format(i))
    # check username uniqueness
    for x in user_disabled:
        if user_disabled.count(x) > 1:
            raise errors.AnsibleFilterError("duplicate user disabled :: user: {}".format(x))
    # __________________________________________________________________________
    # group_names
    if not isinstance(group_names, list):
        raise errors.AnsibleFilterError("group_names is {} expected <type 'list'>".format(type(group_names)))
    # __________________________________________________________________________
    # check conflict between enabled and disabled user list
    if len(set(flat_users_enabled) & set(user_disabled)) > 0:
        raise errors.AnsibleFilterError("duplicate username between enabled and disabled user list")
    # verify user role existence
    flat_used_roles = set(chain(*map(lambda x: user_enabled[x].get('roles', []), user_enabled)))
    for x in flat_used_roles:
        if x not in user_roles:
            raise errors.AnsibleFilterError("role does not exist :: name: {}".format(x))
    # set default user groups
    default_user_groups = user_roles.get('default', {}).get('groups', [])
    user_roles.pop("default", None)
    # ==================================================================================================================
    # ==================================================================================================================
    # Start of the work cycle
    # ==================================================================================================================
    for u_name in user_enabled:
        # print(u_name) #### TEST
        u_config = {u'name': u_name, u'enable': False}
        result.append(u_config)
        # ______________________________________________________________________
        # groups from user.hosts
        for h in user_enabled[u_name].get('hosts', []):
            # print("host >", h) #### TEST
            if isinstance(h, (AnsibleUnicode, unicode)):
                h = {u'name': h, u'groups': default_user_groups}
            elif isinstance(h, dict):
                if not (isinstance(h.get('name'), (AnsibleUnicode, unicode)) and h.get('name')):
                    raise errors.AnsibleFilterError("user.hosts configuration failed :: user: {}".format(u_name))
            else:
                raise errors.AnsibleFilterError(
                    "user.hosts is {} expected <type 'unicode' || 'dict'> :: user: {}".format(type(h), u_name))
            #
            h_name = h.get('name')
            if h_name == hostname or h_name in group_names or h_name == u'all':
                # ansible host/group
                u_config['groups'] = h.get('groups', default_user_groups)
                u_config['enable'] = True
                break
        # _______________________________________________________________________
        if u_config['enable'] is True:
            continue
        # _______________________________________________________________________
        # groups from user.roles
        for r in user_enabled[u_name].get('roles', []):
            # print("role >", r) #### TEST
            if not isinstance(r, (AnsibleUnicode, unicode)):
                raise errors.AnsibleFilterError(
                    "user.roles is {} expected <type 'unicode'> :: user: {}".format(type(r), u_name))
            #
            for h_name in user_roles[r].get('hosts', []):
                # print("     host >", h_name) #### TEST
                if h_name == hostname or h_name in group_names or h_name == u'all':
                    # ansible host/group
                    u_config['groups'] = user_roles[r].get('groups', default_user_groups)
                    u_config['enable'] = True
                    break
            # ___________________________________________________________________
            if u_config['enable'] is True:
                break
    # ==================================================================================================================
    # ==================================================================================================================
    # End of the work cycle
    # ==================================================================================================================
    for x in result:
        # unique groups
        _tmp = list(set(x.get('groups', [])))
        x['groups'] = _tmp
    # __________________________________________________________________________
    return result
