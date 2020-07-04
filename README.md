# Telegram Resender

Simple bot for making hooks on messages in bots, groups and private chats and resend them.
Made with [pyrogram](https://github.com/pyrogram/pyrogram).

## Setup

### Warning

Due to the problems with moving this repo, default `conf.yml` can be not included at all or be in the project root directory
You should move it to `bot/` directory before running **tgresender**

1. `git clone` this repo
2. [Go get Telegram API keys](https://docs.pyrogram.org/intro/setup#api-keys)
3. Fill app_id and api_hash in `conf.yml`

### Running in docker

4. Build Docker image by running `docker build bot -t tgresender_bot:latest`
5. Run `docker run --rm -it tgresender_bot:latest` to start container

### Running on host

4. Check that you have python3.5+ and virtualenv installed
5. Create python env `python3 -m venv .` and enter it `source bin/activate`
6. Run `pip install git+https://github.com/slntopp/simple-rri.git`
7. Install dependencies by running: `python install_requirements.py`
   7.1 If nothing happens(pip doesn't start) copy command from last line and run it yourself
8. Run `python bot/main.py`

## Notes

> ~~If you need to know chat_id(if chat has no username, for example group chat),
> you can first run all this with --verbose and wait for the message from the group you need.
> (Yes, i'm working on just listing all chats)~~ **deprecated|may be removed**

> Use `generate_session.py` script to generate session
> and then run `list_dialogs.py` to list all dialogs
> sorted with titles, usernames and chat_id's

**deprecated! see below**

> ~~After you ran it once on f.e. your local machine,
> you can add `COPY tgresender.session` to Dockerfile and then
> setup by running 4. and `docker run -d tgresender:latest` after.
> Your session data will be stored in Container, so you wan't need
> to login interactively again.~~

> After you ran it once on f.e. your local machine. you can use directory where
> `tgresender.session` was stored as shared volume, by using
> `docker run -dv absolute/path/to/the/dir:/app/shared`.
> Your session data will be stored in Container, so you wan't need
> to login interactively again.

Feel free to contribute or/and create issues with questions and suggestions.
