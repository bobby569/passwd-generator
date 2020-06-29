.PHONY: build
build:
	docker build -t docker.pkg.github.com/bobby569/passwd-generator/passwd-generator:$(tag) .

.PHONY: publish
publish:
	docker push docker.pkg.github.com/bobby569/passwd-generator/passwd-generator:$(tag)
