from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_required_project_files_exist():
    required = [
        'README.md',
        'EXECUTIVE_SUMMARY.md',
        'RESEARCH_METHOD.md',
        'DATA_DICTIONARY.md',
        'requirements.txt',
        'sources.csv',
        'data/processed/game_metadata.csv',
        'data/processed/mission_catalogue.csv',
        'data/processed/optional_missions_activities.csv',
        'data/processed/feature_matrix.csv',
    ]
    for path in required:
        with open(ROOT / path, 'r', encoding='utf-8') as f:
            assert f.readable()


def test_summary_does_not_publish_unverified_mission_totals():
    summary_path = ROOT / 'outputs' / 'tables' / 'project_summary.csv'
    assert summary_path.exists()
    content = summary_path.read_text(encoding='utf-8')
    assert '100' not in content
    assert '69' not in content
    assert 'mission_count' not in content.lower()


def test_mission_catalogue_source_trail_is_recorded():
    df = pd.read_csv(ROOT / 'data' / 'processed' / 'mission_catalogue.csv')
    assert {'source_ids', 'mission_title', 'game_id'}.issubset(df.columns)
    assert df['source_ids'].notna().all()
    assert df['source_ids'].astype(str).str.len().gt(0).all()


def test_metadata_counts_are_plausible():
    df = pd.read_csv(ROOT / 'data' / 'processed' / 'game_metadata.csv')
    assert set(df['game_id']) == {'gta_san_andreas', 'gta_iv', 'crackdown', 'assassins_creed'}
    assert df['release_year'].notna().all()


def test_mission_catalogue_schema_is_valid():
    df = pd.read_csv(ROOT / 'data' / 'processed' / 'mission_catalogue.csv')
    required_columns = {
        'game_id', 'mission_id', 'mission_title', 'mission_status', 'primary_mechanic',
        'setting_or_region', 'source_ids', 'confidence', 'short_coding_rationale'
    }
    assert required_columns.issubset(set(df.columns))
    assert df['mission_status'].isin(['required', 'optional', 'branching/alternative']).all()
    assert df['primary_mechanic'].str.len().gt(0).all()


def test_feature_matrix_has_shared_dimensions():
    df = pd.read_csv(ROOT / 'data' / 'processed' / 'feature_matrix.csv')
    assert {'dimension', 'gta_sa', 'gta_iv', 'crackdown', 'assassins_creed'}.issubset(df.columns)
    assert not df.empty


def test_executive_summary_uses_qualified_language():
    summary_text = (ROOT / 'EXECUTIVE_SUMMARY.md').read_text(encoding='utf-8')
    assert 'most realistic' not in summary_text.lower()
    assert 'denser city' not in summary_text.lower()
    assert 'better graphics' not in summary_text.lower()
