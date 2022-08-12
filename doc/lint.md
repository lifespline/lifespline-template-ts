# About

This document explains the testing and linting frameworks included in the framework, and specifies how to setup your environment, lint and test a [typescript](https://www.typescriptlang.org/) project with the `lifespline-ts-template` bootstrap on [vscode](https://code.visualstudio.com/).

# Test #

## Requirements ##

The bootstrap uses [Jest](https://jestjs.io/) as a testing framework. Jest is designed for JavaScript, so a transpiler is needed to allow Jest to parse TypeScript files. [Babel](https://babeljs.io/) transpiles TypeScript to JavaScript. Notice Babel does not offer typechecking of tests.

If testing performance becomes critical, transpiling could be handled by either [esbuild](https://esbuild.github.io/) (Go) or [swc](https://swc.rs/) (Rust). Mind these technologies also don't test for type errors, but should are easy to replace Babel in the workflow.

### NPM Modules ###

Testing with Jest and Babel requires the following [npm](https://www.npmjs.com/) modules (specified in `package.json`):

* [**jest**](https://www.npmjs.com/package/jest)
  * The JavaScript testing framework
  * Install with `npm i jest`
* [**babel-jest**](https://www.npmjs.com/package/babel-jest) Jest plugin that allows the use of Babel for transformations.
  * Install with `npm i babel-jest`
* [**@babel/core**](https://www.npmjs.com/package/@babel/core) Compiler core for Babel.
  * Install with `npm i @babel/core`
* [**@babel/preset-env**](https://www.npmjs.com/package/@babel/preset-env) Preset that can be used to automatically determine plugins and polyfills for a target runtime environment.
  * Install with `npm i @babel/preset-env`
* [**@babel/preset-typescript**](https://www.npmjs.com/package/@babel/preset-typescript) This preset is recommended when using TypeScript.
  * Install with `npm i @babel/preset-typescript`


### Configuration files ###

* `tsconfig.json` Jest required file
* `babel.config.js` Babel config settings
* `jest.config.js` Jest config settings. Config settings that do not use default values are listed first in the file. All other options are then listed in alphabetical order for easy project customization.

## Testing ##

Type check before testing (Babel doesn't type check) by adding a shortcut to `package.json` and running:

```bash
npm run check-types
```

Test by running:

```bash
npm run test
```

## VSCode Setup ##

Install:
* [Jest Test Explorer](https://marketplace.visualstudio.com/items?itemName=kavod-io.vscode-jest-test-adapter)
* [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer).
* [Test Result Preview](https://marketplace.visualstudio.com/items?itemName=tht13.html-preview-vscode) Coverage reports in html files.

# Lint #

## Requirements ##

The bootstrap uses [ESLint](https://www.npmjs.com/package/eslint) as the linting tool. Bcause ESLint is designed for javascript, extending it to TypeScript requires additional setup.

### NPM Modules ###

Linting with ESLint requires the following [npm](https://www.npmjs.com/) modules (specified in `package.json`):

* [**eslint**](https://eslint.org/docs/user-guide/getting-started) The base ESLint NPM Package, suitable for JavaScript. Install with:
  ```shell
  npm install eslint --save-dev
  npm init @eslint/config
  ```
* [**@typescript-eslint/parser**](https://www.npmjs.com/package/@typescript-eslint/parser) Parser extension to ESLint extending it to TypeScript.

Linting with ESLint also requires additional styling modules (with high community support), added onto the base requirements:

* [**@typescript-eslint/eslint-plugin**](https://www.npmjs.com/package/@typescript-eslint/eslint-plugin)
  * Base ESLint linting rules published by the TypeScript extension team.
  * ***Note*** - The plugin must have the same version number as the Parser (installed as peer dependency for this very same reason)
  * Install with `npm i @typescript-eslint/eslint-plugin`
* [**airbnb-base, airbnb-typescript/base**](https://www.npmjs.com/package/eslint-config-airbnb-typescript)
  * Airbnb ruleset is a highly adopted set of styling rules that follows best practices for code styling.
  * ***Note*** - Peer dependecy with **eslint-plugin-import**
  * Install with `npm i eslint-config-airbnb-typescript`
* [**eslint-plugin-promise**](https://www.npmjs.com/package/eslint-plugin-promise)
  * Rules for handling Promises
  * Install with `npm i eslint-plugin-promise`
* [**eslint-plugin-jest**](https://www.npmjs.com/package/eslint-plugin-jest)
  * Rules for how to test writing
  * Install with `npm i eslint-plugin-jest`
* [**eslint-plugin-jest-formatting**](https://www.npmjs.com/package/eslint-plugin-jest-formatting)
  * Formatting padding rules regarding test blocks
  * Install with `npm i eslint-plugin-jest-formatting`

Content of `package.json`:

``` json
"devDependencies": {
    "eslint": "^8.6.0",
    "@typescript-eslint/eslint-plugin": "5.24.0",
    "@typescript-eslint/parser": "5.24.0",
    "eslint-config-airbnb-base": "^15.0.0",
    "eslint-config-airbnb-typescript": "^17.0.0",
    "eslint-plugin-jest": "^26.2.2",
    "eslint-plugin-import": "^2.26.0",
    "eslint-plugin-jest-formatting": "^3.1.0",
    "eslint-plugin-promise": "^6.0.0",
}
```

### Configuration files ###

* `.eslintrc.js`
  * ***Parser***
    * Defines which parser ESLint uses, this gets set to '@typescript-eslint/parser'
  * ***Plugins***
    * Informs ESLint to load any plugin in the array.
    * Allows loading of plugins, to use additional rules on top of those provided by ESLint, e.g. '@typescript-eslint'
  * ***Extends***
    * Informs ESLint to extend rulesets given in the array - these rulesets may come from plugins
    * E.g. 'eslint:recommended' extends the basic rules that comes with ESLint
    * E.g. 'plugin:@typescript-eslint/recommended' extends a set of rules from the Plugin "@typescript-eslint"

With the modules listed above the eslintrc config ends up as below

``` js
module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  plugins: [
    '@typescript-eslint',
    'jest',
    'jest-formatting',
    'promise',
  ],
  extends: [
    'airbnb-base',
    'airbnb-typescript/base',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:jest/recommended',
    'plugin:jest-formatting/recommended',
    'plugin:promise/recommended',
  ],
};
```

* `.eslintignore` Defines which files we do not want to lint,*e.g.*, build output (`dist/`)

## Linting ##

The easiest way to run ESLint is to define run scripts in the package.json file as shortcuts. E.g. the following code block allows for the simple command npm run lint, to lint everything in the current directory.

``` json
{
  "scripts": {
    "lint": "eslint . --ext .js,.jsx,.ts,.tsx"
  }
}
```

## VSCode Setup ##

Configure VSCode by installing the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint). So that VSCode runs ESLint on typescript files, add to `settings.json`:

``` json
"eslint.validate": ["typescript", "typescriptreact"],
```

VSCode can also be configured to automatically fix linting errors (those simple enough to auto fix). This is done by linting with the `--fix` argument, but can be set to automatically run in your IDE by adding to `settings.json`:

``` json
"editor.codeActionsOnSave": {
        "source.fixAll.eslint": true
},
```

# Resources #

## Testing

+ [Speeding up jest](https://miyauchi.dev/posts/speeding-up-jest/)