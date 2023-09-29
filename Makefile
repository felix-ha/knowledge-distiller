.PHONY: docker_build
docker_build:
	docker build . -t kdistiller

.PHONY: test_release
test_release: docker_build
	docker run --name kdistiller_release -dt kdistiller
	docker exec kdistiller_release /bin/bash ./bin/release_testpypi.sh
	docker stop kdistiller_release
	docker rm kdistiller_release

.PHONY: release
release: docker_build
	docker run --name kdistiller_release -dt kdistiller
	docker exec kdistiller_release /bin/bash ./bin/release.sh
	docker stop kdistiller_release
	docker rm kdistiller_release

.PHONY: docker_build_dev_container
docker_build_dev_container:
	docker build . -f .devcontainer/Dockerfile -t kdistiller-devcontainer
