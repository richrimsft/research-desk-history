#!/bin/bash
cd /workspace/polymarket-sim/copy
[ -f cohorts.json ] || { echo "no cohorts.json yet - run scan.py"; exit 1; }
pgrep -f "polymarket-sim/copy/follow.py" >/dev/null && { echo already running; exit; }
nohup nice -n 15 python3 -u /workspace/polymarket-sim/copy/follow.py >> follow.out 2>&1 &
echo started $!
