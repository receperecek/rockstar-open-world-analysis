CREATE TABLE IF NOT EXISTS source_register (
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
