# nxc.py Script

## Overview

The `nxc.py` script is a command-line utility that initializes a project directory with a set of starter files for web development. This utility copies a predefined set of templates into a specified directory.

## Features

- **Directory Initialization**: Creates a new directory or utilizes an existing one (if empty) to set up the starter files.
- **Error Handling**: Provides logging and error handling to manage issues like non-empty directories or permission errors.
- **Template Copying**: Copies specific template files and directories from a `templates` adjacent to the script.

## Requirements

- Python 3.x
- Access to file system operations that might need administrative, or appropriate user, permissions depending on the setup.

## Usage

```shell
./nxc.py --init [path_to_directory]
```
