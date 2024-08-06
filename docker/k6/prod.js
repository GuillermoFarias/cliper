import http from 'k6/http';
import { check } from 'k6';
import { randomString } from 'https://jslib.k6.io/k6-utils/1.1.0/index.js';

export const options = {
    duration: '30s',
    vus: 30,
    tags: {
        environment: 'prod'
    }
};

export default function () {
    const url = 'https://cliper.gfarias.cl/ping';
    const response = http.get(url);

    check(response, {
        'is status 200': (r) => r.status === 200,
    });
}

