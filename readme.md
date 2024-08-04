# Cliper

## acortador de urls para demo

## tecnologías

1. python 3.11
   1.1 Fastapi + uvicorn
1. mongodb
1. redis

## Despliegue local

### variables de entorno

```
cp .env.example .env
```

Se debe agregar la variables de GeoIP `MAXMIND_LICENSE_KEY` si quieres la geolocalización de ips
Se debe agregar la variables de K6 `K6_CLOUD_TOKEN` si quieres probar en K6cloud los tiempos de respuesta

