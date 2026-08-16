import React, { useState } from 'react';
import Header  from './components/Header/Header';
import Dealers from './components/Dealers/Dealers';
import Dealer  from './components/Dealer/Dealer';
import PostReview from './components/PostReview/PostReview';

const getPage = () => {
  const path = window.location.pathname;
  if (path.startsWith('/dealer/'))     return 'dealer';
  if (path.startsWith('/postreview/')) return 'postreview';
  return 'home';
};

function App() {
  const [user, setUser] = useState(null);
  const page = getPage();

  return (
    <div style={{ minHeight: '100vh', background: '#f0f2f5', fontFamily: "'Segoe UI', sans-serif" }}>
      <Header user={user} setUser={setUser} />
      <main>
        {page === 'home'       && <Dealers user={user} />}
        {page === 'dealer'     && <Dealer  user={user} />}
        {page === 'postreview' && <PostReview user={user} />}
      </main>
    </div>
  );
}

export default App;
