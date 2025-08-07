function showweatherDetails(event) {
  event.preventDefault();

  const city = document.getElementById('city').value.trim();
  const apiKey = '05001835410d6977f1054a05862df8e7';
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`City not found (HTTP ${response.status})`);
      }
      return response.json();
    })
    .then(data => {
      const weatherInfo = document.getElementById('weatherInfo');
      weatherInfo.innerHTML = `
        <h2>Weather in ${data.name}</h2>
        <p>Temperature: ${data.main.temp} &#8451;</p>
        <p>Weather: ${data.weather[0].description}</p>
      `;
    })
    .catch(error => {
      const weatherInfo = document.getElementById('weatherInfo');
      weatherInfo.innerHTML = `<p style="color:red;">Error: ${error.message}</p>`;
      console.error('Error fetching weather data:', error);
    });
}

// Add event listener only after DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('weatherForm').addEventListener('submit', showweatherDetails);
});
