# About

The guide specifies how to configure and test your AWS SDK TS, AWS CDK TS and your TS source files.

# Getting started

## TS Source Files

`lib/Utils.ts` contains a function `sumAges` that sums the ages of Turing `lib/Turing.ts` and Hardy `lib/Hardy.ts`. `test/test.utils.ts` contains a test that verifies that the function does sum the two ages correctly. `package.json::jest.testMatch` specifies the path of the unit tests. Run the unit test with:

```sh
$ npm run test 

> test
> jest --verbose

 PASS  test/test.utils.ts (5.099 s)
  utils
    sumAges
      ✓ Sums the ages of turing and hardy (2 ms)

 PASS  test/test.app.sdk.ts (5.408 s)
  sdk
    request
      ✓ Verify that the account ID of the default AWS profile is correct (143 ms)

Test Suites: 2 passed, 2 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        5.77 s, estimated 6 s
Ran all test suites.
```

## AWS SDK TS Source Files

TODO

## AWS CDK TS Source Files

TODO

# Installation requirements #

Below, the dependencies installed with `npm install` that enable the unit testing:

The bootstrap uses [Jest](https://jestjs.io/) as a testing framework. Jest is designed for JavaScript, so a transpiler is needed to allow Jest to parse TypeScript files. [Babel](https://babeljs.io/) transpiles TypeScript to JavaScript. Notice Babel does not offer typechecking of tests.

If testing performance becomes critical, transpiling could be handled by either [esbuild](https://esbuild.github.io/) (Go) or [swc](https://swc.rs/) (Rust). Mind these technologies also don't test for type errors, but should are easy to replace Babel in the workflow.

### NPM Modules ###

Testing with Jest and Babel requires the following [npm](https://www.npmjs.com/) modules (specified in `package.json`):

* [**jest**](https://www.npmjs.com/package/jest) testing framework
* [**ts-jest**](https://www.npmjs.com/package/ts-jest) helper to run tests written in ts without having to build them first. `ts-jest` compiles first and executes later.
* [**@types/jest**](https://www.npmjs.com/package/@types/jest) jest types
* [**babel-jest**](https://www.npmjs.com/package/babel-jest) Jest plugin that allows the use of Babel for transformations.
* [**@babel/core**](https://www.npmjs.com/package/@babel/core) Compiler core for Babel.
* [**@babel/preset-env**](https://www.npmjs.com/package/@babel/preset-env) Preset that can be used to automatically determine plugins and polyfills for a target runtime environment.
* [**@babel/preset-typescript**](https://www.npmjs.com/package/@babel/preset-typescript) This preset is recommended when using TypeScript.


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



# Resources #

+ [cdk rules pack](https://github.com/cdklabs/cdk-nag)
+ [local stack deployme](https://localstack.cloud/)