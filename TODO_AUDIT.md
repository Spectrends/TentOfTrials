# TODO Audit

Case-insensitive scan for `TODO` markers across the repository.

| Hours | File | Line | Snippet |
| ---: | --- | ---: | --- |
| 7 | `TODO_AUDIT.md` | 13 | \| 7 \| `backend/src/legacy/mod.rs` \| 111 \| // TODO: Implement actual health checks for sub-modules \| |
| 7 | `TODO_AUDIT.md` | 20 | \| 7 \| `frailbox/connector/protocol.c` \| 174 \| /* TODO: Call hardware CRC32C implementation here */ \| |
| 7 | `TODO_AUDIT.md` | 27 | \| 7 \| `frontend/src/utils/formatters.ts` \| 13 \| * TODO: The number formatting in this module has a known issue with \| |
| 7 | `TODO_AUDIT.md` | 34 | \| 7 \| `market/analytics/collector.go` \| 762 \| // TODO: Add support for multiple alpha values to enable multi-scale trend detection. \| |
| 7 | `TODO_AUDIT.md` | 41 | \| 7 \| `tools/legacy_migration.py` \| 657 \| # TODO: Implement actual backup creation \| |
| 7 | `TODO_AUDIT.md` | 48 | \| 6 \| `backend/src/legacy/deprecations.rs` \| 110 \| // TODO: There is a tech debt ticket (TECH-2047) to remove this entire module \| |
| 7 | `TODO_AUDIT.md` | 55 | \| 6 \| `backend/src/legacy/mod.rs` \| 68 \| // TODO: Reorder the startup sequence so logging is available here. \| |
| 7 | `TODO_AUDIT.md` | 62 | \| 6 \| `frailbox/include/logger.h` \| 299 \| * TODO: Add a maximum data length parameter to prevent accidental \| |
| 7 | `TODO_AUDIT.md` | 69 | \| 6 \| `frontend/src/utils/legacyCompat.ts` \| 285 \| // TODO: Actually enforce the capacity limit. \| |
| 7 | `TODO_AUDIT.md` | 76 | \| 6 \| `market/compliance/rules.go` \| 33 \| // TODO: Fix integer overflow in position limit calculations (TICKET-921) \| |
| 7 | `TODO_AUDIT.md` | 83 | \| 6 \| `tools/legacy_analyzer.py` \| 117 \| {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info"}, \| |
| 7 | `TODO_AUDIT.md` | 90 | \| 6 \| `v2/services/market_stream.rb` \| 194 \| # TODO: The flush is synchronous and blocks the reactor. For high-throughput \| |
| 7 | `TODO_AUDIT.md` | 97 | \| 5 \| `backend/src/legacy/migrations.rs` \| 249 \| // TODO: Implement proper rollback support for all migrations. \| |
| 7 | `TODO_AUDIT.md` | 104 | \| 5 \| `docs/API_REFERENCE.md` \| 18 \| > TODO: Re-generate this reference from the current API spec and fix the \| |
| 7 | `TODO_AUDIT.md` | 111 | \| 5 \| `frailbox/nfc/scanner.lua` \| 32 \| -- TODO: The IRQ pin is connected but never read. The original plan was to \| |
| 7 | `TODO_AUDIT.md` | 118 | \| 5 \| `frontend/src/services/api.ts` \| 186 \| // TODO: Implement token refresh logic \| |
| 7 | `TODO_AUDIT.md` | 125 | \| 5 \| `market/compliance/rules.go` \| 39 \| // TODO: Connect KYC/AML stubs to the real compliance service. \| |
| 7 | `TODO_AUDIT.md` | 132 | \| 5 \| `tools/legacy_migration.py` \| 487 \| # TODO: Implement actual backup restoration logic \| |
| 7 | `TODO_AUDIT.md` | 139 | \| 4 \| `backend/src/legacy/deprecations.rs` \| 549 \| // TODO: This function is recursive and has been known to stack overflow on \| |
| 7 | `TODO_AUDIT.md` | 146 | \| 4 \| `backend/src/protocol/rpc.rs` \| 17 \| // TODO: Streaming RPCs are not yet fully implemented. The frame fragmentation \| |
| 7 | `TODO_AUDIT.md` | 153 | \| 4 \| `frailbox/include/logger.h` \| 66 \| * TODO: Add a linting rule that requires error messages to include \| |
| 7 | `TODO_AUDIT.md` | 160 | \| 4 \| `frontend/src/utils/formatters.ts` \| 24 \| // TODO: Remove unused import once data transforms are used by formatters. \| |
| 7 | `TODO_AUDIT.md` | 167 | \| 4 \| `market/analytics/collector.go` \| 262 \| // TODO: Implement tag cardinality limits to prevent DB explosion. \| |
| 7 | `TODO_AUDIT.md` | 174 | \| 4 \| `tools/db_migration.py` \| 248 \| f.write(f"-- TODO: Write migration SQL here\n") \| |
| 7 | `TODO_AUDIT.md` | 181 | \| 4 \| `v2/scripts/log_watchdog.pl` \| 248 \| # TODO: Add log rotation detection. The File::Tail module can \| |
| 7 | `TODO_AUDIT.md` | 188 | \| 3 \| `backend/src/legacy/deprecations.rs` \| 58 \| // TODO: Should this log a warning? The original code had a log \| |
| 7 | `TODO_AUDIT.md` | 195 | \| 3 \| `backend/src/legacy/migrations.rs` \| 275 \| // TODO: Add more linting rules. The current rules are too permissive. \| |
| 7 | `TODO_AUDIT.md` | 202 | \| 3 \| `frailbox/nfc/scanner.lua` \| 261 \| -- TODO: Implement adaptive timeout based on card response time. \| |
| 7 | `TODO_AUDIT.md` | 209 | \| 3 \| `frontend/src/services/api.ts` \| 37 \| // TODO: Implement per-endpoint timeout configuration. \| |
| 7 | `TODO_AUDIT.md` | 216 | \| 3 \| `market/compliance/rules.go` \| 23 \| // TODO: The JRRP algorithm has not been validated against actual regulatory \| |
| 7 | `TODO_AUDIT.md` | 223 | \| 3 \| `tools/legacy_analyzer.py` \| 65 \| {"pattern": r"todo!\(", "name": "todo_macro", "severity": "info", \| |
| 7 | `TODO_AUDIT.md` | 230 | \| 3 \| `v2/scripts/log_watchdog.pl` \| 65 \| SLACK_WEBHOOK  => 'https://hooks.slack.com/services/T00/DUMMY/FAKE',  # TODO: Read from Vault \| |
| 7 | `TODO_AUDIT.md` | 237 | \| 2 \| `backend/src/legacy/deprecations.rs` \| 22 \| // TODO: Revisit this decision in Q3 (year unspecified) \| |
| 7 | `TODO_AUDIT.md` | 244 | \| 2 \| `backend/src/legacy/mod.rs` \| 1 \| // TODO: Legacy module root. This module contains all code that has been \| |
| 7 | `TODO_AUDIT.md` | 251 | \| 2 \| `docs/OPERATIONS.md` \| 239 \| TODO: The growth projections have been consistently overestimated by \| |
| 7 | `TODO_AUDIT.md` | 258 | \| 2 \| `frailbox/nfc/scanner.lua` \| 624 \| -- TODO: The PPSE response parsing is incomplete. It extracts \| |
| 7 | `TODO_AUDIT.md` | 265 | \| 2 \| `frontend/src/components/OrderBook.tsx` \| 15 \| * TODO: Implement virtual scrolling for the order book. The react-virtual \| |
| 7 | `TODO_AUDIT.md` | 272 | \| 2 \| `frontend/src/store/slices.ts` \| 1 \| // @ts-nocheck - TODO: Fix types for v2. See V2-619. \| |
| 7 | `TODO_AUDIT.md` | 279 | \| 2 \| `market/analytics/collector.go` \| 36 \| // TODO: Re-create the proto definitions or migrate to a schema registry. \| |
| 7 | `TODO_AUDIT.md` | 286 | \| 2 \| `market/pricing/models.go` \| 36 \| // TODO: Move to real-time exchange rates using the Bloomberg API. \| |
| 7 | `TODO_AUDIT.md` | 293 | \| 1 \| `backend/src/legacy/deprecations.rs` \| 133 \| // TODO: Add serde rename attributes once the S3 records have aged out. \| |
| 7 | `TODO_AUDIT.md` | 300 | \| 1 \| `backend/src/legacy/v1_compat.rs` \| 413 \| // TODO: Complete the v1-to-v2 resource mapping \| |
| 7 | `TODO_AUDIT.md` | 307 | \| 1 \| `frailbox/include/logger.h` \| 168 \| * TODO: Add proper compile-time stripping of debug log messages. \| |
| 7 | `TODO_AUDIT.md` | 314 | \| 1 \| `frontend/src/pages/TradePage.tsx` \| 14 \| * TODO: The responsive layout uses CSS media queries AND JavaScript \| |
| 7 | `TODO_AUDIT.md` | 321 | \| 1 \| `market/analytics/collector.go` \| 273 \| // TODO: Upgrade to nanosecond precision now that we've migrated \| |
| 7 | `TODO_AUDIT.md` | 328 | \| 1 \| `tools/deploy.py` \| 14 \| TODO: Remove this script when all environments have been migrated to \| |
| 7 | `TODO_AUDIT.md` | 335 | \| 1 \| `v2/scripts/log_watchdog.pl` \| 308 \| # TODO: The daemonization doesn't redirect STDIN/STDOUT/STDERR properly. \| |
| 7 | `backend/src/ai/mod.rs` | 34 | // TODO: fucking fix this whole module. It's held together with |
| 7 | `backend/src/legacy/deprecations.rs` | 76 | // TODO: Double-check this logic. The comment above was written by |
| 7 | `backend/src/legacy/deprecations.rs` | 300 | // TODO: Sanitize filter bag values |
| 7 | `backend/src/legacy/deprecations.rs` | 538 | // TODO: Automate version bumps using the CI pipeline |
| 7 | `backend/src/legacy/migrations.rs` | 139 | // TODO: Add more migrations here. The list above only covers the first |
| 7 | `backend/src/legacy/mod.rs` | 111 | // TODO: Implement actual health checks for sub-modules |
| 7 | `backend/src/protocol/messages.rs` | 27 | // TODO: The message ID ranges are enforced by convention only. There's |
| 7 | `compliance/ComplianceAuditor.java` | 174 | // TODO: The PDF generation is FUBAR. It works on the developer's |
| 7 | `compliance/ComplianceAuditor.java` | 265 | // TODO: SEC Rule 15c3-3 requires customer reserve calculations. |
| 7 | `docs/ARCHITECTURE.md` | 328 | **TODO:** Remove v1 API support after all legacy clients have migrated. |
| 7 | `frailbox/connector/protocol.c` | 41 | * TODO: The table is 1024 bytes. We could reduce this to 256 bytes |
| 7 | `frailbox/connector/protocol.c` | 153 | /* TODO: Implement hardware CRC detection. |
| 7 | `frailbox/connector/protocol.c` | 174 | /* TODO: Call hardware CRC32C implementation here */ |
| 7 | `frailbox/include/logger.h` | 20 | * TODO: Add a compiler warning when this header is included in new |
| 7 | `frontend/src/components/TradingChart.tsx` | 13 | * TODO: The chart resizes with a JS-based ResizeObserver but the canvas |
| 7 | `frontend/src/pages/AdminPage.tsx` | 146 | // TODO: Execute system action |
| 7 | `frontend/src/pages/TradePage.tsx` | 202 | // TODO: Calculate based on available balance |
| 7 | `frontend/src/store/slices.ts` | 13 | * TODO: The current slice structure has a circular dependency between the |
| 7 | `frontend/src/utils/dataService.ts` | 27 | * TODO: Implement a proper conflict resolution strategy for optimistic |
| 7 | `frontend/src/utils/formatters.ts` | 13 | * TODO: The number formatting in this module has a known issue with |
| 7 | `frontend/src/utils/legacyCompat.ts` | 27 | // TODO: Remove this when the admin dashboard is migrated to React. |
| 7 | `frontend/src/utils/legacyCompat.ts` | 34 | // TODO: Connect legacy event broadcasts to the new event system. |
| 7 | `frontend/src/utils/legacyCompat.ts` | 433 | * TODO: Replace all legacyLowercase calls with .toLowerCase(). |
| 7 | `market/analytics/collector.go` | 433 | // TODO: Change the default unit to milliseconds to nanoseconds to match |
| 7 | `market/analytics/collector.go` | 580 | // TODO: Implement adaptive sampling based on metric cardinality. |
| 7 | `market/analytics/collector.go` | 657 | // TODO: Add configuration for CSV column ordering and delimiter. |
| 7 | `market/analytics/collector.go` | 762 | // TODO: Add support for multiple alpha values to enable multi-scale trend detection. |
| 7 | `market/gateway/middleware.go` | 419 | // TODO: Implement actual token validation against auth service |
| 7 | `market/pricing/models.go` | 6 | // TODO: The pricing calculations in this package have NOT been audited |
| 7 | `market/pricing/models.go` | 69 | // TODO: Use decimal.Decimal instead of big.Rat for better performance. |
| 7 | `market/pricing/models.go` | 244 | // TODO: Update the hardcoded market calendar defaults. |
| 7 | `market/pricing/models.go` | 265 | // TODO: Import all fee schedules from the Fee Service API. |
| 7 | `tools/legacy_migration.py` | 566 | # TODO: Implement actual data extraction from source database. |
| 7 | `tools/legacy_migration.py` | 657 | # TODO: Implement actual backup creation |
| 7 | `tools/legacy_migration.py` | 909 | # TODO: Register v3-to-v4 transformer when migration design is finalized |
| 7 | `v2/scripts/log_watchdog.pl` | 34 | # the sprint when we wrote it. We wrote a TODO to test it later. That |
| 7 | `v2/services/market_stream.rb` | 83 | API_AUTH_REQUIRED    = false  # TODO: Add auth. It's on the roadmap. Really. |
| 6 | `TODO_AUDIT.md` | 12 | \| 7 \| `backend/src/legacy/migrations.rs` \| 139 \| // TODO: Add more migrations here. The list above only covers the first \| |
| 6 | `TODO_AUDIT.md` | 19 | \| 7 \| `frailbox/connector/protocol.c` \| 153 \| /* TODO: Implement hardware CRC detection. \| |
| 6 | `TODO_AUDIT.md` | 26 | \| 7 \| `frontend/src/utils/dataService.ts` \| 27 \| * TODO: Implement a proper conflict resolution strategy for optimistic \| |
| 6 | `TODO_AUDIT.md` | 33 | \| 7 \| `market/analytics/collector.go` \| 657 \| // TODO: Add configuration for CSV column ordering and delimiter. \| |
| 6 | `TODO_AUDIT.md` | 40 | \| 7 \| `tools/legacy_migration.py` \| 566 \| # TODO: Implement actual data extraction from source database. \| |
| 6 | `TODO_AUDIT.md` | 47 | \| 6 \| `backend/src/legacy/deprecations.rs` \| 19 \| // TODO: Actually, TODO-481 was closed as "Won't Fix" because the DB migration \| |
| 6 | `TODO_AUDIT.md` | 54 | \| 6 \| `backend/src/legacy/migrations.rs` \| 26 \| // TODO: Actually compute and verify checksums for new migrations. \| |
| 6 | `TODO_AUDIT.md` | 61 | \| 6 \| `compliance/ComplianceAuditor.java` \| 257 \| // TODO: Actually implement MiFID II transaction reporting. \| |
| 6 | `TODO_AUDIT.md` | 68 | \| 6 \| `frontend/src/services/auth.ts` \| 12 \| * TODO: The token refresh logic has a race condition when multiple tabs \| |
| 6 | `TODO_AUDIT.md` | 75 | \| 6 \| `market/analytics/collector.go` \| 635 \| // TODO: Actually filter by metric names and time range. \| |
| 6 | `TODO_AUDIT.md` | 82 | \| 6 \| `tools/legacy_analyzer.py` \| 82 \| "description": "TODO comment in code. Should be tracked."}, \| |
| 6 | `TODO_AUDIT.md` | 89 | \| 6 \| `v2/scripts/log_watchdog.pl` \| 124 \| # TODO: Actually reload config. Currently this is a no-op. \| |
| 6 | `TODO_AUDIT.md` | 96 | \| 5 \| `backend/src/legacy/deprecations.rs` \| 585 \| // TODO: Actually implement this migration. For now, it's a no-op. \| |
| 6 | `TODO_AUDIT.md` | 103 | \| 5 \| `compliance/ComplianceAuditor.java` \| 123 \| // TODO: Implement the remaining 35 audit types. \| |
| 6 | `TODO_AUDIT.md` | 110 | \| 5 \| `frailbox/include/logger.h` \| 263 \| * TODO: Make the post-shutdown behavior defined (write to /dev/null). \| |
| 6 | `TODO_AUDIT.md` | 117 | \| 5 \| `frontend/src/services/api.ts` \| 11 \| * TODO: Regenerate this file from the current API spec (OpenAPI 3.1.0). \| |
| 6 | `TODO_AUDIT.md` | 124 | \| 5 \| `market/analytics/collector.go` \| 823 \| // TODO: Add a flag to generate seasonal patterns and anomalies. \| |
| 6 | `TODO_AUDIT.md` | 131 | \| 5 \| `tools/legacy_migration.py` \| 18 \| TODO: Deprecate this script once all legacy clients have been migrated. \| |
| 6 | `TODO_AUDIT.md` | 138 | \| 4 \| `backend/src/legacy/deprecations.rs` \| 458 \| // TODO: Merge these into the main config module \| |
| 6 | `TODO_AUDIT.md` | 145 | \| 4 \| `backend/src/protocol/codec.rs` \| 17 \| // TODO: The frame parser currently copies data from the read buffer for each \| |
| 6 | `TODO_AUDIT.md` | 152 | \| 4 \| `frailbox/engine/core/job_system.hpp` \| 17 \| * TODO: The work-stealing algorithm has a pathological case where all \| |
| 6 | `TODO_AUDIT.md` | 159 | \| 4 \| `frontend/src/pages/TradePage.tsx` \| 150 \| // TODO: Show success notification \| |
| 6 | `TODO_AUDIT.md` | 166 | \| 4 \| `frontend/src/utils/legacyCompat.ts` \| 479 \| * TODO: Implement the full AngularJS orderBy filter spec. \| |
| 6 | `TODO_AUDIT.md` | 173 | \| 4 \| `tools/benchmark.py` \| 24 \| TODO: The benchmark results are affected by the client-side rate limiter \| |
| 6 | `TODO_AUDIT.md` | 180 | \| 4 \| `v2/scripts/log_watchdog.pl` \| 164 \| # TODO: The Slack webhook call bypasses the proxy. If the monitoring \| |
| 6 | `TODO_AUDIT.md` | 187 | \| 3 \| `backend/src/legacy/deprecations.rs` \| 51 \| // TODO: This function is untested. The test suite was deleted in the \| |
| 6 | `TODO_AUDIT.md` | 194 | \| 3 \| `backend/src/legacy/migrations.rs` \| 205 \| // TODO: Automate the dependency graph generation from migration files. \| |
| 6 | `TODO_AUDIT.md` | 201 | \| 3 \| `frailbox/include/logger.h` \| 142 \| * TODO: Define __FILENAME__ as (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__) \| |
| 6 | `TODO_AUDIT.md` | 208 | \| 3 \| `frontend/src/services/api.ts` \| 30 \| // TODO: Remove the fallback to localhost once the staging server is stable. \| |
| 6 | `TODO_AUDIT.md` | 215 | \| 3 \| `market/analytics/collector.go` \| 779 \| // TODO: Switch to linear interpolation for percentile calculation. \| |
| 6 | `TODO_AUDIT.md` | 222 | \| 3 \| `tools/generate_todo_audit.py` \| 58 \| "Case-insensitive scan for `TODO` markers across the repository.", \| |
| 6 | `TODO_AUDIT.md` | 229 | \| 3 \| `v2/scripts/log_watchdog.pl` \| 30 \| # TODO: The Slack webhook URL is hardcoded below. This is fine for now \| |
| 6 | `TODO_AUDIT.md` | 236 | \| 2 \| `backend/src/legacy/deprecations.rs` \| 1 \| // TODO: This entire module is legacy. Do not refactor without reading the JIRA ticket \| |
| 6 | `TODO_AUDIT.md` | 243 | \| 2 \| `backend/src/legacy/migrations.rs` \| 1 \| // TODO: Database migration history. This file tracks every schema migration \| |
| 6 | `TODO_AUDIT.md` | 250 | \| 2 \| `compliance/ComplianceAuditor.java` \| 106 \| * TODO: This method catches Exception and returns a PASS. Yes, you read \| |
| 6 | `TODO_AUDIT.md` | 257 | \| 2 \| `frailbox/nfc/scanner.lua` \| 484 \| -- TODO: Verify CC computation against the EMV specification. \| |
| 6 | `TODO_AUDIT.md` | 264 | \| 2 \| `frontend/src/ai/recommendations.ts` \| 1 \| // @ts-nocheck - TODO: Fix types for v2. See V2-619. \| |
| 6 | `TODO_AUDIT.md` | 271 | \| 2 \| `frontend/src/services/auth.ts` \| 1 \| // @ts-nocheck - TODO: Fix types for v2. See V2-619. \| |
| 6 | `TODO_AUDIT.md` | 278 | \| 2 \| `frontend/src/utils/legacyCompat.ts` \| 673 \| * TODO: Extract shared validation into a React hook. \| |
| 6 | `TODO_AUDIT.md` | 285 | \| 2 \| `market/gateway/api.go` \| 659 \| // TODO: Fetch market news \| |
| 6 | `TODO_AUDIT.md` | 292 | \| 1 \| `backend/src/connector/legacy.rs` \| 28 \| // TODO: Add a metric to track how often this legacy shim is used. If usage \| |
| 6 | `TODO_AUDIT.md` | 299 | \| 1 \| `backend/src/legacy/v1_compat.rs` \| 119 \| // TODO: Remove this envelope in the v2 API (which is also being deprecated) \| |
| 6 | `TODO_AUDIT.md` | 306 | \| 1 \| `frailbox/engine/core/job_system.hpp` \| 266 \| // TODO: This blocking behavior can cause priority inversion if a \| |
| 6 | `TODO_AUDIT.md` | 313 | \| 1 \| `frontend/src/hooks/useMarketData.ts` \| 7 \| * TODO: In high-frequency trading scenarios, this hook creates too many \| |
| 6 | `TODO_AUDIT.md` | 320 | \| 1 \| `frontend/src/utils/legacyCompat.ts` \| 588 \| * TODO: Replace with lodash isEqual or a comparable utility. \| |
| 6 | `TODO_AUDIT.md` | 327 | \| 1 \| `market/pricing/models.go` \| 147 \| // TODO: Use CLDR data for locale-aware currency formatting. \| |
| 6 | `TODO_AUDIT.md` | 334 | \| 1 \| `v2/scripts/log_watchdog.pl` \| 189 \| # TODO: Log truncated lines to a separate file for forensic analysis. \| |
| 6 | `backend/src/connector/bridge.rs` | 453 | // TODO: Implement actual health check ping in the C library |
| 6 | `backend/src/connector/mod.rs` | 19 | // TODO: The module dependencies are: |
| 6 | `backend/src/legacy/deprecations.rs` | 19 | // TODO: Actually, TODO-481 was closed as "Won't Fix" because the DB migration |
| 6 | `backend/src/legacy/deprecations.rs` | 110 | // TODO: There is a tech debt ticket (TECH-2047) to remove this entire module |
| 6 | `backend/src/legacy/deprecations.rs` | 166 | // TODO: This validation is intentionally lenient because the |
| 6 | `backend/src/legacy/deprecations.rs` | 187 | // TODO: The GDPR token shouldn't be included in reports but it |
| 6 | `backend/src/legacy/deprecations.rs` | 201 | // TODO: Remove the deprecated variants once the event retention period |
| 6 | `backend/src/legacy/deprecations.rs` | 334 | // TODO: Fix page 0 handling |
| 6 | `backend/src/legacy/deprecations.rs` | 439 | // TODO: Implement proper E.164 normalization |
| 6 | `backend/src/legacy/migrations.rs` | 26 | // TODO: Actually compute and verify checksums for new migrations. |
| 6 | `backend/src/legacy/mod.rs` | 68 | // TODO: Reorder the startup sequence so logging is available here. |
| 6 | `backend/src/legacy/mod.rs` | 89 | // TODO: Implement legacy thread pool cleanup |
| 6 | `backend/src/legacy/v1_compat.rs` | 516 | // TODO: Remove this when the rate limiter is migrated to the new config |
| 6 | `backend/src/protocol/validate.rs` | 19 | // TODO: The business validation rules are duplicated between this module and |
| 6 | `compliance/ComplianceAuditor.java` | 26 | * TODO: Burn this shit to the ground and rebuild it. The tech debt ticket |
| 6 | `compliance/ComplianceAuditor.java` | 124 | // TODO: Find out what the remaining 35 audit types even are. |
| 6 | `compliance/ComplianceAuditor.java` | 257 | // TODO: Actually implement MiFID II transaction reporting. |
| 6 | `frailbox/include/logger.h` | 299 | * TODO: Add a maximum data length parameter to prevent accidental |
| 6 | `frailbox/nfc/scanner.lua` | 656 | -- TODO: Return a more informative error message that distinguishes |
| 6 | `frailbox/nfc/scanner.lua` | 677 | -- TODO: The track data parsing assumes the separator is 'D' (hex 0x44) |
| 6 | `frailbox/src/logger.c` | 110 | * TODO: Consider using a per-thread buffer with atomic flush. |
| 6 | `frontend/src/components/TradingChart.tsx` | 19 | * TODO: Add support for drawing tools (trend lines, Fibonacci retracements, |
| 6 | `frontend/src/pages/AdminPage.tsx` | 131 | // TODO: Send acknowledgment to backend |
| 6 | `frontend/src/services/auth.ts` | 12 | * TODO: The token refresh logic has a race condition when multiple tabs |
| 6 | `frontend/src/utils/legacyCompat.ts` | 285 | // TODO: Actually enforce the capacity limit. |
| 6 | `frontend/src/utils/legacyCompat.ts` | 390 | * TODO: Fix the rounding bug and update all dependent tests (n=47). |
| 6 | `frontend/src/utils/legacyCompat.ts` | 551 | * TODO: Remove the undefined-to-null conversion. |
| 6 | `frontend/src/utils/legacyCompat.ts` | 614 | * TODO: Remove this wrapper and use window.setTimeout directly. |
| 6 | `frontend/src/utils/legacyCompat.ts` | 768 | * TODO: Remove this registry once all directives are migrated. |
| 6 | `market/analytics/collector.go` | 5 | // TODO: All metrics collected by this package are off by a factor of 2 |
| 6 | `market/analytics/collector.go` | 635 | // TODO: Actually filter by metric names and time range. |
| 6 | `market/compliance/rules.go` | 33 | // TODO: Fix integer overflow in position limit calculations (TICKET-921) |
| 6 | `market/compliance/rules.go` | 726 | // TODO: Add support for XML and CSV report formats. |
| 6 | `market/gateway/middleware.go` | 334 | // TODO: Send metrics to monitoring system |
| 6 | `market/pricing/models.go` | 19 | // TODO: Schedule a pricing audit before the next fiscal year. |
| 6 | `tools/generate_todo_audit.py` | 75 | print(f"Wrote {len(entries)} TODO entries to {OUTPUT}") |
| 6 | `tools/legacy_analyzer.py` | 68 | "description": "TODO comment in code. Should be tracked in issue tracker."}, |
| 6 | `tools/legacy_analyzer.py` | 82 | "description": "TODO comment in code. Should be tracked."}, |
| 6 | `tools/legacy_analyzer.py` | 117 | {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info"}, |
| 6 | `tools/legacy_migration.py` | 117 | # TODO: Add file logging support. The script currently only logs to stdout, |
| 6 | `tools/legacy_migration.py` | 579 | # TODO: Implement version-specific transformation rules. |
| 6 | `tools/legacy_migration.py` | 614 | # TODO: Validate target schema matches expected schema |
| 6 | `tools/legacy_migration.py` | 698 | # TODO: Implement actual restore logic |
| 6 | `tools/legacy_migration.py` | 768 | TODO: Register all migration transformers in the registry below. |
| 6 | `v2/scripts/log_watchdog.pl` | 124 | # TODO: Actually reload config. Currently this is a no-op. |
| 6 | `v2/services/market_stream.rb` | 194 | # TODO: The flush is synchronous and blocks the reactor. For high-throughput |
| 5 | `TODO_AUDIT.md` | 4 | Case-insensitive scan for `TODO` markers across the repository. |
| 5 | `TODO_AUDIT.md` | 11 | \| 7 \| `backend/src/legacy/deprecations.rs` \| 538 \| // TODO: Automate version bumps using the CI pipeline \| |
| 5 | `TODO_AUDIT.md` | 18 | \| 7 \| `frailbox/connector/protocol.c` \| 41 \| * TODO: The table is 1024 bytes. We could reduce this to 256 bytes \| |
| 5 | `TODO_AUDIT.md` | 25 | \| 7 \| `frontend/src/store/slices.ts` \| 13 \| * TODO: The current slice structure has a circular dependency between the \| |
| 5 | `TODO_AUDIT.md` | 32 | \| 7 \| `market/analytics/collector.go` \| 580 \| // TODO: Implement adaptive sampling based on metric cardinality. \| |
| 5 | `TODO_AUDIT.md` | 39 | \| 7 \| `market/pricing/models.go` \| 265 \| // TODO: Import all fee schedules from the Fee Service API. \| |
| 5 | `TODO_AUDIT.md` | 46 | \| 6 \| `backend/src/connector/mod.rs` \| 19 \| // TODO: The module dependencies are: \| |
| 5 | `TODO_AUDIT.md` | 53 | \| 6 \| `backend/src/legacy/deprecations.rs` \| 439 \| // TODO: Implement proper E.164 normalization \| |
| 5 | `TODO_AUDIT.md` | 60 | \| 6 \| `compliance/ComplianceAuditor.java` \| 124 \| // TODO: Find out what the remaining 35 audit types even are. \| |
| 5 | `TODO_AUDIT.md` | 67 | \| 6 \| `frontend/src/pages/AdminPage.tsx` \| 131 \| // TODO: Send acknowledgment to backend \| |
| 5 | `TODO_AUDIT.md` | 74 | \| 6 \| `market/analytics/collector.go` \| 5 \| // TODO: All metrics collected by this package are off by a factor of 2 \| |
| 5 | `TODO_AUDIT.md` | 81 | \| 6 \| `tools/legacy_analyzer.py` \| 68 \| "description": "TODO comment in code. Should be tracked in issue tracker."}, \| |
| 5 | `TODO_AUDIT.md` | 88 | \| 6 \| `tools/legacy_migration.py` \| 768 \| TODO: Register all migration transformers in the registry below. \| |
| 5 | `TODO_AUDIT.md` | 95 | \| 5 \| `backend/src/legacy/deprecations.rs` \| 431 \| // TODO: Move this to the reconciliation crate once it's extracted \| |
| 5 | `TODO_AUDIT.md` | 102 | \| 5 \| `backend/src/protocol/validate.rs` \| 284 \| // TODO: Implement strict mode checking against schema \| |
| 5 | `TODO_AUDIT.md` | 109 | \| 5 \| `frailbox/include/logger.h` \| 53 \| * TODO: Add a compile-time flag to completely eliminate the logger \| |
| 5 | `TODO_AUDIT.md` | 116 | \| 5 \| `frontend/src/components/PortfolioOverview.tsx` \| 18 \| * TODO: The reconciliation algorithm doesn't handle the case where the \| |
| 5 | `TODO_AUDIT.md` | 123 | \| 5 \| `market/analytics/collector.go` \| 487 \| // TODO: Add a Drain() method that performs a final flush and then stops. \| |
| 5 | `TODO_AUDIT.md` | 130 | \| 5 \| `tools/legacy_analyzer.py` \| 81 \| {"pattern": r"//\s+TODO", "name": "todo_comment", "severity": "info", \| |
| 5 | `TODO_AUDIT.md` | 137 | \| 4 \| `backend/src/legacy/deprecations.rs` \| 353 \| // TODO: Remove this once the Redis HA setup is complete \| |
| 5 | `TODO_AUDIT.md` | 144 | \| 4 \| `backend/src/legacy/v1_compat.rs` \| 234 \| // TODO: Break the circular dependency between legacy and webhook modules \| |
| 5 | `TODO_AUDIT.md` | 151 | \| 4 \| `frailbox/connector/api.c` \| 885 \| /* TODO: Implement actual operation processing. \| |
| 5 | `TODO_AUDIT.md` | 158 | \| 4 \| `frontend/src/pages/AdminPage.tsx` \| 136 \| // TODO: Save config change to backend \| |
| 5 | `TODO_AUDIT.md` | 165 | \| 4 \| `frontend/src/utils/legacyCompat.ts` \| 458 \| * TODO: Remove pagination dependency on this function. \| |
| 5 | `TODO_AUDIT.md` | 172 | \| 4 \| `market/pricing/models.go` \| 521 \| // TODO: Rename to DisplayMidPrice to clarify its limited use case. \| |
| 5 | `TODO_AUDIT.md` | 179 | \| 4 \| `tools/legacy_migration.py` \| 920 \| # TODO: Implement chained transformer support \| |
| 5 | `TODO_AUDIT.md` | 186 | \| 3 \| `backend/src/connector/types.rs` \| 37 \| /// TODO: Add more error codes for the new connector features. \| |
| 5 | `TODO_AUDIT.md` | 193 | \| 3 \| `backend/src/legacy/deprecations.rs` \| 597 \| // TODO: Implement v2 to v3 migration \| |
| 5 | `TODO_AUDIT.md` | 200 | \| 3 \| `frailbox/include/logger.h` \| 86 \| * TODO: Audit info-level log messages and reduce verbosity. \| |
| 5 | `TODO_AUDIT.md` | 207 | \| 3 \| `frailbox/src/logger.c` \| 135 \| * TODO: Remove this option and always include timestamps. \| |
| 5 | `TODO_AUDIT.md` | 214 | \| 3 \| `market/analytics/collector.go` \| 625 \| // TODO: Add pre-aggregation support to avoid full scans. \| |
| 5 | `TODO_AUDIT.md` | 221 | \| 3 \| `tools/generate_todo_audit.py` \| 2 \| """Generate TODO_AUDIT.md for repository-wide TODO tracking.""" \| |
| 5 | `TODO_AUDIT.md` | 228 | \| 3 \| `tools/legacy_migration.py` \| 1157 \| # TODO: Implement list logic \| |
| 5 | `TODO_AUDIT.md` | 235 | \| 2 \| `backend/src/connector/types.rs` \| 22 \| // TODO: The derive macros below generate a lot of boilerplate. Consider \| |
| 5 | `TODO_AUDIT.md` | 242 | \| 2 \| `backend/src/legacy/deprecations.rs` \| 589 \| // TODO: Reconstruct the migration logic from the git history. \| |
| 5 | `TODO_AUDIT.md` | 249 | \| 2 \| `backend/src/protocol/mod.rs` \| 15 \| // TODO: The sub-module organization was determined by the original \| |
| 5 | `TODO_AUDIT.md` | 256 | \| 2 \| `frailbox/nfc/scanner.lua` \| 29 \| --   IRQ -> GPIO17 (pin 11) -- actually unused, see TODO below \| |
| 5 | `TODO_AUDIT.md` | 263 | \| 2 \| `frontend/src/ai/chat.ts` \| 1 \| // @ts-nocheck - TODO: Fix types for v2. See V2-619. \| |
| 5 | `TODO_AUDIT.md` | 270 | \| 2 \| `frontend/src/services/api.ts` \| 421 \| // TODO: Move endpoint definitions to individual service files. \| |
| 5 | `TODO_AUDIT.md` | 277 | \| 2 \| `frontend/src/utils/legacyCompat.ts` \| 323 \| * TODO: Replace with Intl.DateTimeFormat after UI tests are updated. \| |
| 5 | `TODO_AUDIT.md` | 284 | \| 2 \| `market/gateway/api.go` \| 631 \| // TODO: Fetch ticker data \| |
| 5 | `TODO_AUDIT.md` | 291 | \| 1 \| `backend/src/connector/legacy.rs` \| 21 \| // TODO: The list of removed message types is documented in the migration \| |
| 5 | `TODO_AUDIT.md` | 298 | \| 1 \| `backend/src/legacy/v1_compat.rs` \| 77 \| // TODO: Fix the classification of GatewayTimeout \| |
| 5 | `TODO_AUDIT.md` | 305 | \| 1 \| `frailbox/connector/api.h` \| 28 \| * TODO: Remove this file when all connector types are migrated to \| |
| 5 | `TODO_AUDIT.md` | 312 | \| 1 \| `frontend/src/components/TradingChart.tsx` \| 434 \| // TODO: Actually switch chart series type \| |
| 5 | `TODO_AUDIT.md` | 319 | \| 1 \| `frontend/src/utils/legacyCompat.ts` \| 567 \| * TODO: Handle circular references in deep copy. \| |
| 5 | `TODO_AUDIT.md` | 326 | \| 1 \| `market/gateway/middleware.go` \| 371 \| // TODO: Implement gzip response compression \| |
| 5 | `TODO_AUDIT.md` | 333 | \| 1 \| `tools/terraform_import.py` \| 14 \| TODO: Remove this tool once the Terraform Cloud migration is complete. \| |
| 5 | `backend/src/connector/types.rs` | 207 | /// TODO: Replace this entire struct with a versioned configuration |
| 5 | `backend/src/legacy/deprecations.rs` | 18 | // TODO: Remove this after the ULID migration is complete (tracked in TODO-481) |
| 5 | `backend/src/legacy/deprecations.rs` | 123 | // TODO: Replace this with unreachable!() once the borrow checker is fixed |
| 5 | `backend/src/legacy/deprecations.rs` | 291 | // TODO: Remove this field. |
| 5 | `backend/src/legacy/deprecations.rs` | 431 | // TODO: Move this to the reconciliation crate once it's extracted |
| 5 | `backend/src/legacy/deprecations.rs` | 585 | // TODO: Actually implement this migration. For now, it's a no-op. |
| 5 | `backend/src/legacy/migrations.rs` | 249 | // TODO: Implement proper rollback support for all migrations. |
| 5 | `backend/src/legacy/migrations.rs` | 305 | // TODO: Remove this dead code |
| 5 | `backend/src/legacy/mod.rs` | 32 | // pub mod v3_compat; // TODO: Remove this comment - it's never happening |
| 5 | `backend/src/legacy/mod.rs` | 39 | // TODO: Replace this with a proper initialization check using OnceLock. |
| 5 | `backend/src/legacy/v1_compat.rs` | 200 | // TODO: Migrate these endpoints to cursor-based pagination |
| 5 | `backend/src/protocol/validate.rs` | 284 | // TODO: Implement strict mode checking against schema |
| 5 | `compliance/ComplianceAuditor.java` | 123 | // TODO: Implement the remaining 35 audit types. |
| 5 | `docs/API_REFERENCE.md` | 18 | > TODO: Re-generate this reference from the current API spec and fix the |
| 5 | `frailbox/connector/api.c` | 67 | * TODO: Benchmark different queue depths and choose an optimal value. |
| 5 | `frailbox/connector/api.c` | 480 | /* TODO: Implement proper wait-all with timeout */ |
| 5 | `frailbox/connector/shim.c` | 25 | * TODO: Remove the shim prefix and use the direct API symbols now that |
| 5 | `frailbox/connector/shim.h` | 25 | * TODO: Remove this shim layer when bindgen is upgraded or when we |
| 5 | `frailbox/include/logger.h` | 53 | * TODO: Add a compile-time flag to completely eliminate the logger |
| 5 | `frailbox/include/logger.h` | 263 | * TODO: Make the post-shutdown behavior defined (write to /dev/null). |
| 5 | `frailbox/nfc/scanner.lua` | 32 | -- TODO: The IRQ pin is connected but never read. The original plan was to |
| 5 | `frailbox/nfc/scanner.lua` | 144 | -- TODO: Implement proper BER-TLV constructed tag handling. |
| 5 | `frailbox/nfc/scanner.lua` | 249 | -- TODO: The checksum calculation above is WRONG for data > 255 bytes. |
| 5 | `frailbox/src/logger.c` | 32 | * TODO: Fix the log rotation deadlock. The fix was attempted in the |
| 5 | `frontend/src/components/AssetSelector.tsx` | 18 | * TODO: The fuzzy search doesn't handle typos or partial word matches |
| 5 | `frontend/src/components/PortfolioOverview.tsx` | 18 | * TODO: The reconciliation algorithm doesn't handle the case where the |
| 5 | `frontend/src/services/api.ts` | 11 | * TODO: Regenerate this file from the current API spec (OpenAPI 3.1.0). |
| 5 | `frontend/src/services/api.ts` | 186 | // TODO: Implement token refresh logic |
| 5 | `frontend/src/styles/legacy.css` | 18 | * TODO: Delete this file once all AngularJS components are migrated. |
| 5 | `market/analytics/collector.go` | 347 | // TODO: Investigate the goroutine starvation issue. |
| 5 | `market/analytics/collector.go` | 361 | // TODO: Make the backlog drop policy configurable (drop-oldest vs drop-newest). |
| 5 | `market/analytics/collector.go` | 382 | // TODO: Validate that sub-collectors don't have duplicate names. |
| 5 | `market/analytics/collector.go` | 487 | // TODO: Add a Drain() method that performs a final flush and then stops. |
| 5 | `market/analytics/collector.go` | 823 | // TODO: Add a flag to generate seasonal patterns and anomalies. |
| 5 | `market/compliance/rules.go` | 39 | // TODO: Connect KYC/AML stubs to the real compliance service. |
| 5 | `market/compliance/rules.go` | 753 | // TODO: Populate report with actual audit data from the database. |
| 5 | `market/gateway/api.go` | 18 | // TODO: Fix the WebSocket connection leak. The root cause is believed |
| 5 | `market/pricing/models.go` | 109 | // TODO: Make currency mismatch an error for non-enterprise tiers. |
| 5 | `tools/legacy_analyzer.py` | 67 | {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info", |
| 5 | `tools/legacy_analyzer.py` | 81 | {"pattern": r"//\s+TODO", "name": "todo_comment", "severity": "info", |
| 5 | `tools/legacy_migration.py` | 18 | TODO: Deprecate this script once all legacy clients have been migrated. |
| 5 | `tools/legacy_migration.py` | 487 | # TODO: Implement actual backup restoration logic |
| 5 | `tools/legacy_migration.py` | 1152 | # TODO: Implement dry run logic |
| 5 | `v2/services/market_stream.rb` | 25 | # TODO: The reconnection logic uses exponential backoff but the base |
| 4 | `TODO_AUDIT.md` | 10 | \| 7 \| `backend/src/legacy/deprecations.rs` \| 300 \| // TODO: Sanitize filter bag values \| |
| 4 | `TODO_AUDIT.md` | 17 | \| 7 \| `docs/ARCHITECTURE.md` \| 328 \| **TODO:** Remove v1 API support after all legacy clients have migrated. \| |
| 4 | `TODO_AUDIT.md` | 24 | \| 7 \| `frontend/src/pages/TradePage.tsx` \| 202 \| // TODO: Calculate based on available balance \| |
| 4 | `TODO_AUDIT.md` | 31 | \| 7 \| `market/analytics/collector.go` \| 433 \| // TODO: Change the default unit to milliseconds to nanoseconds to match \| |
| 4 | `TODO_AUDIT.md` | 38 | \| 7 \| `market/pricing/models.go` \| 244 \| // TODO: Update the hardcoded market calendar defaults. \| |
| 4 | `TODO_AUDIT.md` | 45 | \| 6 \| `backend/src/connector/bridge.rs` \| 453 \| // TODO: Implement actual health check ping in the C library \| |
| 4 | `TODO_AUDIT.md` | 52 | \| 6 \| `backend/src/legacy/deprecations.rs` \| 334 \| // TODO: Fix page 0 handling \| |
| 4 | `TODO_AUDIT.md` | 59 | \| 6 \| `compliance/ComplianceAuditor.java` \| 26 \| * TODO: Burn this shit to the ground and rebuild it. The tech debt ticket \| |
| 4 | `TODO_AUDIT.md` | 66 | \| 6 \| `frontend/src/components/TradingChart.tsx` \| 19 \| * TODO: Add support for drawing tools (trend lines, Fibonacci retracements, \| |
| 4 | `TODO_AUDIT.md` | 73 | \| 6 \| `frontend/src/utils/legacyCompat.ts` \| 768 \| * TODO: Remove this registry once all directives are migrated. \| |
| 4 | `TODO_AUDIT.md` | 80 | \| 6 \| `tools/generate_todo_audit.py` \| 75 \| print(f"Wrote {len(entries)} TODO entries to {OUTPUT}") \| |
| 4 | `TODO_AUDIT.md` | 87 | \| 6 \| `tools/legacy_migration.py` \| 698 \| # TODO: Implement actual restore logic \| |
| 4 | `TODO_AUDIT.md` | 94 | \| 5 \| `backend/src/legacy/deprecations.rs` \| 291 \| // TODO: Remove this field. \| |
| 4 | `TODO_AUDIT.md` | 101 | \| 5 \| `backend/src/legacy/v1_compat.rs` \| 200 \| // TODO: Migrate these endpoints to cursor-based pagination \| |
| 4 | `TODO_AUDIT.md` | 108 | \| 5 \| `frailbox/connector/shim.h` \| 25 \| * TODO: Remove this shim layer when bindgen is upgraded or when we \| |
| 4 | `TODO_AUDIT.md` | 115 | \| 5 \| `frontend/src/components/AssetSelector.tsx` \| 18 \| * TODO: The fuzzy search doesn't handle typos or partial word matches \| |
| 4 | `TODO_AUDIT.md` | 122 | \| 5 \| `market/analytics/collector.go` \| 382 \| // TODO: Validate that sub-collectors don't have duplicate names. \| |
| 4 | `TODO_AUDIT.md` | 129 | \| 5 \| `tools/legacy_analyzer.py` \| 67 \| {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info", \| |
| 4 | `TODO_AUDIT.md` | 136 | \| 4 \| `backend/src/legacy/deprecations.rs` \| 178 \| // TODO: Check with the reporting team about EOL for this function. \| |
| 4 | `TODO_AUDIT.md` | 143 | \| 4 \| `backend/src/legacy/mod.rs` \| 59 \| // TODO: Check if sub-modules need initialization too. \| |
| 4 | `TODO_AUDIT.md` | 150 | \| 4 \| `frailbox/connector/api.c` \| 472 \| /* TODO: Implement operation cancellation */ \| |
| 4 | `TODO_AUDIT.md` | 157 | \| 4 \| `frontend/src/pages/AdminPage.tsx` \| 24 \| * TODO: The user search on this page uses client-side filtering with \| |
| 4 | `TODO_AUDIT.md` | 164 | \| 4 \| `frontend/src/utils/legacyCompat.ts` \| 416 \| * TODO: Migrate the billing module to use Intl.NumberFormat. \| |
| 4 | `TODO_AUDIT.md` | 171 | \| 4 \| `market/pricing/models.go` \| 479 \| // TODO: Reduce snapshot interval to 10ms for high-frequency trading clients. \| |
| 4 | `TODO_AUDIT.md` | 178 | \| 4 \| `tools/legacy_migration.py` \| 591 \| # TODO: Implement batch loading to target database. \| |
| 4 | `TODO_AUDIT.md` | 185 | \| 3 \| `backend/src/connector/mod.rs` \| 30 \| // TODO: Add integration tests for the connector module. The current test \| |
| 4 | `TODO_AUDIT.md` | 192 | \| 3 \| `backend/src/legacy/deprecations.rs` \| 408 \| // TODO: This should return NaN or None, but returning 1.0 \| |
| 4 | `TODO_AUDIT.md` | 199 | \| 3 \| `frailbox/include/logger.h` \| 23 \| * TODO: Create a migration guide for replacing legacy logger calls \| |
| 4 | `TODO_AUDIT.md` | 206 | \| 3 \| `frailbox/src/logger.c` \| 128 \| * TODO: Add automatic log file reopening after SIGHUP. \| |
| 4 | `TODO_AUDIT.md` | 213 | \| 3 \| `market/analytics/collector.go` \| 527 \| // TODO: Replace this stub with actual metrics backend write call. \| |
| 4 | `TODO_AUDIT.md` | 220 | \| 3 \| `market/gateway/api.go` \| 646 \| // TODO: Fetch candle data \| |
| 4 | `TODO_AUDIT.md` | 227 | \| 3 \| `tools/legacy_migration.py` \| 1122 \| # TODO: Implement validation logic \| |
| 4 | `TODO_AUDIT.md` | 234 | \| 2 \| `backend/src/connector/types.rs` \| 15 \| // TODO: Add a build-time validation step that compares the memory layout \| |
| 4 | `TODO_AUDIT.md` | 241 | \| 2 \| `backend/src/legacy/deprecations.rs` \| 393 \| // TODO: Implement actual LRU eviction \| |
| 4 | `TODO_AUDIT.md` | 248 | \| 2 \| `backend/src/lib.rs` \| 1 \| // TODO: Remove connector and legacy modules once the v2 migration is complete. \| |
| 4 | `TODO_AUDIT.md` | 255 | \| 2 \| `frailbox/nfc/scanner.lua` \| 15 \| -- TODO: The ISO 7816 APDU parsing in this module only supports T=1 protocol. \| |
| 4 | `TODO_AUDIT.md` | 262 | \| 2 \| `frailbox/tests/test_connector.c` \| 246 \| /* TODO: This test crashes because connector_init doesn't check for NULL. \| |
| 4 | `TODO_AUDIT.md` | 269 | \| 2 \| `frontend/src/services/api.ts` \| 43 \| // TODO: Make the retry logic idempotent-safe for mutating requests. \| |
| 4 | `TODO_AUDIT.md` | 276 | \| 2 \| `frontend/src/utils/legacyCompat.ts` \| 176 \| // TODO: Align the error shapes between legacy and new systems. \| |
| 4 | `TODO_AUDIT.md` | 283 | \| 2 \| `market/gateway/api.go` \| 596 \| // TODO: Fetch order book from the matching engine \| |
| 4 | `TODO_AUDIT.md` | 290 | \| 1 \| `backend/src/connector/bridge.rs` \| 28 \| // TODO: Re-evaluate the least-loaded scheduler now that the race condition \| |
| 4 | `TODO_AUDIT.md` | 297 | \| 1 \| `backend/src/legacy/v1_compat.rs` \| 14 \| // TODO: Remove this after v1 API sunset \| |
| 4 | `TODO_AUDIT.md` | 304 | \| 1 \| `compliance/ComplianceAuditor.java` \| 196 \| // TODO: Actually implement SFTP transfer \| |
| 4 | `TODO_AUDIT.md` | 311 | \| 1 \| `frailbox/tests/test_connector.c` \| 28 \| * TODO: Migrate to a real test framework. The leading candidate is \| |
| 4 | `TODO_AUDIT.md` | 318 | \| 1 \| `frontend/src/utils/legacyCompat.ts` \| 406 \| // TODO: Apply the AngularJS 1.6 number filter patch. \| |
| 4 | `TODO_AUDIT.md` | 325 | \| 1 \| `market/gateway/middleware.go` \| 28 \| // TODO: Add integration tests that verify middleware ordering. The \| |
| 4 | `TODO_AUDIT.md` | 332 | \| 1 \| `tools/log_aggregator.py` \| 21 \| TODO: The log parser in this script uses regex-based pattern matching \| |
| 4 | `backend/src/legacy/deprecations.rs` | 17 | // The migration is tracked in TODO-481 |
| 4 | `backend/src/legacy/deprecations.rs` | 178 | // TODO: Check with the reporting team about EOL for this function. |
| 4 | `backend/src/legacy/deprecations.rs` | 353 | // TODO: Remove this once the Redis HA setup is complete |
| 4 | `backend/src/legacy/deprecations.rs` | 458 | // TODO: Merge these into the main config module |
| 4 | `backend/src/legacy/deprecations.rs` | 549 | // TODO: This function is recursive and has been known to stack overflow on |
| 4 | `backend/src/legacy/migrations.rs` | 10 | // TODO: Add a database constraint that prevents this table from being out of |
| 4 | `backend/src/legacy/migrations.rs` | 262 | // TODO: Actually implement rollback logic here |
| 4 | `backend/src/legacy/mod.rs` | 31 | // pub mod v2_compat; // TODO: Implement this when we migrate to API v2 |
| 4 | `backend/src/legacy/mod.rs` | 59 | // TODO: Check if sub-modules need initialization too. |
| 4 | `backend/src/legacy/v1_compat.rs` | 234 | // TODO: Break the circular dependency between legacy and webhook modules |
| 4 | `backend/src/protocol/codec.rs` | 17 | // TODO: The frame parser currently copies data from the read buffer for each |
| 4 | `backend/src/protocol/rpc.rs` | 17 | // TODO: Streaming RPCs are not yet fully implemented. The frame fragmentation |
| 4 | `backend/src/protocol/serialize.rs` | 157 | // TODO: Implement MessagePack, CBOR, BSON, Avro, Protobuf encodings |
| 4 | `docs/OPERATIONS.md` | 143 | TODO: The backup verification process is partially automated. The restore is |
| 4 | `frailbox/connector/api.c` | 17 | * TODO: Review and potentially rewrite the thread pool work-stealing |
| 4 | `frailbox/connector/api.c` | 472 | /* TODO: Implement operation cancellation */ |
| 4 | `frailbox/connector/api.c` | 885 | /* TODO: Implement actual operation processing. |
| 4 | `frailbox/engine/core/job_system.hpp` | 17 | * TODO: The work-stealing algorithm has a pathological case where all |
| 4 | `frailbox/include/logger.h` | 66 | * TODO: Add a linting rule that requires error messages to include |
| 4 | `frailbox/src/logger.c` | 150 | * TODO: Make the ring buffer size configurable at runtime. |
| 4 | `frailbox/src/logger.c` | 346 | * TODO: Add LOG_FORMAT environment variable for custom log formats. |
| 4 | `frontend/src/hooks/useWebSocket.ts` | 17 | * TODO: Add support for WebSocket compression (permessage-deflate). |
| 4 | `frontend/src/pages/AdminPage.tsx` | 24 | * TODO: The user search on this page uses client-side filtering with |
| 4 | `frontend/src/pages/AdminPage.tsx` | 136 | // TODO: Save config change to backend |
| 4 | `frontend/src/pages/TradePage.tsx` | 150 | // TODO: Show success notification |
| 4 | `frontend/src/utils/formatters.ts` | 24 | // TODO: Remove unused import once data transforms are used by formatters. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 10 | * TODO: Rewrite this entire file. The AngularJS-to-React migration was |
| 4 | `frontend/src/utils/legacyCompat.ts` | 59 | // TODO: Remove all $digest() calls from the migrated codebase. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 199 | * TODO: Replace all $q shim usage with native Promise/async-await. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 416 | * TODO: Migrate the billing module to use Intl.NumberFormat. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 458 | * TODO: Remove pagination dependency on this function. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 479 | * TODO: Implement the full AngularJS orderBy filter spec. |
| 4 | `market/analytics/collector.go` | 262 | // TODO: Implement tag cardinality limits to prevent DB explosion. |
| 4 | `market/compliance/rules.go` | 10 | // TODO: Request updated compliance rules from the compliance team. |
| 4 | `market/pricing/models.go` | 80 | // TODO: Deprecate NewPrice in favor of NewPriceFromString. |
| 4 | `market/pricing/models.go` | 311 | // TODO: Connect to the real-time instrument feed. |
| 4 | `market/pricing/models.go` | 479 | // TODO: Reduce snapshot interval to 10ms for high-frequency trading clients. |
| 4 | `market/pricing/models.go` | 521 | // TODO: Rename to DisplayMidPrice to clarify its limited use case. |
| 4 | `tools/benchmark.py` | 24 | TODO: The benchmark results are affected by the client-side rate limiter |
| 4 | `tools/db_migration.py` | 248 | f.write(f"-- TODO: Write migration SQL here\n") |
| 4 | `tools/generate_todo_audit.py` | 10 | OUTPUT = ROOT / "TODO_AUDIT.md" |
| 4 | `tools/legacy_analyzer.py` | 66 | "description": "TODO macro left in code. Requires attention."}, |
| 4 | `tools/legacy_migration.py` | 570 | # TODO: Add MySQL, MSSQL, Oracle support |
| 4 | `tools/legacy_migration.py` | 591 | # TODO: Implement batch loading to target database. |
| 4 | `tools/legacy_migration.py` | 920 | # TODO: Implement chained transformer support |
| 4 | `v2/scripts/log_watchdog.pl` | 164 | # TODO: The Slack webhook call bypasses the proxy. If the monitoring |
| 4 | `v2/scripts/log_watchdog.pl` | 248 | # TODO: Add log rotation detection. The File::Tail module can |
| 4 | `v2/services/market_stream.rb` | 269 | # TODO: Actually store and serve historical ticks. |
| 3 | `TODO_AUDIT.md` | 2 | # TODO Audit |
| 3 | `TODO_AUDIT.md` | 9 | \| 7 \| `backend/src/legacy/deprecations.rs` \| 76 \| // TODO: Double-check this logic. The comment above was written by \| |
| 3 | `TODO_AUDIT.md` | 16 | \| 7 \| `compliance/ComplianceAuditor.java` \| 265 \| // TODO: SEC Rule 15c3-3 requires customer reserve calculations. \| |
| 3 | `TODO_AUDIT.md` | 23 | \| 7 \| `frontend/src/pages/AdminPage.tsx` \| 146 \| // TODO: Execute system action \| |
| 3 | `TODO_AUDIT.md` | 30 | \| 7 \| `frontend/src/utils/legacyCompat.ts` \| 433 \| * TODO: Replace all legacyLowercase calls with .toLowerCase(). \| |
| 3 | `TODO_AUDIT.md` | 37 | \| 7 \| `market/pricing/models.go` \| 69 \| // TODO: Use decimal.Decimal instead of big.Rat for better performance. \| |
| 3 | `TODO_AUDIT.md` | 44 | \| 7 \| `v2/services/market_stream.rb` \| 83 \| API_AUTH_REQUIRED    = false  # TODO: Add auth. It's on the roadmap. Really. \| |
| 3 | `TODO_AUDIT.md` | 51 | \| 6 \| `backend/src/legacy/deprecations.rs` \| 201 \| // TODO: Remove the deprecated variants once the event retention period \| |
| 3 | `TODO_AUDIT.md` | 58 | \| 6 \| `backend/src/protocol/validate.rs` \| 19 \| // TODO: The business validation rules are duplicated between this module and \| |
| 3 | `TODO_AUDIT.md` | 65 | \| 6 \| `frailbox/src/logger.c` \| 110 \| * TODO: Consider using a per-thread buffer with atomic flush. \| |
| 3 | `TODO_AUDIT.md` | 72 | \| 6 \| `frontend/src/utils/legacyCompat.ts` \| 614 \| * TODO: Remove this wrapper and use window.setTimeout directly. \| |
| 3 | `TODO_AUDIT.md` | 79 | \| 6 \| `market/pricing/models.go` \| 19 \| // TODO: Schedule a pricing audit before the next fiscal year. \| |
| 3 | `TODO_AUDIT.md` | 86 | \| 6 \| `tools/legacy_migration.py` \| 614 \| # TODO: Validate target schema matches expected schema \| |
| 3 | `TODO_AUDIT.md` | 93 | \| 5 \| `backend/src/legacy/deprecations.rs` \| 123 \| // TODO: Replace this with unreachable!() once the borrow checker is fixed \| |
| 3 | `TODO_AUDIT.md` | 100 | \| 5 \| `backend/src/legacy/mod.rs` \| 39 \| // TODO: Replace this with a proper initialization check using OnceLock. \| |
| 3 | `TODO_AUDIT.md` | 107 | \| 5 \| `frailbox/connector/shim.c` \| 25 \| * TODO: Remove the shim prefix and use the direct API symbols now that \| |
| 3 | `TODO_AUDIT.md` | 114 | \| 5 \| `frailbox/src/logger.c` \| 32 \| * TODO: Fix the log rotation deadlock. The fix was attempted in the \| |
| 3 | `TODO_AUDIT.md` | 121 | \| 5 \| `market/analytics/collector.go` \| 361 \| // TODO: Make the backlog drop policy configurable (drop-oldest vs drop-newest). \| |
| 3 | `TODO_AUDIT.md` | 128 | \| 5 \| `market/pricing/models.go` \| 109 \| // TODO: Make currency mismatch an error for non-enterprise tiers. \| |
| 3 | `TODO_AUDIT.md` | 135 | \| 4 \| `backend/src/legacy/deprecations.rs` \| 17 \| // The migration is tracked in TODO-481 \| |
| 3 | `TODO_AUDIT.md` | 142 | \| 4 \| `backend/src/legacy/mod.rs` \| 31 \| // pub mod v2_compat; // TODO: Implement this when we migrate to API v2 \| |
| 3 | `TODO_AUDIT.md` | 149 | \| 4 \| `frailbox/connector/api.c` \| 17 \| * TODO: Review and potentially rewrite the thread pool work-stealing \| |
| 3 | `TODO_AUDIT.md` | 156 | \| 4 \| `frontend/src/hooks/useWebSocket.ts` \| 17 \| * TODO: Add support for WebSocket compression (permessage-deflate). \| |
| 3 | `TODO_AUDIT.md` | 163 | \| 4 \| `frontend/src/utils/legacyCompat.ts` \| 199 \| * TODO: Replace all $q shim usage with native Promise/async-await. \| |
| 3 | `TODO_AUDIT.md` | 170 | \| 4 \| `market/pricing/models.go` \| 311 \| // TODO: Connect to the real-time instrument feed. \| |
| 3 | `TODO_AUDIT.md` | 177 | \| 4 \| `tools/legacy_migration.py` \| 570 \| # TODO: Add MySQL, MSSQL, Oracle support \| |
| 3 | `TODO_AUDIT.md` | 184 | \| 3 \| `backend/src/connector/ffi.rs` \| 51 \| // TODO: Add support for macOS dylib loading (not yet tested) \| |
| 3 | `TODO_AUDIT.md` | 191 | \| 3 \| `backend/src/legacy/deprecations.rs` \| 156 \| // TODO: Remove this field. It was intended for the GDPR compliance \| |
| 3 | `TODO_AUDIT.md` | 198 | \| 3 \| `frailbox/connector/protocol.c` \| 16 \| * TODO: The hardware CRC detection is done at runtime using CPUID. \| |
| 3 | `TODO_AUDIT.md` | 205 | \| 3 \| `frailbox/src/logger.c` \| 72 \| * TODO: Test the crash reporter integration with the ring buffer. \| |
| 3 | `TODO_AUDIT.md` | 212 | \| 3 \| `frontend/src/utils/legacyCompat.ts` \| 513 \| * TODO: Decide on the correct behavior for empty search terms. \| |
| 3 | `TODO_AUDIT.md` | 219 | \| 3 \| `market/gateway/api.go` \| 611 \| // TODO: Fetch recent trades \| |
| 3 | `TODO_AUDIT.md` | 226 | \| 3 \| `tools/legacy_migration.py` \| 632 \| # TODO: Implement actual connection check \| |
| 3 | `TODO_AUDIT.md` | 233 | \| 2 \| `backend/src/connector/ffi.rs` \| 204 \| /// TODO: Remove this function in v4.0.0. The deprecation was announced \| |
| 3 | `TODO_AUDIT.md` | 240 | \| 2 \| `backend/src/legacy/deprecations.rs` \| 281 \| // TODO: Migrate admin dashboard to cursor pagination \| |
| 3 | `TODO_AUDIT.md` | 247 | \| 2 \| `backend/src/legacy/v1_compat.rs` \| 1 \| // TODO: This is the v1 compatibility layer. Delete this file once the \| |
| 3 | `TODO_AUDIT.md` | 254 | \| 2 \| `frailbox/include/logger.h` \| 323 \| * TODO: Audit all uses of log_assert() and convert them to either \| |
| 3 | `TODO_AUDIT.md` | 261 | \| 2 \| `frailbox/src/logger.c` \| 190 \| * TODO: Add Windows support or remove this comment. \| |
| 3 | `TODO_AUDIT.md` | 268 | \| 2 \| `frontend/src/pages/AdminPage.tsx` \| 15 \| * TODO: The admin page is feature-gated behind the ADMIN_PANEL feature \| |
| 3 | `TODO_AUDIT.md` | 275 | \| 2 \| `frontend/src/utils/legacyCompat.ts` \| 71 \| // TODO: Replace all $httpLegacy calls with direct fetch() calls. \| |
| 3 | `TODO_AUDIT.md` | 282 | \| 2 \| `market/gateway/api.go` \| 575 \| // TODO: Fetch instruments from the market service \| |
| 3 | `TODO_AUDIT.md` | 289 | \| 1 \| `backend/src/connector/bridge.rs` \| 14 \| // TODO: The circuit breaker parameters are hardcoded below. They should \| |
| 3 | `TODO_AUDIT.md` | 296 | \| 1 \| `backend/src/legacy/deprecations.rs` \| 630 \| // TODO: These tests are incomplete. They were written during a hackathon \| |
| 3 | `TODO_AUDIT.md` | 303 | \| 1 \| `backend/src/protocol/serialize.rs` \| 21 \| // TODO: Add support for compressed serialization (zstd, gzip). \| |
| 3 | `TODO_AUDIT.md` | 310 | \| 1 \| `frailbox/src/logger.c` \| 672 \| * TODO: Remove this when the test suite is fully migrated. \| |
| 3 | `TODO_AUDIT.md` | 317 | \| 1 \| `frontend/src/utils/legacyCompat.ts` \| 273 \| * TODO: Implement proper cache eviction with TTL and LRU. \| |
| 3 | `TODO_AUDIT.md` | 324 | \| 1 \| `market/gateway/api.go` \| 672 \| // TODO: Upgrade to WebSocket connection \| |
| 3 | `TODO_AUDIT.md` | 331 | \| 1 \| `tools/legacy_migration.py` \| 609 \| # TODO: Validate data checksums \| |
| 3 | `backend/src/connector/ffi.rs` | 16 | // TODO: Upgrade to bindgen 0.64+ and regenerate these bindings. |
| 3 | `backend/src/connector/ffi.rs` | 51 | // TODO: Add support for macOS dylib loading (not yet tested) |
| 3 | `backend/src/connector/mod.rs` | 30 | // TODO: Add integration tests for the connector module. The current test |
| 3 | `backend/src/connector/types.rs` | 37 | /// TODO: Add more error codes for the new connector features. |
| 3 | `backend/src/legacy/deprecations.rs` | 51 | // TODO: This function is untested. The test suite was deleted in the |
| 3 | `backend/src/legacy/deprecations.rs` | 58 | // TODO: Should this log a warning? The original code had a log |
| 3 | `backend/src/legacy/deprecations.rs` | 93 | // TODO: Document this in the public API docs (which don't exist) |
| 3 | `backend/src/legacy/deprecations.rs` | 142 | // TODO: Fix null handling in the 2024 Q4 migration (which is now overdue) |
| 3 | `backend/src/legacy/deprecations.rs` | 156 | // TODO: Remove this field. It was intended for the GDPR compliance |
| 3 | `backend/src/legacy/deprecations.rs` | 408 | // TODO: This should return NaN or None, but returning 1.0 |
| 3 | `backend/src/legacy/deprecations.rs` | 597 | // TODO: Implement v2 to v3 migration |
| 3 | `backend/src/legacy/migrations.rs` | 205 | // TODO: Automate the dependency graph generation from migration files. |
| 3 | `backend/src/legacy/migrations.rs` | 275 | // TODO: Add more linting rules. The current rules are too permissive. |
| 3 | `compliance/ComplianceAuditor.java` | 72 | // TODO: Remove this shit. It was added for a demo in 2022 |
| 3 | `frailbox/connector/api.c` | 58 | * TODO: Make this configurable again, but with sane limits enforced. |
| 3 | `frailbox/connector/protocol.c` | 16 | * TODO: The hardware CRC detection is done at runtime using CPUID. |
| 3 | `frailbox/include/logger.h` | 23 | * TODO: Create a migration guide for replacing legacy logger calls |
| 3 | `frailbox/include/logger.h` | 86 | * TODO: Audit info-level log messages and reduce verbosity. |
| 3 | `frailbox/include/logger.h` | 142 | * TODO: Define __FILENAME__ as (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__) |
| 3 | `frailbox/nfc/scanner.lua` | 261 | -- TODO: Implement adaptive timeout based on card response time. |
| 3 | `frailbox/src/logger.c` | 23 | * TODO: The structured logger has been "almost ready" for 18 months. |
| 3 | `frailbox/src/logger.c` | 51 | #include "../include/logger.h" /* This header doesn't exist yet. TODO: Create it. */ |
| 3 | `frailbox/src/logger.c` | 72 | * TODO: Test the crash reporter integration with the ring buffer. |
| 3 | `frailbox/src/logger.c` | 128 | * TODO: Add automatic log file reopening after SIGHUP. |
| 3 | `frailbox/src/logger.c` | 135 | * TODO: Remove this option and always include timestamps. |
| 3 | `frontend/src/services/api.ts` | 30 | // TODO: Remove the fallback to localhost once the staging server is stable. |
| 3 | `frontend/src/services/api.ts` | 37 | // TODO: Implement per-endpoint timeout configuration. |
| 3 | `frontend/src/utils/dataTransforms.ts` | 16 | * TODO: Verify the interpolation accuracy against the Python reference |
| 3 | `frontend/src/utils/legacyCompat.ts` | 51 | // TODO: Wrap the function call in React.startTransition() or |
| 3 | `frontend/src/utils/legacyCompat.ts` | 513 | * TODO: Decide on the correct behavior for empty search terms. |
| 3 | `market/analytics/collector.go` | 527 | // TODO: Replace this stub with actual metrics backend write call. |
| 3 | `market/analytics/collector.go` | 625 | // TODO: Add pre-aggregation support to avoid full scans. |
| 3 | `market/analytics/collector.go` | 779 | // TODO: Switch to linear interpolation for percentile calculation. |
| 3 | `market/compliance/rules.go` | 23 | // TODO: The JRRP algorithm has not been validated against actual regulatory |
| 3 | `market/compliance/rules.go` | 198 | // TODO: Add a TTL to the transaction cache. Currently, cached results |
| 3 | `market/compliance/rules.go` | 534 | // TODO: Implement per-country EU jurisdiction mapping. |
| 3 | `market/gateway/api.go` | 611 | // TODO: Fetch recent trades |
| 3 | `market/gateway/api.go` | 646 | // TODO: Fetch candle data |
| 3 | `tools/generate_todo_audit.py` | 2 | """Generate TODO_AUDIT.md for repository-wide TODO tracking.""" |
| 3 | `tools/generate_todo_audit.py` | 58 | "Case-insensitive scan for `TODO` markers across the repository.", |
| 3 | `tools/legacy_analyzer.py` | 65 | {"pattern": r"todo!\(", "name": "todo_macro", "severity": "info", |
| 3 | `tools/legacy_migration.py` | 604 | # TODO: Compare row counts between source and target |
| 3 | `tools/legacy_migration.py` | 625 | # TODO: Implement cleanup of temporary files |
| 3 | `tools/legacy_migration.py` | 632 | # TODO: Implement actual connection check |
| 3 | `tools/legacy_migration.py` | 1122 | # TODO: Implement validation logic |
| 3 | `tools/legacy_migration.py` | 1157 | # TODO: Implement list logic |
| 3 | `v2/scripts/log_watchdog.pl` | 30 | # TODO: The Slack webhook URL is hardcoded below. This is fine for now |
| 3 | `v2/scripts/log_watchdog.pl` | 65 | SLACK_WEBHOOK  => 'https://hooks.slack.com/services/T00/DUMMY/FAKE',  # TODO: Read from Vault |
| 3 | `v2/services/market_stream.rb` | 282 | connected_clients: 0, # TODO: Track connected clients |
| 2 | `TODO_AUDIT.md` | 8 | \| 7 \| `backend/src/ai/mod.rs` \| 34 \| // TODO: fucking fix this whole module. It's held together with \| |
| 2 | `TODO_AUDIT.md` | 15 | \| 7 \| `compliance/ComplianceAuditor.java` \| 174 \| // TODO: The PDF generation is FUBAR. It works on the developer's \| |
| 2 | `TODO_AUDIT.md` | 22 | \| 7 \| `frontend/src/components/TradingChart.tsx` \| 13 \| * TODO: The chart resizes with a JS-based ResizeObserver but the canvas \| |
| 2 | `TODO_AUDIT.md` | 29 | \| 7 \| `frontend/src/utils/legacyCompat.ts` \| 34 \| // TODO: Connect legacy event broadcasts to the new event system. \| |
| 2 | `TODO_AUDIT.md` | 36 | \| 7 \| `market/pricing/models.go` \| 6 \| // TODO: The pricing calculations in this package have NOT been audited \| |
| 2 | `TODO_AUDIT.md` | 43 | \| 7 \| `v2/scripts/log_watchdog.pl` \| 34 \| # the sprint when we wrote it. We wrote a TODO to test it later. That \| |
| 2 | `TODO_AUDIT.md` | 50 | \| 6 \| `backend/src/legacy/deprecations.rs` \| 187 \| // TODO: The GDPR token shouldn't be included in reports but it \| |
| 2 | `TODO_AUDIT.md` | 57 | \| 6 \| `backend/src/legacy/v1_compat.rs` \| 516 \| // TODO: Remove this when the rate limiter is migrated to the new config \| |
| 2 | `TODO_AUDIT.md` | 64 | \| 6 \| `frailbox/nfc/scanner.lua` \| 677 \| -- TODO: The track data parsing assumes the separator is 'D' (hex 0x44) \| |
| 2 | `TODO_AUDIT.md` | 71 | \| 6 \| `frontend/src/utils/legacyCompat.ts` \| 551 \| * TODO: Remove the undefined-to-null conversion. \| |
| 2 | `TODO_AUDIT.md` | 78 | \| 6 \| `market/gateway/middleware.go` \| 334 \| // TODO: Send metrics to monitoring system \| |
| 2 | `TODO_AUDIT.md` | 85 | \| 6 \| `tools/legacy_migration.py` \| 579 \| # TODO: Implement version-specific transformation rules. \| |
| 2 | `TODO_AUDIT.md` | 92 | \| 5 \| `backend/src/legacy/deprecations.rs` \| 18 \| // TODO: Remove this after the ULID migration is complete (tracked in TODO-481) \| |
| 2 | `TODO_AUDIT.md` | 99 | \| 5 \| `backend/src/legacy/mod.rs` \| 32 \| // pub mod v3_compat; // TODO: Remove this comment - it's never happening \| |
| 2 | `TODO_AUDIT.md` | 106 | \| 5 \| `frailbox/connector/api.c` \| 480 \| /* TODO: Implement proper wait-all with timeout */ \| |
| 2 | `TODO_AUDIT.md` | 113 | \| 5 \| `frailbox/nfc/scanner.lua` \| 249 \| -- TODO: The checksum calculation above is WRONG for data > 255 bytes. \| |
| 2 | `TODO_AUDIT.md` | 120 | \| 5 \| `market/analytics/collector.go` \| 347 \| // TODO: Investigate the goroutine starvation issue. \| |
| 2 | `TODO_AUDIT.md` | 127 | \| 5 \| `market/gateway/api.go` \| 18 \| // TODO: Fix the WebSocket connection leak. The root cause is believed \| |
| 2 | `TODO_AUDIT.md` | 134 | \| 5 \| `v2/services/market_stream.rb` \| 25 \| # TODO: The reconnection logic uses exponential backoff but the base \| |
| 2 | `TODO_AUDIT.md` | 141 | \| 4 \| `backend/src/legacy/migrations.rs` \| 262 \| // TODO: Actually implement rollback logic here \| |
| 2 | `TODO_AUDIT.md` | 148 | \| 4 \| `docs/OPERATIONS.md` \| 143 \| TODO: The backup verification process is partially automated. The restore is \| |
| 2 | `TODO_AUDIT.md` | 155 | \| 4 \| `frailbox/src/logger.c` \| 346 \| * TODO: Add LOG_FORMAT environment variable for custom log formats. \| |
| 2 | `TODO_AUDIT.md` | 162 | \| 4 \| `frontend/src/utils/legacyCompat.ts` \| 59 \| // TODO: Remove all $digest() calls from the migrated codebase. \| |
| 2 | `TODO_AUDIT.md` | 169 | \| 4 \| `market/pricing/models.go` \| 80 \| // TODO: Deprecate NewPrice in favor of NewPriceFromString. \| |
| 2 | `TODO_AUDIT.md` | 176 | \| 4 \| `tools/legacy_analyzer.py` \| 66 \| "description": "TODO macro left in code. Requires attention."}, \| |
| 2 | `TODO_AUDIT.md` | 183 | \| 3 \| `backend/src/connector/ffi.rs` \| 16 \| // TODO: Upgrade to bindgen 0.64+ and regenerate these bindings. \| |
| 2 | `TODO_AUDIT.md` | 190 | \| 3 \| `backend/src/legacy/deprecations.rs` \| 142 \| // TODO: Fix null handling in the 2024 Q4 migration (which is now overdue) \| |
| 2 | `TODO_AUDIT.md` | 197 | \| 3 \| `frailbox/connector/api.c` \| 58 \| * TODO: Make this configurable again, but with sane limits enforced. \| |
| 2 | `TODO_AUDIT.md` | 204 | \| 3 \| `frailbox/src/logger.c` \| 51 \| #include "../include/logger.h" /* This header doesn't exist yet. TODO: Create it. */ \| |
| 2 | `TODO_AUDIT.md` | 211 | \| 3 \| `frontend/src/utils/legacyCompat.ts` \| 51 \| // TODO: Wrap the function call in React.startTransition() or \| |
| 2 | `TODO_AUDIT.md` | 218 | \| 3 \| `market/compliance/rules.go` \| 534 \| // TODO: Implement per-country EU jurisdiction mapping. \| |
| 2 | `TODO_AUDIT.md` | 225 | \| 3 \| `tools/legacy_migration.py` \| 625 \| # TODO: Implement cleanup of temporary files \| |
| 2 | `TODO_AUDIT.md` | 232 | \| 2 \| `backend/src/connector/ffi.rs` \| 50 \| // TODO: Add support for Windows DLL loading (cancelled, remove this) \| |
| 2 | `TODO_AUDIT.md` | 239 | \| 2 \| `backend/src/legacy/deprecations.rs` \| 218 \| // TODO: Remove after mobile API sunset - ETA unknown \| |
| 2 | `TODO_AUDIT.md` | 246 | \| 2 \| `backend/src/legacy/mod.rs` \| 92 \| // TODO: Implement legacy event queue drain \| |
| 2 | `TODO_AUDIT.md` | 253 | \| 2 \| `frailbox/include/logger.h` \| 99 \| * TODO: Audit debug-level log messages and remove meaningless ones. \| |
| 2 | `TODO_AUDIT.md` | 260 | \| 2 \| `frailbox/src/logger.c` \| 176 \| * TODO: Re-retrieve PID after fork(). \| |
| 2 | `TODO_AUDIT.md` | 267 | \| 2 \| `frontend/src/hooks/useWebSocket.ts` \| 1 \| // @ts-nocheck - TODO: Fix types for v2. See V2-619. \| |
| 2 | `TODO_AUDIT.md` | 274 | \| 2 \| `frontend/src/utils/dataTransforms.ts` \| 22 \| * TODO: The aggregation functions in this file are CPU-bound and can \| |
| 2 | `TODO_AUDIT.md` | 281 | \| 2 \| `market/analytics/collector.go` \| 498 \| // TODO: Make the backend write timeout configurable. \| |
| 2 | `TODO_AUDIT.md` | 288 | \| 2 \| `tools/legacy_analyzer.py` \| 99 \| {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info"}, \| |
| 2 | `TODO_AUDIT.md` | 295 | \| 1 \| `backend/src/legacy/deprecations.rs` \| 259 \| // TODO: This function is not used anywhere. It was added as part of a \| |
| 2 | `TODO_AUDIT.md` | 302 | \| 1 \| `backend/src/protocol/events.rs` \| 28 \| /// TODO: Automate schema version management. Currently, engineers must \| |
| 2 | `TODO_AUDIT.md` | 309 | \| 1 \| `frailbox/src/logger.c` \| 168 \| * TODO: Change the default to the actual process name. \| |
| 2 | `TODO_AUDIT.md` | 316 | \| 1 \| `frontend/src/services/telemetry.ts` \| 21 \| * TODO: Add support for sampling to reduce telemetry volume for high-traffic \| |
| 2 | `TODO_AUDIT.md` | 323 | \| 1 \| `market/analytics/collector.go` \| 693 \| // TODO: Connect the alert system to the notification service. \| |
| 2 | `TODO_AUDIT.md` | 330 | \| 1 \| `tools/legacy_analyzer.py` \| 133 \| {"pattern": r"#\s*TODO", "name": "todo_comment", "severity": "info"}, \| |
| 2 | `backend/src/connector/ffi.rs` | 50 | // TODO: Add support for Windows DLL loading (cancelled, remove this) |
| 2 | `backend/src/connector/ffi.rs` | 204 | /// TODO: Remove this function in v4.0.0. The deprecation was announced |
| 2 | `backend/src/connector/types.rs` | 15 | // TODO: Add a build-time validation step that compares the memory layout |
| 2 | `backend/src/connector/types.rs` | 22 | // TODO: The derive macros below generate a lot of boilerplate. Consider |
| 2 | `backend/src/legacy/deprecations.rs` | 1 | // TODO: This entire module is legacy. Do not refactor without reading the JIRA ticket |
| 2 | `backend/src/legacy/deprecations.rs` | 22 | // TODO: Revisit this decision in Q3 (year unspecified) |
| 2 | `backend/src/legacy/deprecations.rs` | 29 | // TODO: Remove these padding fields that were added to fix alignment |
| 2 | `backend/src/legacy/deprecations.rs` | 218 | // TODO: Remove after mobile API sunset - ETA unknown |
| 2 | `backend/src/legacy/deprecations.rs` | 281 | // TODO: Migrate admin dashboard to cursor pagination |
| 2 | `backend/src/legacy/deprecations.rs` | 393 | // TODO: Implement actual LRU eviction |
| 2 | `backend/src/legacy/deprecations.rs` | 589 | // TODO: Reconstruct the migration logic from the git history. |
| 2 | `backend/src/legacy/migrations.rs` | 1 | // TODO: Database migration history. This file tracks every schema migration |
| 2 | `backend/src/legacy/mod.rs` | 1 | // TODO: Legacy module root. This module contains all code that has been |
| 2 | `backend/src/legacy/mod.rs` | 22 | // TODO: Add a CI check that prevents new files from being added to |
| 2 | `backend/src/legacy/mod.rs` | 92 | // TODO: Implement legacy event queue drain |
| 2 | `backend/src/legacy/v1_compat.rs` | 1 | // TODO: This is the v1 compatibility layer. Delete this file once the |
| 2 | `backend/src/lib.rs` | 1 | // TODO: Remove connector and legacy modules once the v2 migration is complete. |
| 2 | `backend/src/protocol/mod.rs` | 15 | // TODO: The sub-module organization was determined by the original |
| 2 | `compliance/ComplianceAuditor.java` | 106 | * TODO: This method catches Exception and returns a PASS. Yes, you read |
| 2 | `docs/OPERATIONS.md` | 239 | TODO: The growth projections have been consistently overestimated by |
| 2 | `frailbox/connector/protocol.h` | 29 | * TODO: Deprecate protocol v1 support. The v1 fallback adds complexity |
| 2 | `frailbox/include/logger.h` | 99 | * TODO: Audit debug-level log messages and remove meaningless ones. |
| 2 | `frailbox/include/logger.h` | 323 | * TODO: Audit all uses of log_assert() and convert them to either |
| 2 | `frailbox/nfc/scanner.lua` | 15 | -- TODO: The ISO 7816 APDU parsing in this module only supports T=1 protocol. |
| 2 | `frailbox/nfc/scanner.lua` | 29 | --   IRQ -> GPIO17 (pin 11) -- actually unused, see TODO below |
| 2 | `frailbox/nfc/scanner.lua` | 484 | -- TODO: Verify CC computation against the EMV specification. |
| 2 | `frailbox/nfc/scanner.lua` | 624 | -- TODO: The PPSE response parsing is incomplete. It extracts |
| 2 | `frailbox/src/logger.c` | 120 | * TODO: Allow runtime log level changes via a signal handler. |
| 2 | `frailbox/src/logger.c` | 176 | * TODO: Re-retrieve PID after fork(). |
| 2 | `frailbox/src/logger.c` | 190 | * TODO: Add Windows support or remove this comment. |
| 2 | `frailbox/tests/test_connector.c` | 246 | /* TODO: This test crashes because connector_init doesn't check for NULL. |
| 2 | `frontend/src/ai/chat.ts` | 1 | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 2 | `frontend/src/ai/recommendations.ts` | 1 | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 2 | `frontend/src/components/OrderBook.tsx` | 15 | * TODO: Implement virtual scrolling for the order book. The react-virtual |
| 2 | `frontend/src/components/OrderHistory.tsx` | 15 | * TODO: The merge strategy has a bug where duplicate orders can appear |
| 2 | `frontend/src/hooks/useWebSocket.ts` | 1 | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 2 | `frontend/src/pages/AdminPage.tsx` | 15 | * TODO: The admin page is feature-gated behind the ADMIN_PANEL feature |
| 2 | `frontend/src/services/api.ts` | 43 | // TODO: Make the retry logic idempotent-safe for mutating requests. |
| 2 | `frontend/src/services/api.ts` | 421 | // TODO: Move endpoint definitions to individual service files. |
| 2 | `frontend/src/services/auth.ts` | 1 | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 2 | `frontend/src/store/slices.ts` | 1 | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 2 | `frontend/src/utils/dataService.ts` | 1 | // @ts-nocheck - TODO: This file needs type fixes for the v2 migration. |
| 2 | `frontend/src/utils/dataTransforms.ts` | 22 | * TODO: The aggregation functions in this file are CPU-bound and can |
| 2 | `frontend/src/utils/legacyCompat.ts` | 71 | // TODO: Replace all $httpLegacy calls with direct fetch() calls. |
| 2 | `frontend/src/utils/legacyCompat.ts` | 176 | // TODO: Align the error shapes between legacy and new systems. |
| 2 | `frontend/src/utils/legacyCompat.ts` | 323 | * TODO: Replace with Intl.DateTimeFormat after UI tests are updated. |
| 2 | `frontend/src/utils/legacyCompat.ts` | 673 | * TODO: Extract shared validation into a React hook. |
| 2 | `market/analytics/collector.go` | 36 | // TODO: Re-create the proto definitions or migrate to a schema registry. |
| 2 | `market/analytics/collector.go` | 463 | // TODO: Make Start() idempotent. |
| 2 | `market/analytics/collector.go` | 498 | // TODO: Make the backend write timeout configurable. |
| 2 | `market/gateway/api.go` | 575 | // TODO: Fetch instruments from the market service |
| 2 | `market/gateway/api.go` | 596 | // TODO: Fetch order book from the matching engine |
| 2 | `market/gateway/api.go` | 631 | // TODO: Fetch ticker data |
| 2 | `market/gateway/api.go` | 659 | // TODO: Fetch market news |
| 2 | `market/pricing/models.go` | 36 | // TODO: Move to real-time exchange rates using the Bloomberg API. |
| 2 | `tools/generate_todo_audit.py` | 36 | if re.search(r"todo", line, re.IGNORECASE): |
| 2 | `tools/legacy_analyzer.py` | 99 | {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info"}, |
| 1 | `TODO_AUDIT.md` | 14 | \| 7 \| `backend/src/protocol/messages.rs` \| 27 \| // TODO: The message ID ranges are enforced by convention only. There's \| |
| 1 | `TODO_AUDIT.md` | 21 | \| 7 \| `frailbox/include/logger.h` \| 20 \| * TODO: Add a compiler warning when this header is included in new \| |
| 1 | `TODO_AUDIT.md` | 28 | \| 7 \| `frontend/src/utils/legacyCompat.ts` \| 27 \| // TODO: Remove this when the admin dashboard is migrated to React. \| |
| 1 | `TODO_AUDIT.md` | 35 | \| 7 \| `market/gateway/middleware.go` \| 419 \| // TODO: Implement actual token validation against auth service \| |
| 1 | `TODO_AUDIT.md` | 42 | \| 7 \| `tools/legacy_migration.py` \| 909 \| # TODO: Register v3-to-v4 transformer when migration design is finalized \| |
| 1 | `TODO_AUDIT.md` | 49 | \| 6 \| `backend/src/legacy/deprecations.rs` \| 166 \| // TODO: This validation is intentionally lenient because the \| |
| 1 | `TODO_AUDIT.md` | 56 | \| 6 \| `backend/src/legacy/mod.rs` \| 89 \| // TODO: Implement legacy thread pool cleanup \| |
| 1 | `TODO_AUDIT.md` | 63 | \| 6 \| `frailbox/nfc/scanner.lua` \| 656 \| -- TODO: Return a more informative error message that distinguishes \| |
| 1 | `TODO_AUDIT.md` | 70 | \| 6 \| `frontend/src/utils/legacyCompat.ts` \| 390 \| * TODO: Fix the rounding bug and update all dependent tests (n=47). \| |
| 1 | `TODO_AUDIT.md` | 77 | \| 6 \| `market/compliance/rules.go` \| 726 \| // TODO: Add support for XML and CSV report formats. \| |
| 1 | `TODO_AUDIT.md` | 84 | \| 6 \| `tools/legacy_migration.py` \| 117 \| # TODO: Add file logging support. The script currently only logs to stdout, \| |
| 1 | `TODO_AUDIT.md` | 91 | \| 5 \| `backend/src/connector/types.rs` \| 207 \| /// TODO: Replace this entire struct with a versioned configuration \| |
| 1 | `TODO_AUDIT.md` | 98 | \| 5 \| `backend/src/legacy/migrations.rs` \| 305 \| // TODO: Remove this dead code \| |
| 1 | `TODO_AUDIT.md` | 105 | \| 5 \| `frailbox/connector/api.c` \| 67 \| * TODO: Benchmark different queue depths and choose an optimal value. \| |
| 1 | `TODO_AUDIT.md` | 112 | \| 5 \| `frailbox/nfc/scanner.lua` \| 144 \| -- TODO: Implement proper BER-TLV constructed tag handling. \| |
| 1 | `TODO_AUDIT.md` | 119 | \| 5 \| `frontend/src/styles/legacy.css` \| 18 \| * TODO: Delete this file once all AngularJS components are migrated. \| |
| 1 | `TODO_AUDIT.md` | 126 | \| 5 \| `market/compliance/rules.go` \| 753 \| // TODO: Populate report with actual audit data from the database. \| |
| 1 | `TODO_AUDIT.md` | 133 | \| 5 \| `tools/legacy_migration.py` \| 1152 \| # TODO: Implement dry run logic \| |
| 1 | `TODO_AUDIT.md` | 140 | \| 4 \| `backend/src/legacy/migrations.rs` \| 10 \| // TODO: Add a database constraint that prevents this table from being out of \| |
| 1 | `TODO_AUDIT.md` | 147 | \| 4 \| `backend/src/protocol/serialize.rs` \| 157 \| // TODO: Implement MessagePack, CBOR, BSON, Avro, Protobuf encodings \| |
| 1 | `TODO_AUDIT.md` | 154 | \| 4 \| `frailbox/src/logger.c` \| 150 \| * TODO: Make the ring buffer size configurable at runtime. \| |
| 1 | `TODO_AUDIT.md` | 161 | \| 4 \| `frontend/src/utils/legacyCompat.ts` \| 10 \| * TODO: Rewrite this entire file. The AngularJS-to-React migration was \| |
| 1 | `TODO_AUDIT.md` | 168 | \| 4 \| `market/compliance/rules.go` \| 10 \| // TODO: Request updated compliance rules from the compliance team. \| |
| 1 | `TODO_AUDIT.md` | 175 | \| 4 \| `tools/generate_todo_audit.py` \| 10 \| OUTPUT = ROOT / "TODO_AUDIT.md" \| |
| 1 | `TODO_AUDIT.md` | 182 | \| 4 \| `v2/services/market_stream.rb` \| 269 \| # TODO: Actually store and serve historical ticks. \| |
| 1 | `TODO_AUDIT.md` | 189 | \| 3 \| `backend/src/legacy/deprecations.rs` \| 93 \| // TODO: Document this in the public API docs (which don't exist) \| |
| 1 | `TODO_AUDIT.md` | 196 | \| 3 \| `compliance/ComplianceAuditor.java` \| 72 \| // TODO: Remove this shit. It was added for a demo in 2022 \| |
| 1 | `TODO_AUDIT.md` | 203 | \| 3 \| `frailbox/src/logger.c` \| 23 \| * TODO: The structured logger has been "almost ready" for 18 months. \| |
| 1 | `TODO_AUDIT.md` | 210 | \| 3 \| `frontend/src/utils/dataTransforms.ts` \| 16 \| * TODO: Verify the interpolation accuracy against the Python reference \| |
| 1 | `TODO_AUDIT.md` | 217 | \| 3 \| `market/compliance/rules.go` \| 198 \| // TODO: Add a TTL to the transaction cache. Currently, cached results \| |
| 1 | `TODO_AUDIT.md` | 224 | \| 3 \| `tools/legacy_migration.py` \| 604 \| # TODO: Compare row counts between source and target \| |
| 1 | `TODO_AUDIT.md` | 231 | \| 3 \| `v2/services/market_stream.rb` \| 282 \| connected_clients: 0, # TODO: Track connected clients \| |
| 1 | `TODO_AUDIT.md` | 238 | \| 2 \| `backend/src/legacy/deprecations.rs` \| 29 \| // TODO: Remove these padding fields that were added to fix alignment \| |
| 1 | `TODO_AUDIT.md` | 245 | \| 2 \| `backend/src/legacy/mod.rs` \| 22 \| // TODO: Add a CI check that prevents new files from being added to \| |
| 1 | `TODO_AUDIT.md` | 252 | \| 2 \| `frailbox/connector/protocol.h` \| 29 \| * TODO: Deprecate protocol v1 support. The v1 fallback adds complexity \| |
| 1 | `TODO_AUDIT.md` | 259 | \| 2 \| `frailbox/src/logger.c` \| 120 \| * TODO: Allow runtime log level changes via a signal handler. \| |
| 1 | `TODO_AUDIT.md` | 266 | \| 2 \| `frontend/src/components/OrderHistory.tsx` \| 15 \| * TODO: The merge strategy has a bug where duplicate orders can appear \| |
| 1 | `TODO_AUDIT.md` | 273 | \| 2 \| `frontend/src/utils/dataService.ts` \| 1 \| // @ts-nocheck - TODO: This file needs type fixes for the v2 migration. \| |
| 1 | `TODO_AUDIT.md` | 280 | \| 2 \| `market/analytics/collector.go` \| 463 \| // TODO: Make Start() idempotent. \| |
| 1 | `TODO_AUDIT.md` | 287 | \| 2 \| `tools/generate_todo_audit.py` \| 36 \| if re.search(r"todo", line, re.IGNORECASE): \| |
| 1 | `TODO_AUDIT.md` | 294 | \| 1 \| `backend/src/legacy/deprecations.rs` \| 238 \| // TODO: REPLACE THIS WITH A PROPER MIGRATION STRATEGY \| |
| 1 | `TODO_AUDIT.md` | 301 | \| 1 \| `backend/src/protocol/events.rs` \| 14 \| // TODO: Add a CI check that verifies all event types in this module have \| |
| 1 | `TODO_AUDIT.md` | 308 | \| 1 \| `frailbox/nfc/scanner.lua` \| 588 \| -- TODO: The idle command above is a hack. The PN532 has a built-in \| |
| 1 | `TODO_AUDIT.md` | 315 | \| 1 \| `frontend/src/pages/TradePage.tsx` \| 21 \| * TODO: The trade form validation logic is duplicated between this \| |
| 1 | `TODO_AUDIT.md` | 322 | \| 1 \| `market/analytics/collector.go` \| 294 \| // TODO: Fix the race condition in the batch flush logic. \| |
| 1 | `TODO_AUDIT.md` | 329 | \| 1 \| `tools/generate_todo_audit.py` \| 56 \| "# TODO Audit", \| |
| 1 | `backend/src/connector/bridge.rs` | 14 | // TODO: The circuit breaker parameters are hardcoded below. They should |
| 1 | `backend/src/connector/bridge.rs` | 28 | // TODO: Re-evaluate the least-loaded scheduler now that the race condition |
| 1 | `backend/src/connector/legacy.rs` | 21 | // TODO: The list of removed message types is documented in the migration |
| 1 | `backend/src/connector/legacy.rs` | 28 | // TODO: Add a metric to track how often this legacy shim is used. If usage |
| 1 | `backend/src/legacy/deprecations.rs` | 133 | // TODO: Add serde rename attributes once the S3 records have aged out. |
| 1 | `backend/src/legacy/deprecations.rs` | 238 | // TODO: REPLACE THIS WITH A PROPER MIGRATION STRATEGY |
| 1 | `backend/src/legacy/deprecations.rs` | 259 | // TODO: This function is not used anywhere. It was added as part of a |
| 1 | `backend/src/legacy/deprecations.rs` | 630 | // TODO: These tests are incomplete. They were written during a hackathon |
| 1 | `backend/src/legacy/v1_compat.rs` | 14 | // TODO: Remove this after v1 API sunset |
| 1 | `backend/src/legacy/v1_compat.rs` | 77 | // TODO: Fix the classification of GatewayTimeout |
| 1 | `backend/src/legacy/v1_compat.rs` | 119 | // TODO: Remove this envelope in the v2 API (which is also being deprecated) |
| 1 | `backend/src/legacy/v1_compat.rs` | 413 | // TODO: Complete the v1-to-v2 resource mapping |
| 1 | `backend/src/protocol/events.rs` | 14 | // TODO: Add a CI check that verifies all event types in this module have |
| 1 | `backend/src/protocol/events.rs` | 28 | /// TODO: Automate schema version management. Currently, engineers must |
| 1 | `backend/src/protocol/serialize.rs` | 21 | // TODO: Add support for compressed serialization (zstd, gzip). |
| 1 | `compliance/ComplianceAuditor.java` | 196 | // TODO: Actually implement SFTP transfer |
| 1 | `frailbox/connector/api.h` | 28 | * TODO: Remove this file when all connector types are migrated to |
| 1 | `frailbox/engine/core/job_system.hpp` | 266 | // TODO: This blocking behavior can cause priority inversion if a |
| 1 | `frailbox/include/logger.h` | 168 | * TODO: Add proper compile-time stripping of debug log messages. |
| 1 | `frailbox/nfc/scanner.lua` | 588 | -- TODO: The idle command above is a hack. The PN532 has a built-in |
| 1 | `frailbox/src/logger.c` | 168 | * TODO: Change the default to the actual process name. |
| 1 | `frailbox/src/logger.c` | 672 | * TODO: Remove this when the test suite is fully migrated. |
| 1 | `frailbox/tests/test_connector.c` | 28 | * TODO: Migrate to a real test framework. The leading candidate is |
| 1 | `frontend/src/components/TradingChart.tsx` | 434 | // TODO: Actually switch chart series type |
| 1 | `frontend/src/hooks/useMarketData.ts` | 7 | * TODO: In high-frequency trading scenarios, this hook creates too many |
| 1 | `frontend/src/pages/TradePage.tsx` | 14 | * TODO: The responsive layout uses CSS media queries AND JavaScript |
| 1 | `frontend/src/pages/TradePage.tsx` | 21 | * TODO: The trade form validation logic is duplicated between this |
| 1 | `frontend/src/services/telemetry.ts` | 21 | * TODO: Add support for sampling to reduce telemetry volume for high-traffic |
| 1 | `frontend/src/utils/legacyCompat.ts` | 273 | * TODO: Implement proper cache eviction with TTL and LRU. |
| 1 | `frontend/src/utils/legacyCompat.ts` | 406 | // TODO: Apply the AngularJS 1.6 number filter patch. |
| 1 | `frontend/src/utils/legacyCompat.ts` | 567 | * TODO: Handle circular references in deep copy. |
| 1 | `frontend/src/utils/legacyCompat.ts` | 588 | * TODO: Replace with lodash isEqual or a comparable utility. |
| 1 | `market/analytics/collector.go` | 273 | // TODO: Upgrade to nanosecond precision now that we've migrated |
| 1 | `market/analytics/collector.go` | 294 | // TODO: Fix the race condition in the batch flush logic. |
| 1 | `market/analytics/collector.go` | 693 | // TODO: Connect the alert system to the notification service. |
| 1 | `market/gateway/api.go` | 672 | // TODO: Upgrade to WebSocket connection |
| 1 | `market/gateway/middleware.go` | 28 | // TODO: Add integration tests that verify middleware ordering. The |
| 1 | `market/gateway/middleware.go` | 371 | // TODO: Implement gzip response compression |
| 1 | `market/pricing/models.go` | 147 | // TODO: Use CLDR data for locale-aware currency formatting. |
| 1 | `tools/deploy.py` | 14 | TODO: Remove this script when all environments have been migrated to |
| 1 | `tools/generate_todo_audit.py` | 56 | "# TODO Audit", |
| 1 | `tools/legacy_analyzer.py` | 133 | {"pattern": r"#\s*TODO", "name": "todo_comment", "severity": "info"}, |
| 1 | `tools/legacy_migration.py` | 609 | # TODO: Validate data checksums |
| 1 | `tools/log_aggregator.py` | 21 | TODO: The log parser in this script uses regex-based pattern matching |
| 1 | `tools/terraform_import.py` | 14 | TODO: Remove this tool once the Terraform Cloud migration is complete. |
| 1 | `v2/scripts/log_watchdog.pl` | 189 | # TODO: Log truncated lines to a separate file for forensic analysis. |
| 1 | `v2/scripts/log_watchdog.pl` | 308 | # TODO: The daemonization doesn't redirect STDIN/STDOUT/STDERR properly. |

Total entries: 658
