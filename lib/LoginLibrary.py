import os.path
import subprocess
import sys

import requests

URL = "http://localhost:8080"

class LoginLibrary(object):

    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__),
                                      '..', 'sut', 'login.py')
        self._status = ''

    def register(self, email=None, password=None, password_repeat=None, nick_name=None):
        data = {}
        if email is not None:
            data["email"] = email
        elif password is not None:
            data["password"] = password
        elif password_repeat is not None:
            data["password_repeat"] = password_repeat
        elif nick_name is not None:
            data["nick_name"] = nick_name

        url = "%s/register" % URI
        resp = requests.post(url, json=data)
        if resp.status_code == 200:



    def create_user(self, username, password):
        self._run_command('create', username, password)

    def change_password(self, username, old_pwd, new_pwd):
        self._run_command('change-password', username, old_pwd, new_pwd)

    def attempt_to_login_with_credentials(self, username, password):
        self._run_command('login', username, password)

    def status_should_be(self, expected_status):
        if expected_status != self._status:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(args)
        print command
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        self._status = process.communicate()[0].strip()
