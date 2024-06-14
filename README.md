# nxc.py Script

## Overview

The `nxc.py` script is a command-line utility that initializes an `nxc` project directory with required configuration and web template files to support web publishing. This utility copies a predefined set of templates into a specified directory.

## Features

- **Directory Initialization**: Creates a new directory or utilizes an existing one (if empty, or if not yet initialized) to set up the starter files.  
- **Error Handling**: Provides logging and error handling to manage issues like non-empty directories or permission errors.  
- **Template Copying**: Copies specific template files and directories from a `templates` adjacent to the script.  

## Requirements

- Python 3.8  
- Access to file system operations that might need administrative, or appropriate user, permissions depending on the setup.  

## Usage

```shell
./nxc.py init directory_name
```
