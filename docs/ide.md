# About

The guide provides information on how to install the selected TS ide [vscode](https://code.visualstudio.com/download).

# Project Settings

*TODO* The vscode IDE already supports Typescript. The project settings are specified at `.vscode/settings.json` and extend/overwrite the workspace settings at `settings.json`. Read more about the contents of `.vscode/settings.json` at [`layout`](layout.md). Some configuration comes in the template in `.vscode/settings.json`, but additional manual configurations must be performed. Add to your workspace `settings.json`:

```json
    // explicitly enable CodeLens on the editor
    "editor.codeLens": true,

    // inline count of reference for classes, interfaces, methods, properties, 
    // and exported objects
    "typescript.referencesCodeLens.enabled": true,

    // displays the number of implementors of an interface
    "typescript.implementationsCodeLens.enabled": true,

    "typescript.referencesCodeLens.showOnAllFunctions": true,
```

# Formatting

# Linting

The linting extension is installed by running `sudo init.sh`. The `eslint` linter requires the configuration file `.eslintrc` (which can be generated with `npm init @eslint/config`). The linter is now running automatically in the IDE. To call it explicitly:

`./node_modules/.bin/eslint <file>.ts`

# CodeLens

# Error checking

# Quick Fixes

# Debugging

The project debugging settings are specified at `.vscode/launch.json` Read more about the contents of the file at [`layout`](layout.md).

Place your breakpoints and select a debugging case from the file.

# Resources

[doc](https://code.visualstudio.com/docs/typescript/typescript-tutorial)
