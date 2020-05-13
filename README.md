<p>
<a href="https://travis-ci.org/travelgateX/jira-bot" target="_blank">
    <img src="https://travis-ci.org/travelgateX/jira-botx.svg?branch=master" alt="Build Status">
</a>
<a href="https://codecov.io/gh/travelgateX/jira-bot" target="_blank">
    <img src="https://codecov.io/gh/travelgateX/jira-bot/branch/master/graph/badge.svg" alt="Coverage">
</a>
</p>

[TravelgateX Jira](https://xmltravelgate.atlassian.net/) bot written in Python:

* Based on [Jira Webhooks](https://developer.atlassian.com/server/jira/platform/webhooks/)
* Powered by [FastAPI web framework](https://fastapi.tiangolo.com)
* Using standard [Python 3.8+ type hints](https://docs.python.org/3/library/typing.html)
* Easy to contribute using standard [Plugins Ecosystem](https://packaging.python.org/guides/creating-and-discovering-plugins/)
* Easy background execution with [Starlette Background Tasks](https://www.starlette.io/background)
* Complex background execution with [Apache Airflow](https://airflow.apache.org/)
* Command help with [Python commandline argparse](https://docs.python.org/3/library/argparse.html)

## Features

* Respond to Slack Events API:
  * [x] Modify issue

## Requirements

Requires Python 3.8+

```bash
pip install -r requirements.txt
```

## Development

### Environment

Modify app/config.ini and/or set environment variables:

* Linux

```bash
export API_KEY="your-api-key-secret"
```

* Windows

```bash
set API_KEY=xoxb-your-api-key-secret
```

## Run

### Local

Run the server with:

```bash
uvicorn app.main:app --reload
```

### Docker

Build the image and run the container

```bash
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage
```

## Tests

```bash
pytest
```

## Cloud deployment

* TODO

## Contributing

Refer to [CONTRIBUTING.md](https://github.com/travelgateX/slack-botx/blob/master/CONTRIBUTING.md)
