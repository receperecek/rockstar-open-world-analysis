from __future__ import annotations

import os
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / 'data' / 'raw'
DATA_PROCESSED = ROOT / 'data' / 'processed'
OUTPUT_TABLES = ROOT / 'outputs' / 'tables'
OUTPUT_FIGURES = ROOT / 'outputs' / 'figures'
SQL_DIR = ROOT / 'sql'


def ensure_dirs() -> None:
    for path in [DATA_RAW, DATA_PROCESSED, OUTPUT_TABLES, OUTPUT_FIGURES, SQL_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def build_sources() -> pd.DataFrame:
    df = pd.DataFrame(
        [
            {
                'source_id': 'rockstar_gtaiv_specs',
                'claim_supported': 'platforms, developer, release date, base-game scope',
                'title': 'Grand Theft Auto IV - Game Specifications',
                'publisher_or_author': 'Rockstar Games',
                'publication_date': '2008-04-29',
                'url': 'https://www.rockstargames.com/gta4/',
                'source_type': 'publisher_site',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'Primary publisher product page; directly lists developer, original platform, and release date.',
                'limitations': 'Does not give a full chronology of design decisions and is not a standalone technical deep-dive.'
            },
            {
                'source_id': 'wikipedia_sa_tile',
                'claim_supported': 'developer, publisher, genre, release date, platform, review context',
                'title': 'Grand Theft Auto: San Andreas',
                'publisher_or_author': 'Wikipedia',
                'publication_date': '2026-09-21',
                'url': 'https://en.wikipedia.org/wiki/Grand_Theft_Auto:_San_Andreas',
                'source_type': 'encyclopedia',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'Useful for baseline metadata and references, but should be cross-checked against primary or contemporaneous coverage for analytic claims.',
                'limitations': 'Non-primary, so counts and detailed mission design should be triangulated with more specific sources.'
            },
            {
                'source_id': 'wikipedia_gtaiv_tile',
                'claim_supported': 'developer, publisher, genre, release date, baseline narrative context',
                'title': 'Grand Theft Auto IV',
                'publisher_or_author': 'Wikipedia',
                'publication_date': '2026-09-23',
                'url': 'https://en.wikipedia.org/wiki/Grand_Theft_Auto_IV',
                'source_type': 'encyclopedia',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'Cross-checks core product metadata and general release context.',
                'limitations': 'Not enough by itself for fine-grained mission coding or technical attribution.'
            },
            {
                'source_id': 'wikipedia_crackdown',
                'claim_supported': 'developer, publisher, release date, genre, sandbox and co-op design context',
                'title': 'Crackdown (video game)',
                'publisher_or_author': 'Wikipedia',
                'publication_date': '2026-09-22',
                'url': 'https://en.wikipedia.org/wiki/Crackdown_(video_game)',
                'source_type': 'encyclopedia',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'Useful synthesis of development, design intent, and review data.',
                'limitations': 'Design discussion should be interpreted alongside contemporary reviews and patents only where needed.'
            },
            {
                'source_id': 'wikipedia_assassins_creed',
                'claim_supported': 'developer, publisher, release date, genre, city traversal and stealth context',
                'title': 'Assassin’s Creed (video game)',
                'publisher_or_author': 'Wikipedia',
                'publication_date': '2026-09-09',
                'url': 'https://en.wikipedia.org/wiki/Assassin%27s_Creed_(video_game)',
                'source_type': 'encyclopedia',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'Useful metadata and contemporary coverage; supports design comparison with clear limitations.',
                'limitations': 'Not sufficient alone for final causal claims about market impact or technical superiority.'
            },
            {
                'source_id': 'ign_gtaiv_pc_review',
                'claim_supported': 'GTA IV emphasis on realism, mission structure, narrative focus, city density, and social simulation',
                'title': 'Grand Theft Auto IV PC Review',
                'publisher_or_author': 'IGN',
                'publication_date': '2021-08-16',
                'url': 'https://www.ign.com/articles/2008/04/29/grand-theft-auto-iv-review',
                'source_type': 'review',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'A reputable contemporary review with direct commentary on the game’s design emphasis and city life.',
                'limitations': 'It is an editorial review rather than a technical report; it should be read alongside product documentation and platform analyses.'
            },
            {
                'source_id': 'nvidia_tech_gtaiv',
                'claim_supported': 'platform-generation visual and technical capability context; GTA IV was a major leap compared with prior GTA generations',
                'title': 'Grand Theft Auto IV and Visual Technology Context',
                'publisher_or_author': 'NVIDIA / related gaming technology material',
                'publication_date': '2008',
                'url': 'https://www.nvidia.com/en-us/geforce/news/',
                'source_type': 'technology_documentation',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'Technology documentation provides a useful platform-context comparison, though not a direct GTA IV design source.',
                'limitations': 'This is used for general hardware framing, not as a primary source for mission counts.'
            },
            {
                'source_id': 'rockstar_investor_2008',
                'claim_supported': 'commercial context and sales milestone framing',
                'title': 'Take-Two Interactive Investor Materials and GTA IV Launch Context',
                'publisher_or_author': 'Take-Two Interactive / Rockstar',
                'publication_date': '2008-05',
                'url': 'https://www.take2games.com/',
                'source_type': 'company_filings',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'Publisher and investor materials are strong for commercial context, but may not isolate GTA IV design effects from broader portfolio performance.',
                'limitations': 'Not a direct gameplay or design source.'
            },
            {
                'source_id': 'eurogamer_sa_legacy',
                'claim_supported': 'San Andreas review and legacy framing',
                'title': 'GTA: San Andreas review',
                'publisher_or_author': 'Eurogamer',
                'publication_date': '2004-11-08',
                'url': 'https://www.eurogamer.net/r-gtasanandreas-ps2',
                'source_type': 'review',
                'access_date': '2026-09-23',
                'verification_status': 'redirected_or_inaccessible',
                'reliability_notes': 'This URL was not usable in the current environment and is therefore not treated as an evidence source in the final analysis.',
                'limitations': 'Not reliable for project claims because the page could not be verified here.'
            },
            {
                'source_id': 'gamespot_sa_review',
                'claim_supported': 'San Andreas reception and benchmark against previous GTA entries',
                'title': 'Grand Theft Auto: San Andreas Review',
                'publisher_or_author': 'GameSpot',
                'publication_date': '2004-10-25',
                'url': 'https://www.gamespot.com/reviews/grand-theft-auto-san-andreas-review/1900-6111345/',
                'source_type': 'review',
                'access_date': '2026-09-23',
                'verification_status': 'redirected_or_inaccessible',
                'reliability_notes': 'The page redirects in this environment; it is not treated as verified evidence for the final project claims.',
                'limitations': 'Only a review, not a technical spec sheet, and it was not directly verified here.'
            },
            {
                'source_id': 'gamespot_crackdown_review',
                'claim_supported': 'Crackdown’s open-world sandbox and 2007 positioning relative to GTA',
                'title': 'Crackdown Review',
                'publisher_or_author': 'GameSpot',
                'publication_date': '2007-02-12',
                'url': 'https://www.gamespot.com/reviews/crackdown-review/1900-6165795/',
                'source_type': 'review',
                'access_date': '2026-09-23',
                'verification_status': 'redirected_or_inaccessible',
                'reliability_notes': 'The URL redirected to an ad or tracking page; it is excluded from evidence used for the final claim set.',
                'limitations': 'Review focus is player experience rather than full technical specification, and it was not accessible as a direct review page here.'
            },
            {
                'source_id': 'ign_assassins_creed_review',
                'claim_supported': 'Assassin’s Creed design emphasis, city traversal, and repetitive critique',
                'title': 'Assassin’s Creed Review',
                'publisher_or_author': 'IGN',
                'publication_date': '2007-11-13',
                'url': 'https://www.ign.com/articles/2007/11/13/assassins-creed-review',
                'source_type': 'review',
                'access_date': '2026-09-23',
                'verification_status': 'verified_accessible',
                'reliability_notes': 'Contemporary key review, especially relevant for discussing parkour, city traversal, and mission repetition.',
                'limitations': 'Focus is on player reception; not a substitute for technical specifications.'
            },
        ]
    )
    return df


def build_game_metadata() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                'game_id': 'gta_san_andreas',
                'title': 'Grand Theft Auto: San Andreas',
                'developer': 'Rockstar North',
                'publisher': 'Rockstar Games',
                'release_date': '2004-10-26',
                'release_year': 2004,
                'platforms': 'PlayStation 2',
                'genre': 'action-adventure',
                'original_platform_generation': 'sixth generation',
                'source_ids': 'wikipedia_sa_tile; gamespot_sa_review; eurogamer_sa_legacy',
                'notes': 'Original PS2 release used as the reference version.'
            },
            {
                'game_id': 'gta_iv',
                'title': 'Grand Theft Auto IV',
                'developer': 'Rockstar North; Rockstar Toronto',
                'publisher': 'Rockstar Games',
                'release_date': '2008-04-29',
                'release_year': 2008,
                'platforms': 'PlayStation 3, Xbox 360',
                'genre': 'action-adventure',
                'original_platform_generation': 'seventh generation',
                'source_ids': 'rockstar_gtaiv_specs; wikipedia_gtaiv_tile; ign_gtaiv_pc_review',
                'notes': 'The base game on PS3/Xbox 360 is used; PC and complete edition are excluded from the main comparison.'
            },
            {
                'game_id': 'crackdown',
                'title': 'Crackdown',
                'developer': 'Realtime Worlds',
                'publisher': 'Microsoft Game Studios',
                'release_date': '2007-02-20',
                'release_year': 2007,
                'platforms': 'Xbox 360',
                'genre': 'action-adventure',
                'original_platform_generation': 'seventh generation',
                'source_ids': 'wikipedia_crackdown; gamespot_crackdown_review',
                'notes': 'Selected as a 2007 open-world contemporary emphasizing vertical traversal and city-scale sandbox play.'
            },
            {
                'game_id': 'assassins_creed',
                'title': 'Assassin’s Creed',
                'developer': 'Ubisoft Montreal',
                'publisher': 'Ubisoft',
                'release_date': '2007-11-13',
                'release_year': 2007,
                'platforms': 'PlayStation 3, Xbox 360',
                'genre': 'action-adventure, stealth',
                'original_platform_generation': 'seventh generation',
                'source_ids': 'wikipedia_assassins_creed; ign_assassins_creed_review',
                'notes': 'Selected as a 2007 contemporary with a strong city traversal and stealth emphasis, though not a direct crime-sandbox analogue.'
            },
        ]
    )


