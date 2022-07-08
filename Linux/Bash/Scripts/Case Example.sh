#!/bin/bash
if [ "$1" = "foo" ]; then
case "$2" in

bar)  echo "fooing bar $2"
    foo_bar
    ;;

*) echo "Command Not recognized"
;;
esac

fi