#!/bin/bash

echo "======================================"
echo "Cleaning OSS Audit Platform"
echo "======================================"

echo ""
echo "Removing generated SBOMs..."

rm -rf storage/sboms/*

echo ""
echo "Removing generated CBOMs..."

rm -rf storage/cboms/*

echo ""
echo "Removing generated Reports..."

rm -rf storage/reports/*

echo ""
echo "Cleaning Metadata..."

rm -rf storage/metadata/*

echo ""
echo "Cleaning Logs..."

> logs/scheduler.log
> logs/scanner.log
> logs/ai.log
> logs/dashboard.log

echo ""
echo "Cleanup completed successfully."
