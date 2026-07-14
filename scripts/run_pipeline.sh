#!/bin/bash

echo "======================================"
echo "Running OSS Audit Platform Pipeline"
echo "======================================"

echo ""
echo "Starting pipeline..."

python automation/orchestrator/orchestrator.py

PIPELINE_STATUS=$?

echo ""

if [ $PIPELINE_STATUS -eq 0 ]; then

    echo "======================================"
    echo "Pipeline completed successfully."
    echo "======================================"

else

    echo "======================================"
    echo "Pipeline failed."
    echo "======================================"

    exit 1

fi
