#!/bin/bash

echo "======================================"
echo "OSS Audit Platform Backup"
echo "======================================"

BACKUP_DIR="backup/$(date +%Y%m%d_%H%M%S)"

echo ""
echo "Creating backup directory..."

mkdir -p "$BACKUP_DIR"

echo ""
echo "Backing up storage..."

cp -r storage "$BACKUP_DIR/"

echo ""
echo "Backing up logs..."

cp -r logs "$BACKUP_DIR/"

echo ""
echo "Backing up configuration..."

cp -r config "$BACKUP_DIR/"

echo ""
echo "Backup completed successfully."

echo "Backup Location: $BACKUP_DIR"
