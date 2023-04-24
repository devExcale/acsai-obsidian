import os
import re
import sys

from typing import Callable

# compile the regex
pattern = re.compile('\\[(.*?)]\\((?!\\w+:/)(?![.#?/])(.*?)\\)')


def main():
	check_parameters()

	# get all md files
	files = unroll_dir(sys.argv[1], ignore_dir=lambda x: x.startswith("."))
	files = [path for path in files if path.endswith(".md")]

	# fix links
	for file in files:
		fix_relative_links(file)


def check_parameters():
	# check if there is an argument
	if len(sys.argv) < 2:
		print("Usage: python fix_mdlinks.py <path>")
		sys.exit(1)

	# check if the argument is a directory
	if not os.path.isdir(sys.argv[1]):
		print("The argument must be a directory")
		sys.exit(1)
	else:
		print(f"Using directory '{sys.argv[1]}'")


def unroll_dir(path: str, ignore_dir: Callable[[str], bool] = None) -> list[str]:
	# get all files in the first argument directory
	children = os.listdir(path)
	children = [os.path.join(path, child) for child in children]
	filepaths = [os.path.join(path, child) for child in children if os.path.isfile(child)]

	if not ignore_dir:
		ignore_dir = lambda x: True

	# get all files in subdirectories
	for child in children:
		if os.path.isdir(child) and not ignore_dir(child):
			filepaths.extend(unroll_dir(child, ignore_dir=ignore_dir))

	return filepaths


def fix_relative_links(file: str):
	# open file in read/write mode
	with open(file, "r+") as f:
		# read the whole file
		content = f.read()
		og_len = len(content)

		# replace all relative links
		content = pattern.sub(r"[\1](/\2)", content)

		# check if the file was changed
		if og_len != len(content):
			print(f"Fixing links in '{file}'")

			# write the new content
			f.seek(0)
			f.write(content)
			f.truncate()


if __name__ == "__main__":
	main()
