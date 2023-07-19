import os
import re
import sys

from typing import Callable
from urllib.parse import unquote

exit_codes = {
	"success": 0,
	"generic_error": 1,
	"invalid_arguments": 2,
}

# Regex: relative markdown link [text](link)
reg_mdlink_rel = re.compile('\\[(.*?)]\\((?!\\w+:/)(?![.#?/])(.*?)\\)')
# Regex: absolute markdown link to a markdown file [text](/link.md)
reg_mdlink_mdfile = re.compile('\\[(.*?)]\\((?!\\w+:/)(?![.#?])(/.*?).md\\)', flags=re.IGNORECASE)
# Regex: absolute markdown link to a README.md file [text](/link/README.md)
reg_mdlink_readme = re.compile('\\[(.*?)]\\((?!\\w+:/)(?![.#?])(.*?)/README.md\\)', flags=re.IGNORECASE)

options = {
	# help: help message
	# args_check: function to check the arguments (optional)
	# action: function to run
}

args = {
	"command": "",
	"arguments": [],
}


def init_options() -> None:
	options["rel-abs"] = {
		"help": "Convert relative links to absolute decoded links",
		"args_check": check_argument_directory,
		"action": command_rel_abs,
	}

	options["md-dir"] = {
		"help": "Convert links that point to a markdown file to a directory with the same name",
		"args_check": check_argument_directory,
		"action": command_md_dir,
	}


def main() -> None:
	init_options()
	parse_args()

	# run the command
	options[args["command"]]["action"]()


def parse_args() -> None:
	# check if there is an argument
	if len(sys.argv) < 2:
		print("Usage: python fix_notes.py <command> <arguments>")
		sys.exit(exit_codes["invalid_arguments"])

	# parse the arguments
	args["command"] = sys.argv[1]
	command = args["command"]
	if len(sys.argv) > 2:
		args["arguments"] = sys.argv[2:]

	# check if the command is valid
	if command not in options:
		print(f"Unknown command '{command}'")
		sys.exit(exit_codes["invalid_arguments"])

	# check if the arguments are valid
	if args_check := options[command]["args_check"]:
		args_check()


def check_argument_directory() -> None:
	# check the number of arguments
	if len(args["arguments"]) < 1:

		print("Too few arguments")
		sys.exit(exit_codes["invalid_arguments"])

	elif len(args["arguments"]) > 1:

		print("Too many arguments")
		sys.exit(exit_codes["invalid_arguments"])

	directory = args["arguments"][0]

	# check if the argument is a directory
	if not os.path.isdir(directory):

		print("The argument must be a directory")
		sys.exit(exit_codes["invalid_arguments"])

	else:
		print(f"Using directory '{directory}'")


def command_md_dir() -> None:
	# get all md files
	files = get_md_files(args["arguments"][0])

	# convert links
	edited = sum(convert_mdfile_links(file) for file in files)

	print(f"Changed {edited} files")


def command_rel_abs() -> None:
	# get all md files
	files = get_md_files(args["arguments"][0])

	# convert links
	edited = sum(convert_relative_links(file) for file in files)

	print(f"Changed {edited} files")


def get_md_files(directory: str) -> list[str]:
	files = unroll_dir(directory, ignore_dir=lambda x: x.startswith("."))
	files = [path for path in files if path.endswith(".md")]

	return files


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


def convert_mdfile_links(file: str) -> bool:
	# open file in read/write mode
	with open(file, "r+") as f:
		# read the whole file
		content = f.read()
		og_len = len(content)

		# replace all links to a README.md file
		content = reg_mdlink_readme.sub(r"[\1](\2)", content)
		# replace all other links to a markdown file
		content = reg_mdlink_mdfile.sub(r"[\1](\2/)", content)

		# check if the file was changed
		if og_len != len(content):
			print(f"Converting mdlinks from mdfile to dir in '{file}'")

			# write the new content
			f.seek(0)
			f.write(content)
			f.truncate()

			# file changed
			return True
	# file not changed
	return False


def convert_relative_links(file: str) -> bool:
	# open file in read/write mode
	with open(file, "r+") as f:
		# read the whole file
		content = f.read()
		og_len = len(content)

		# replace all relative links and decode urls
		content = unquote(reg_mdlink_rel.sub(r"[\1](/\2)", content))

		# check if the file was changed
		if og_len != len(content):
			print(f"Converting mdlinks from relative to absolute in '{file}'")

			# write the new content
			f.seek(0)
			f.write(content)
			f.truncate()

			# file changed
			return True
	# file not changed
	return False


if __name__ == "__main__":
	# noinspection PyBroadException
	try:
		main()

	except Exception as e:
		print("An error occurred:", e)
		sys.exit(exit_codes["generic_error"])

	sys.exit(exit_codes["success"])
