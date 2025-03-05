function getStockData() {
    const stockSymbol = document.getElementById("stockInput").value;
    const loadingIndicator = document.getElementById("loading");
    loadingIndicator.style.display = "block";

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ticker: stockSymbol })
    })
    .then(response => response.json())
    .then(data => {
        loadingIndicator.style.display = "none";
        const ticker = data.ticker;
        const plots = data.plots;

        // Clear previous plots
        const chartContainer = document.getElementById("chartContainer");
        chartContainer.innerHTML = '';

        // Display new plots
        plots.forEach(plot => {
            const img = document.createElement("img");
            img.src = 'data:image/png;base64,' + plot;
            img.alt = 'Stock Chart';
            chartContainer.appendChild(img);
        });
    })
    .catch(error => {
        console.error("Error fetching stock data:", error);
        loadingIndicator.style.display = "none";
    });
}
