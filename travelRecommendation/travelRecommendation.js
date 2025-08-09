// travelRecommendation.js

const jsonUrl = 'travelRecommendation.json'; // Your JSON filename

const searchInput = document.querySelector('.search-input');
const searchBtn = document.querySelector('.search-btn');
const clearBtn = document.querySelector('.clear-btn');
const resultsDiv = document.getElementById('results');

let travelData = null;

// Fetch data from JSON
fetch(jsonUrl)
  .then(response => {
    if (!response.ok) throw new Error('Network response was not ok');
    return response.json();
  })
  .then(data => {
    travelData = data;
    console.log('Travel data loaded:', travelData);
  })
  .catch(err => {
    console.error('Failed to load travel data:', err);
  });

// Clear results container
function clearResults() {
  resultsDiv.innerHTML = '';
}

// Create place card element
function createPlaceCard(name, imageUrl, description) {
  const card = document.createElement('div');
  card.classList.add('place-card');
  card.style.border = '1px solid white';
  card.style.padding = '10px';
  card.style.margin = '10px 0';
  card.style.backgroundColor = 'rgba(0,0,0,0.6)';
  card.style.borderRadius = '5px';

  const img = document.createElement('img');
  img.src = imageUrl; // replace with your actual image paths
  img.alt = name;
  img.style.width = '100%';
  img.style.maxWidth = '400px';
  img.style.borderRadius = '5px';

  const title = document.createElement('h4');
  title.innerText = name;

  const desc = document.createElement('p');
  desc.innerText = description;

  card.appendChild(img);
  card.appendChild(title);
  card.appendChild(desc);

  return card;
}

// Display recommendations based on search
function displayRecommendations() {
  clearResults();

  if (!travelData) {
    resultsDiv.innerText = 'Data not loaded yet. Please try again later.';
    return;
  }

  const keyword = searchInput.value.trim().toLowerCase();

  // Normalize keyword for plurals
  let normalizedKeyword = '';
  if (keyword === 'beach' || keyword === 'beaches') normalizedKeyword = 'beaches';
  else if (keyword === 'temple' || keyword === 'temples') normalizedKeyword = 'temples';
  else if (keyword === 'country' || keyword === 'countries') normalizedKeyword = 'countries';
  else {
    resultsDiv.innerText = 'Please enter a valid keyword: beach, temple, or country.';
    return;
  }

  if (normalizedKeyword === 'beaches') {
    travelData.beaches.forEach(place => {
      resultsDiv.appendChild(createPlaceCard(place.name, place.imageUrl, place.description));
    });
  } else if (normalizedKeyword === 'temples') {
    travelData.temples.forEach(place => {
      resultsDiv.appendChild(createPlaceCard(place.name, place.imageUrl, place.description));
    });
  } else if (normalizedKeyword === 'countries') {
    travelData.countries.forEach(country => {
      // Country container
      const countryContainer = document.createElement('div');
      countryContainer.style.marginBottom = '30px';

      const countryTitle = document.createElement('h3');
      countryTitle.innerText = country.name;
      countryContainer.appendChild(countryTitle);

      country.cities.forEach(city => {
        countryContainer.appendChild(createPlaceCard(city.name, city.imageUrl, city.description));
      });

      resultsDiv.appendChild(countryContainer);
    });
  }
}

// Event listeners
searchBtn.addEventListener('click', displayRecommendations);

clearBtn.addEventListener('click', () => {
  clearResults();
  searchInput.value = '';
});
