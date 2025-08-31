import React from 'react'

const Header = ({ showPage, currentPage }) => {
  return (
    <header>
      <nav className="container">
        <div className="logo">ServiceRate_</div>
        <ul className="nav-links">
          <li><a href="#" onClick={(e) => { e.preventDefault(); showPage('home') }}>Home</a></li>
          <li><a href="#" onClick={(e) => { e.preventDefault(); showPage('features') }}>Features</a></li>
          <li><a href="#" onClick={(e) => { e.preventDefault(); showPage('about') }}>About</a></li>
          <li><a href="#" onClick={(e) => { e.preventDefault(); showPage('contact') }}>Contact</a></li>
        </ul>
        <a href="#" className="cta-nav" onClick={(e) => { e.preventDefault(); showPage('search') }}>Find Services</a>
      </nav>
    </header>
  )
}

export default Header