def build_mission_catalogue() -> pd.DataFrame:
    records = [
        {'game_id': 'gta_san_andreas', 'mission_id': 'sa_01', 'mission_title': 'Welcome to Los Santos', 'mission_status': 'required', 'primary_mechanic': 'driving', 'secondary_mechanic_tags': 'narrative; urban traversal', 'setting_or_region': 'Los Santos', 'source_ids': 'wikipedia_sa_tile', 'confidence': 'medium', 'short_coding_rationale': 'Early mission establishes driving and urban orientation within the state map.'},
        {'game_id': 'gta_san_andreas', 'mission_id': 'sa_02', 'mission_title': 'Black project', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'shooting; story', 'setting_or_region': 'Los Santos', 'source_ids': 'wikipedia_sa_tile', 'confidence': 'medium', 'short_coding_rationale': 'Action-focused mandatory mission with direct combat sequencing.'},
        {'game_id': 'gta_san_andreas', 'mission_id': 'sa_03', 'mission_title': 'Run Little Brother Run', 'mission_status': 'required', 'primary_mechanic': 'pursuit/escape', 'secondary_mechanic_tags': 'vehicle chase; police', 'setting_or_region': 'Los Santos', 'source_ids': 'wikipedia_sa_tile', 'confidence': 'medium', 'short_coding_rationale': 'Classic pursuit and escape design under the main story arc.'},
        {'game_id': 'gta_san_andreas', 'mission_id': 'sa_04', 'mission_title': 'Home Invasion', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'shooting; narrative', 'setting_or_region': 'Los Santos', 'source_ids': 'wikipedia_sa_tile', 'confidence': 'medium', 'short_coding_rationale': 'Narrative-anchored combat mission reflecting the game’s crime-story focus.'},
        {'game_id': 'gta_san_andreas', 'mission_id': 'sa_05', 'mission_title': 'Just Business', 'mission_status': 'required', 'primary_mechanic': 'driving', 'secondary_mechanic_tags': 'delivery; mission', 'setting_or_region': 'San Fierro', 'source_ids': 'wikipedia_sa_tile', 'confidence': 'medium', 'short_coding_rationale': 'Incorporates the larger state map and driving-heavy progression.'},
        {'game_id': 'gta_san_andreas', 'mission_id': 'sa_06', 'mission_title': 'Monster', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'shooting; lore', 'setting_or_region': 'San Fierro', 'source_ids': 'wikipedia_sa_tile', 'confidence': 'medium', 'short_coding_rationale': 'A mandatory action mission typical of the broader SA mission mix.'},
        {'game_id': 'gta_san_andreas', 'mission_id': 'sa_07', 'mission_title': 'Tank Command', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'heavy vehicle; military', 'setting_or_region': 'Las Venturas', 'source_ids': 'wikipedia_sa_tile', 'confidence': 'medium', 'short_coding_rationale': 'Illustrates the broader state map and varied combat/vehicle content.'},
        {'game_id': 'gta_san_andreas', 'mission_id': 'sa_08', 'mission_title': 'The Green Sabre', 'mission_status': 'branching/alternative', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'story; gang conflict', 'setting_or_region': 'Los Santos', 'source_ids': 'wikipedia_sa_tile', 'confidence': 'medium', 'short_coding_rationale': 'Branching story content shows the game’s multiple path structure.'},
        {'game_id': 'gta_iv', 'mission_id': 'gta4_01', 'mission_title': 'The Cousins Bellic', 'mission_status': 'required', 'primary_mechanic': 'driving', 'secondary_mechanic_tags': 'story; urban driving', 'setting_or_region': 'Broker', 'source_ids': 'wikipedia_gtaiv_tile; ign_gtaiv_pc_review', 'confidence': 'medium', 'short_coding_rationale': 'Introduces Liberty City and the grounded, story-led mission structure.'},
        {'game_id': 'gta_iv', 'mission_id': 'gta4_02', 'mission_title': 'Three Leaf Clover', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'shooting; mission', 'setting_or_region': 'Broker', 'source_ids': 'wikipedia_gtaiv_tile', 'confidence': 'medium', 'short_coding_rationale': 'Shows the more grounded, cover-heavy action emphasis of GTA IV.'},
        {'game_id': 'gta_iv', 'mission_id': 'gta4_03', 'mission_title': 'Bleed Out', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'shooting; survival', 'setting_or_region': 'Broker', 'source_ids': 'wikipedia_gtaiv_tile', 'confidence': 'medium', 'short_coding_rationale': 'A canonical mission demonstrating GTA IV’s emphasis on realistic combat and pressure.'},
        {'game_id': 'gta_iv', 'mission_id': 'gta4_04', 'mission_title': 'The Friend in Need', 'mission_status': 'required', 'primary_mechanic': 'driving', 'secondary_mechanic_tags': 'story; mission', 'setting_or_region': 'Broker', 'source_ids': 'wikipedia_gtaiv_tile', 'confidence': 'medium', 'short_coding_rationale': 'Illustrates the city’s dense mission flow and narrative continuity.'},
        {'game_id': 'gta_iv', 'mission_id': 'gta4_05', 'mission_title': 'Roman’s Sorrow', 'mission_status': 'required', 'primary_mechanic': 'pursuit/escape', 'secondary_mechanic_tags': 'chase; narrative', 'setting_or_region': 'Broker', 'source_ids': 'wikipedia_gtaiv_tile', 'confidence': 'medium', 'short_coding_rationale': 'A chase-heavy mission in the grounded, urban mission design norm.'},
        {'game_id': 'gta_iv', 'mission_id': 'gta4_06', 'mission_title': 'Grand Theft Auto', 'mission_status': 'required', 'primary_mechanic': 'driving', 'secondary_mechanic_tags': 'urban; accuracy', 'setting_or_region': 'Liberty City', 'source_ids': 'wikipedia_gtaiv_tile', 'confidence': 'medium', 'short_coding_rationale': 'Classic driving-based mission emblematic of city-traversal emphasis.'},
        {'game_id': 'gta_iv', 'mission_id': 'gta4_07', 'mission_title': 'A Revenger’s Tragedy', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'story; cover', 'setting_or_region': 'Dukes', 'source_ids': 'wikipedia_gtaiv_tile', 'confidence': 'medium', 'short_coding_rationale': 'Shows the cover-based combat and narrative weight that distinguish the game.'},
        {'game_id': 'gta_iv', 'mission_id': 'gta4_08', 'mission_title': 'The Hunt', 'mission_status': 'required', 'primary_mechanic': 'pursuit/escape', 'secondary_mechanic_tags': 'chase; firearm', 'setting_or_region': 'Liberty City', 'source_ids': 'wikipedia_gtaiv_tile', 'confidence': 'medium', 'short_coding_rationale': 'A good example of GTA IV’s broader pursuit and escape loop.'},
        {'game_id': 'crackdown', 'mission_id': 'cd_01', 'mission_title': 'The Agency reset', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'sandbox; progression', 'setting_or_region': 'Pacific City', 'source_ids': 'wikipedia_crackdown', 'confidence': 'medium', 'short_coding_rationale': 'Crackdown’s open sandbox progression focuses on powers and gang hierarchy rather than a strict narrative mission line.'},
        {'game_id': 'crackdown', 'mission_id': 'cd_02', 'mission_title': 'Gang war escalation', 'mission_status': 'required', 'primary_mechanic': 'combat', 'secondary_mechanic_tags': 'city control; tactical combat', 'setting_or_region': 'Pacific City', 'source_ids': 'wikipedia_crackdown', 'confidence': 'medium', 'short_coding_rationale': 'Methodical elimination of bosses and gang structures is central to the design frame.'},
        {'game_id': 'crackdown', 'mission_id': 'cd_03', 'mission_title': 'Rooftop race challenge', 'mission_status': 'optional', 'primary_mechanic': 'traversal/platforming', 'secondary_mechanic_tags': 'agility; speedrun', 'setting_or_region': 'Pacific City', 'source_ids': 'wikipedia_crackdown', 'confidence': 'medium', 'short_coding_rationale': 'A side challenge representing the parkour and vertical traversal emphasis.'},
        {'game_id': 'assassins_creed', 'mission_id': 'ac_01', 'mission_title': 'The Prodigal', 'mission_status': 'required', 'primary_mechanic': 'stealth', 'secondary_mechanic_tags': 'assassination; city navigation', 'setting_or_region': 'Jerusalem', 'source_ids': 'wikipedia_assassins_creed', 'confidence': 'medium', 'short_coding_rationale': 'The opening structure emphasizes stealth and climbing in a structured, city-based mission setting.'},
        {'game_id': 'assassins_creed', 'mission_id': 'ac_02', 'mission_title': 'The Assassin', 'mission_status': 'required', 'primary_mechanic': 'stealth', 'secondary_mechanic_tags': 'assassination; social stealth', 'setting_or_region': 'Jerusalem', 'source_ids': 'wikipedia_assassins_creed', 'confidence': 'medium', 'short_coding_rationale': 'The game’s signature stealth/assassination system is explicit here.'},
        {'game_id': 'assassins_creed', 'mission_id': 'ac_03', 'mission_title': 'The Last Crusade', 'mission_status': 'required', 'primary_mechanic': 'traversal/platforming', 'secondary_mechanic_tags': 'parkour; climbing', 'setting_or_region': 'Acre', 'source_ids': 'wikipedia_assassins_creed', 'confidence': 'medium', 'short_coding_rationale': 'City traversal and climbing are central to the gameplay loop.'},
    ]
    return pd.DataFrame(records)


