# Usa la imagen oficial de Node.js 20 para construir Angular 19
FROM node:20 AS build

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de configuración y paquetes
COPY package.json package-lock.json ./

# Instalar dependencias
RUN npm install

# Copiar todo el código fuente
COPY . .

# Compilar la aplicación en modo producción
RUN npm run build -- --output-path=dist --configuration=production

# Usa Nginx para servir Angular
FROM nginx:latest

# Copiar la build de Angular al servidor Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

# Comando por defecto para iniciar Nginx
CMD ["nginx", "-g", "daemon off;"]
