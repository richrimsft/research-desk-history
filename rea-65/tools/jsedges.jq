.normalized_result.graph as $g
| ($g.nodes | map({key:.node_id, value:(.observations[0].properties.path // .observations[0].properties.logical_module_key // .identity.key)}) | from_entries) as $p
| "FILES:",
  ($g.nodes[] | select(.kind=="javascript-asset" or .kind=="unknown") | "  \(.kind|.[0:17]) \(.observations[0].properties.path // .identity.key)  state=\(.observations[0].evidence.state)"),
  "IMPORT EDGES:",
  ($g.edges[] | select(.relation=="imports") | "  \($p[.source_node_id]) --\(.properties.kind // ("binding " + .properties.imported_name))--> \(.properties.resolved_path) [\(.properties.resolution_status); \(.evidence.state)/\(.evidence.confidence)]")
