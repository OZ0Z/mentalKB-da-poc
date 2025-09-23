"""Utility functions for persistence hooks."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any, Dict

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

DB_URL_ENV = "MENTALKB_DB_URL"


def _engine() -> Engine:
    url = os.environ.get(DB_URL_ENV)
    if not url:
        raise RuntimeError(f"Environment variable {DB_URL_ENV} must be set for docassemble-mentalkb")
    return create_engine(url, pool_pre_ping=True)


def save_session_results(user_email: str | None, payload: Dict[str, Any]) -> None:
    """Persist a JSON snapshot of the session to the intake_sessions table."""
    engine = _engine()
    create_sql = text(
        """
        CREATE TABLE IF NOT EXISTS intake_sessions (
            id BIGSERIAL PRIMARY KEY,
            created_at TIMESTAMPTZ NOT NULL,
            user_email TEXT,
            data JSONB NOT NULL
        );
        """
    )
    insert_sql = text(
        """
        INSERT INTO intake_sessions (created_at, user_email, data)
        VALUES (:created_at, :user_email, CAST(:data AS jsonb));
        """
    )
    json_payload = json.dumps(payload, default=str)
    with engine.begin() as conn:
        conn.execute(create_sql)
        conn.execute(
            insert_sql,
            {
                "created_at": datetime.now(timezone.utc),
                "user_email": user_email,
                "data": json_payload,
            },
        )
