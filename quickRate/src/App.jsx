import { useState, useEffect } from 'react'
import './App.css'
import Header from './components/Header'
import HomePage from './components/HomePage'
import SearchPage from './components/SearchPage'
import DetailsPage from './components/DetailsPage'
import ContactPage from './components/ContactPage'
import QuoteModal from './components/QuoteModal'

function App() {
  const [currentPage, setCurrentPage] = useState('home')
  const [selectedRadius, setSelectedRadius] = useState('1')
  const [selectedServiceIndex, setSelectedServiceIndex] = useState(null)
  const [isQuoteModalOpen, setIsQuoteModalOpen] = useState(false)
  const [quoteData, setQuoteData] = useState({ businessName: '', prefillService: '' })

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

  // Header scroll effect
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
      <div className="bg-animation"></div>
      
      <Header 
        showPage={showPage} 
        currentPage={currentPage}
      />

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

      <QuoteModal 
        isOpen={isQuoteModalOpen}
        onClose={closeQuoteModal}
        quoteData={quoteData}
      />
    </div>
  )
}

export default App
