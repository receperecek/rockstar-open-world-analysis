# Data dictionary

## Game metadata

Fields:

- game_id: Stable internal identifier for each game.
- title: Release title.
- developer: Primary developer(s).
- publisher: Publisher.
- release_date: Original release date in ISO format.
- release_year: Release year used for timeline work.
- platforms: Original platform(s) for the reference version.
- genre: Shared genre label.
- original_platform_generation: Platform-generation group used to contextualize technical difference.
- source_ids: Semicolon-separated source IDs supporting the row.
- notes: Scope notes and exclusions.

## Mission catalogue

Fields:

- game_id: Game identifier.
- mission_id: Unique mission identifier.
- mission_title: Short title of the mission or task.
- mission_status: One of required, optional, or branching/alternative.
- primary_mechanic: One mutually exclusive main mechanic category.
- secondary_mechanic_tags: Optional tags that may overlap.
- setting_or_region: Region or city used.
- source_ids: Source IDs covering the record.
- confidence: High, medium, or low based on source clarity.
- short_coding_rationale: Brief explanation of why the row was coded as it was.

## Optional missions and activities

Fields:

- game_id: Game identifier.
- activity_type: Activity class.
- activity_count: Count used in the side-activity comparison.
- source_ids: Supporting sources.
- notes: Scope and interpretation notes.

## Feature matrix

Fields:

- dimension: Shared dimension for comparison.
- gta_sa: San Andreas value.
- gta_iv: GTA IV value.
- crackdown: Crackdown value.
- assassins_creed: Assassin’s Creed value.
- source_ids: Source register references.

## Source register

Fields:

- source_id: Unique source ID.
- claim_supported: What claim the source supports.
- title: Source title.
- publisher_or_author: Publication or organization.
- publication_date: Source publication date.
- url: URL for verification.
- source_type: Publisher site, review, technology documentation, etc.
- access_date: Date the reference was accessed.
- verification_status: `verified_accessible` or `redirected_or_inaccessible`.
- reliability_notes: Why the source was used and what caution applies.
- limitations: Known limitations of the source.

Only records with `verification_status = verified_accessible` are treated as current evidence for the final analytic claim set. Redirected or inaccessible URLs are tracked, but they are not used to prove a factual claim.

## Summary metrics

- Mission count: Count of story missions under the project’s documented rule.
- Primary mechanic distribution: Count of missions by dominant mechanic.
- Side-activity totals: Count of optional activities by type.
- Platform generation: Original hardware generation to clarify technical assumptions.
- Sensitivity check: Alternate classification is stored in the documentation, not as a disguised objective fact.

## Permitted values

Primary mechanics used in the project are:

- driving
- flight
- watercraft
- combat
- stealth
- pursuit/escape
- racing
- traversal/platforming
- other

Mission status values are:

- required
- optional
- branching/alternative
