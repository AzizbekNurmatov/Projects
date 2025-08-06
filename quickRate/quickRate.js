const businesses = [
  {
    name: "CleanPro Carpet Services",
    description: "Expert carpet cleaning for homes and offices.",
    rating: 4.5,
    category: "cleaning"
  },
  {
    name: "EZ Plumbing & Repair",
    description: "Fast and affordable plumbing services.",
    rating: 4.8,
    category: "plumbing"
  },
  {
    name: "Glide Window Washers",
    description: "Professional window cleaning with satisfaction guarantee.",
    rating: 4.3,
    category: "cleaning"
  },
  {
    name: "Coastal Detailers",
    description: "Amazing cleaning and detailing; exterior and interior.",
    rating: 4.5,
    category: "cleaning"
  }
];

const businessList = document.getElementById('business-list');

// Function to render all business cards
function renderBusinessCards(businessesToRender) {
  businessList.innerHTML = ''; // Clear existing cards

  businessesToRender.forEach(business => {
    const card = document.createElement('div');
    card.className = 'business-card';

    card.innerHTML = `
      <h2>${business.name}</h2>
      <p>${business.description}</p>
      <p class="rating">Rating: ⭐ ${business.rating.toFixed(1)}</p>
      <button onclick="alert('Booking for ${business.name}')">Book Now</button>
      <button onclick="alert('Requesting quote from ${business.name}')">Request Quote</button>
    `;

    businessList.appendChild(card);
  });
}

// Initial render of all businesses
renderBusinessCards(businesses);

// Optional: Add filtering by category on sidebar select
const categoryFilter = document.getElementById('categoryFilter');
categoryFilter.addEventListener('change', () => {
  const selectedCategory = categoryFilter.value;
  if (!selectedCategory) {
    renderBusinessCards(businesses);
  } else {
    const filtered = businesses.filter(b => b.category === selectedCategory);
    renderBusinessCards(filtered);
  }
});

// Optional: Search bar filter
const searchInput = document.getElementById('searchInput');
searchInput.addEventListener('input', () => {
  const query = searchInput.value.toLowerCase();
  const filtered = businesses.filter(business => 
    business.name.toLowerCase().includes(query) || 
    business.description.toLowerCase().includes(query)
  );
  renderBusinessCards(filtered);
});
