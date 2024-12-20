# nxc PyPI package

## Overview

The `nxc` PyPI package proveds a command-line utility that:  
1. initializes an `nxc` project directory with required configuration and web template files to support web publishing. This utility copies a predefined set of templates into a specified directory.
2. builds a static website from Markdown files in an initialized directory.

## Features

- **Directory Initialization**: Creates a new directory or utilizes an existing one (if empty, or if not yet initialized) to set up the starter files.  
- **Website Building**: Constructs a static website from a collection of Markdown files.    
- **Error Handling**: Provides logging and error handling to manage issues like non-empty directories or permission errors.    
- **Template Copying**: Copies specific template files and directories from a `templates` adjacent to the script.  

## Requirements

- Python 3.8  
- Access to file system operations that might need administrative, or appropriate user, permissions depending on the setup.  

## Usage
- This package is still being tested and is housed on `test.pyi.org`;
it can be installed using `pip`:  

``` shell
pip install --extra-index-url https://test.pypi.org/simple/ nxc
```  

- Once installed usage information is available using `--help` or `-h`
  options; e.g.:  

``` shell
nxc --help|-h
```

- Further documentation is under development.  



