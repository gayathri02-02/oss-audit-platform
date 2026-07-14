#!/bin/bash

echo "======================================"
echo "Stopping OSS Audit Platform"
echo "======================================"

echo ""
echo "Stopping Dashboard Backend..."

pkill -f "python app.py"

echo ""
echo "OSS Audit Platform stopped successfully."
