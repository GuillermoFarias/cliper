# <img src="https://github.com/user-attachments/assets/7151506b-1782-44b3-a6d7-317c29d7005d" alt="image" width="50" align="left"> Cliper
[![Build, Push and Deploy to Kubernetes](https://github.com/GuillermoFarias/cliper/actions/workflows/deploy.yml/badge.svg)](https://github.com/GuillermoFarias/cliper/actions/workflows/deploy.yml)

## Cut all, share better

### More than demo, a functional app

Demo: [https://cliper-app.gfarias.cl](https://cliper-app.gfarias.cl)

Cliper es una aplicación desarrollada en Python que permite acortar URLs y compartirlas de manera eficiente.

## Tecnologías utilizadas

- **Backend**: FastAPI
- **Cache**: Redis
- **Base de Datos**: MongoDB

## Repos de interés
- **Front**: https://github.com/GuillermoFarias/cliper-front
- **Infra**: https://github.com/GuillermoFarias/cliper-infra

## Documentación

- **Colección de Postman**: Encuentra la colección [aquí](./api-collection.json)
- **Documentación completa**: [Notion Documentation](https://www.notion.so/Cliper-f42e6b2de7aa4e719ecda753d560d38c?pvs=4)

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
