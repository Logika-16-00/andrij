const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 8080 });
console.log("Lobby server running on ws://localhost:8080");

let lobbies = [];
// lobby = { id, host, players: [socketId] }

function broadcastLobbies() {
  const data = JSON.stringify({
    type: "LOBBY_LIST",
    lobbies: lobbies.map(l => ({
      id: l.id,
      host: l.host,
      count: l.players.length
    }))
  });

  wss.clients.forEach(c => {
    if (c.readyState === WebSocket.OPEN) {
      c.send(data);
    }
  });
}

wss.on("connection", ws => {
  ws.id = Math.random().toString(36).slice(2);

  // одразу відправляємо АКТУАЛЬНИЙ список
  broadcastLobbies();

  ws.on("message", msg => {
    const data = JSON.parse(msg);

    // CREATE LOBBY
    if (data.type === "CREATE_LOBBY") {
      // ❗ НЕ дозволяємо створювати більше 1 лобі з одного клієнта
      if (lobbies.some(l => l.players.includes(ws.id))) return;

      lobbies.push({
        id: Date.now(),
        host: data.name,
        players: [ws.id]
      });

      broadcastLobbies();
    }

    // JOIN LOBBY
    if (data.type === "JOIN_LOBBY") {
      const lobby = lobbies.find(l => l.id === data.id);
      if (!lobby) return;

      // ❗ НЕ дозволяємо JOIN повторно
      if (lobby.players.includes(ws.id)) return;

      lobby.players.push(ws.id);
      broadcastLobbies();
    }
  });

  ws.on("close", () => {
    lobbies.forEach(l => {
      l.players = l.players.filter(id => id !== ws.id);
    });

    lobbies = lobbies.filter(l => l.players.length > 0);
    broadcastLobbies();
  });
});
