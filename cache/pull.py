#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 23.12.2020
# ----------------------------------------------------------------------------------------------------------------------
import os
import signal
import sys
import traceback
import warnings

warnings.filterwarnings(action='ignore', module='OpenSSL')

import requests
import urllib3

urllib3.disable_warnings()

try:
    # python 3
    # noinspection PyUnresolvedReferences,PyUnresolvedReferences
    from urllib.parse import urlparse
except ImportError:
    # python 2
    # noinspection PyUnresolvedReferences,PyUnresolvedReferences
    from urlparse import urlparse

_SELF_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
_LINKS_FILE_NAME = ".links"
_BUFFER = {}


def main():
    main_return_value = True
    set_of_directories = set()
    # __________________________________________________________________________
    # scan directory tree
    for i, x in enumerate(os.walk(_SELF_DIR)):
        if i == 0:
            continue
        d = x[0]  # directory
        f = x[2]  # files
        if _LINKS_FILE_NAME in f:
            set_of_directories.add(d)
    # ==================================================================================================================
    signal.signal(signal.SIGINT, signal_handler_sigint)
    for d in sorted(set_of_directories):
        set_of_url = set()
        # ______________________________________________________________________
        # read links
        try:
            with open(os.path.join(d, _LINKS_FILE_NAME), 'r') as f:
                for line_read in f.readlines():
                    line_strip = line_read.strip()
                    if not line_strip:
                        continue
                    if line_strip.find('#') == 0:
                        continue
                    line_split = line_strip.split()
                    complex_url = ComplexURL(line_split[0])
                    if not complex_url.valid:
                        print("[EE] Invalid URL :: {}".format(line_strip))
                        main_return_value = False
                        continue
                    if len(line_split) == 1:
                        file_url = complex_url.url
                        file_name = os.path.basename(complex_url.path)
                        file_perm = None
                    elif len(line_split) == 2:
                        file_url = complex_url.url
                        file_name = line_split[1]
                        file_perm = None
                    elif len(line_split) == 3:
                        file_url = complex_url.url
                        file_name = line_split[1]
                        file_perm = line_split[2]
                    else:
                        print("[EE] Invalid string :: {}".format(line_strip))
                        main_return_value = False
                        continue
                    # __________________________________________________________
                    set_of_url.add((d, file_url, file_name, file_perm))
        except Exception as err:
            print("[!!] Exception :: {}\n{}".format(err, "".join(traceback.format_exc())))
            main_return_value = False
        # ______________________________________________________________________
        # download files
        for x in set_of_url:
            d = x[0]
            url = x[1]
            name = x[2]
            perm = x[3]
            path = os.path.join(d, name)
            if os.path.exists(path):
                print("Cached:   {}".format(path.split(_SELF_DIR + os.path.sep)[1]))
            else:
                if not download(url, path, perm):
                    main_return_value = False
    # ==================================================================================================================
    print("\n{}".format("-" * 120))
    if main_return_value:
        print("Successfully done")
    else:
        print("Exit with an error")
    # __________________________________________________________________________
    return main_return_value


# ======================================================================================================================
# Classes
# ======================================================================================================================
class ComplexURL(object):
    def __init__(self, url):
        self.valid = False
        self.url = url
        try:
            # scheme://netloc/path;parameters?query#fragmen
            url_parse = urlparse(url)
            self.scheme = url_parse.scheme
            self.netloc = url_parse.netloc
            self.username = url_parse.username
            self.password = url_parse.password
            self.hostname = url_parse.hostname
            self.port = url_parse.port
            self.path = url_parse.path
            self.params = url_parse.params
            self.query = url_parse.query
        except Exception as err:
            print("[!!] Exception :: {}\n{}".format(err, "".join(traceback.format_exc())))
            return
        # ______________________________________________________________________
        if not (self.scheme and self.netloc and self.hostname):
            return
        if not self.port:
            if self.scheme == 'https':
                self.port = 443
            else:
                self.port = 80
        if not self.path:
            self.path = "/"
        # ______________________________________________________________________
        self.valid = True
        return


# ======================================================================================================================
# Functions
# ======================================================================================================================
def fs_rm_file(path):
    try:
        os.remove(path)
    except Exception as err:
        print("[!!] Exception :: {}\n{}".format(err, "".join(traceback.format_exc())))
        return False
    # __________________________________________________________________________
    return True


def download(src, trg, perm=None):
    # proxies = get_proxies()
    # print(proxies)
    try:
        _BUFFER['path'] = trg
        with open(trg, "wb") as f:
            # __________________________________________________________________
            print("Download: {} \n          ({})".format(trg.split(_SELF_DIR + os.path.sep)[1], src))
            sys.stdout.flush()
            sys.stdout.write(" connecting ...\r")
            sys.stdout.flush()
            response = requests.get(src, stream=True, verify=False)
            content_length = response.headers.get('content-length')
            if content_length is None:
                content_download = 0
                sys.stdout.write("{}\r".format(content_download))
                sys.stdout.flush()
                for data in response.iter_content(chunk_size=32768):
                    content_download += len(data)
                    sys.stdout.write("{:<64}\r".format(content_download))
                    sys.stdout.flush()
                    f.write(data)
            else:
                content_length_len = len(content_length)
                content_length_int = int(content_length)
                content_download = 0
                for data in response.iter_content(chunk_size=32768):
                    content_download += len(data)
                    content_percentage = int(content_download * 100 / content_length_int)
                    _tmp = "{}".format(content_download).rjust(content_length_len)
                    _tmp = "{} / {}".format(_tmp, content_length_int).ljust(64 - 5)
                    sys.stdout.write("{:>3}% {}\r".format(content_percentage, _tmp))
                    sys.stdout.flush()
                    f.write(data)
            # __________________________________________________________________
            if isinstance(perm, str) and perm.isdigit():
                os.chmod(trg, int(perm, 8))
    except Exception as err:
        print("[!!] Exception :: {}\n{}".format(err, "".join(traceback.format_exc())))
        _BUFFER['path'] = None
        fs_rm_file(trg)
        return False
    finally:
        _BUFFER['path'] = None
    # __________________________________________________________________________
    return True


# ======================================================================================================================
# Signal Handlers
# ======================================================================================================================
def signal_handler_sigint(signum, frame):
    print("\nKeyboardInterrupt\n")
    path = _BUFFER.get('path')
    if path:
        fs_rm_file(path)
    sys.exit(1)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if __name__ == '__main__':
    sys.exit(not main())  # Compatible return code
