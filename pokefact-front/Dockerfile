# Etapa 1: construir la app
FROM node:18 AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Etapa 2: servir la app construida con Nginx
FROM nginx:stable-alpine

# Copia el build generado desde la etapa anterior
COPY --from=build /app/dist /usr/share/nginx/html

# Expone el puerto por donde servirá la web
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
