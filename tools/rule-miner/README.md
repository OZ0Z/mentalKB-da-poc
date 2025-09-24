# Rule Miner (Java → Docassemble)

Purpose: inventory rule sites in the legacy Java code so we can map them to Docassemble patterns and track parity.

## Inputs
- Path to the Java sources (e.g., `../nlghten-master`).
- Optional: compiled classes/JARs if decompilation is needed.

## Outputs
- `sample-output/rules.csv` containing rows with columns: `kind,scope,target,inputs,condition_snippet,file,line`.

## Quick start (grep-only)
```bash
cd tools/rule-miner
./mine.sh ../nlghten-master > sample-output/rules.csv
```

## Rich parse (optional)
```bash
pip install javalang
python mine.py ../nlghten-master > sample-output/rules.csv
```

## What we look for
- Visibility / gating (`setVisible`, `show`, `hide`)
- Branching / navigation (`next`, `previous`, `route`, `switch`)
- Validation (`required`, `validate`, `error`, regex usage)
- Computed values (`equals`, `compareTo`, date comparisons)
- Repeatables (`add`, `[i]`, list operations)
- Dynamic options (`options`, `lookup`, `filter`)
- Localization (`_es`, `_pt`, phrase helpers)

Commit the resulting CSV (or summaries) to keep rule coverage inspectable per PR.
