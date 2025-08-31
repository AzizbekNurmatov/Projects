import React from 'react'

const HomePage = ({ showPage }) => {
  return (
    <div id="home-page">
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <div className="hero-text">
              <h1>Your Local Service Universe</h1>
              <p className="hero-subtitle">Discover trusted service providers with radical transparency. Real ratings for speed, cost & effectiveness from your actual neighbors.</p>
              <div className="hero-actions">
                <a href="#" className="btn-primary" onClick={(e) => { e.preventDefault(); showPage('search') }}>
                  🚀 Explore Services
                </a>
                <a href="#" className="btn-secondary">
                  💼 List Your Business
                </a>
              </div>
            </div>
            <div className="hero-visual">
              <div className="floating-card">
                <div className="card-header">
                  <div className="service-icon" style={{ background: 'linear-gradient(135deg, var(--accent), var(--primary))' }}>🔧</div>
                  <div>
                    <div style={{ fontWeight: 600 }}>Mike's Repairs</div>
                    <div className="rating-stars">⭐⭐⭐⭐⭐ 4.9</div>
                  </div>
                </div>
                <div className="service-stats">
                  <div><strong>⚡ Speed:</strong> 9.2</div>
                  <div><strong>💰 Cost:</strong> 8.8</div>
                  <div><strong>✨ Quality:</strong> 9.5</div>
                </div>
              </div>
              <div className="floating-card">
                <div className="card-header">
                  <div className="service-icon" style={{ background: 'linear-gradient(135deg, var(--secondary), var(--accent))' }}>🏠</div>
                  <div>
                    <div style={{ fontWeight: 600 }}>Clean Squad</div>
                    <div className="rating-stars">⭐⭐⭐⭐⭐ 4.8</div>
                  </div>
                </div>
                <div className="service-stats">
                  <div><strong>⚡ Speed:</strong> 9.5</div>
                  <div><strong>💰 Cost:</strong> 9.1</div>
                  <div><strong>✨ Quality:</strong> 9.3</div>
                </div>
              </div>
              <div className="floating-card">
                <div className="card-header">
                  <div className="service-icon" style={{ background: 'linear-gradient(135deg, var(--primary), var(--secondary))' }}>🚗</div>
                  <div>
                    <div style={{ fontWeight: 600 }}>Quick Fix Auto</div>
                    <div className="rating-stars">⭐⭐⭐⭐⭐ 4.7</div>
                  </div>
                </div>
                <div className="service-stats">
                  <div><strong>⚡ Speed:</strong> 8.9</div>
                  <div><strong>💰 Cost:</strong> 9.0</div>
                  <div><strong>✨ Quality:</strong> 9.2</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="features">
        <div className="container">
          <div className="features-header">
            <h2>Why We're Different</h2>
            <p style={{ color: 'rgba(255, 255, 255, 0.8)', fontSize: '1.2rem' }}>No more guessing games. Real transparency for real people.</p>
          </div>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">⚡</div>
              <h3>Radical Transparency</h3>
              <p>Speed, Cost, Effectiveness ratings from actual customers. No fluff, no fake reviews, just brutal honesty.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🎯</div>
              <h3>Hyper-Local Focus</h3>
              <p>Find hidden gems in your exact neighborhood. Small businesses that big platforms ignore.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">💬</div>
              <h3>Instant Quotes</h3>
              <p>Get quotes from multiple providers in minutes. Compare and decide without the runaround.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🛡️</div>
              <h3>Trust by Design</h3>
              <p>Verified reviews, real photos, and transparent pricing. Know exactly what you're getting.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🚀</div>
              <h3>Lightning Fast</h3>
              <p>Book services in under 60 seconds. No forms, no hassle, just results.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">💎</div>
              <h3>Support Local</h3>
              <p>Empower neighborhood businesses. Your money stays in your community.</p>
            </div>
          </div>
        </div>
      </section>

      <section className="cta-section">
        <div className="container">
          <div className="cta-content">
            <h2>Ready to Find Amazing Services?</h2>
            <p>Join thousands who've discovered their go-to local providers</p>
            <div className="hero-actions">
              <a href="#" className="btn-primary" onClick={(e) => { e.preventDefault(); showPage('search') }}>
                🚀 Start Exploring
              </a>
              <a href="#" className="btn-secondary">
                💼 List Your Business
              </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default HomePage
