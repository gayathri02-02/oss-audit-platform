#!/bin/bash

echo "======================================"
echo "Starting OSS Audit Platform"
echo "======================================"

echo ""
echo "Starting Dashboard Backend..."

cd dashboard/backend

python app.py &

BACKEND_PID=$!

cd ../..

echo ""
echo "Backend started successfully."

echo ""
echo "OSS Audit Platform is now running."

echo ""
echo "Backend PID: $BACKEND_PID"
