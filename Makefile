clean:
	rm -rf __pycache__

weblog:
	export FLASK_APP=weblog.py

debug:
	export FLASK_DEBUG=1

nodebug:
	export FLASK_DEBUG=0

local:
	export MAIL_SERVER=localhost
	export MAIL_PORT=8025

server:
	export MAIL_SERVER=smtp.google.com
	export MAIL_PORT=587
	export MAIL_USE_TLS=1

