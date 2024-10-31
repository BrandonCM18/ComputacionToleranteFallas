#Imagen de Node.js como base
FROM node:14

#Directorio de trabajo
WORKDIR /usr/src/app

#Copia package.json e instala dependencias
COPY package*.json ./
RUN npm install

#Copia el codigo de la aplicacion
COPY . .

#Expone el puerto 3000
EXPOSE 3000

#Ejecuta la aplicacion
CMD ["node", "app.js"]