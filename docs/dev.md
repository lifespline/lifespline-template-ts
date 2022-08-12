# About #

The guide shows how to extend the template.

# Getting started #

Install the system and application dependencies to `node_modules` with `sudo bash init.sh`. The template uses npm scripts as the task-runner ([`doc`](task_runner.md)). The scripts automate work flows like:

- format
- lint `npm run lint`
- test `npm run test`
- copy the refreshed AWS profile SSO credentials `npm run cpsso -- --profile <profile>`
- synthesize the cdk app `npm run synth -- --profile <profile>`
- deploy the cdk app `npm run deploy -- --profile <profile>`
