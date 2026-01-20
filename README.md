# UniAttack: A Unified Fusion-Based Framework for Evaluating Defensive Weaknesses in LLMs

This repository contains the official artifacts for the paper:  
**"[UNIATTACK: A Uniformed Fusion-Based Framework for Evaluating Defensive
Weaknesses in LLMs]"** (Submitted to USENIX Security 2026).

---

## 1. Overview
This artifact provides the implementation of `UniAttack`, a framework designed to identify and evaluate structural vulnerabilities in LLM safety mechanisms through feature extraction and template fusion.

### Core Components:
- **Feature & Template Engine**: Logic for analyzing attack vectors and generating high-quality adversarial templates.
- **Library of Assets**: A systematic collection of effective attack features and seed templates.
- **Experimental Results**: Comprehensive raw data comparing UniAttack with four state-of-the-art baselines. **Note**: If you prefer not to run the full `quick-start` package, you can directly inspect the representative experimental logs and results provided in the `results.7z` archive.
- **Quick-Start Package**: A streamlined environment for rapid reproduction and sample inspection.

---

## 2. Ethical Statement & Safety Note
This repository is provided strictly for academic peer-review and defensive research purposes. 

- **De-sensitization**: The "Template & Seed Library" has been sanitized by replacing all harmful payloads with `{user_input/query}` placeholders.
- **Harmful Content Warning**: Some files in the `quick_start` and `data/advbench_txt` directories contain raw adversarial queries from the public AdvBench dataset. These are necessary for evaluating Attack Success Rate (ASR) but should be handled with caution.
- **Controlled Access to Results**: To prevent potential misuse of harmful content, we have uploaded a selection of **representative results** rather than the entire raw dataset. These files (especially prompt-response logs) are stored in a password-protected archive: `results.7z`. 
- **Password Access**: The decryption password is provided in the **"Open Science"** section of our submitted paper. This ensures that detailed adversarial logs are accessible only to authorized peer-reviewers, effectively eliminating the risk of public abuse.
- **Technical Note**: We recommend using [7-Zip](https://www.7-zip.org/) (Windows), [Keka](https://www.keka.io/) (macOS), or `p7zip` (Linux) to extract the `.7z` archive.
- **Responsible Use**: We emphasize that this framework is intended to help model providers harden their "reasoning-aware" defenses.

---

## 3. Project Structure
```text
tool_artifact/
├── code/                    # Core scripts for extraction and generation
├── data/                    # Libraries and external datasets
│   ├── advbench_txt/        # Harmful query dataset (Public baseline)
│   ├── uniattack_features/  # Feature collection (features.txt)
│   └── uniattack_templates/ # Sanitized template and seed library
├── quick_start/             # Minimal environment for rapid reproduction
│   ├── run_demo.py          # Full workflow demo (with detection)
│   ├── run_without_detect.py # Attack-only demo
│   ├── sample/              # Sample prompt-response and evaluation results
│   └── *_trans_to_json.py   # Format conversion utilities
├── results/                 # Raw experimental data (Password Protected)
│   ├── baseline/            # Results of 4 baseline methods (pair, deepinception, etc.)
│   └── uniattack/           # Our framework's representative results
├── LICENSE                  # MIT License (Anonymous)
├── requirements.txt         # Dependency specifications
└── README.md                # This documentation


