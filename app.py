from os import environ
from subprocess import call

# from nkm.helpers.database import init_databases
# from ymp3.schedulers import trending


if __name__ == '__main__':
    # http://docs.gunicorn.org/en/stable/settings.html
    cmd = 'gunicorn nkm:app -w 4 --worker-class eventlet --reload --log-level info'
    cmd += ' -b %s:%s' % (
        environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
        environ.get('OPENSHIFT_PYTHON_PORT', '5000')
    )
    cmd += ' --worker-connections 1000 -t 100'  # 4 mins = 10 secs
    call(cmd.split())
