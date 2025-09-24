CREATE TABLE IF NOT EXISTS public.intake_sessions (
    id BIGSERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    user_email TEXT,
    data JSONB NOT NULL
);
