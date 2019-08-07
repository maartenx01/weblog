web: 
export FLASK_DEBUG=0; 
export MAIL_SERVER=smtp.googlemail.com;
export MAIL_PORT=587;
export MAIL_USE_TLS=1;
export MAIL_ADMIN=snailmaildaemon@gmail.com;
export MAIL_USERNAME=snailmaildaemon
export MAIL_PASSWORD=Shoreland#19#
flask db upgrade; 
gunicorn weblog:app;
