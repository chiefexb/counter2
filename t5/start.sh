#uwsgi  --ini counter.ini 
uwsgi --socket :8082 --module counter.wsgi --daemonize /home/shilo/counter.log --pidfile /tmp/counter.pid
