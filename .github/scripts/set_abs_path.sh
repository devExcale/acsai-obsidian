#!/bin/bash

# Thanks ChatGPT-3.5

# Check if script is being run at the root of the repository
if [ ! -d .git ]; then
  # Try to find the root of the repository
  repo_root=$(git rev-parse --show-toplevel 2>/dev/null)

  # If the root can't be found, print an error message and exit
  if [ -z "$repo_root" ]; then
    echo "Not a git repository"
    exit 1
  fi

  # Change directory to the root of the repository
  cd "$repo_root"
fi

# Parse command line options
commit=false

while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    -c|--commit)
      commit=true
      shift
      ;;
    *)
	  echo "Unknown option: $key"
      exit 1
      ;;
  esac
done

# find .md files that are tracked by git
FILES=$(git ls-files | grep -E '[^\.].*\.md$')

# regex to match relative markdown paths
REGEX='\\[(.*)\\]\\((?!\\w+:\\/)(?![.#?\\/])(.*?)\\)'

# loop through the files
IFS=$'\n'
for FILE in $FILES; do

	echo "Processing $FILE"

	# Replace all relative links with absolute paths
	awk -v regex="$REGEX" '{ if ($0 ~ regex) { gsub(regex, "[\\1](/\\2)", $0); printf("Fixed %s\n", FILE) } } 1' "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"

	# Mark file for commit
	git add "$file"
done

# Commit only if option is enabled
if [ "$commit" = true ]; then
	git commit -m "[Workflow] Updated absolute paths"
fi
