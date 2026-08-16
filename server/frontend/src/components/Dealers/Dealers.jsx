import React, { useState, useEffect } from 'react';

const US_STATES = [
  'All','Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut',
  'Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
  'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan',
  'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire',
  'New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio',
  'Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota',
  'Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia',
  'Wisconsin','Wyoming',
];

const Dealers = ({ user }) => {
  const [dealers, setDealers]   = useState([]);
  const [state, setState]       = useState('All');
  const [loading, setLoading]   = useState(false);
  const [error, setError]       = useState('');

  const fetchDealers = async (selectedState) => {
    setLoading(true);
    setError('');
    const url = selectedState === 'All'
      ? '/djangoapp/get_dealers'
      : `/djangoapp/get_dealers/${selectedState}`;

    try {
      const res  = await fetch(url);
      const data = await res.json();
      setDealers(data.dealers || []);
    } catch {
      setError('Failed to load dealerships. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchDealers('All'); }, []);

  const handleStateChange = (e) => {
    const val = e.target.value;
    setState(val);
    fetchDealers(val);
  };

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto', padding: '32px 16px' }}>

      {/* Header row */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 28, flexWrap: 'wrap', gap: 14 }}>
        <div>
          <h1 style={{ color: '#1a3c5e', fontWeight: 700, margin: 0, fontSize: '1.9rem' }}>Find a Dealership</h1>
          <p style={{ color: '#666', margin: '4px 0 0' }}>Browse our nationwide network of trusted dealers</p>
        </div>

        {/* State filter */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <label style={{ fontWeight: 600, color: '#1a3c5e' }}>Filter by State:</label>
          <select
            value={state}
            onChange={handleStateChange}
            style={{ padding: '8px 14px', borderRadius: 8, border: '1px solid #ccc', fontSize: '0.95rem', cursor: 'pointer' }}
          >
            {US_STATES.map(s => <option key={s} value={s}>{s}</option>)}
          </select>
        </div>
      </div>

      {/* Error */}
      {error && <div style={{ background: '#fde8ea', color: '#c0303b', padding: '12px 18px', borderRadius: 8, marginBottom: 20 }}>{error}</div>}

      {/* Loading */}
      {loading && (
        <div style={{ textAlign: 'center', padding: 60, color: '#666' }}>
          <div className="spinner-border text-primary" role="status" />
          <p className="mt-3">Loading dealerships…</p>
        </div>
      )}

      {/* Dealer grid */}
      {!loading && !error && (
        <>
          <p style={{ color: '#888', marginBottom: 20 }}>{dealers.length} dealership{dealers.length !== 1 ? 's' : ''} found</p>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: 20 }}>
            {dealers.map((dealer) => (
              <div
                key={dealer.id}
                style={{
                  background: '#fff', borderRadius: 12, padding: 22,
                  boxShadow: '0 2px 14px rgba(0,0,0,.08)',
                  transition: 'transform .2s, box-shadow .2s',
                  cursor: 'pointer',
                }}
                onMouseEnter={e => { e.currentTarget.style.transform = 'translateY(-4px)'; e.currentTarget.style.boxShadow = '0 6px 22px rgba(0,0,0,.13)'; }}
                onMouseLeave={e => { e.currentTarget.style.transform = 'none'; e.currentTarget.style.boxShadow = '0 2px 14px rgba(0,0,0,.08)'; }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <h3 style={{ color: '#1a3c5e', fontWeight: 700, fontSize: '1.05rem', margin: 0 }}>
                    {dealer.full_name || dealer.dealer_name || 'Dealership'}
                  </h3>
                  <span style={{ background: '#e8f0fe', color: '#1a3c5e', borderRadius: 20, padding: '2px 10px', fontSize: '0.78rem', fontWeight: 600 }}>
                    #{dealer.id}
                  </span>
                </div>

                <p style={{ color: '#555', margin: '8px 0 4px', fontSize: '0.88rem' }}>
                  📍 {dealer.city}, {dealer.state} {dealer.zip}
                </p>
                <p style={{ color: '#777', fontSize: '0.84rem', margin: '2px 0' }}>
                  {dealer.address}
                </p>
                <p style={{ color: '#777', fontSize: '0.84rem', margin: '2px 0 14px' }}>
                  📞 {dealer.phone || 'N/A'}
                </p>

                <a
                  href={`/dealer/${dealer.id}`}
                  style={{
                    display: 'inline-block', background: '#1a3c5e', color: '#fff',
                    padding: '7px 18px', borderRadius: 7, textDecoration: 'none', fontSize: '0.87rem', fontWeight: 600,
                    marginRight: 8,
                  }}
                >
                  View Details
                </a>

                {user && (
                  <a
                    href={`/postreview/${dealer.id}`}
                    style={{
                      display: 'inline-block', background: '#e63946', color: '#fff',
                      padding: '7px 18px', borderRadius: 7, textDecoration: 'none', fontSize: '0.87rem', fontWeight: 600,
                    }}
                  >
                    Review Dealer
                  </a>
                )}
              </div>
            ))}
          </div>

          {dealers.length === 0 && !loading && (
            <div style={{ textAlign: 'center', padding: 60, color: '#999' }}>
              <p style={{ fontSize: '1.1rem' }}>No dealerships found for the selected state.</p>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default Dealers;
