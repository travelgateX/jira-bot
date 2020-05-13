# Contributing

There are 2 ways to contribute:

- **As core maintainer**: Fixing or developing new features on `app` folder
- **Plugin contributor**: Developing reactions to [Jira Events](#event-development) 

In both cases, the workflow to contribute is the same:

1. Open a [new issue][] to discuss the changes you would like to make.  This is
   not strictly required but it may help reduce the amount of rework you need
   to do later.
1. Make changes to `app` or contribute with new commands or events:
   - [Events](#event-development)
1. Ensure you have added proper tests and documentation.
1. Open a new [pull request][].

## Common development tasks

Application will find all contributions on `contrib` folder using [plugin discovery](https://packaging.python.org/guides/creating-and-discovering-plugins/)

### Event development

Manage [Jira Webhooks](https://developer.atlassian.com/server/jira/platform/webhooks/).

1. Ask to your JIRA Admin to subscribe the Webhook  do you plan to develop.
1. On `contrib/plugins/events` create a file named _webhook name_
1. Create a class named _Task_ inherit from class _Event_
1. Hack the _abstract methods_
