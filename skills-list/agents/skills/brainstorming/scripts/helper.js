(function() {
  const MIN_RECONNECT_MS = 500;
  const MAX_RECONNECT_MS = 30000;
  const TOMBSTONE_AFTER_MS = 15000;

  function nextReconnectDelay(current, max) {
    return Math.min(current * 2, max);
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { nextReconnectDelay, MIN_RECONNECT_MS, MAX_RECONNECT_MS, TOMBSTONE_AFTER_MS };
  }
  if (typeof window === 'undefined') return;

  let ws = null, eventQueue = [], reconnectDelay = MIN_RECONNECT_MS, reconnectTimer = null;
  let disconnectedSince = null, everConnected = false, tombstoneShown = false;

  function sessionKey() {
    try { return window.sessionStorage && window.sessionStorage.getItem('brainstorm-session-key'); } catch (e) {}
    return null;
  }
  function websocketUrl() {
    const key = sessionKey();
    return 'ws://' + window.location.host + (key ? '/?key=' + encodeURIComponent(key) : '');
  }
  function setStatus(state) { /* connection status pill */ }
  function showTombstone() { /* paused overlay */ }
  function connect() { /* WebSocket connection with reconnection logic */ }
  function sendEvent(event) { /* queue or send event */ }

  document.addEventListener('click', (e) => {
    const target = e.target.closest('[data-choice]');
    if (!target) return;
    sendEvent({ type: 'click', text: target.textContent.trim(), choice: target.dataset.choice, id: target.id || null });
  });

  window.toggleSelect = function(el) {
    const container = el.closest('.options') || el.closest('.cards');
    const multi = container && container.dataset.multiselect !== undefined;
    if (container && !multi) container.querySelectorAll('.option, .card').forEach(o => o.classList.remove('selected'));
    if (multi) { el.classList.toggle('selected'); } else { el.classList.add('selected'); }
    window.selectedChoice = el.dataset.choice;
  };

  window.brainstorm = { send: sendEvent, choice: (value, metadata = {}) => sendEvent({ type: 'choice', value, ...metadata }) };
  connect();
})();