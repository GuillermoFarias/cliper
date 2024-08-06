# Cliper

## Cut all, share better

### More than demo, a functional app

Demo: [https://cliper-app.gfarias.cl](https://cliper-app.gfarias.cl)

Cliper es una aplicación desarrollada en Python que permite acortar URLs y compartirlas de manera eficiente.

## Tecnologías utilizadas

- **Backend**: FastAPI
- **Cache**: Redis
- **Base de Datos**: MongoDB

## Documentación

- **Colección de Postman**: Encuentra la colección [aquí](./api-collection.json)
- **Documentación completa**: [Notion Documentation](enlace-a-la-documentacion-en-notion)

## Configuración local

Para levantar la aplicación en tu entorno local, sigue estos pasos:

1. **Copiar archivo de configuración**:
   Copia el archivo `.env` a `.env.example` y configura las variables de entorno según sea necesario.

   ```bash
   cp .env .env.example
   ```

2. **Levantar la aplicación con Docker Compose**
   Ejecuta el siguiente comando para levantar los servicios definidos en el archivo `docker-compose.yml`
   ```
   docker-compose up -d
   ```

## Producción
Para instrucciones sobre cómo desplegar Cliper en un entorno de producción, por favor, revisa el [pipeline de despliegue.](./.github/workflows/deploy.yml)