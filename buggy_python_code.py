# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import cPickle
import subprocess
import base64
import subprocess
import flask

# Input injection
def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def access_check(request, user):
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh(object):
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))


def version_check(version):
    x = version.split('.')
    if len(x) > 2 :
        return False
    if len(x) == 1:
        x = version.split(',')
    if len(x) > 2 :
        return False
    if !(isNumeric(x[0])):
        return False
    if !(isNumeric(x[1])):
        return False
    return True


def import_urlib_version(version):
    if version_check(version):
        exec("import urllib%s as urllib" % version)


@app.route('/')
def index():
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
