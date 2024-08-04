import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    duration: '30s', // Duración de la prueba
    vus: 20,        // Número de usuarios virtuales
};

export default function () {
    console.log('Ping');
    // send body {"url":"http://app:8000/ping"}
    const url = 'http://app:8000/ping';
    const response = http.post(url,
        JSON.stringify({ url: url }),
        {
            headers: {
                'Content-Type': 'application/json',
            },
        });

    // Verifica que la respuesta sea 200 OK
    check(response, {
        'is status 200': (r) => r.status === 200,
    });

    // Agrega un pequeño retraso entre las solicitudes
    sleep(1);
}