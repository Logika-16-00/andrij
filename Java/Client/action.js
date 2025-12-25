function leaveLobby() {
  // очистити multiplayer меню
  const multiplayerMenu = document.querySelector('.menu--multiplayer');
  if (multiplayerMenu) {
    multiplayerMenu.innerHTML = `
      <h1>MULTIPLAYER</h1>
      <div class="multiplayer-items"></div>
      <button id="createLobbyBtn">CREATE LOBBY</button>
    `;
  }

  // показати головне меню
  setActiveMenu(MENU_MAIN);
}