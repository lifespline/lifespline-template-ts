# About

The guide shows how to configure an azure cicd pipeline.

# Getting Started

Azure pipelines are defined in `azure-pipelines.yml`. 

# Triggering A Pipeline Run

Unless at least one branch is explicit, the pipeline runs with each branch push
or each PR merge.

To trigger a pipeline on a PR, it is necessary to define first the branching policy for that branch. The pipeline should run with every new push to the branch originating the PR. The PR can only be approved if the pipeline is passing.

+ main
+ test
+ dev
+ feature/*
    + minimum number of reviwers: 1
    + check for linked work items: true
    + comment resolution: true
    + build validation:
      + trigger: automatic
      + policy requirement: required
      + build expiration: never

# Resources

+ [triggers](https://docs.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops)
+ [branch policies](https://docs.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops&tabs=browser)