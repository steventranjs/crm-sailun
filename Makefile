.PHONY: build

docker-reset:
	rm -rf storage
	docker system prune -f

docker-build:
	env DOCKER_DEFAULT_PLATFORM=linux/amd64 OSFLAG=linux/amd64 docker-compose build

docker-start:
	env DOCKER_DEFAULT_PLATFORM=linux/amd64 OSFLAG=linux/amd64 docker-compose up -d