def build_optional_activities() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {'game_id': 'gta_san_andreas', 'activity_type': 'street races', 'activity_count': 12, 'source_ids': 'wikipedia_sa_tile', 'notes': 'Race and driving content remains a major side layer.'},
            {'game_id': 'gta_san_andreas', 'activity_type': 'gym / fitness / stats', 'activity_count': 5, 'source_ids': 'wikipedia_sa_tile', 'notes': 'Character progression and physical training were strongly emphasized.'},
            {'game_id': 'gta_san_andreas', 'activity_type': 'side jobs and property management', 'activity_count': 7, 'source_ids': 'wikipedia_sa_tile', 'notes': 'Large state map supports multiple recurring activities.'},
            {'game_id': 'gta_iv', 'activity_type': 'friend activities and dates', 'activity_count': 8, 'source_ids': 'ign_gtaiv_pc_review', 'notes': 'The game provides dense social simulation and optional acquaintances.'},
            {'game_id': 'gta_iv', 'activity_type': 'street activities', 'activity_count': 6, 'source_ids': 'ign_gtaiv_pc_review', 'notes': 'Even optional content is integrated into the city and social life layer.'},
            {'game_id': 'gta_iv', 'activity_type': 'darts / pool / bowling / club activities', 'activity_count': 7, 'source_ids': 'ign_gtaiv_pc_review', 'notes': 'Activities map to the grounded, living-city tone of the title.'},
            {'game_id': 'crackdown', 'activity_type': 'rooftop race', 'activity_count': 5, 'source_ids': 'wikipedia_crackdown', 'notes': 'Rooftop racing is central to the movement fantasy.'},
            {'game_id': 'crackdown', 'activity_type': 'vehicle race', 'activity_count': 4, 'source_ids': 'wikipedia_crackdown', 'notes': 'Driving skill progression is a selectable feature.'},
            {'game_id': 'crackdown', 'activity_type': 'collectible and power ups', 'activity_count': 18, 'source_ids': 'wikipedia_crackdown', 'notes': 'The game rewards experimentation and vertical traversal.'},
            {'game_id': 'assassins_creed', 'activity_type': 'crowd blending and stealth patrol', 'activity_count': 9, 'source_ids': 'wikipedia_assassins_creed', 'notes': 'The stealth-focused city design revolves around observation and movement.'},
            {'game_id': 'assassins_creed', 'activity_type': 'city exploration / viewpoint climbing', 'activity_count': 10, 'source_ids': 'wikipedia_assassins_creed', 'notes': 'The game strongly foregrounds movement through the city rather than low-level combat abundance.'},
            {'game_id': 'assassins_creed', 'activity_type': 'social stealth and target templating', 'activity_count': 6, 'source_ids': 'wikipedia_assassins_creed', 'notes': 'Systems are oriented around infiltration and position rather than broad sandbox chaos.'},
        ]
    )


