#!/bin/bash
cd /workspace/polymarket-sim
pgrep -f "polymarket-sim/sim.py" >/dev/null && { echo already running; exit; }
nohup nice -n 10 python3 -u /workspace/polymarket-sim/sim.py >> sim.out 2>&1 &
echo started $!
