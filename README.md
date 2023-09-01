# Discord Voting Bot

## Overview

This Discord bot allows you to create and manage polls (votes) in your Discord server. Users can vote on various options, and the bot provides the final results of the poll.

## Features

- Create a poll with a title and multiple options.
- Users can react to the options to vote.
- Close the poll and view the voting results.

## Prerequisites

- Python 3.6 or higher
- discord.py library
- A Discord bot token (see Discord Developer Portal)

## Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Install the required Python packages:

```
pip install -r requirements.txt
```

## Create a .env file in the project directory with your Discord bot token:

```makefile
DISCORD_TOKEN=your_bot_token_here
```

## Usage

- Start the bot by running the following command:

  ```bash
  python3 vote_bot.py
  ```

- Invite the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal.

### Use the following commands to interact with the bot:

- `!start_vote` Start a new poll. The bot will guide you through creating the poll's title and options.

- `!close_vote` Close the current poll and display the voting results.

- Follow the bot's prompts and react to them accordingly to create and manage polls.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thanks to the discord.py library for making it easy to develop Discord bots in Python.
Feel free to modify and expand upon this README to include any additional details or acknowledgments specific to your project.
