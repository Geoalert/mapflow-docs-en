#!/bin/bash

# Build script for all language versions of Mapflow documentation
# This script extracts translatable messages, updates PO files, and builds all language versions

echo "================================================"
echo "Building Mapflow Documentation (All Languages)"
echo "================================================"
echo ""

# 1. Extract translatable strings to POT files (template files)
echo "Step 1: Extracting translatable messages..."
sphinx-build -b gettext source source/locale
if [ $? -eq 0 ]; then
    echo "✓ Message extraction complete"
else
    echo "✗ Message extraction failed"
    exit 1
fi
echo ""

# 2. Create/Update English PO files (base language)
echo "Step 2: Creating/Updating English PO files..."
sphinx-intl update -p source/locale -l en
if [ $? -eq 0 ]; then
    echo "✓ English PO files updated"
else
    echo "✗ English PO files update failed"
    exit 1
fi
echo ""

# 3. Update existing translation PO files
echo "Step 3: Updating Russian PO files..."
sphinx-intl update -p source/locale -l ru
if [ $? -eq 0 ]; then
    echo "✓ Russian PO files updated"
else
    echo "✗ Russian PO files update failed"
    exit 1
fi
echo ""

# Add more languages here as needed:
# echo "Updating Spanish PO files..."
# sphinx-intl update -p source/locale -l es
# echo "Updating German PO files..."
# sphinx-intl update -p source/locale -l de

# 4. Build HTML for each language
echo "Step 4: Building English documentation..."
sphinx-build -b html source build/docs/en
if [ $? -eq 0 ]; then
    echo "✓ English documentation built successfully"
else
    echo "✗ English documentation build failed"
    exit 1
fi
echo ""

echo "Step 5: Building Russian documentation..."
sphinx-build -b html -D language=ru source build/docs/ru
if [ $? -eq 0 ]; then
    echo "✓ Russian documentation built successfully"
else
    echo "✗ Russian documentation build failed"
    exit 1
fi
echo ""

# Add more languages here as needed:
# echo "Building Spanish documentation..."
# sphinx-build -b html -D language=es source build/docs/es
# echo "Building German documentation..."
# sphinx-build -b html -D language=de source build/docs/de

echo "================================================"
echo "✓ All documentation builds complete!"
echo "================================================"
echo ""
echo "Documentation locations:"
echo "  English: build/docs/en/index.html"
echo "  Russian: build/docs/ru/index.html"
echo ""
