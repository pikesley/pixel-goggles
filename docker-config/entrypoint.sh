#!/bin/bash

function __show_help() {
    echo "Container entrypoint commands:"
    echo "  help - show this help"
    echo "  test - run the tests"
    echo ""
    echo "Any other command will be executed within the container."
}

case ${1} in
  help )
    __show_help
    ;;

  test )
    cd /opt/pixel-goggles/goggles
    make
    ;;

  * )
    exec "$@"
    ;;
esac
