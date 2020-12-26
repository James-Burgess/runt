# runt
run-it

Create random python tasks to be triggered by secure api calls.

## Usage

 - create a tasks directory (default=tasks)
 - create a new directory for each task
 - the directory entrypoint is `task.run`
 - args to the run function will be required in the post
 - install requirements ` pip install -r requirements.txt`
 - run `python run.py`
 - navigate to [localhost:8080](localhost:8080) and see all the loaded apps
 - send a post request with your sever key to trigger the script

 ## ENV VARS
 create a `.env` file in the project root for it to be autoloaded on startup

These are the configs for runt (actual defaults)
- PORT=8080
- TASKS_DIR=tasks/
- SERVER_KEY=unsafe
