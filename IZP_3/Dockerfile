# Этап 1: Сборка
FROM gcc:latest AS build
WORKDIR /usr/src/app
COPY . .
RUN make

# Этап 2: Запуск
FROM debian:stable-slim
WORKDIR /app
COPY --from=build /usr/src/app/app .
CMD ["./app"]