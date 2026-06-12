#!/bin/sh
export PYTHONHOME=/usr
export PYTHONPATH=$APPDIR/usr/src:$PYTHONPATH
exec /usr/bin/python3 "$APPDIR/usr/src/main.py" "$@"
