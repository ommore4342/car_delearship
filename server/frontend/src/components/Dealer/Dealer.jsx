import React, { useState, useEffect } from 'react';

const sentimentIcon = (s) => {
  if (s === 'positive') return '😊';
  if (s === 'negative') return '😞';
  return '😐';
};

const sentimentColor = (s) => {
  if (s === 'positive') return '#d4edda';
  if (s === 'negative') return '#f8d7da';
  return '#fff3cd';
};

const Dealer = ({ dealerId, user }) => {
  const id = dealerId || window.location.pathname.split('/').pop();

  const [dealer,  setDealer]  = useState(null);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error,   setError]   = useState('');

  useEffect(() => {
    const load = async () => {
      try {
        const [dRes, rRes] = await Promise.all([
          fetch(`/djangoapp/dealer/${id}`),
          fetch(`/djangoapp/reviews/dealer/${id}`),
        ]);
        const dData = await dRes.json();
        const rData = await rRes.json();
        setDealer(dData.dealer);
        setReviews(rData.reviews || []);
      } catch {
        setError('Failed to load dealer information.');
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [id]);

  if (loading) return (
    <div style={{ textAlign: 'center', padding: 80 }}>
      <div className="spinner-border text-primary" role="status" />
      <p className="mt-3 text-muted">Loading dealer…</p>
    </div>
  );

  if (error) return (
    <div style={{ maxWidth: 700, margin: '60px auto', padding: 24, textAlign: 'center', color: '#c0303b' }}>{error}</div>
  );

  return (
    <div style={{ maxWidth: 900, margin: '0 auto', padding: '32px 16px' }}>

      {/* Dealer card */}
      {dealer && (
        <div style={{ background: '#fff', borderRadius: 14, padding: 28, boxShadow: '0 2px 16px rgba(0,0,0,.09)', marginBottom: 32 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap', gap: 12 }}>
            <div>
              <h1 style={{ color: '#1a3c5e', fontWeight: 700, fontSize: '1.7rem', margin: 0 }}>
                {dealer.full_name || dealer.dealer_name}
              </h1>
              <p style={{ color: '#555', marginTop: 6 }}>📍 {dealer.city}, {dealer.state} {dealer.zip}</p>
              <p style={{ color: '#777', fontSize: '0.9rem' }}>{dealer.address}</p>
              <p style={{ color: '#777', fontSize: '0.9rem' }}>📞 {dealer.phone || 'N/A'}</p>
            </div>
            {user && (
              <a
                href={`/postreview/${id}`}
                style={{
                  display: 'inline-block', background: '#e63946', color: '#fff',
                  padding: '10px 24px', borderRadius: 8, textDecoration: 'none', fontWeight: 700,
                  alignSelf: 'flex-start',
                }}
              >
                + Write a Review
              </a>
            )}
          </div>
        </div>
      )}

      {/* Reviews */}
      <h2 style={{ color: '#1a3c5e', fontWeight: 700, marginBottom: 18 }}>Customer Reviews ({reviews.length})</h2>

      {reviews.length === 0 ? (
        <div style={{ textAlign: 'center', padding: 50, background: '#fff', borderRadius: 12, color: '#999' }}>
          <p style={{ fontSize: '1.05rem' }}>No reviews yet. Be the first to review!</p>
        </div>
      ) : (
        reviews.map((r, i) => (
          <div
            key={i}
            style={{
              background: sentimentColor(r.sentiment),
              borderRadius: 12, padding: 20, marginBottom: 16,
              boxShadow: '0 2px 10px rgba(0,0,0,.07)',
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap', gap: 8, marginBottom: 8 }}>
              <span style={{ fontWeight: 700, color: '#1a3c5e' }}>
                {sentimentIcon(r.sentiment)} {r.name || 'Anonymous'}
              </span>
              <span style={{ color: '#888', fontSize: '0.83rem' }}>
                {r.purchase_date ? new Date(r.purchase_date).toLocaleDateString() : ''}
              </span>
            </div>

            <p style={{ color: '#333', margin: '0 0 10px', lineHeight: 1.6 }}>{r.review}</p>

            <div style={{ fontSize: '0.8rem', color: '#666', display: 'flex', gap: 16, flexWrap: 'wrap' }}>
              {r.car_make && <span>🚗 {r.car_make} {r.car_model} ({r.car_year})</span>}
              {r.purchase && <span>✅ Verified Purchase</span>}
              <span style={{
                background: r.sentiment === 'positive' ? '#28a745' : r.sentiment === 'negative' ? '#dc3545' : '#ffc107',
                color: '#fff', borderRadius: 20, padding: '2px 10px', fontWeight: 600,
              }}>
                {r.sentiment || 'neutral'}
              </span>
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default Dealer;
