#!/bin/bash

# ==============================================================================
# Okapi Tikal Automation Script for MyST Markdown
# ==============================================================================

set -euo pipefail

usage() {
    echo "Usage: $0 [pre|post] [folder_path] [fprm_path] [optional: target_lang] [optional: cleanup]"
    echo "  pre:     Recursively extract .md files to .xlf"
    echo "  post:    Recursively merge .xlf files back to .md"
    echo "  cleanup: (Post-mode only) Enter 'cleanup' to delete .xlf files after success"
    echo "Example: $0 post ./content ./okf_markdown@MyST.fprm fr cleanup"
    exit 1
}

if [ "$#" -lt 3 ]; then
    usage
fi

MODE=$1
FOLDER=$2
CONFIG=$3
TARGET_LANG=${4:-"fr"}
CLEANUP_FLAG=${5:-""}
SOURCE_LANG="en"
INPUT_ENCODING="UTF-8"
OUTPUT_ENCODING="UTF-8"

if [ ! -d "$FOLDER" ] || [ ! -f "$CONFIG" ]; then
    echo "Error: Directory or config file missing."
    echo "Folder: $FOLDER"
    echo "Config: $CONFIG"
    exit 1
fi

if [ "$MODE" == "pre" ]; then
    echo "--- Starting Pre-Processing ---"
    echo "Source folder: $FOLDER"
    echo "Filter config: $CONFIG"
    echo "Source language: $SOURCE_LANG"
    echo "Target language: $TARGET_LANG"
    echo "Input encoding: $INPUT_ENCODING"
    echo "Output encoding: $OUTPUT_ENCODING"
    echo "Skipping translated folders: es, fr"
    echo "Skipping translated filename prefixes: es_*.md, fr_*.md"

    find "$FOLDER" \
        -type f \
        -name "*.md" \
        ! -path "*/es/*" \
        ! -path "*/fr/*" \
        ! -name "es_*.md" \
        ! -name "fr_*.md" \
        -print0 \
        | while IFS= read -r -d '' file; do
            echo "Extracting: $file"

            if ! tikal.sh \
                -x "$file" \
                -fc "$CONFIG" \
                -sl "$SOURCE_LANG" \
                -tl "$TARGET_LANG" \
                -ie "$INPUT_ENCODING" \
                -oe "$OUTPUT_ENCODING"; then

                echo "Warning: Extraction failed for $file"
            fi
        done

    echo "Extraction complete."

elif [ "$MODE" == "post" ]; then
    echo "--- Starting Post-Processing ---"
    echo "Source folder: $FOLDER"
    echo "Filter config: $CONFIG"
    echo "Source language: $SOURCE_LANG"
    echo "Target language: $TARGET_LANG"
    echo "Input encoding: $INPUT_ENCODING"
    echo "Output encoding: $OUTPUT_ENCODING"

    find "$FOLDER" \
        -type f \
        -name "*.xlf" \
        -print0 \
        | while IFS= read -r -d '' xlf_file; do
            echo "Merging: $xlf_file"

            if tikal.sh \
                -m "$xlf_file" \
                -fc "$CONFIG" \
                -sl "$SOURCE_LANG" \
                -tl "$TARGET_LANG" \
                -ie "$INPUT_ENCODING" \
                -oe "$OUTPUT_ENCODING"; then

                if [ "$CLEANUP_FLAG" == "cleanup" ]; then
                    echo "Success. Removing intermediate file: $xlf_file"
                    rm "$xlf_file"
                fi
            else
                echo "Warning: Merge failed for $xlf_file. Keeping file for debugging."
            fi
        done

    echo "Merging complete."

else
    usage
fi