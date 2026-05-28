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

### .concept_graph/
- `.concept_graph/graph.json`

### .gitbook/
- `.gitbook/assets/Gemini_Generated_Image_iljs2xiljs2xiljs.jpg`

### docs/
- `docs/SUMMARY.md`
- `docs/developer_resources/01_testnet_access.md`
- `docs/developer_resources/02_api_reference.md`
- `docs/developer_resources/03_full_developer_docs.md`
- `docs/gurufin_chain/01_protocol_overview.md`
- `docs/gurufin_chain/02_network_architecture.md`
- `docs/gurufin_chain/03_interoperability.md`
- `docs/gurufin_chain/04_guru_peg.md`
- `docs/gurufin_chain/05_tokenomics.md`
- `docs/gurufin_chain/06_governance.md`
- ... and 14 more files

### pr-drafts/
- `pr-drafts/01_주권안디지털통화_안정적_미래.md`
- `pr-drafts/02_스테이블코인_규제_동향_글로벌_표준_논의.md`
- `pr-drafts/03_온체인_환전_다국적_디지털경제의필수조건.md`
- `pr-drafts/04_주권_디지털통화_신흥국_금융주권.md`
- `pr-drafts/05_스테이블코인과_CBD_CBDvs스테이블코인.md`
- `pr-drafts/06_주권스테이블코인_미래_금융_인프라.md`
- `pr-drafts/07_다국적_디지털경제_통화_환전의_변화.md`
- `pr-drafts/08_신흥국_스테이블코인_금융포용성.md`
- `pr-drafts/09_Gurufin_그루핀_온체인_FX_해결_접근.md`
- `pr-drafts/10_온체인_FX_금융_미래_변화_예측.md`
- `pr-drafts/gurufin-pr-drafts-all.pdf`

## How To Make Changes

1. Read SUMMARY.md to understand where target content sits in the book
2. If changing a concept, grep across ALL .md files — docs cross-reference each other
3. After editing any doc, check if SUMMARY.md needs updating
4. Files with `-legacy` in the name are outdated — prefer new files over editing them

## Conventions

- SUMMARY.md defines the sidebar navigation
- Cross-references use relative markdown links
- Legacy docs are suffixed with `-legacy` in filename
