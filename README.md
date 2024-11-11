# Bot Safe Agents

A library for fetching a list of bot-safe user agents.

Made for educational purposes. I hope it will help!

## Table of Contents

* [How to Install](#how-to-install)
	* [Standard Install](#standard-install)
	* [Build and Install From the Source](#build-and-install-from-the-source)
* [Usage](#usage)

## How to Install

### Standard Install

```bash
pip3 install bot-safe-agents

pip3 install --upgrade bot-safe-agents
```

### Build and Install From the Source

Run the following commands:

```bash
git clone https://github.com/ivan-sincek/bot-safe-agents && cd bot-safe-agents

python3 -m pip install --upgrade build

python3 -m build

python3 -m pip install dist/bot-safe-agents-1.0-py3-none-any.whl
```

## Usage

Get all user agents:

```python
import bot_safe_agents

user_agents = bot_safe_agents.get_all()
print(user_agents)

# do something
```

Get a random user agent:

```python
import bot_safe_agents

user_agents = bot_safe_agents.get_random()
print(user_agents)

# do something
```
