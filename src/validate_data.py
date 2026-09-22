from __future__ import annotations

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate() -> None:
    source_df = pd.read_csv(ROOT / 'sources.csv')
    assert source_df['source_id'].is_unique
    assert source_df['url'].notna().all()
    assert source_df['verification_status'].isin(
        ['verified_accessible', 'redirected_or_inaccessible']
    ).all()
    source_ids = set(source_df['source_id'])

    meta = pd.read_csv(ROOT / 'data' / 'processed' / 'game_metadata.csv')
    assert set(meta['game_id']) == {'gta_san_andreas', 'gta_iv', 'crackdown', 'assassins_creed'}

    mission = pd.read_csv(ROOT / 'data' / 'processed' / 'mission_catalogue.csv')
    assert mission['primary_mechanic'].notna().all()
    assert mission['mission_status'].isin(['required', 'optional', 'branching/alternative']).all()
    assert mission['source_ids'].map(lambda value: set(str(value).split('; ')).issubset(source_ids)).all()

    feature = pd.read_csv(ROOT / 'data' / 'processed' / 'feature_matrix.csv')
    assert not feature.empty
    assert feature['source_ids'].map(lambda value: set(str(value).split('; ')).issubset(source_ids)).all()

    activities = pd.read_csv(ROOT / 'data' / 'processed' / 'optional_missions_activities.csv')
    assert activities['source_ids'].map(lambda value: set(str(value).split('; ')).issubset(source_ids)).all()

    print('Validation checks passed.')


if __name__ == '__main__':
    validate()
