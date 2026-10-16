#!/bin/bash
cd /workspace/re/lab; source ~/.local/rea-env.sh
f=/workspace/rea-article/transcripts/t22-har.txt; : > $f
for c in "rea inspect-web-network-capture \$PWD/web/demo.har har --json > har-evidence.json; jq -c '.evidence_id, .confidence, {total_records: .normalized_result.total_records, redactions: .normalized_result.container.redactions}' har-evidence.json" \
 "jq -c '.normalized_result.records[] | {ordinal, method: .reported.request.method, url: .reported.request.url, status: .reported.response.status, body: .reported.request.postData.text}' har-evidence.json" \
 "jq -c '.normalized_result.runtime_attribution' har-evidence.json"; do echo "\$ $c" >> $f; bash -c "source ~/.local/rea-env.sh; cd /workspace/re/lab; $c" >> $f 2>&1; echo >> $f; done
