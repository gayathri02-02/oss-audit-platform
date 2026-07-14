#!/bin/bash

echo "======================================"
echo "OSS Audit Platform Setup"
echo "======================================"

echo ""
echo "Creating required directories..."

mkdir -p storage/sboms
mkdir -p storage/cboms
mkdir -p storage/reports
mkdir -p storage/metadata

mkdir -p logs

echo ""
echo "Creating log files..."

touch logs/scheduler.log
touch logs/scanner.log
touch logs/ai.log
touch logs/dashboard.log

echo ""
echo "Setup completed successfully."
