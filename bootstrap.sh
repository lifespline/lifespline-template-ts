#!/bin/bash

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

# task runner
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
