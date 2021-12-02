STATES := app tests
REPO := vitaliykuz/lab5_bobas

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .  # об'єднюємо директиви в одну стічку з підстановкою

run: #запускаємо 2 наших контейнера в цій мережі, та чистяться коли зупинені
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app: #test run
	@docker run --rm -it --name test --net=appnet $(REPO):tests

push:
	@docker push $(REPO):app
	@docker push $(REPO):tests
docker-prune: # очищає все що створили імеджі в ран
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force

auto-delete:
	@docker rmi --force $$(docker images -q)

