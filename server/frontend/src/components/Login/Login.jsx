import React, { useState } from 'react';

const Login = ({ onClose, onLogin }) => {
  const [formData, setFormData] = useState({ userName: '', password: '' });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const res = await fetch('/djangoapp/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const data = await res.json();
      if (data.error) {
        setError(data.error);
      } else {
        if (onLogin) onLogin(data.userName);
        if (onClose) onClose();
      }
    } catch {
      setError('Login failed. Please try again.');
    }
  };

  return (
    <div
      style={{
        position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.55)',
        display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999,
      }}
    >
      <div
        style={{
          background: '#fff', borderRadius: 14, padding: '38px 36px',
          width: '100%', maxWidth: 400, boxShadow: '0 8px 32px rgba(0,0,0,.18)', position: 'relative',
        }}
      >
        <h2 style={{ color: '#1a3c5e', fontWeight: 700, marginBottom: 6 }}>Sign In</h2>
        <p style={{ color: '#666', marginBottom: 24, fontSize: '0.93rem' }}>
          Welcome back! Enter your credentials to continue.
        </p>

        {error && <div className="alert alert-danger py-2">{error}</div>}

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label fw-semibold">Username</label>
            <input
              type="text"
              name="userName"
              className="form-control"
              placeholder="Your username"
              value={formData.userName}
              onChange={handleChange}
              required
            />
          </div>

          <div className="mb-4">
            <label className="form-label fw-semibold">Password</label>
            <input
              type="password"
              name="password"
              className="form-control"
              placeholder="Your password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>

          <button
            type="submit"
            className="btn w-100"
            style={{ background: '#1a3c5e', color: '#fff', fontWeight: 600, padding: '10px', borderRadius: 8 }}
          >
            Sign In
          </button>
        </form>

        <button
          onClick={() => { if (onClose) onClose(); }}
          style={{
            position: 'absolute', top: 14, right: 18,
            background: 'none', border: 'none', fontSize: '1.4rem', cursor: 'pointer', color: '#aaa',
          }}
          aria-label="Close"
        >
          &times;
        </button>
      </div>
    </div>
  );
};

export default Login;
