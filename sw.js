const CACHE = 'viewer-cache-v1';
const ASSETS = [
  './viewer.html',
  './icons/icon-180.png',
  './icons/icon-192.png',
  './icons/icon-512.png'
  // 사용 중인 로컬 리소스가 더 있으면 여기에 추가 (예: './data/sample.json')
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
});

self.addEventListener('fetch', (e) => {
  // 캐시 우선 → 약한 네트워크/완전 오프라인에서도 즉시 응답
  e.respondWith(
    caches.match(e.request).then(res => res || fetch(e.request))
  );
});
