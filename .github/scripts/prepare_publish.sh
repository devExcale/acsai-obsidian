#!/bin/sh

# Process the links in markdown files to make them work with mkdocs
echo Processing links...
python .github/scripts/fix_notes.py md-dir ${GITHUB_WORKSPACE}

echo Creating directory \'docs\'...
mkdir docs


# Move all files (except dotfiles) into /docs
echo Moving all files into \'docs\'...

for file in *
do
   if [[ $file != "docs" && $file != .* ]]; then
      mv "$file" docs/
   fi
done


# Move mkdocs.yml into root

echo Moving mkdocs.yml to root...
mv .github/mkdocs/mkdocs.yml .


# Print current structure
tree


# Install mkdocs and dependencies

echo Installing python requirements...
pip install -r .github/mkdocs/requirements.txt