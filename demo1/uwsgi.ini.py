


[uwsgi]
#socket=外网ip:端口（使用nginx连接时，使用socket）
http=0.0.0.0:15000
chdir=
wsgi-file=demo2/wsgi.py
processes=4
threads=2
master=True
pidfile=uwsgi.pid
daemonize=uwsgi.log
