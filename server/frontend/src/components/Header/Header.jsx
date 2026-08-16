import React, { useState } from 'react';
import Login from '../Login/Login';
import Register from '../Register/Register';

const Header = ({ user, setUser }) => {
  const [showLogin, setShowLogin]       = useState(false);
  const [showRegister, setShowRegister] = useState(false);

  const handleLogout = async () => {
    await fetch('/djangoapp/logout');
    setUser(null);
  };

  return (
    <>
      <nav style={{ background: '#1a3c5e', padding: '0 24px', display: 'flex', alignItems: 'center', height: 60 }}>
        <a href="/" style={{ color: '#fff', fontWeight: 700, fontSize: '1.3rem', textDecoration: 'none', flex: 1 }}>
          🚗 Cars Dealership
        </a>
        <div style={{ display: 'flex', gap: 16, alignItems: 'center' }}>
          <a href="/static/About.html"   style={{ color: 'rgba(255,255,255,.85)', textDecoration: 'none' }}>About</a>
          <a href="/static/Contact.html" style={{ color: 'rgba(255,255,255,.85)', textDecoration: 'none' }}>Contact</a>

          {user ? (
            <>
              <span style={{ color: '#fff', fontWeight: 600 }}>👤 {user}</span>
              <button
                onClick={handleLogout}
                style={{ background: '#e63946', border: 'none', color: '#fff', borderRadius: 6, padding: '6px 16px', cursor: 'pointer', fontWeight: 600 }}
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <button
                onClick={() => setShowLogin(true)}
                style={{ background: 'transparent', border: '1px solid rgba(255,255,255,.6)', color: '#fff', borderRadius: 6, padding: '6px 16px', cursor: 'pointer' }}
              >
                Login
              </button>
              <button
                onClick={() => setShowRegister(true)}
                style={{ background: '#e63946', border: 'none', color: '#fff', borderRadius: 6, padding: '6px 16px', cursor: 'pointer', fontWeight: 600 }}
              >
                Register
              </button>
            </>
          )}
        </div>
      </nav>

      {showLogin && (
        <Login
          onLogin={(username) => setUser(username)}
          onClose={() => setShowLogin(false)}
        />
      )}

      {showRegister && (
        <Register
          onClose={(username) => {
            setShowRegister(false);
            if (username) setUser(username);
          }}
        />
      )}
    </>
  );
};

export default Header;
