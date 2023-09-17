.PHONY: docker_build_dev
docker_build_dev:
	docker build -f Dockerfile.dev . -t kdistiller
