up:
	docker compose up -d

logs:
	docker compose logs -f

reset:
	docker compose down -v && docker compose up -d

psql:
	docker compose exec -it postgres psql -U $$MENTALKB_USER -d $$MENTALKB_DB
