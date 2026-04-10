# AGENTS.md

Project: gurufin-gitbook
Type: gitbook

## Navigation

**SUMMARY.md is the master table of contents.** Always read it first.
It defines every page and its position in the book.

## Structure

### Root files
- `Gurufin_OPRS_Architecture.pdf`
- `Gurufin_OPRS_Architecture_v2.html`
- `Gurufin_OPRS_Architecture_v2.pdf`
- `combined-pdf-content.md`
- `.gitbook.yaml`
- `.gitignore`
- `README.md`
- `STRUCTURE.md`
- `SUMMARY.md`
- `book.json`
- `developer_resource.json`
- `gurufin-oprs-architecture.html`
- `gurufin_chain_whitepaper.md`
- `gx_chain_litepaper.md`
- `pdf-outline.md`
- `pdf-style.css`
- `project_purpose.md`

### .gitbook/
- `.gitbook/assets/Gemini_Generated_Image_iljs2xiljs2xiljs.jpg`

### developer_resources/
- `developer_resources/01_testnet_access.md`
- `developer_resources/02_api_reference.md`
- `developer_resources/03_full_developer_docs.md`
- `developer_resources/04_ecosystem_grant_program.md`

### gurudex/
- `gurudex/01_dex_overview.md`
- `gurudex/02_hybrid_pools.md`
- `gurudex/03_liquidity_and_rewards.md`
- `gurudex/04_smart_contract_logic.md`
- `gurudex/05_risk_mitigation.md`

### gurufin_chain/
- `gurufin_chain/gurufin_chain_whitepaper.md`
- `gurufin_chain/01_protocol_overview.md`
- `gurufin_chain/02_network_architecture.md`
- `gurufin_chain/03_interoperability.md`
- `gurufin_chain/04_guru_peg.md`
- `gurufin_chain/05_tokenomics.md`
- `gurufin_chain/06_governance.md`
- `gurufin_chain/07_validator_guide.md`

### gx_chain/
- `gx_chain/01_overview.md`
- `gx_chain/02_reserve_and_backing.md`
- `gx_chain/03_mint_and_burn.md`
- `gx_chain/04_multi_currency_support.md`
- `gx_chain/05_compliance_and_regulation.md`

### introduction/
- `introduction/01_vision_mission.md`
- `introduction/02_what_is_gurufin.md`
- `introduction/03_roadmap.md`

### pdf-sections/
- `pdf-sections/00-title.md`
- `pdf-sections/01-executive-summary.md`
- `pdf-sections/02-introduction.md`
- `pdf-sections/03-oprs-architecture.md`
- `pdf-sections/04-liquidity-market.md`
- `pdf-sections/05-smart-contracts.md`
- `pdf-sections/06-risk-mitigation.md`
- `pdf-sections/07-use-cases.md`
- `pdf-sections/08-developer-resources.md`
- `pdf-sections/09-conclusion.md`
- `pdf-sections/10-glossary.md`

### use_cases/
- `use_cases/01_cross_border_payments.md`
- `use_cases/02_stablecoin_fx_trading.md`
- `use_cases/03_institutional_defi.md`
- `use_cases/04_government_and_cbdc.md`

## How To Make Changes

1. Read SUMMARY.md to understand where target content sits in the book
2. If changing a concept, grep across ALL .md files — docs cross-reference each other
3. After editing any doc, check if SUMMARY.md needs updating
4. Files with `-legacy` in the name are outdated — prefer new files over editing them

## Conventions

- README heading: Gurufin Documentation
- SUMMARY.md defines the sidebar navigation
- Cross-references use relative markdown links
- Legacy docs are suffixed with `-legacy` in filename
