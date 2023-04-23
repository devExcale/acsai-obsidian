#!/bin/sh

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