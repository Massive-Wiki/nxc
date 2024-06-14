#!/usr/bin/env python3

import argparse
import glob
import logging
import os
from pathlib import Path
import shutil
import yaml

# load config file                                                                                                          
def load_config(path):
    with open(path) as infile:
        return yaml.safe_load(infile)

def init_site(directory):
    # Check and handle the specified directory
    init_dir = Path(directory)
    if init_dir.exists():
        # if any(init_dir.iterdir()):
         if any(glob.iglob(f"{init_dir}/**/.massivewikibuilder/nxc.yaml",recursive=True)):
             logging.error(f"The directory {init_dir} has been initialized.")
             return
    else:
        # create and initialize directory
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
        logging.debug(f"template file copy successful in {init_dir}")
    except Exception as e:
        logging.error(f"Failed to initialize project: {e}")
    
    # initialize configuration file
    logging.info(f"get and write config info into {init_dir}/.massivewikibuilder/nxc.yaml")
    # get configuration input
    website_title = input("Enter the website title: ")
    author_name = input("Enter the author name(s): ")
    git_repo = input("Enter Git forge/repository name: ")

    # read in mwb.yaml template
    with open(templates_dir / 'mwb.yaml','r',encoding='utf-8') as f:
        config_doc = yaml.safe_load(f)
        config_doc['wiki_title'] = website_title
        config_doc['author'] = author_name
        config_doc['edit_url'] = f"https://{git_repo}/"
        config_doc['repo'] = f'<a href="https://"{git_repo}">{git_repo.split("/")[-1]}</a>'

    # write out configuration information
    output_file = f'{init_dir}/.massivewikibuilder/nxc.yaml'
    with open(output_file, 'w', encoding='utf-8') as file:
        yaml.safe_dump(config_doc, file, default_flow_style=False, sort_keys=False)

    return

def build_site(args):
    site_dir = args.input
    output_dir = args.output
    logging.info('build this website from %s to %s', site_dir, output_dir)
    logging.info(f"config file: {site_dir}{args.config}")
    logging.info(f"templates: {site_dir}{args.templates}")
    return

def main():
    # setup logger
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # setup argument parsers
    parser = argparse.ArgumentParser(description='Initialize or build website for a collection of Markdown files.')
    subparsers = parser.add_subparsers(required=True)
    # subparser for "init" command
    parser_init = subparsers.add_parser('init')
    parser_init.add_argument('directory', nargs=1)
    parser_init.set_defaults(cmd='init')
    # subparser for "build" command
    parser_build = subparsers.add_parser('build')
    parser_build.add_argument('-i', '--input', required=True, help='input directory of Markdown files')
    parser_build.add_argument('-o', '--output', required=True, help='output website directory')
    parser_build.add_argument('--config', '-c', default='/.massivewikibuilder/nxc.yaml', help='path to YAML config file')
    parser_build.add_argument('--templates', '-t', default='/.massivewikibuilder/this-wiki-themes/dolce', help='directory for HTML templates')
    parser_build.add_argument('--lunr', action='store_true', help='include this to create lunr index (requires npm and lunr to be installed, read docs)')
    parser_build.add_argument('--commits', action='store_true', help='include this to read Git commit messages and times, for All Pages')
    parser_build.set_defaults(cmd='build')
    
    args = parser.parse_known_args()
    logging.info(args)


    match args[0].cmd:
        case 'init':
            logging.info('Initializing in directory: %s', {args[0].directory[0]})
            init_site(args[0].directory[0])
        case 'build':
            print(f'Building from input directory: {args.input} to output: {args.output}')
            #            build_site(args)
        case _:
            return

if __name__ == '__main__':
    exit(main())
