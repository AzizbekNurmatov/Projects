import React from 'react'

// Sample service data (same as in SearchPage)
const sampleServices = [
  {
    name: "Mike's Rapid Repairs",
    type: "plumbing",
    icon: "🔧",
    rating: 4.9,
    speed: 9.2,
    cost: 8.8,
    quality: 9.5,
    description: "24/7 emergency plumbing. Fixed my burst pipe in 30 minutes!",
    price: "$80-120/hr",
    reviews: 127,
    services: [
      { title: 'Emergency Leak Repair', price: '$120 flat', eta: '30-90 min', blurb: 'Rapid response for burst pipes and major leaks.' },
      { title: 'Drain Cleaning', price: '$90+', eta: 'Same day', blurb: 'Clears clogs with hydro-jet or snake.' },
      { title: 'Water Heater Repair', price: '$150+', eta: '1-2 days', blurb: 'Diagnostics and part replacement for most brands.' }
    ]
  },
  {
    name: "Clean Squad Pro",
    type: "cleaning",
    icon: "🏠",
    rating: 4.8,
    speed: 9.5,
    cost: 9.1,
    quality: 9.3,
    description: "Eco-friendly deep cleaning. They're magicians!",
    price: "$25-35/hr",
    reviews: 89,
    services: [
      { title: 'Standard Home Cleaning', price: '$30/hr', eta: '2-4 hrs', blurb: 'Kitchen, bathrooms, floors, and surfaces.' },
      { title: 'Deep Cleaning', price: '$35/hr', eta: '4-6 hrs', blurb: 'Inside appliances, baseboards, detailed attention.' },
      { title: 'Move-in/Move-out', price: '$40/hr', eta: 'Half-day', blurb: 'Full reset ready for handover.' }
    ]
  },
  {
    name: "QuickFix Auto",
    type: "auto",
    icon: "🚗",
    rating: 4.7,
    speed: 8.9,
    cost: 9.0,
    quality: 9.2,
    description: "Honest pricing, no upsells. Fixed my car same day.",
    price: "$95-150/hr",
    reviews: 156,
    services: [
      { title: 'Oil Change', price: '$65', eta: '45 min', blurb: 'Full synthetic with filter.' },
      { title: 'Brake Pad Replacement', price: '$220 axle', eta: '2 hrs', blurb: 'Includes parts and labor.' },
      { title: 'Check Engine Diagnostics', price: '$95', eta: '1 hr', blurb: 'OBD-II scan and report.' }
    ]
  },
  {
    name: "Spark Masters",
    type: "electrical",
    icon: "⚡",
    rating: 4.9,
    speed: 8.7,
    cost: 8.5,
    quality: 9.8,
    description: "Licensed electricians. Rewired my house perfectly.",
    price: "$120-180/hr",
    reviews: 203,
    services: [
      { title: 'Outlet/Switch Install', price: '$120', eta: '1-2 hrs', blurb: 'Add or replace outlets and switches.' },
      { title: 'Lighting Upgrade', price: '$180+', eta: '2-4 hrs', blurb: 'Recessed, pendants, and smart lighting.' },
      { title: 'Panel Upgrade', price: '$1,800+', eta: '1-2 days', blurb: 'Modernize and increase capacity.' }
    ]
  },
  {
    name: "Green Thumb Co",
    type: "landscaping",
    icon: "🌱",
    rating: 4.6,
    speed: 8.3,
    cost: 9.2,
    quality: 9.1,
    description: "Transformed my backyard into paradise!",
    price: "$50-75/hr",
    reviews: 74,
    services: [
      { title: 'Lawn Mowing', price: '$45', eta: 'Weekly', blurb: 'Trim, edge, and blow off.' },
      { title: 'Mulch & Beds', price: '$200+', eta: '1 day', blurb: 'Refresh beds and install seasonal plants.' },
      { title: 'Hedge Trimming', price: '$90+', eta: '2-3 hrs', blurb: 'Shape and clean up shrubs.' }
    ]
  },
  {
    name: "Cool Breeze HVAC",
    type: "hvac",
    icon: "❄️",
    rating: 4.8,
    speed: 8.8,
    cost: 8.6,
    quality: 9.4,
    description: "Installed new AC unit. Professional and clean work.",
    price: "$110-160/hr",
    reviews: 112,
    services: [
      { title: 'AC Tune-Up', price: '$129', eta: '90 min', blurb: '21-point inspection and cleaning.' },
      { title: 'Thermostat Install', price: '$149', eta: '1-2 hrs', blurb: 'Smart thermostat setup.' },
      { title: 'Emergency No-Cool', price: '$199+', eta: 'Same day', blurb: 'Priority diagnostics and fix.' }
    ]
  }
]

