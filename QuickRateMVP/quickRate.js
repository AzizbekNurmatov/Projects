let currentPage = 'home';
        let selectedRadius = '1';

        // Page navigation
        function showPage(page) {
            // Hide all pages
            document.getElementById('home-page').classList.add('hidden');
            document.getElementById('search-page').classList.add('hidden');
            
            // Show selected page
            if (page === 'search') {
                document.getElementById('search-page').classList.remove('hidden');
                currentPage = 'search';
            } else {
                document.getElementById('home-page').classList.remove('hidden');
                currentPage = 'home';
            }
        }

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
                reviews: 127
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
                reviews: 89
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
                reviews: 156
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
                reviews: 203
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
                reviews: 74
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
                reviews: 112
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
                ${services.map(service => `
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
                                <button class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.9rem;">
                                    📅 Book Now
                                </button>
                            </div>
                        </div>
                    </div>
                `).join('')}
            `;
        }

        // Header scroll effect
        window.addEventListener('scroll', () => {
            const header = document.querySelector('header');
            if (window.scrollY > 100) {
                header.style.background = 'rgba(15, 15, 35, 0.95)';
                header.style.borderBottom = '1px solid rgba(6, 214, 160, 0.3)';
            } else {
                header.style.background = 'rgba(255, 255, 255, 0.1)';
                header.style.borderBottom = '1px solid rgba(255, 255, 255, 0.1)';
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
                e.target.style.borderColor = 'var(--accent)';
            } else {
                e.target.style.borderColor = 'rgba(255, 255, 255, 0.2)';
            }
        });

        // Auto-complete simulation for location
        document.getElementById('location').addEventListener('focus', function() {
            this.placeholder = 'e.g., 123 Main St, Charleston, SC';
        });

        document.getElementById('location').addEventListener('blur', function() {
            this.placeholder = 'Enter your address or ZIP';
        });