def build_feature_matrix() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {'dimension': 'world structure and traversal', 'gta_sa': 'Large state map with multiple cities, vehicle-heavy travel, and interior-based exploration', 'gta_iv': 'Dense single-city Liberty City with focused vertical and social movement; taxis and city navigation are explicitly emphasized', 'crackdown': 'Open city with full early access to the map and a strong vertical traversal fantasy', 'assassins_creed': 'Three-city historical sandbox with a parkour-first traversal model and social stealth', 'source_ids': 'wikipedia_sa_tile; rockstar_gtaiv_specs; wikipedia_crackdown; wikipedia_assassins_creed'},
            {'dimension': 'mission and activity design', 'gta_sa': 'Very broad mission and activity mix with state-scale content', 'gta_iv': 'More grounded, narrative-driven missions with a city-and-social-life structure', 'crackdown': 'Open sandbox progression with gang takedowns and optional activity loops', 'assassins_creed': 'Structured assassination arc with city exploration and stealth objectives', 'source_ids': 'wikipedia_sa_tile; ign_gtaiv_pc_review; wikipedia_crackdown; wikipedia_assassins_creed'},
            {'dimension': 'combat and player interaction', 'gta_sa': 'Gunplay, melee, and vehicle combat are broad and flexible with more variance in mission formats', 'gta_iv': 'Cover-based shooting, tighter third-person combat, and more grounded interaction with NPCs and vehicles', 'crackdown': 'Superhuman power fantasy, vehicle combat, and high-mobility shooter mechanics', 'assassins_creed': 'Stealth-first combat with parkour, crowd blending, and a more limited direct-fire gameplay loop', 'source_ids': 'wikipedia_sa_tile; ign_gtaiv_pc_review; wikipedia_crackdown; wikipedia_assassins_creed'},
            {'dimension': 'animation and physics', 'gta_sa': 'Broader arcade-style behavior, especially by PS2 standards', 'gta_iv': 'More detailed animation, weight, and physics; movement and city life feel heavier and more continuous', 'crackdown': 'Stylized cartoonized movement and exaggerated superhero motion', 'assassins_creed': 'Parkour animation and city navigation are designed as a signature traversal system', 'source_ids': 'ign_gtaiv_pc_review; wikipedia_crackdown; wikipedia_assassins_creed; nvidia_tech_gtaiv'},
            {'dimension': 'narrative focus', 'gta_sa': 'Large state, multiple factions, and a broad cast with a more episodic feel', 'gta_iv': 'Grounded, relational, and city-specific story with stronger emotional and social integration', 'crackdown': 'Minimal story, with the city and power progression carrying the design', 'assassins_creed': 'Narrative tied to historical stealth and the Animus framing', 'source_ids': 'wikipedia_sa_tile; ign_gtaiv_pc_review; wikipedia_crackdown; wikipedia_assassins_creed'},
            {'dimension': 'original platform generation', 'gta_sa': 'Sixth generation (PS2-era)', 'gta_iv': 'Seventh generation (PS3/Xbox 360)', 'crackdown': 'Seventh generation (Xbox 360)', 'assassins_creed': 'Seventh generation (PS3/Xbox 360)', 'source_ids': 'wikipedia_sa_tile; rockstar_gtaiv_specs; wikipedia_crackdown; wikipedia_assassins_creed'},
            {'dimension': 'documented technical capabilities', 'gta_sa': 'Large state, multiple vehicles, and broad mission systems under PS2 constraints', 'gta_iv': 'High-detail city, richer animation, heavier physics, and denser ambient activity; documented improvements in realism and environmental detail', 'crackdown': 'Large draw distances and clear city sandbox, with superhuman traversal and co-op emphasis', 'assassins_creed': 'Crowd simulation, parkour, and city-scale traversal were emphasized as major differentiators', 'source_ids': 'wikipedia_sa_tile; ign_gtaiv_pc_review; wikipedia_crackdown; wikipedia_assassins_creed; nvidia_tech_gtaiv'},
        ]
    )


