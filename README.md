\# UniAttack: A Unified Fusion-Based Framework for Evaluating Defensive Weaknesses in LLMs



This repository contains the official artifacts for the paper:  

\*\*"\[Full Paper Title]"\*\* (Submitted to USENIX Security 2026).



---



\## 1. Overview

This artifact provides the implementation of `UniAttack`, a framework designed to identify and evaluate structural vulnerabilities in LLM safety mechanisms through feature extraction and template fusion.



\### Core Components:

\- \*\*Feature \& Template Engine\*\*: Logic for analyzing attack vectors and generating high-quality adversarial templates.

\- \*\*Library of Assets\*\*: A systematic collection of effective attack features and seed templates.

\- \*\*Experimental Results\*\*: Comprehensive raw data comparing UniAttack with four state-of-the-art baselines.

\- \*\*Quick-Start Package\*\*: A streamlined environment for rapid reproduction and sample inspection.



---



\## 2. Ethical Statement \& Safety Note

This repository is provided strictly for academic peer-review and defensive research purposes. 

\- \*\*De-sensitization\*\*: The "Template \& Seed Library" has been sanitized by replacing all harmful payloads with `{user\_input/query}` placeholders.

\- \*\*Harmful Content Warning\*\*: Some files in the `quick\_start` and `data/advbench\_txt` directories contain raw adversarial queries from the public AdvBench dataset. These are necessary for evaluating Attack Success Rate (ASR) but should be handled with caution.

\- \*\*Responsible Use\*\*: We emphasize that this framework is intended to help model providers harden their "reasoning-aware" defenses.



---



\## 3. Project Structure

```text

tool\_artifact/

├── code/                    # Core scripts for extraction and generation

├── data/                    # Libraries and external datasets

│   ├── advbench\_txt/        # Harmful query dataset (Public baseline)

│   ├── uniattack\_features/  # Feature collection (features.txt)

│   └── uniattack\_templates/ # Sanitized template and seed library

├── quick\_start/             # Minimal environment for rapid reproduction

│   ├── run\_demo.py          # Full workflow demo (with detection)

│   ├── run\_without\_detect.py # Attack-only demo

│   ├── sample/              # Sample prompt-response and evaluation results

│   └── \*\_trans\_to\_json.py   # Format conversion utilities

├── results/                 # Raw experimental data for paper reproduction

│   ├── baseline/            # Results of 4 baseline methods

│   │   ├── pair/

│   │   ├── deepinception/

│   │   ├── llm-fuzzer/

│   │   └── cipher/

│   └── uniattack/           # Our framework's results

├── LICENSE                  # MIT License (Anonymous)

├── requirements.txt         # Dependency specifications

└── README.md                # This documentation

