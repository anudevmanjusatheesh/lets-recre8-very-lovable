#!/bin/bash

# Define the directory where server.js is located
SERVER_DIR="../external_sandbox/"
SERVER_PORT=8050

# Check if the port is in use and get the process ID
PID=$(lsof -t -i:$SERVER_PORT)

if [ -n "$PID" ]; then
  echo "Port $SERVER_PORT is in use by PID $PID. Killing the process..."
  kill -9 $PID
  echo "Process killed."
else
  echo "No process running on port $SERVER_PORT."
fi

# Navigate to the server directory
cd "$SERVER_DIR" || exit

# Start the Node.js server
echo "Starting server.js..."
nohup node server.js > server.log 2>&1 &

echo "Server started successfully on port $SERVER_PORT."
