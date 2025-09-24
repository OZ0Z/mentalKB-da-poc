ENV ?= .env
DOCKER ?= docker compose

.PHONY: up down logs ps psql reseed smoke

up:            ## Boot the full stack
	$(DOCKER) up -d

down:          ## Stop and remove volumes (fresh reset)
	$(DOCKER) down -v

logs:          ## Follow docassemble + Postgres logs
	$(DOCKER) logs -f docassemble
	$(DOCKER) logs -f mentalkb-postgres

ps:            ## Container status
	$(DOCKER) ps

psql:          ## psql into the DB
	$(DOCKER) exec -it mentalkb-postgres psql -U $$MENTALKB_USER -d $$MENTALKB_DB

reseed:        ## Full reseed (drops volumes, boots fresh)
	$(MAKE) down && $(MAKE) up

smoke:         ## 60s proof: pages exist + intake_sessions writeable
	$(DOCKER) exec -it mentalkb-postgres psql -U $$MENTALKB_USER -d $$MENTALKB_DB -c "SELECT count(*) AS pages FROM public.pages;"
	$(DOCKER) exec -it mentalkb-postgres psql -U $$MENTALKB_USER -d $$MENTALKB_DB -c "CREATE TABLE IF NOT EXISTS intake_sessions(id bigserial PRIMARY KEY, created_at timestamptz NOT NULL DEFAULT now(), user_email text, data jsonb NOT NULL);"
	$(DOCKER) exec -it mentalkb-postgres psql -U $$MENTALKB_USER -d $$MENTALKB_DB -c "SELECT 'ok' AS intake_sessions_ready;"
