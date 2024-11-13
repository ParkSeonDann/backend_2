if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/static/service-worker.js')
    .then((reg) => console.log('Service Worker registrado con éxito:', reg))
    .catch((err) => console.log('Error al registrar el Service Worker:', err));
}
