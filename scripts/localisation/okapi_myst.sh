#!/bin/bash

# ==============================================================================
# Okapi Tikal Automation Script for MyST Markdown (with Cleanup)
# ==============================================================================

usage() {
    echo "Usage: $0 [pre|post] [folder_path] [fprm_path] [optional: target_lang] [optional: cleanup]"
    echo "  pre:     Recursively extract .md files to .xlf"
    echo "  post:    Recursively merge .xlf files back to .md"
    echo "  cleanup: (Post-mode only) Enter 'cleanup' to delete .xlf files after success"
    echo "Example: $0 post ./content ./myst.fprm fr cleanup"
    exit 1
}

if [ "$#" -lt 3 ]; then
    usage
fi

MODE=$1
FOLDER=$2
CONFIG=$3
TARGET_LANG=${4:-"fr"}
CLEANUP_FLAG=$5
SOURCE_LANG="en"

if [ ! -d "$FOLDER" ] || [ ! -f "$CONFIG" ]; then
    echo "Error: Directory or Config file missing."
    exit 1
fi

if [ "$MODE" == "pre" ]; then
    echo "--- Starting Pre-Processing ---"
    echo "Source folder: $FOLDER"
    echo "Filter config: $CONFIG"
    echo "Source language: $SOURCE_LANG"
    echo "Target language: $TARGET_LANG"
    echo "Skipping translated folders: es, fr"

    find "$FOLDER" \
        -type f \
        -name "*.md" \
        ! -path "*/es/*" \
        ! -path "*/fr/*" \
        | while read -r file; do
            echo "Extracting: $file"
            tikal.sh -x "$file" -fc "$CONFIG" -sl "$SOURCE_LANG" -tl "$TARGET_LANG"

            if [ $? -ne 0 ]; then
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

    find "$FOLDER" \
        -type f \
        -name "*.xlf" \
        | while read -r xlf_file; do
            echo "Merging: $xlf_file"

            tikal.sh -m "$xlf_file" -fc "$CONFIG" -sl "$SOURCE_LANG" -tl "$TARGET_LANG"

            if [ $? -eq 0 ]; then
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
