#!/bin/sh
set -e

APP_PATH="application/application"
if [ "$MAKE_MIGRATIONS" = "true" ];
then
    ws-alembic -c $APP_PATH/conf/development.ini -x packages=all revision --auto
fi

ws-alembic -c $APP_PATH/conf/development.ini -x packages=all upgrade head
ws-sync-db ws://$APP_PATH/conf/development.ini

if [ "$CREATE_DEFAULT_USER" = "true" ];
then
    ws-create-user ws://$APP_PATH/conf/development.ini $APP_DEFAULT_USER APP_DEFAULT_PASSWORD
fi
exec "$@"