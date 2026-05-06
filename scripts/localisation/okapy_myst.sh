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
    find "$FOLDER" -type f -name "*.md" | while read -r file; do
        tikal.sh -x "$file" -fc "$CONFIG" -sl "$SOURCE_LANG" -tl "$TARGET_LANG"
    done
    echo "Extraction complete."

elif [ "$MODE" == "post" ]; then
    echo "--- Starting Post-Processing ---"
    find "$FOLDER" -type f -name "*.xlf" | while read -r xlf_file; do
        echo "Merging: $xlf_file"
        
        # Perform the merge
        tikal.sh -m "$xlf_file" -fc "$CONFIG" -sl "$SOURCE_LANG" -tl "$TARGET_LANG"
        
        # Check if Tikal succeeded before deleting
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