const DetailsPage = ({ selectedServiceIndex, showPage, openQuote }) => {
  const svc = sampleServices[selectedServiceIndex]

  if (!svc) {
    return (
      <div id="details-page">
        <section className="search-page">
          <div className="search-container">
            <div className="search-header">
              <h1>Service Not Found</h1>
              <p style={{ color: 'rgba(255, 255, 255, 0.8)', fontSize: '1.2rem' }}>The requested service could not be found.</p>
            </div>
            <div style={{ marginBottom: '2rem', display: 'flex', gap: '1rem' }}>
              <button className="btn-secondary" onClick={() => showPage('search')}>⬅ Back to results</button>
            </div>
          </div>
        </section>
      </div>
    )
  }

  const servicesList = (svc.services && svc.services.length ? svc.services : [
    { title: 'General Service', price: svc.price || '$—', eta: 'Varies', blurb: 'Contact for details and availability.' }
  ])

  return (
    <div id="details-page">
      <section className="search-page">
        <div className="search-container">
          <div className="search-header">
            <h1 id="details-title">{svc.name}</h1>
            <p style={{ color: 'rgba(255, 255, 255, 0.8)', fontSize: '1.2rem' }}>Explore services, pricing, and availability</p>
          </div>

          <div style={{ marginBottom: '2rem', display: 'flex', gap: '1rem' }}>
            <button className="btn-secondary" onClick={() => showPage('search')}>⬅ Back to results</button>
            <button className="btn-primary" onClick={() => openQuote(svc.name)}>💬 Get Quote</button>
          </div>

          <div id="details-content" className="search-results">
            <div className="service-card" style={{ gridColumn: '1/-1' }}>
              <div className="service-header">
                <div className="service-avatar">{svc.icon}</div>
                <div className="service-info">
                  <h3>{svc.name}</h3>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                    <div className="rating-stars">⭐ {svc.rating}</div>
                    <div style={{ color: 'rgba(255,255,255,0.6)' }}>{svc.reviews} reviews</div>
                  </div>
                </div>
              </div>
              <p style={{ color: 'rgba(255,255,255,0.85)' }}>{svc.description}</p>
            </div>
            {servicesList.map((item, idx) => (
              <div key={idx} className="service-card">
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '1rem' }}>
                  <div>
                    <h3 style={{ marginBottom: '0.5rem' }}>{item.title}</h3>
                    <div style={{ color: 'rgba(255,255,255,0.75)' }}>{item.blurb}</div>
                  </div>
                  <div style={{ textAlign: 'right' }}>
                    <div style={{ color: 'var(--accent)', fontWeight: 600 }}>{item.price}</div>
                    <div style={{ color: 'rgba(255,255,255,0.6)', fontSize: '0.9rem' }}>ETA: {item.eta}</div>
                  </div>
                </div>
                <div style={{ display: 'flex', gap: '0.75rem', marginTop: '1rem' }}>
                  <button 
                    className="btn-secondary" 
                    onClick={() => openQuote(svc.name, item.title)}
                  >
                    Add to quote
                  </button>
                  <button 
                    className="btn-primary" 
                    onClick={() => openQuote(svc.name, item.title)}
                  >
                    Book inquiry
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}

export default DetailsPage
