import React, { useState } from 'react'

/**
 * ContactPage Component - Contact form with mailto functionality
 * 
 * Features:
 * - Contact form with validation
 * - Mailto link generation for direct email sending
 * - Fallback email app integration
 */
const ContactPage = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  })

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const buildMailto = () => {
    const { name, email, subject, message } = formData
    const founderEmail = 'youremail@example.com' // TODO: replace with your address
    const body = `From: ${name} <${email}>%0D%0A%0D%0A${encodeURIComponent(message)}`
    return `mailto:${founderEmail}?subject=${encodeURIComponent(subject || 'ServiceRate Inquiry')}&body=${body}`
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const href = buildMailto()
    window.location.href = href
  }

  const handleFallbackClick = (e) => {
    e.preventDefault()
    const href = buildMailto()
    window.location.href = href
  }

  return (
    <div id="contact-page">
      <section className="search-page">
        <div className="search-container">
          <div className="search-header">
            <h1>Contact Us</h1>
            <p style={{ color: 'rgba(255, 255, 255, 0.8)', fontSize: '1.2rem' }}>Have questions or feedback? Send a message and it will go directly to the founder.</p>
          </div>

          <div className="search-form">
            <form id="contact-form" onSubmit={handleSubmit}>
              <div className="form-grid">
                <div className="form-group">
                  <label htmlFor="contact-name">👤 Your Name</label>
                  <input 
                    type="text" 
                    id="contact-name" 
                    name="name"
                    className="form-control" 
                    placeholder="Jane Doe" 
                    required
                    value={formData.name}
                    onChange={handleInputChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="contact-email">✉️ Your Email</label>
                  <input 
                    type="email" 
                    id="contact-email" 
                    name="email"
                    className="form-control" 
                    placeholder="you@example.com" 
                    required
                    value={formData.email}
                    onChange={handleInputChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="contact-subject">📝 Subject</label>
                  <input 
                    type="text" 
                    id="contact-subject" 
                    name="subject"
                    className="form-control" 
                    placeholder="Question about ServiceRate" 
                    required
                    value={formData.subject}
                    onChange={handleInputChange}
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="contact-message">💬 Message</label>
                <textarea 
                  id="contact-message" 
                  name="message"
                  className="form-control" 
                  placeholder="Type your message here..." 
                  rows="6" 
                  required
                  value={formData.message}
                  onChange={handleInputChange}
                ></textarea>
              </div>

              <div style={{ textAlign: 'center', marginTop: '1.5rem' }}>
                <button type="submit" className="btn-primary" style={{ fontSize: '1.1rem', padding: '0.9rem 2rem' }}>
                  Send Message
                </button>
                <a 
                  id="contact-mailto-fallback" 
                  href="#" 
                  className="btn-secondary" 
                  style={{ marginLeft: '0.75rem' }}
                  onClick={handleFallbackClick}
                >
                  Open Email App
                </a>
              </div>
            </form>
          </div>
        </div>
      </section>
    </div>
  )
}

export default ContactPage
