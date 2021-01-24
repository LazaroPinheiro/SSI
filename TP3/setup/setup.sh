#!/bin/sh

case "$(uname -s)" in
   Darwin)
     echo 'No support to MacOS!'
     exit 1
     ;;

   Linux)
     echo 'Linux does supports this app.\\nBeginning setup!'
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


if which pip3 > /dev/null 2>&1;
then
    echo Installing Nexmo
    pip3 install nexmo
else
    echo Installing Nexmo
    pip install nexmo
fi