#!/usr/bin/env python3

import argparse
import os
import shutil
import logging
from pathlib import Path

def main():
    # Setup logger
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Initialize project directory with starter files.')
    parser.add_argument('--init', metavar='DIR', type=str, help='The directory to initialize')
    args = parser.parse_args()
    
    # Check if --init was used
    if args.init is None:
        print("Please specify the directory to initialize with --init")
        return
    
    # Check and handle the specified directory
    init_dir = Path(args.init)
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
    logging.info(f"__file__: {__file__}")
    logging.info(f"script_dir: {script_dir}")
    
    # Copy files from templates
    try:
        # Copy netlify.toml to the root of the new directory
        shutil.copy(templates_dir / "netlify.toml", init_dir / "netlify.toml")
        # Copy this-website-themes directory
        shutil.copytree(templates_dir / "this-website-themes", init_dir / ".massivewikibuilder" / "this-website-themes")
        logging.info(f"Project initialization successful in {init_dir}")
    except Exception as e:
        logging.error(f"Failed to initialize project: {e}")

if __name__ == '__main__':
    main()
