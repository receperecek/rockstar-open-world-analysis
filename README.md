# Rockstar’s Open-World Shift: From San Andreas to GTA IV in the Context of 2007 Games

## Research question

How did Rockstar change the open-world experience from Grand Theft Auto: San Andreas to Grand Theft Auto IV, and on which documented dimensions did GTA IV distinguish itself from selected 2007 open-world games?

## Scope

This project compares:

- Grand Theft Auto: San Andreas (original PlayStation 2 release as the reference version)
- Grand Theft Auto IV (original base game on PlayStation 3/Xbox 360)
- Crackdown (2007)
- Assassin’s Creed (2007)

The analysis is anchored in a source register, metric definitions, and reproducible data processing; later remasters, ports, and expansion content are excluded unless needed to explain a limitation.

## Key findings

- The project treats all hypotheses as provisional. Evidence supports the view that GTA IV was a major technical and stylistic shift from San Andreas, especially in its urban design, mission structure, and animation/physics emphasis.
- San Andreas remains comparatively broader in state-scale travel and activity variety, while GTA IV is described in contemporary review evidence as more grounded and socially integrated around Liberty City.
- In 2007, GTA IV distinguished itself from Crackdown and Assassin’s Creed primarily on city-scale density, narrative integration, and the interaction layer of vehicles, pedestrians, and mission logic rather than on pure mission count alone.
- The comparison is limited by platform generation, different design goals, and the fact that open-world games in 2007 differed in structure and genre emphasis.

## Methods

1. Assemble a source register with URL, publication date, source type, and reliability notes.
2. Use a rule-based mission catalogue for main story missions and a separate catalogue for optional missions and activities.
3. Code primary mechanics into mutually exclusive categories and track secondary tags.
4. Build feature matrices using only clearly shared dimensions.
5. Generate deterministic tables and figures from the processed data.

## Setup on Windows

```powershell
cd rockstar-open-world-analysis
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pytest -q
python src/build_project.py
```

## Repository structure

- data/raw/
- data/processed/
- sql/
- src/
- tests/
- outputs/tables/
- outputs/figures/

## Source notes

The project relies on primary publisher and platform-holder material, reputable contemporary reviews, and technical documentation when available. Fan wikis are used only to discover candidate lists and are cross-checked against independent sources where feasible.

## Limitations

- Unsupported mission totals are intentionally omitted; the project retains only source-traced classifications and activity records.
- Open-world comparison across different titles must be interpreted as a design comparison, not a direct quality ranking.
- Technical claims are constrained by the generation of hardware and by the original platform and engine choices.

## License

This project code and documentation are released under the MIT License. The games themselves remain the property of their original rights holders. No copyrighted game files or assets are bundled in this repository.
