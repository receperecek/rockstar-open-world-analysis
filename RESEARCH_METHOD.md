# Research method

## Source hierarchy

1. Primary publisher and company materials
   - Rockstar product pages, investor materials, and platform-holder documentation
2. Contemporaneous reviews and technical analyses
   - Critic review coverage and design commentary from 2004-2008
3. Secondary reference sources used for metadata and cross-checking
   - Wikipedia and encyclopedia references are used to identify candidate facts, but they are not treated as stand-alone evidence for the final analytic claim unless cross-checked.

## Selection logic for contemporaries

The comparison set was limited to the following works:

- Crackdown (2007)
- Assassin’s Creed (2007)

These titles were selected because they were released in the same year, were recognized as open-world or city-based design references, and offered a useful contrast to GTA IV’s design priorities along shared dimensions such as traversal, city structure, and mission design. A broader 2007 field could have been included, but that would blur the comparison and weaken claims about specific product strategy.

## Mission-count rules

- Main-story mission counts are tracked separately from optional story missions, side missions, and ambient activities.
- Branching or alternative outcomes are recorded under a separate mission-status label rather than mixed into the main required total.
- No mission total is retained unless it has a clear counting rule and a source trail. Unsupported totals are removed from the project outputs and summary tables.
- This project deliberately excludes later remasters, ports, and DLC unless a limitation requires explanation.

## Classification method

Each mission is classified under a single primary mechanic category and may also carry overlapping secondary tags. Mechanical categories include driving, flight, watercraft, combat, stealth, pursuit/escape, racing, traversal/platforming, and other. This enables a distribution analysis without implying that one category is intrinsically more valuable than another.

The chart values are produced by this exact rule:

1. Start from the approved mission catalogue rows in `data/processed/mission_catalogue.csv`.
2. Assign each row exactly one `primary_mechanic` from the rule set.
3. Count the rows grouped by `primary_mechanic` to create the mission mechanic distribution chart.
4. For side-activity values, use the rows in `data/processed/optional_missions_activities.csv` and sum `activity_count` by `game_id` and `activity_type`.
5. The source trail for every plotted row is held in the `source_ids` field; those values are the only evidence used to support the chart.

## Evidence map for the charts

- Mission mechanic distribution: derived from the `primary_mechanic` column in the mission catalogue, with each row reporting its `source_ids`.
- Side-activity comparison: derived from the `activity_count` rows in the optional activities table, with each row reporting its `source_ids`.
- Any chart value that does not map to a recorded source ID is excluded from the project’s evidence-backed claims.

## Data validation approach

- Every material fact is stored with a source ID in the source register.
- Duplicate IDs, missing categories, and missing source references are explicitly checked.
- All generated CSV tables and charts are built from the same processed data and therefore can be cross-checked directly.
- The project now treats exact mission totals as a separate evidence problem: if a count cannot be verified through the recorded source trail, it is removed rather than presented as fact.

## Limitations

- Mission counts can vary because of different definitions of what counts as a story mission or a side activity.
- Platform-generation differences mean that GTA IV cannot be compared purely on “graphics + performance” without clear hardware context.
- This project tests design strategy and market positioning, not a universal “best game” ranking.
