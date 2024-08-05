import http from 'k6/http';
import { check, sleep } from 'k6';
import { randomString } from 'https://jslib.k6.io/k6-utils/1.1.0/index.js';

export const options = {
    duration: '30s', // Duración de la prueba
    vus: 20,        // Número de usuarios virtuales
    tags: {
        environment: 'local'  // Agrega una etiqueta para el entorno
    }
};

export default function () {
    const randomUrl = randomString(10);  // Genera una URL aleatoria de 10 caracteres
    const longUrl = `http://example.com/${randomUrl}`; // URL larga que será acortada
    const url = 'http://app:8000/url'; // Endpoint para crear URL corta

    console.log(`Creating short link for: ${longUrl}`);

    const response = http.post(url,
        JSON.stringify({ url: longUrl }),
        {
            headers: {
                'Content-Type': 'application/json',
            },
        });

    // Verifica que la respuesta sea 200 OK
    check(response, {
        'is status 200': (r) => r.status === 200,
    });
}
