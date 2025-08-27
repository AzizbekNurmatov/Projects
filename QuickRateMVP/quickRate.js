let currentPage = 'home';
        let selectedRadius = '1';
        let selectedServiceIndex = null;

        // Page navigation
        function showPage(page) {
            // Hide all pages
            document.getElementById('home-page').classList.add('hidden');
            document.getElementById('search-page').classList.add('hidden');
            const detailsPage = document.getElementById('details-page');
            if (detailsPage) {
                detailsPage.classList.add('hidden');
            }
            const contactPage = document.getElementById('contact-page');
            if (contactPage) {
                contactPage.classList.add('hidden');
            }
            
            // Show selected page
            if (page === 'search') {
                document.getElementById('search-page').classList.remove('hidden');
                currentPage = 'search';
            } else if (page === 'details') {
                if (detailsPage) {
                    detailsPage.classList.remove('hidden');
                }
                currentPage = 'details';
            } else if (page === 'contact') {
                if (contactPage) {
                    contactPage.classList.remove('hidden');
                }
                currentPage = 'contact';
            } else {
                document.getElementById('home-page').classList.remove('hidden');
                currentPage = 'home';
            }
        }

        // Contact form (mailto) handler
        (function setupContactForm() {
            const form = document.getElementById('contact-form');
            const fallback = document.getElementById('contact-mailto-fallback');
            if (!form) return;
            const founderEmail = 'youremail@example.com'; // TODO: replace with your address

            function buildMailto() {
                const name = document.getElementById('contact-name')?.value || '';
                const email = document.getElementById('contact-email')?.value || '';
                const subject = document.getElementById('contact-subject')?.value || 'ServiceRate Inquiry';
                const message = document.getElementById('contact-message')?.value || '';
                const body = `From: ${name} <${email}>%0D%0A%0D%0A${encodeURIComponent(message)}`;
                return `mailto:${founderEmail}?subject=${encodeURIComponent(subject)}&body=${body}`;
            }

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                const href = buildMailto();
                window.location.href = href;
            });

            if (fallback) {
                fallback.addEventListener('click', function(e) {
                    e.preventDefault();
                    const href = buildMailto();
                    window.location.href = href;
                });
            }
        })();

        // Radius selection
        function selectRadius(element, radius) {
            document.querySelectorAll('.radius-option').forEach(opt => opt.classList.remove('active'));
            element.classList.add('active');
            selectedRadius = radius;
        }

        // Sample service data
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
        ];

        // Search services
        function searchServices() {
            const serviceType = document.getElementById('service').value;
            const location = document.getElementById('location').value;
            const urgency = document.getElementById('urgency').value;

            if (!location) {
                alert('Please enter your location');
                return;
            }

            if (!serviceType) {
                alert('Please select a service type');
                return;
            }

            // Filter services based on selection
            let results = sampleServices.filter(service => 
                serviceType === '' || service.type === serviceType
            );

            // Add some randomization and urgency-based sorting
            if (urgency === 'asap') {
                results = results.sort((a, b) => b.speed - a.speed);
            }

            displayResults(results, serviceType);
        }

        function displayResults(services, serviceType) {
            const resultsContainer = document.getElementById('search-results');
            
            if (services.length === 0) {
                resultsContainer.innerHTML = `
                    <div style="text-align: center; color: rgba(255, 255, 255, 0.7); padding: 3rem;">
                        <h3>No services found</h3>
                        <p>Try expanding your search radius or selecting a different service type.</p>
                    </div>
                `;
                return;
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
            };

            resultsContainer.innerHTML = `
                <div style="grid-column: 1/-1; text-align: center; margin-bottom: 2rem;">
                    <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                        Found ${services.length} ${serviceTypeNames[serviceType]} providers
                    </h2>
                    <p style="color: rgba(255, 255, 255, 0.7);">
                        Showing results within ${selectedRadius} mile${selectedRadius !== '1' ? 's' : ''} of your location
                    </p>
                </div>
                ${services.map((service, idx) => `
                    <div class="service-card">
                        <div class="service-header">
                            <div class="service-avatar">
                                ${service.icon}
                            </div>
                            <div class="service-info">
                                <h3>${service.name}</h3>
                                <div style="display: flex; align-items: center; gap: 1rem;">
                                    <div class="rating-stars">⭐ ${service.rating}</div>
                                    <div style="color: rgba(255, 255, 255, 0.6);">${service.reviews} reviews</div>
                                </div>
                            </div>
                        </div>
                        
                        <p style="color: rgba(255, 255, 255, 0.8); margin-bottom: 1.5rem;">
                            "${service.description}"
                        </p>

                        <div class="service-metrics">
                            <div class="metric">
                                <div class="metric-value">${service.speed}</div>
                                <div class="metric-label">⚡ Speed</div>
                            </div>
                            <div class="metric">
                                <div class="metric-value">${service.cost}</div>
                                <div class="metric-label">💰 Value</div>
                            </div>
                            <div class="metric">
                                <div class="metric-value">${service.quality}</div>
                                <div class="metric-label">✨ Quality</div>
                            </div>
                        </div>

                        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.5rem;">
                            <div style="color: var(--accent); font-weight: 600; font-size: 1.1rem;">
                                ${service.price}
                            </div>
                            <div style="display: flex; gap: 1rem;">
                                <button class="btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.9rem;">
                                    💬 Get Quote
                                </button>
                                <button class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.9rem;" onclick="openDetails(${idx})">
                                    📅 Check Services
                                </button>
                            </div>
                        </div>
                    </div>
                `).join('')}
            `;
        }

        function openDetails(index) {
            selectedServiceIndex = index;
            const svc = sampleServices[index];
            const titleEl = document.getElementById('details-title');
            const ctaEl = document.getElementById('details-cta');
            const contentEl = document.getElementById('details-content');

            if (!svc || !titleEl || !contentEl) {
                return;
            }

            titleEl.textContent = svc.name;
            if (ctaEl) {
                ctaEl.style.display = 'inline-flex';
            }

            const servicesList = (svc.services && svc.services.length ? svc.services : [
                { title: 'General Service', price: svc.price || '$—', eta: 'Varies', blurb: 'Contact for details and availability.' }
            ]);

            contentEl.innerHTML = `
                <div class="service-card" style="grid-column: 1/-1;">
                    <div class="service-header">
                        <div class="service-avatar">${svc.icon}</div>
                        <div class="service-info">
                            <h3>${svc.name}</h3>
                            <div style="display:flex; align-items:center; gap:1rem;">
                                <div class="rating-stars">⭐ ${svc.rating}</div>
                                <div style="color: rgba(255,255,255,0.6);">${svc.reviews} reviews</div>
                            </div>
                        </div>
                    </div>
                    <p style="color: rgba(255,255,255,0.85);">${svc.description}</p>
                </div>
                ${servicesList.map(item => `
                    <div class="service-card">
                        <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:1rem;">
                            <div>
                                <h3 style="margin-bottom:0.5rem;">${item.title}</h3>
                                <div style="color: rgba(255,255,255,0.75);">${item.blurb}</div>
                            </div>
                            <div style="text-align:right;">
                                <div style="color: var(--accent); font-weight:600;">${item.price}</div>
                                <div style="color: rgba(255,255,255,0.6); font-size:0.9rem;">ETA: ${item.eta}</div>
                            </div>
                        </div>
                        <div style="display:flex; gap:0.75rem; margin-top:1rem;">
                            <button class="btn-secondary">Add to quote</button>
                            <button class="btn-primary">Book inquiry</button>
                        </div>
                    </div>
                `).join('')}
            `;

            showPage('details');
        }

        // Header scroll effect
        window.addEventListener('scroll', () => {
            const header = document.querySelector('header');
            if (window.scrollY > 100) {
                header.style.background = 'rgba(15, 15, 35, 0.9)';
            } else {
                header.style.background = 'rgba(15, 15, 35, 0.7)';
            }
        });

        // Smooth scrolling for better UX
        document.addEventListener('DOMContentLoaded', function() {
            // Add some demo data on load for better demo
            setTimeout(() => {
                if (currentPage === 'search') {
                    displayResults(sampleServices.slice(0, 3), 'all');
                }
            }, 1000);
        });

        // Add some interactive elements
        document.addEventListener('click', function(e) {
            if (e.target.closest('.service-card')) {
                const card = e.target.closest('.service-card');
                card.style.transform = 'translateY(-5px) scale(1.02)';
                setTimeout(() => {
                    card.style.transform = 'translateY(-5px)';
                }, 150);
            }
        });

        // Form validation and UX improvements
        document.getElementById('location').addEventListener('input', function(e) {
            if (e.target.value.length > 2) {
                e.target.style.boxShadow = '0 0 0 2px rgba(6, 214, 160, 0.3)';
            } else {
                e.target.style.boxShadow = 'none';
            }
        });

        // Auto-complete simulation for location
        document.getElementById('location').addEventListener('focus', function() {
            this.placeholder = 'e.g., 123 Main St, Charleston, SC';
        });

        document.getElementById('location').addEventListener('blur', function() {
            this.placeholder = 'Enter your address or ZIP';
        });