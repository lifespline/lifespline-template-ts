#!/bin/bash

##  About
#
# The script bootstraps your TS project.
#
## Getting started
#
# - Change these values to you project's corresponding values:
#     - `package.json::name`
#     - `package.json::author`
#     - `package.json::version`
#
# - Run `sudo bash init.sh` to install the default system and application 
# dependencies of your TS project template.
#
## Script
#
# 1 - install system dependencies
# node is required to run JS files compiled from TS files
# and to install npm
sudo apt install nodejs
    
# required to install TS
sudo apt install npm

# remove "no longer required" packages
yes | sudo apt autoremove

# 2 - install app dependencies
#
# read `doc/layout.md::package.json` to learn about the dev and prod project 
# requirements
npm i

# 3 - install vscode extensions
extensions=(

    # ts linter
    "dbaeumer.vscode-eslint"

    # unit test
    "kavod-io.vscode-jest-test-adapter"
    "hbenl.vscode-test-explorer"

    # copilot (requires account)
    "GitHub.copilot"

    # code format (TODO rm one of the below)
    "esbenp.prettier-vscode"
    "SimonSiefke.prettier-vscode"

    # md (TODO rm one of the below)
    "vscode.markdown-language-features"
    "yzhang.markdown-all-in-one"
    "DavidAnson.vscode-markdownlint"
    "vscode.markdown-math"

    # spell checker
    "streetsidesoftware.code-spell-checker"

    # json
    "vscode.json-language-features"
    
    # csv
    "mechatroner.rainbow-csv"

    # shell check
    "timonwong.shellcheck"

    # ts and js
    "vscode.typescript-language-features"

    # npm
    "vscode.npm"

    # docker
    "ms-vscode-remote.remote-containers"
)

for extension in "${extensions[@]}"; do
    code --install-extension "$extension" --force
done

# 4 - reset docs
echo > CHANGELOG.md
echo > README.md

# 5 - clean
rm init.sh
