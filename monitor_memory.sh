#!/bin/bash
python3 main.py &
PID=$!
while ps -p $PID > /dev/null; do
  top -l 1 -o mem | head -n 10
  sleep 1
done
