import React, { useState } from 'react'

/**
 * SearchPage Component - Service discovery and filtering interface
 * 
 * This component provides:
 * - Search form with location, service type, and urgency filters
 * - Radius selector for geographic search scope
 * - Dynamic results display with service cards
 * - Integration with quote modal and details page
 */

// Sample service data - represents local service providers with ratings
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

const SearchPage = ({ selectedRadius, setSelectedRadius, openQuote, openDetails }) => {
  // Search state management
  const [searchResults, setSearchResults] = useState([])
  const [hasSearched, setHasSearched] = useState(false)
  const [formData, setFormData] = useState({
    location: '',
    service: '',
    urgency: ''
  })

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const selectRadius = (radius) => {
    setSelectedRadius(radius)
  }

  // Main search function - filters and sorts services based on user input
  const searchServices = () => {
    const { service, location, urgency } = formData

    // Form validation
    if (!location) {
      alert('Please enter your location')
      return
    }

    if (!service) {
      alert('Please select a service type')
      return
    }

    // Filter services based on selected service type
    let results = sampleServices.filter(serviceItem => 
      service === '' || serviceItem.type === service
    )

    // Sort by speed rating for urgent requests
    if (urgency === 'asap') {
      results = results.sort((a, b) => b.speed - a.speed)
    }

    setSearchResults(results)
    setHasSearched(true)
  }

  const displayResults = () => {
    if (!hasSearched) return null

    if (searchResults.length === 0) {
      return (
        <div style={{ textAlign: 'center', color: 'rgba(255, 255, 255, 0.7)', padding: '3rem' }}>
          <h3>No services found</h3>
          <p>Try expanding your search radius or selecting a different service type.</p>
        </div>
      )
    }

    const serviceTypeNames = {
      plumbing: 'Plumbing',
      cleaning: 'House Cleaning',
      electrical: 'Electrical',
      auto: 'Auto Repair',
      landscaping: 'Landscaping',
      hvac: 'HVAC',
      handyman: 'Handyman',
      pest: 'Pest Control'
    }

    return (
      <>
        <div style={{ gridColumn: '1/-1', textAlign: 'center', marginBottom: '2rem' }}>
          <h2 style={{ fontSize: '2rem', marginBottom: '1rem' }}>
            Found {searchResults.length} {serviceTypeNames[formData.service] || 'Service'} providers
          </h2>
          <p style={{ color: 'rgba(255, 255, 255, 0.7)' }}>
            Showing results within {selectedRadius} mile{selectedRadius !== '1' ? 's' : ''} of your location
          </p>
        </div>
        {searchResults.map((service, idx) => (
          <div key={idx} className="service-card">
            <div className="service-header">
              <div className="service-avatar">
                {service.icon}
              </div>
              <div className="service-info">
                <h3>{service.name}</h3>
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                  <div className="rating-stars">⭐ {service.rating}</div>
                  <div style={{ color: 'rgba(255, 255, 255, 0.6)' }}>{service.reviews} reviews</div>
                </div>
              </div>
            </div>
            
            <p style={{ color: 'rgba(255, 255, 255, 0.8)', marginBottom: '1.5rem' }}>
              "{service.description}"
            </p>

            <div className="service-metrics">
              <div className="metric">
                <div className="metric-value">{service.speed}</div>
                <div className="metric-label">⚡ Speed</div>
              </div>
              <div className="metric">
                <div className="metric-value">{service.cost}</div>
                <div className="metric-label">💰 Value</div>
              </div>
              <div className="metric">
                <div className="metric-value">{service.quality}</div>
                <div className="metric-label">✨ Quality</div>
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '1.5rem' }}>
              <div style={{ color: 'var(--accent)', fontWeight: 600, fontSize: '1.1rem' }}>
                {service.price}
              </div>
              <div style={{ display: 'flex', gap: '1rem' }}>
                <button 
                  className="btn-secondary" 
                  style={{ padding: '0.5rem 1rem', fontSize: '0.9rem' }}
                  onClick={() => openQuote(service.name)}
                >
                  💬 Get Quote
                </button>
                <button 
                  className="btn-primary" 
                  style={{ padding: '0.5rem 1rem', fontSize: '0.9rem' }}
                  onClick={() => openDetails(idx)}
                >
                  📅 Check Services
                </button>
              </div>
            </div>
          </div>
        ))}
      </>
    )
  }

  return (
    <div id="search-page">
      <section className="search-page">
        <div className="search-container">
          <div className="search-header">
            <h1>Find Your Perfect Service</h1>
            <p style={{ color: 'rgba(255, 255, 255, 0.8)', fontSize: '1.2rem' }}>Tell us what you need, and we'll show you the best local options</p>
          </div>

          {/* Main search form with location, service type, urgency, and radius */}
          <div className="search-form">
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="location">📍 Your Location</label>
                <input 
                  type="text" 
                  id="location" 
                  name="location"
                  className="form-control" 
                  placeholder="Enter your address or ZIP"
                  value={formData.location}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="service">🛠️ Service Type</label>
                <select 
                  id="service" 
                  name="service"
                  className="form-control"
                  value={formData.service}
                  onChange={handleInputChange}
                >
                  <option value="">Select a service...</option>
                  <option value="plumbing">🔧 Plumbing</option>
                  <option value="cleaning">🏠 House Cleaning</option>
                  <option value="electrical">⚡ Electrical</option>
                  <option value="auto">🚗 Auto Repair</option>
                  <option value="landscaping">🌱 Landscaping</option>
                  <option value="hvac">❄️ HVAC</option>
                  <option value="handyman">🔨 Handyman</option>
                  <option value="pest">🐜 Pest Control</option>
                </select>
              </div>
              <div className="form-group">
                <label htmlFor="urgency">⏰ When do you need it?</label>
                <select 
                  id="urgency" 
                  name="urgency"
                  className="form-control"
                  value={formData.urgency}
                  onChange={handleInputChange}
                >
                  <option value="">Select timeframe...</option>
                  <option value="asap">🚨 ASAP (Emergency)</option>
                  <option value="today">📅 Today</option>
                  <option value="week">📆 This Week</option>
                  <option value="month">🗓️ This Month</option>
                  <option value="flexible">🤷 I'm Flexible</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label>📏 Search Radius</label>
              <div className="radius-selector">
                <div 
                  className={`radius-option ${selectedRadius === '1' ? 'active' : ''}`} 
                  onClick={() => selectRadius('1')}
                >
                  1 mile
                </div>
                <div 
                  className={`radius-option ${selectedRadius === '5' ? 'active' : ''}`} 
                  onClick={() => selectRadius('5')}
                >
                  5 miles
                </div>
                <div 
                  className={`radius-option ${selectedRadius === '10' ? 'active' : ''}`} 
                  onClick={() => selectRadius('10')}
                >
                  10 miles
                </div>
                <div 
                  className={`radius-option ${selectedRadius === '25' ? 'active' : ''}`} 
                  onClick={() => selectRadius('25')}
                >
                  25 miles
                </div>
                <div 
                  className={`radius-option ${selectedRadius === '50' ? 'active' : ''}`} 
                  onClick={() => selectRadius('50')}
                >
                  50+ miles
                </div>
              </div>
            </div>

            <div style={{ textAlign: 'center', marginTop: '2rem' }}>
              <button 
                className="btn-primary" 
                onClick={searchServices}
                style={{ fontSize: '1.2rem', padding: '1.2rem 3rem' }}
              >
                🔍 Find Services
              </button>
            </div>
          </div>

          {/* Dynamic search results - displays service cards based on search criteria */}
          <div id="search-results" className="search-results">
            {displayResults()}
          </div>
        </div>
      </section>
    </div>
  )
}

export default SearchPage
