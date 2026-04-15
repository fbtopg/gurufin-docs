# AGENTS.md

Project: gurufin-gitbook
Type: gitbook

## Navigation

**SUMMARY.md is the master table of contents.** Always read it first.
It defines every page and its position in the book.

## Structure

### Root files
- `.gitignore`
- `SUMMARY.md`
- `_sidebar.json`
- `gurufin-x-posts.md`

### .concept_graph/
- `.concept_graph/graph.json`

### .gitbook/
- `.gitbook/assets/Gemini_Generated_Image_iljs2xiljs2xiljs.jpg`

### docs/
- `docs/developer_resources/01_testnet_access.md`
- `docs/developer_resources/02_api_reference.md`
- `docs/developer_resources/03_full_developer_docs.md`
- `docs/developer_resources/04_ecosystem_grant_program.md`
- `docs/gurudex/01_dex_overview.md`
- `docs/gurudex/02_hybrid_pools.md`
- `docs/gurudex/03_liquidity_and_rewards.md`
- `docs/gurudex/04_smart_contract_logic.md`
- `docs/gurudex/05_risk_mitigation.md`
- `docs/gurufin_chain/01_protocol_overview.md`
- ... and 18 more files

## How To Make Changes

1. Read SUMMARY.md to understand where target content sits in the book
2. If changing a concept, grep across ALL .md files — docs cross-reference each other
3. After editing any doc, check if SUMMARY.md needs updating
4. Files with `-legacy` in the name are outdated — prefer new files over editing them

## Conventions

- SUMMARY.md defines the sidebar navigation
- Cross-references use relative markdown links
- Legacy docs are suffixed with `-legacy` in filename
