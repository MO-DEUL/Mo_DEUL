import React, { useState } from 'react';
import AppRouter from 'components/Router';

function App() {
  const [isLoggedIn, SetIsLoggedIn] = useState(false);
  return (
    <>
      <AppRouter isLoggedIn={isLoggedIn} />
      <footer>&copy; {new Date().getFullYear()} Modeul</footer>
    </>
  );
}

export default App;
