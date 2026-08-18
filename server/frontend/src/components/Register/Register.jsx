import React, { useState } from 'react';

const initialFormData = {
  userName: '',
  firstName: '',
  lastName: '',
  email: '',
  password: '',
};

const Register = ({ onClose }) => {
  const [formData, setFormData] = useState(initialFormData);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = ({ target }) => {
    setFormData((current) => ({
      ...current,
      [target.name]: target.value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setSuccess('');
    setLoading(true);

    try {
      const response = await fetch('/djangoapp/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      let data = {};
      try {
        data = await response.json();
      } catch {
        data = {};
      }

      if (!response.ok || data.error) {
        setError(data.error || 'Registration failed. Please check your details.');
        return;
      }

      setSuccess(`Welcome, ${data.userName || formData.userName}! Registration successful.`);

      setTimeout(() => {
        if (onClose) {
          onClose(data.userName || formData.userName);
        }
      }, 1200);
    } catch (requestError) {
      setError('Unable to connect to the server. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="register-title"
      style={{
        position: 'fixed',
        inset: 0,
        background: 'rgba(0, 0, 0, 0.55)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 20,
        zIndex: 9999,
        overflowY: 'auto',
      }}
    >
      <div
        style={{
          position: 'relative',
          background: '#ffffff',
          borderRadius: 14,
          padding: '34px 32px 28px',
          width: '100%',
          maxWidth: 460,
          boxShadow: '0 8px 32px rgba(0, 0, 0, 0.18)',
        }}
      >
        <button
          type="button"
          onClick={() => onClose && onClose(null)}
          aria-label="Close registration form"
          style={{
            position: 'absolute',
            top: 10,
            right: 14,
            background: 'none',
            border: 'none',
            fontSize: '1.5rem',
            lineHeight: 1,
            cursor: 'pointer',
            color: '#888',
          }}
        >
          &times;
        </button>

        <h2
          id="register-title"
          style={{
            color: '#1a3c5e',
            fontWeight: 700,
            marginBottom: 6,
          }}
        >
          Sign-up
        </h2>
        <p style={{ color: '#666', marginBottom: 24, fontSize: '0.93rem' }}>
          Create your Cars Dealership account to leave reviews and access exclusive features.
        </p>

        {error && <div className="alert alert-danger py-2">{error}</div>}
        {success && <div className="alert alert-success py-2">{success}</div>}

        <form onSubmit={handleSubmit} noValidate>
          <div className="mb-3">
            <label htmlFor="register-username" className="form-label fw-semibold">
              Username <span className="text-danger">*</span>
            </label>
            <input
              id="register-username"
              type="text"
              name="userName"
              className="form-control"
              placeholder="e.g. johndoe92"
              value={formData.userName}
              onChange={handleChange}
              autoComplete="username"
              required
            />
          </div>

          <div className="mb-3">
            <label htmlFor="register-first-name" className="form-label fw-semibold">
              First Name <span className="text-danger">*</span>
            </label>
            <input
              id="register-first-name"
              type="text"
              name="firstName"
              className="form-control"
              placeholder="John"
              value={formData.firstName}
              onChange={handleChange}
              autoComplete="given-name"
              required
            />
          </div>

          <div className="mb-3">
            <label htmlFor="register-last-name" className="form-label fw-semibold">
              Last Name <span className="text-danger">*</span>
            </label>
            <input
              id="register-last-name"
              type="text"
              name="lastName"
              className="form-control"
              placeholder="Doe"
              value={formData.lastName}
              onChange={handleChange}
              autoComplete="family-name"
              required
            />
          </div>

          <div className="mb-3">
            <label htmlFor="register-email" className="form-label fw-semibold">
              Email <span className="text-danger">*</span>
            </label>
            <input
              id="register-email"
              type="email"
              name="email"
              className="form-control"
              placeholder="john@example.com"
              value={formData.email}
              onChange={handleChange}
              autoComplete="email"
              required
            />
          </div>

          <div className="mb-4">
            <label htmlFor="register-password" className="form-label fw-semibold">
              Password <span className="text-danger">*</span>
            </label>
            <input
              id="register-password"
              type="password"
              name="password"
              className="form-control"
              placeholder="Minimum 8 characters"
              value={formData.password}
              onChange={handleChange}
              autoComplete="new-password"
              minLength={8}
              required
            />
          </div>

          <button
            type="submit"
            className="btn w-100"
            disabled={loading}
            style={{
              background: '#e63946',
              color: '#fff',
              fontWeight: 600,
              padding: '10px',
              borderRadius: 8,
              opacity: loading ? 0.75 : 1,
              cursor: loading ? 'not-allowed' : 'pointer',
            }}
          >
            {loading ? 'Registering...' : 'Register'}
          </button>
        </form>

        <p className="text-center mt-3" style={{ fontSize: '0.88rem', color: '#888' }}>
          Already have an account?{' '}
          <button
            type="button"
            onClick={() => onClose && onClose(null)}
            style={{
              background: 'none',
              border: 'none',
              color: '#1a3c5e',
              fontWeight: 600,
              cursor: 'pointer',
              padding: 0,
            }}
          >
            Sign In
          </button>
        </p>
      </div>
    </div>
  );
};

export default Register;
