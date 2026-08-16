import React, { useState, useEffect } from 'react';

const PostReview = ({ user }) => {
  const dealerId = window.location.pathname.split('/').pop();

  const [dealer,   setDealer]   = useState(null);
  const [carMakes, setCarMakes] = useState([]);
  const [formData, setFormData] = useState({
    review: '',
    purchase: false,
    purchase_date: '',
    car_make: '',
    car_model: '',
    car_year: new Date().getFullYear(),
  });
  const [submitted, setSubmitted] = useState(false);
  const [error,     setError]     = useState('');

  useEffect(() => {
    // Load dealer info
    fetch(`/djangoapp/dealer/${dealerId}`)
      .then(r => r.json())
      .then(d => setDealer(d.dealer))
      .catch(() => {});

    // Load car makes
    fetch('/djangoapp/get_cars')
      .then(r => r.json())
      .then(d => setCarMakes(d.CarMakes || []))
      .catch(() => {});
  }, [dealerId]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({ ...prev, [name]: type === 'checkbox' ? checked : value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    const reviewPayload = {
      review: {
        name: user,
        dealership: Number(dealerId),
        review: formData.review,
        purchase: formData.purchase,
        purchase_date: formData.purchase_date,
        car_make: formData.car_make,
        car_model: formData.car_model,
        car_year: Number(formData.car_year),
        id: Date.now(),
      },
    };

    try {
      const res = await fetch('/djangoapp/add_review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(reviewPayload),
      });
      const data = await res.json();
      if (data.status === 200) {
        setSubmitted(true);
      } else {
        setError(data.error || 'Failed to submit review.');
      }
    } catch {
      setError('Network error. Please try again.');
    }
  };

  if (!user) {
    return (
      <div style={{ textAlign: 'center', padding: 80 }}>
        <h2 style={{ color: '#c0303b' }}>Please log in to write a review.</h2>
        <a href="/" style={{ color: '#1a3c5e', fontWeight: 600 }}>← Back to Home</a>
      </div>
    );
  }

  if (submitted) {
    return (
      <div style={{ textAlign: 'center', padding: 80 }}>
        <div style={{ fontSize: '3rem' }}>🎉</div>
        <h2 style={{ color: '#28a745', fontWeight: 700 }}>Review Submitted!</h2>
        <p style={{ color: '#666' }}>Thank you for sharing your experience.</p>
        <a
          href={`/dealer/${dealerId}`}
          style={{ display: 'inline-block', marginTop: 16, background: '#1a3c5e', color: '#fff', padding: '10px 24px', borderRadius: 8, textDecoration: 'none', fontWeight: 600 }}
        >
          View All Reviews
        </a>
      </div>
    );
  }

  const currentYear = new Date().getFullYear();
  const years = Array.from({ length: 30 }, (_, i) => currentYear - i);

  return (
    <div style={{ maxWidth: 680, margin: '0 auto', padding: '32px 16px' }}>
      <h1 style={{ color: '#1a3c5e', fontWeight: 700, marginBottom: 4 }}>
        Write a Review
      </h1>
      {dealer && (
        <p style={{ color: '#666', marginBottom: 28 }}>
          for <strong>{dealer.full_name || dealer.dealer_name}</strong> — {dealer.city}, {dealer.state}
        </p>
      )}

      {error && <div className="alert alert-danger">{error}</div>}

      <form onSubmit={handleSubmit} style={{ background: '#fff', borderRadius: 14, padding: 28, boxShadow: '0 2px 16px rgba(0,0,0,.09)' }}>

        <div className="mb-3">
          <label className="form-label fw-semibold">Your Review <span className="text-danger">*</span></label>
          <textarea
            name="review"
            className="form-control"
            rows={5}
            placeholder="Share your experience with this dealership…"
            value={formData.review}
            onChange={handleChange}
            required
          />
        </div>

        <div className="mb-3 form-check">
          <input
            type="checkbox"
            name="purchase"
            className="form-check-input"
            id="purchase"
            checked={formData.purchase}
            onChange={handleChange}
          />
          <label className="form-check-label fw-semibold" htmlFor="purchase">
            I purchased a vehicle at this dealership
          </label>
        </div>

        {formData.purchase && (
          <div className="mb-3">
            <label className="form-label fw-semibold">Purchase Date</label>
            <input
              type="date"
              name="purchase_date"
              className="form-control"
              value={formData.purchase_date}
              onChange={handleChange}
            />
          </div>
        )}

        <div className="row">
          <div className="col-md-4 mb-3">
            <label className="form-label fw-semibold">Car Make</label>
            <select name="car_make" className="form-select" value={formData.car_make} onChange={handleChange}>
              <option value="">-- Select Make --</option>
              {carMakes.map(m => <option key={m.name} value={m.name}>{m.name}</option>)}
            </select>
          </div>

          <div className="col-md-4 mb-3">
            <label className="form-label fw-semibold">Car Model</label>
            <input
              type="text"
              name="car_model"
              className="form-control"
              placeholder="e.g. Camry"
              value={formData.car_model}
              onChange={handleChange}
            />
          </div>

          <div className="col-md-4 mb-3">
            <label className="form-label fw-semibold">Car Year</label>
            <select name="car_year" className="form-select" value={formData.car_year} onChange={handleChange}>
              {years.map(y => <option key={y} value={y}>{y}</option>)}
            </select>
          </div>
        </div>

        <div style={{ display: 'flex', gap: 12, marginTop: 8 }}>
          <button
            type="submit"
            style={{ background: '#e63946', border: 'none', color: '#fff', padding: '11px 28px', borderRadius: 8, fontWeight: 700, fontSize: '1rem', cursor: 'pointer' }}
          >
            Submit Review
          </button>
          <a
            href={`/dealer/${dealerId}`}
            style={{ display: 'inline-flex', alignItems: 'center', color: '#1a3c5e', textDecoration: 'none', fontWeight: 600 }}
          >
            ← Cancel
          </a>
        </div>
      </form>
    </div>
  );
};

export default PostReview;
