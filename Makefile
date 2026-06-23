.PHONY: build

docker-reset:
	docker compose down
	rm -rf storage
	docker system prune -f

docker-build:
	OSFLAG=linux/amd64 docker-compose build

docker-start:
	OSFLAG=linux/amd64 docker-compose up -d