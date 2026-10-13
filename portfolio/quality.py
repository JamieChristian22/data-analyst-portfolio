"""Fail closed on broken contracts; preserve ambiguous repeated events."""
import numpy as np
import pandas as pd


def clean_table(frame, specification, primary_key=None):
    expected = dict(token.split(':') for token in specification.split())
    if set(frame.columns) != set(expected):
        raise ValueError(f'Schema mismatch: expected {list(expected)}, got {list(frame.columns)}')
    if frame.isna().any().any():
        raise ValueError('Missing required value; repair source or document a new policy')
    clean = frame.copy()
    for column, kind in expected.items():
        if kind == 's':
            clean[column] = clean[column].astype(str).str.strip()
            if clean[column].eq('').any():
                raise ValueError(f'Empty string: {column}')
        elif kind == 'd':
            clean[column] = pd.to_datetime(clean[column], format='%Y-%m-%d', errors='raise').dt.strftime('%Y-%m-%d')
        elif kind == 'b':
            values = clean[column].astype(str).str.lower().str.strip().map({'true':1,'false':0,'1':1,'0':0})
            if values.isna().any():
                raise ValueError(f'Invalid binary value: {column}')
            clean[column] = values.astype('int64')
        else:
            values = pd.to_numeric(clean[column], errors='raise')
            if not np.isfinite(values).all():
                raise ValueError(f'Nonfinite number: {column}')
            if kind == 'i' and not (values % 1 == 0).all():
                raise ValueError(f'Noninteger: {column}')
            if (values < 0).any():
                raise ValueError(f'Negative number outside contract: {column}')
            clean[column] = values.astype('int64' if kind == 'i' else 'float64')
    if primary_key and clean[primary_key].duplicated().any():
        raise ValueError(f'Duplicate primary key: {primary_key}')
    if 'rating' in clean and not clean.rating.between(0,5).all():
        raise ValueError('Rating outside 0–5')
    for column in [c for c in clean if c.endswith('_id') or c in ('seats','units','units_sold')]:
        if (clean[column] <= 0).any():
            raise ValueError(f'Nonpositive ID/count: {column}')
    return clean


def foreign_key(child, parent, key):
    missing = set(child[key]) - set(parent[key])
    if missing:
        raise ValueError(f'Orphan {key}: {len(missing)} distinct values')


def ordered_funnel(users, events, stages, event_column, start_column=None):
    """Unique-user cumulative funnel; same-day ties allowed at date granularity.

    Use the earliest qualifying event at/after the prior step, not merely the
    earliest event for that label. Observation-window censoring is not corrected.
    """
    current = {int(row.user_id): getattr(row,start_column) if start_column else '0001-01-01'
               for row in users.itertuples()}
    results = []
    for stage in stages:
        matching = events[events[event_column].eq(stage)].sort_values('event_date')
        following = {}
        for row in matching.itertuples():
            uid = int(row.user_id)
            if uid in current and uid not in following and row.event_date >= current[uid]:
                following[uid] = row.event_date
        results.append(len(following))
        current = following
    return results
