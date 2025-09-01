import { useState, useEffect } from 'react'
import './App.css'
import Header from './components/Header'
import HomePage from './components/HomePage'
import SearchPage from './components/SearchPage'
import DetailsPage from './components/DetailsPage'
import ContactPage from './components/ContactPage'
import QuoteModal from './components/QuoteModal'

/**
 * Main App Component - Root component that manages global state and routing
 * 
 * This component handles:
 * - Client-side routing between different pages
 * - Global state management for search parameters and modal state
 * - Header scroll effects for glassmorphism styling
 */
function App() {
  // Navigation state - controls which page is currently displayed
  const [currentPage, setCurrentPage] = useState('home')
  
  // Search state - manages search radius selection across components
  const [selectedRadius, setSelectedRadius] = useState('1')
  
  // Service details state - tracks which service is selected for details view
  const [selectedServiceIndex, setSelectedServiceIndex] = useState(null)
  
  // Modal state - controls quote modal visibility and data
  const [isQuoteModalOpen, setIsQuoteModalOpen] = useState(false)
  const [quoteData, setQuoteData] = useState({ businessName: '', prefillService: '' })

  // Navigation functions
  const showPage = (page) => {
    setCurrentPage(page)
  }

  const openQuote = (businessName, prefillService = '') => {
    setQuoteData({ businessName, prefillService })
    setIsQuoteModalOpen(true)
  }

  const closeQuoteModal = () => {
    setIsQuoteModalOpen(false)
  }

  const openDetails = (index) => {
    setSelectedServiceIndex(index)
    setCurrentPage('details')
  }

  // Dynamic header styling based on scroll position
  // Creates glassmorphism effect that becomes more opaque when scrolled
  useEffect(() => {
    const handleScroll = () => {
      const header = document.querySelector('header')
      if (header) {
        if (window.scrollY > 100) {
          header.style.background = 'rgba(15, 15, 35, 0.9)'
        } else {
          header.style.background = 'rgba(15, 15, 35, 0.7)'
        }
      }
    }

    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <div className="app-container">
      {/* Animated background with floating gradient effects */}
      <div className="bg-animation"></div>
      
      {/* Fixed header with glassmorphism effect */}
      <Header 
        showPage={showPage} 
        currentPage={currentPage}
      />

      {/* Conditional page rendering based on current navigation state */}
      {currentPage === 'home' && (
        <HomePage showPage={showPage} />
      )}

      {currentPage === 'search' && (
        <SearchPage 
          selectedRadius={selectedRadius}
          setSelectedRadius={setSelectedRadius}
          openQuote={openQuote}
          openDetails={openDetails}
        />
      )}

      {currentPage === 'details' && (
        <DetailsPage 
          selectedServiceIndex={selectedServiceIndex}
          showPage={showPage}
          openQuote={openQuote}
        />
      )}

      {currentPage === 'contact' && (
        <ContactPage />
      )}

      {/* Global quote modal - appears over all pages when triggered */}
      <QuoteModal 
        isOpen={isQuoteModalOpen}
        onClose={closeQuoteModal}
        quoteData={quoteData}
      />
    </div>
  )
}

export default App
