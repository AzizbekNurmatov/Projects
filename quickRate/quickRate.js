const businesses = [
  {
    name: "CleanPro Carpet Services",
    description: "Expert carpet cleaning for homes and offices.",
    rating: 4.5
  },
  {
    name: "EZ Plumbing & Repair",
    description: "Fast and affordable plumbing services.",
    rating: 4.8
  },
  {
    name: "Glide Window Washers",
    description: "Professional window cleaning with satisfaction guarantee.",
    rating: 4.3
  }
];

const businessList = document.getElementById('business-list');

businesses.forEach(business => {
  const card = document.createElement('div');
  card.className = 'business-card';

  card.innerHTML = `
    <h2>${business.name}</h2>
    <p>${business.description}</p>
    <p>Rating: ${business.rating} ⭐</p>
    <button onclick="alert('Booking for ${business.name}')">Book Now</button>
    <button onclick="alert('Requesting quote from ${business.name}')">Request Quote</button>
  `;

  businessList.appendChild(card);
});
