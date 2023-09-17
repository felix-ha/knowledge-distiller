.PHONY: docker_build
docker_build:
	docker build . -t kdistiller

.PHONY: test_release
test_release:
	docker run --name kdistiller_release -dt kdistiller
	docker exec kdistiller_release /bin/bash ./bin/test_release/release_testpypi.sh
	docker stop kdistiller_release
	docker rm kdistiller_release

.PHONY: release
release:
	docker run --name kdistiller_release -dt kdistiller
	docker exec kdistiller_release /bin/bash ./bin/release/release_pypi.sh
	docker stop kdistiller_release
	docker rm kdistiller_release
