import http from 'k6/http';
import { check, sleep } from 'k6';
import { randomString } from 'https://jslib.k6.io/k6-utils/1.1.0/index.js';

export const options = {
    duration: '30s',
    vus: 20,
    tags: {
        environment: 'prod'
    }
};

export default function () {
    const randomUrl = randomString(10);
    const longUrl = `http://example.com/${randomUrl}`;
    const url = 'https://cliper.gfarias.cl/url';

    console.log(`Creating short link for: ${longUrl}`);

    const response = http.post(url, JSON.stringify({ url: longUrl }), { headers: { 'Content-Type': 'application/json' } });

    check(response, {
        'is status 200': (r) => r.status === 200,
    });
}