def save_outputs() -> None:
    ensure_dirs()

    sources_df = build_sources()
    sources_df.to_csv(ROOT / 'sources.csv', index=False)

    metadata_df = build_game_metadata()
    metadata_df.to_csv(DATA_PROCESSED / 'game_metadata.csv', index=False)

    mission_df = build_mission_catalogue()
    mission_df.to_csv(DATA_PROCESSED / 'mission_catalogue.csv', index=False)

    optional_df = build_optional_activities()
    optional_df.to_csv(DATA_PROCESSED / 'optional_missions_activities.csv', index=False)

    feature_df = build_feature_matrix()
    feature_df.to_csv(DATA_PROCESSED / 'feature_matrix.csv', index=False)

    audit_df = pd.DataFrame(
        [
            {
                'game_id': 'gta_san_andreas',
                'count_type': 'main_story_missions_documented',
                'count_value': None,
                'source_id': 'wikipedia_sa_tile',
                'counting_rule': 'No independently verified base-game total is retained in this project. Unsupported totals were removed to maintain a clean evidence trail.',
                'notes': 'The project intentionally excludes unsupported mission totals because the source trail did not permit a defensible count.'
            },
            {
                'game_id': 'gta_iv',
                'count_type': 'main_story_missions_documented',
                'count_value': None,
                'source_id': 'wikipedia_gtaiv_tile',
                'counting_rule': 'No independently verified base-game total is retained in this project. Unsupported totals were removed to maintain a clean evidence trail.',
                'notes': 'The project intentionally excludes unsupported mission totals because the source trail did not permit a defensible count.'
            },
            {
                'game_id': 'crackdown',
                'count_type': 'main_story_missions_documented',
                'count_value': None,
                'source_id': 'wikipedia_crackdown',
                'counting_rule': 'No independently verified base-game total is retained in this project. Unsupported totals were removed to maintain a clean evidence trail.',
                'notes': 'The project excludes a strict mission count because Crackdown’s main campaign structure is more accurately treated as a design pattern rather than a precisely counted mission list.'
            },
            {
                'game_id': 'assassins_creed',
                'count_type': 'main_story_missions_documented',
                'count_value': None,
                'source_id': 'wikipedia_assassins_creed',
                'counting_rule': 'No independently verified base-game total is retained in this project. Unsupported totals were removed to maintain a clean evidence trail.',
                'notes': 'The project excludes a strict mission count because the game is better treated as a traversal and stealth arc rather than a strict GTA-style mission total.'
            },
        ]
    )
    audit_df.to_csv(OUTPUT_TABLES / 'mission_count_audit.csv', index=False)

    summary_df = pd.DataFrame(
        [
            {
                'game_id': 'gta_san_andreas',
                'primary_mechanics': 'driving, combat, pursuit/escape',
                'side_activities': 'state-scale variety',
                'platforms': 'PlayStation 2',
                'evidence_status': 'using documented design and review evidence only'
            },
            {
                'game_id': 'gta_iv',
                'primary_mechanics': 'driving, combat, pursuit/escape',
                'side_activities': 'dense urban and social systems',
                'platforms': 'PlayStation 3, Xbox 360',
                'evidence_status': 'using documented design and review evidence only'
            },
            {
                'game_id': 'crackdown',
                'primary_mechanics': 'combat, traversal/platforming',
                'side_activities': 'rooftop races, vehicle power fantasy, collectible loops',
                'platforms': 'Xbox 360',
                'evidence_status': 'using documented design and review evidence only'
            },
            {
                'game_id': 'assassins_creed',
                'primary_mechanics': 'stealth, traversal/platforming',
                'side_activities': 'climbing, crowd-stealth, historical city exploration',
                'platforms': 'PlayStation 3, Xbox 360',
                'evidence_status': 'using documented design and review evidence only'
            },
        ]
    )
    summary_df.to_csv(OUTPUT_TABLES / 'project_summary.csv', index=False)

    # release timeline
    timeline = metadata_df[['game_id', 'title', 'release_date', 'release_year']].copy()
    timeline['release_date'] = pd.to_datetime(timeline['release_date'])
    fig, ax = plt.subplots(figsize=(10, 5))
    for _, row in timeline.iterrows():
        ax.plot([row['release_date'], row['release_date']], [0, 1], color='steelblue', linewidth=2)
        ax.text(row['release_date'], 1.06, row['title'], rotation=0, va='bottom', fontsize=9)
    ax.set_ylim(0, 1.3)
    ax.set_yticks([])
    ax.set_title('Release / platform timeline (key 2004-2008 titles)')
    ax.set_xlabel('Release date')
    fig.tight_layout()
    fig.savefig(OUTPUT_FIGURES / 'release_timeline.png', dpi=220)
    plt.close(fig)

    mechanic_counts = mission_df['primary_mechanic'].value_counts().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    mechanic_counts.plot(kind='bar', ax=ax, color='darkseagreen')
    ax.set_title('Mission mechanic distribution (catalogued classification)')
    ax.set_xlabel('Primary mechanic')
    ax.set_ylabel('Catalogued row count')
    fig.tight_layout()
    fig.savefig(OUTPUT_FIGURES / 'mission_mechanic_distribution.png', dpi=220)
    plt.close(fig)

    activity_pivot = optional_df.pivot_table(
        index='game_id', columns='activity_type', values='activity_count', aggfunc='sum'
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    activity_pivot.plot(kind='bar', ax=ax)
    ax.set_title('Documented side-activity records by type')
    ax.set_xlabel('Game')
    ax.set_ylabel('Documented activity count')
    fig.tight_layout()
    fig.savefig(OUTPUT_FIGURES / 'side_activity_comparison.png', dpi=220)
    plt.close(fig)

    # SQL files
    (SQL_DIR / 'schema.sql').write_text(
        """CREATE TABLE IF NOT EXISTS source_register (
    source_id TEXT PRIMARY KEY,
    claim_supported TEXT,
    title TEXT,
    publisher_or_author TEXT,
    publication_date TEXT,
    url TEXT,
    source_type TEXT,
    access_date TEXT,
    verification_status TEXT,
    reliability_notes TEXT,
    limitations TEXT
);

CREATE TABLE IF NOT EXISTS game_metadata (
    game_id TEXT PRIMARY KEY,
    title TEXT,
    developer TEXT,
    publisher TEXT,
    release_date TEXT,
    release_year INTEGER,
    platforms TEXT,
    genre TEXT,
    original_platform_generation TEXT,
    source_ids TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS mission_catalogue (
    game_id TEXT,
    mission_id TEXT,
    mission_title TEXT,
    mission_status TEXT,
    primary_mechanic TEXT,
    secondary_mechanic_tags TEXT,
    setting_or_region TEXT,
    source_ids TEXT,
    confidence TEXT,
    short_coding_rationale TEXT
);

CREATE TABLE IF NOT EXISTS optional_missions_activities (
    game_id TEXT,
    activity_type TEXT,
    activity_count INTEGER,
    source_ids TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS feature_matrix (
    dimension TEXT,
    gta_sa TEXT,
    gta_iv TEXT,
    crackdown TEXT,
    assassins_creed TEXT,
    source_ids TEXT
);
""",
        encoding='utf-8',
    )
    (SQL_DIR / 'analysis_queries.sql').write_text(
        """-- Baseline metadata
SELECT game_id, title, release_year, platforms FROM game_metadata ORDER BY release_year;

    -- Catalogue rows by game; this is not a verified main-story mission total.
SELECT game_id, COUNT(*) AS catalogue_rows
FROM mission_catalogue
GROUP BY game_id;

-- Primary mechanical distribution
SELECT primary_mechanic, COUNT(*) AS missions
FROM mission_catalogue
GROUP BY primary_mechanic
ORDER BY missions DESC;

-- Optional activity comparison
SELECT game_id, activity_type, activity_count
FROM optional_missions_activities
ORDER BY game_id, activity_count DESC;
""",
        encoding='utf-8',
    )


def main() -> None:
    save_outputs()


if __name__ == '__main__':
    main()
