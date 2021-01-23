#!/bin/sh

a=python3
b=pip3


case "$(uname -s)" in
   Darwin)
     echo 'No support to MacOS!'
     exit 1
     ;;

   Linux)
     ;;

   CYGWIN*|MINGW32*|MSYS*|MINGW*)
     echo 'No support to Windows!'
     exit 1
     ;;
   *)
     echo 'No support to your OS!'
     exit 1
     ;;
esac

if ! python3 --version ; then
    echo "python3 is not installed"
fi

#pip install nexmo
#pip3 install nexmo