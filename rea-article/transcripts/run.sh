#!/bin/bash
# Runs each step for real and records "$ command" + its actual output.
source ~/.local/rea-env.sh
export GHIDRA_INSTALL_DIR=/workspace/ghidra/ghidra_12.1.4_PUBLIC
cd /workspace/re/crackme
T=/workspace/re/crackme/target/crackme
step() { local name=$1; shift; : > /workspace/rea-article/transcripts/$name.txt; for c in "$@"; do echo "\$ $c" >> /workspace/rea-article/transcripts/$name.txt; bash -c "source ~/.local/rea-env.sh; export GHIDRA_INSTALL_DIR=$GHIDRA_INSTALL_DIR; cd /workspace/re/crackme; $c" >> /workspace/rea-article/transcripts/$name.txt 2>&1; echo >> /workspace/rea-article/transcripts/$name.txt; done; }
step t01-prereqs "node --version" "npm --version" "java -version 2>&1 | head -1" "echo \$GHIDRA_INSTALL_DIR" "rea --version" "npm view rea-agents dist-tags.latest"
step t02-setup-dryrun "rea setup --client cursor --client claude_code --dry-run 2>&1 | head -60"
step t03-doctor-grokbot "rea doctor --client grok_bot 2>&1 | head -40"
step t04-doctor-ghidra "rea doctor --provider ghidra --filter-output healthy,scope_checks"
step t05-providers "rea providers 2>&1 | head -40"
step t06-workspace "ls -la target/" "sha256sum target/crackme" "touch target/test 2>&1 || echo '(write refused: target/ is read-only)'"
step t07-search "rea search $T password --provider ghidra --filter-output evidence_id,normalized_result,confidence"
step t08-trace "rea trace $T 'Wrong password' --provider ghidra --filter-output evidence_id,normalized_result.matches,normalized_result.references[0].source_address,normalized_result.references[0].containing_procedure.procedure.address,normalized_result.references[0].containing_procedure.procedure.name,confidence"
step t09-decompile-main "rea decompile $T 0x1011f5 --provider ghidra --json | jq -r '.evidence_id, .normalized_result'"
step t10-decompile-check "rea decompile $T 0x101179 --provider ghidra --json | jq -r '.evidence_id, .normalized_result'"
step t11-read-bytes "rea read-bytes $T 0x102008 --length 12 --provider ghidra --filter-output evidence_id,normalized_result,confidence"
step t12-decode-verify "python3 -c \"print(bytes(b ^ 0x2A for b in bytes.fromhex('4d421b4e584b75581a494159')).decode())\"" "printf 'gh1dra_r0cks\n' | ./target/crackme; echo \"  [exit \$?]\"" "printf 'wrong\n' | ./target/crackme; echo \"  [exit \$?]\""
step t13-pe "rea search /workspace/re/crackme/target/crackme.exe password --provider ghidra --filter-output evidence_id,subject.format,subject.architecture,normalized_result,confidence"
step t14-stars "curl -s https://api.github.com/repos/morluto/rea | jq '{full_name, stargazers_count, forks_count, license: .license.spdx_id, pushed_at}'" "TZ=America/New_York date"
