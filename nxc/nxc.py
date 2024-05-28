#!/usr/bin/env python3

import argparse
import os
import shutil
import logging
from pathlib import Path

def init_site(directory):
    # Check and handle the specified directory
    init_dir = Path(directory)
    if init_dir.exists():
        if any(init_dir.iterdir()):
            logging.error(f"The directory {init_dir} is not empty.")
            return
    else:
        logging.info(f"Creating directory {init_dir}")
        os.makedirs(init_dir)
        
    # Define the source template directory
    script_dir = Path(__file__).parent
    templates_dir = script_dir / "templates"
    
    # Copy files from templates
    try:
        # Copy netlify.toml to the root of the new directory
        shutil.copy(templates_dir / "netlify.toml", init_dir / "netlify.toml")
        # Copy this-website-themes directory
        shutil.copytree(templates_dir / "this-website-themes", init_dir / ".massivewikibuilder" / "this-website-themes")
        logging.info(f"Project initialization successful in {init_dir}")
    except Exception as e:
        logging.error(f"Failed to initialize project: {e}")
    return

def main():
    # Setup logger
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Initialize project directory with starter files.')
    parser.add_argument('command', choices=['init', 'build'], help='Command to execute')
    parser.add_argument('-d','--directory', metavar='DIR', type=str, help='Directory to process')

    args = parser.parse_args()
    logging.info(args)

    # Validate and process arguments
    match args.command:
        case 'init':
            if not args.directory:
                parser.error("Please specify the directory to initialize with --directory")
                return
            print(f'Initializing in directory: {args.directory}')
            init_site(args.directory)
        case 'build':
            print(f'Building from directory: {args.directory} to output: {args.output}')
            return
        case _:
            return

if __name__ == '__main__':
    exit(main())
