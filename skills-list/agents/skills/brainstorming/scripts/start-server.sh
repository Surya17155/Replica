#!/usr/bin/env bash
# Start the brainstorm server and output connection info
# Usage: start-server.sh [--project-dir <path>] [--host <bind-host>] [--url-host <display-host>] [--foreground] [--background]
#
# Options:
#   --project-dir <path>  Store session files under <path>/.superpowers/brainstorm/
#   --host <bind-host>    Host/interface to bind (default: 127.0.0.1)
#   --url-host <host>     Hostname shown in returned URL JSON
#   --idle-timeout-minutes <n>  Shut down after n minutes idle (default 240)
#   --open                Auto-open the browser on first screen
#   --foreground          Run server in current terminal
#   --background          Force background mode
#
# Starts server on a random high port, outputs JSON with URL.
# Each session gets its own directory to avoid conflicts.