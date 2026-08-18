import React, { useState } from 'react';

const Register = ({ onClose }) => {
  const [formData, setFormData] = useState({
    userName: '',
    firstName: '',
    lastName: '',
    email: '',
    password: '',
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    try {
      const res = await fetch('/djangoapp/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const data = await res.json();
      if (data.error) {
        setError(data.error);
      } else {
        setSuccess(`Welcome, ${data.userName}! Registration successful.`);
        setTimeout(() => { if (onClose) onClose(data.userName); }, 1500);
      }
    } catch (err) {
      setError('Registration failed. Please try again.');
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
          width: '100%', maxWidth: 440, boxShadow: '0 8px 32px rgba(0,0,0,.18)',
        }}
      >
        <h2 style={{ color: '#1a3c5e', fontWeight: 700, marginBottom: 6 }}>Create Account</h2>
        <p style={{ color: '#666', marginBottom: 24, fontSize: '0.93rem' }}>
          Sign up to leave reviews and access exclusive features.
        </p>

        {error   && <div className="alert alert-danger py-2">{error}</div>}
        {success && <div className="alert alert-success py-2">{success}</div>}

        <form onSubmit={handleSubmit}>
          {/* Username */}
          <div className="mb-3">
            <label className="form-label fw-semibold">Username <span className="text-danger">*</span></label>
            <input
              type="text"
              name="userName"
              className="form-control"
              placeholder="e.g. johndoe92"
              value={formData.userName}
              onChange={handleChange}
              required
            />
          </div>

          {/* First Name */}
          <div className="mb-3">
            <label className="form-label fw-semibold">First Name <span className="text-danger">*</span></label>
            <input
              type="text"
              name="firstName"
              className="form-control"
              placeholder="John"
              value={formData.firstName}
              onChange={handleChange}
              required
            />
          </div>

          {/* Last Name */}
          <div className="mb-3">
            <label className="form-label fw-semibold">Last Name <span className="text-danger">*</span></label>
            <input
              type="text"
              name="lastName"
              className="form-control"
              placeholder="Doe"
              value={formData.lastName}
              onChange={handleChange}
              required
            />
          </div>

          {/* Email */}
          <div className="mb-3">
            <label className="form-label fw-semibold">Email Address <span className="text-danger">*</span></label>
            <input
              type="email"
              name="email"
              className="form-control"
              placeholder="john@example.com"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>

          {/* Password */}
          <div className="mb-4">
            <label className="form-label fw-semibold">Password <span className="text-danger">*</span></label>
            <input
              type="password"
              name="password"
              className="form-control"
              placeholder="Min. 8 characters"
              value={formData.password}
              onChange={handleChange}
              required
              minLength={8}
            />
          </div>

          <button
            type="submit"
            className="btn w-100"
            style={{ background: '#e63946', color: '#fff', fontWeight: 600, padding: '10px', borderRadius: 8 }}
          >
            Register
          </button>
        </form>

        <p className="text-center mt-3" style={{ fontSize: '0.88rem', color: '#888' }}>
          Already have an account?{' '}
          <button
            onClick={() => { if (onClose) onClose(null); }}
            style={{ background: 'none', border: 'none', color: '#1a3c5e', fontWeight: 600, cursor: 'pointer', padding: 0 }}
          >
            Sign In
          </button>
        </p>

        <button
          onClick={() => { if (onClose) onClose(null); }}
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

export default Register;
