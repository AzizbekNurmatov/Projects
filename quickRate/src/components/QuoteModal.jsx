import React, { useState } from 'react'

const QuoteModal = ({ isOpen, onClose, quoteData }) => {
  const [quoteMode, setQuoteMode] = useState('quick')
  const [quickFormData, setQuickFormData] = useState({
    phone: '',
    bestTime: ''
  })
  const [detailedFormData, setDetailedFormData] = useState({
    service: '',
    datetime: '',
    description: '',
    email: '',
    phone: ''
  })

  if (!isOpen) return null

  const handleQuickInputChange = (e) => {
    const { name, value } = e.target
    setQuickFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleDetailedInputChange = (e) => {
    const { name, value } = e.target
    setDetailedFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const sendMailto = (subject, body) => {
    const founderEmail = 'youremail@example.com' // replace with your email
    const href = `mailto:${founderEmail}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`
    window.location.href = href
  }

  const handleQuickSubmit = (e) => {
    e.preventDefault()
    const { businessName } = quoteData
    const { phone, bestTime } = quickFormData
    const subject = `Quick Call Request - ${businessName}`
    const body = `Business: ${businessName}\nType: Quick Call\nPhone: ${phone}\nBest Time: ${bestTime}`
    sendMailto(subject, body)
    onClose()
  }

  const handleDetailedSubmit = (e) => {
    e.preventDefault()
    const { businessName } = quoteData
    const { service, datetime, description, email, phone } = detailedFormData
    const subject = `Quote Request - ${businessName} (${service})`
    const body = `Business: ${businessName}\nType: Detailed\nService: ${service}\nWhen: ${datetime}\nContact: ${email} / ${phone}\n\nDescription:\n${description}`
    sendMailto(subject, body)
    onClose()
  }

  const setQuoteModeHandler = (mode) => {
    setQuoteMode(mode)
  }

  return (
    <div id="quote-modal" aria-hidden="false">
      <div className="modal-backdrop" onClick={onClose}></div>
      <div className="modal">
        <div className="modal-header">
          <h3 id="quote-title">Request a Quote</h3>
          <button className="modal-close" onClick={onClose}>✖</button>
        </div>
        <div className="modal-body">
          <div className="toggle-group">
            <button 
              id="toggle-quick" 
              className={`toggle-btn ${quoteMode === 'quick' ? 'active' : ''}`} 
              type="button"
              onClick={() => setQuoteModeHandler('quick')}
            >
              📞 I want a call
            </button>
            <button 
              id="toggle-detailed" 
              className={`toggle-btn ${quoteMode === 'detailed' ? 'active' : ''}`} 
              type="button"
              onClick={() => setQuoteModeHandler('detailed')}
            >
              📝 Submit details
            </button>
          </div>

          <form id="quote-quick" className={`quote-form ${quoteMode === 'quick' ? '' : 'hidden'}`} onSubmit={handleQuickSubmit}>
            <div className="form-group">
              <label>Business</label>
              <input 
                id="quote-business-quick" 
                className="form-control" 
                type="text" 
                value={quoteData.businessName}
                readOnly
              />
            </div>
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="quote-phone">📱 Phone Number</label>
                <input 
                  id="quote-phone" 
                  name="phone"
                  className="form-control" 
                  type="tel" 
                  placeholder="(555) 123-4567" 
                  required
                  value={quickFormData.phone}
                  onChange={handleQuickInputChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="quote-besttime">🕒 Best time to call</label>
                <input 
                  id="quote-besttime" 
                  name="bestTime"
                  className="form-control" 
                  type="text" 
                  placeholder="Today 2-4pm or ASAP"
                  value={quickFormData.bestTime}
                  onChange={handleQuickInputChange}
                />
              </div>
            </div>
            <div style={{ textAlign: 'right', marginTop: '1rem' }}>
              <button type="submit" className="btn-primary">Request Call</button>
            </div>
          </form>

          <form id="quote-detailed" className={`quote-form ${quoteMode === 'detailed' ? '' : 'hidden'}`} onSubmit={handleDetailedSubmit}>
            <div className="form-group">
              <label>Business</label>
              <input 
                id="quote-business-detailed" 
                className="form-control" 
                type="text" 
                value={quoteData.businessName}
                readOnly
              />
            </div>
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="quote-service">🛠️ Service Required</label>
                <input 
                  id="quote-service" 
                  name="service"
                  className="form-control" 
                  type="text" 
                  placeholder="e.g., Emergency Leak Repair" 
                  required
                  value={detailedFormData.service}
                  onChange={handleDetailedInputChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="quote-datetime">📅 Preferred Date/Time</label>
                <input 
                  id="quote-datetime" 
                  name="datetime"
                  className="form-control" 
                  type="text" 
                  placeholder="Tomorrow 10am or This Week"
                  value={detailedFormData.datetime}
                  onChange={handleDetailedInputChange}
                />
              </div>
            </div>
            <div className="form-group">
              <label htmlFor="quote-description">📝 Description</label>
              <textarea 
                id="quote-description" 
                name="description"
                className="form-control" 
                rows="4" 
                placeholder="Briefly describe the issue or request" 
                required
                value={detailedFormData.description}
                onChange={handleDetailedInputChange}
              ></textarea>
            </div>
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="quote-email">✉️ Email</label>
                <input 
                  id="quote-email" 
                  name="email"
                  className="form-control" 
                  type="email" 
                  placeholder="you@example.com" 
                  required
                  value={detailedFormData.email}
                  onChange={handleDetailedInputChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="quote-phone2">📱 Phone</label>
                <input 
                  id="quote-phone2" 
                  name="phone"
                  className="form-control" 
                  type="tel" 
                  placeholder="(555) 123-4567" 
                  required
                  value={detailedFormData.phone}
                  onChange={handleDetailedInputChange}
                />
              </div>
            </div>
            <div style={{ textAlign: 'right', marginTop: '1rem' }}>
              <button type="submit" className="btn-primary">Submit Details</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}

export default QuoteModal
