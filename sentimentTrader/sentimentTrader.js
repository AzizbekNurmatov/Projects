let priceChart;
        let currentTicker = 'AAPL';

        // Mock sentiment data generator
        function generateMockSentiment(ticker) {
            const sentiments = [
                { source: '🐦 Twitter', text: `${ticker} earnings beat expectations! Great quarter ahead 🚀`, score: 0.85, platform: 'Twitter' },
                { source: '📰 Reddit r/stocks', text: `Thinking of loading up on more ${ticker}. The fundamentals look solid`, score: 0.72, platform: 'Reddit' },
                { source: '📈 StockTwits', text: `${ticker} breaking resistance levels. Bulls in control! 📈💪`, score: 0.78, platform: 'StockTwits' },
                { source: '📰 Reddit r/investing', text: `Concerned about ${ticker}'s valuation at these levels. Might be overextended`, score: -0.45, platform: 'Reddit' },
                { source: '🐦 Twitter', text: `${ticker} partnership announcement could be a game changer for the industry`, score: 0.68, platform: 'Twitter' },
                { source: '📈 StockTwits', text: `Taking profits on ${ticker} here. Looks like it might pull back soon`, score: -0.32, platform: 'StockTwits' },
                { source: '📰 Reddit r/SecurityAnalysis', text: `${ticker}'s moat is getting stronger. Long-term hold for sure`, score: 0.91, platform: 'Reddit' },
                { source: '🐦 Twitter', text: `${ticker} CEO selling shares again... not a good look for confidence`, score: -0.58, platform: 'Twitter' }
            ];
            
            return sentiments.map(sentiment => ({
                ...sentiment,
                timestamp: new Date(Date.now() - Math.random() * 3600000),
                confidence: Math.random() * 0.3 + 0.7
            })).sort((a, b) => b.timestamp - a.timestamp);
        }

        // Mock price data generator with corresponding sentiment
        function generateMockPriceData() {
            const data = [];
            const basePrice = 150 + Math.random() * 50;
            let price = basePrice;
            
            for (let i = 0; i < 30; i++) {
                const sentimentInfluence = (Math.random() - 0.5) * 2;
                const priceChange = sentimentInfluence * 3 + (Math.random() - 0.5) * 2;
                price += priceChange;
                price = Math.max(price, 10);
                
                data.push({
                    time: new Date(Date.now() - (29 - i) * 24 * 60 * 60 * 1000),
                    price: price,
                    sentiment: sentimentInfluence * 0.8
                });
            }
            return data;
        }

        function updateSentimentGauge(score) {
            const gauge = document.getElementById('sentimentGauge');
            const scoreElement = document.getElementById('sentimentScore');
            const labelElement = document.getElementById('sentimentLabel');
            
            const angle = ((score + 1) / 2) * 180;
            
            let color, label;
            if (score > 0.2) {
                color = '#10b981';
                label = 'Bullish';
            } else if (score < -0.2) {
                color = '#ef4444';
                label = 'Bearish';
            } else {
                color = '#f59e0b';
                label = 'Neutral';
            }
            
            gauge.style.borderColor = color;
            gauge.style.transform = `rotate(${angle - 90}deg)`;
            
            scoreElement.textContent = score.toFixed(2);
            scoreElement.className = `metric-value ${score > 0.2 ? 'positive' : score < -0.2 ? 'negative' : 'neutral'}`;
            labelElement.innerHTML = `<span>${label}</span>`;
            labelElement.className = `metric-change ${score > 0.2 ? 'positive' : score < -0.2 ? 'negative' : 'neutral'}`;
        }

        function updateSentimentFeed(sentiments) {
            const feedContent = document.getElementById('sentimentFeedContent');
            feedContent.innerHTML = '';
            
            sentiments.slice(0, 6).forEach(sentiment => {
                const timeAgo = Math.floor((Date.now() - sentiment.timestamp) / (1000 * 60));
                const borderColor = sentiment.score > 0.2 ? '#00ff88' : sentiment.score < -0.2 ? '#ff0066' : '#ffa500';
                
                const item = document.createElement('div');
                item.className = 'sentiment-item';
                item.style.borderLeftColor = borderColor;
                item.innerHTML = `
                    <div class="sentiment-source">
                        <span>${sentiment.source}</span>
                        <span>${timeAgo}m ago</span>
                    </div>
                    <div class="sentiment-text">${sentiment.text}</div>
                    <div class="sentiment-score">
                        <span>Score: ${sentiment.score.toFixed(2)}</span>
                        <span>Confidence: ${(sentiment.confidence * 100).toFixed(0)}%</span>
                    </div>
                `;
                feedContent.appendChild(item);
            });
        }

        function updateTradingSignals(avgSentiment, confidence) {
            const signalsContent = document.getElementById('tradingSignalsContent');
            signalsContent.innerHTML = '';
            
            let signal, signalClass, description;
            
            if (avgSentiment > 0.3 && confidence > 0.75) {
                signal = 'STRONG BUY';
                signalClass = 'signal-buy';
                description = 'High positive sentiment with strong confidence';
            } else if (avgSentiment > 0.1) {
                signal = 'BUY';
                signalClass = 'signal-buy';
                description = 'Positive sentiment detected across platforms';
            } else if (avgSentiment < -0.3 && confidence > 0.75) {
                signal = 'STRONG SELL';
                signalClass = 'signal-sell';
                description = 'High negative sentiment with strong confidence';
            } else if (avgSentiment < -0.1) {
                signal = 'SELL';
                signalClass = 'signal-sell';
                description = 'Negative sentiment detected across platforms';
            } else {
                signal = 'HOLD';
                signalClass = 'signal-hold';
                description = 'Mixed or neutral sentiment, wait for clearer signal';
            }
            
            const signalElement = document.createElement('div');
            signalElement.className = `signal-item ${signalClass}`;
            signalElement.innerHTML = `
                <div>
                    <div class="signal-action">${signal}</div>
                    <div style="font-size: 0.8rem; color: #888;">${description}</div>
                </div>
                <div class="signal-confidence">Confidence: ${(confidence * 100).toFixed(0)}%</div>
            `;
            signalsContent.appendChild(signalElement);
        }

        function initChart() {
            const ctx = document.getElementById('priceChart').getContext('2d');
            priceChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [
                        {
                            label: 'Stock Price ($)',
                            data: [],
                            borderColor: '#22d3ee',
                            backgroundColor: 'rgba(34, 211, 238, 0.18)',
                            tension: 0.4,
                            fill: 'origin',
                            yAxisID: 'y',
                            borderWidth: 3,
                            pointRadius: 0,
                            pointHoverRadius: 6
                        },
                        {
                            label: 'Sentiment Score',
                            data: [],
                            borderColor: '#a78bfa',
                            backgroundColor: 'rgba(167, 139, 250, 0.18)',
                            tension: 0.4,
                            fill: 'origin',
                            yAxisID: 'y1',
                            borderWidth: 3,
                            pointRadius: 0,
                            pointHoverRadius: 6
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    interaction: {
                        mode: 'index',
                        intersect: false,
                    },
                    plugins: {
                        legend: {
                            labels: {
                                color: '#0f172a',
                                usePointStyle: true,
                                padding: 20
                            }
                        },
                        tooltip: {
                            backgroundColor: 'rgba(255,255,255,0.95)',
                            titleColor: '#0f172a',
                            bodyColor: '#0f172a',
                            borderColor: 'rgba(2,6,23,0.08)',
                            borderWidth: 1,
                            titleFont: { weight: '700' }
                        }
                    },
                    scales: {
                        x: {
                            ticks: { 
                                color: '#64748b',
                                maxTicksLimit: 10
                            },
                            grid: { color: 'rgba(2, 6, 23, 0.06)' }
                        },
                        y: {
                            type: 'linear',
                            display: true,
                            position: 'left',
                            ticks: { 
                                color: '#0f172a',
                                callback: function(value) {
                                    return '$' + value.toFixed(0);
                                }
                            },
                            grid: { color: 'rgba(2, 6, 23, 0.06)' },
                            title: {
                                display: true,
                                text: 'Stock Price ($)',
                                color: '#22d3ee'
                            }
                        },
                        y1: {
                            type: 'linear',
                            display: true,
                            position: 'right',
                            ticks: { 
                                color: '#0f172a',
                                min: -1,
                                max: 1,
                                stepSize: 0.5,
                                callback: function(value) {
                                    return value.toFixed(1);
                                }
                            },
                            grid: {
                                drawOnChartArea: false,
                                color: 'rgba(2, 6, 23, 0.06)'
                            },
                            title: {
                                display: true,
                                text: 'Sentiment Score',
                                color: '#a78bfa'
                            }
                        }
                    }
                }
            });
        }

        function updateChart(priceData) {
            const labels = priceData.map(d => d.time.toLocaleDateString());
            const prices = priceData.map(d => d.price);
            const sentiments = priceData.map(d => d.sentiment);
            
            priceChart.data.labels = labels;
            priceChart.data.datasets[0].data = prices;
            priceChart.data.datasets[1].data = sentiments;
            priceChart.update('none');
        }

        async function analyzeStock() {
            const ticker = document.getElementById('tickerInput').value.trim().toUpperCase();
            if (!ticker) return;
            
            currentTicker = ticker;
            const loadingIndicator = document.getElementById('loadingIndicator');
            loadingIndicator.style.display = 'block';
            
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            const sentiments = generateMockSentiment(ticker);
            const priceData = generateMockPriceData();
            const avgSentiment = sentiments.reduce((sum, s) => sum + s.score, 0) / sentiments.length;
            const avgConfidence = sentiments.reduce((sum, s) => sum + s.confidence, 0) / sentiments.length;
            
            const currentPrice = priceData[priceData.length - 1].price;
            const previousPrice = priceData[priceData.length - 2].price;
            const priceChange = currentPrice - previousPrice;
            const priceChangePercent = (priceChange / previousPrice) * 100;
            
            document.getElementById('currentPrice').textContent = `$${currentPrice.toFixed(2)}`;
            document.getElementById('priceChange').innerHTML = `
                <span class="${priceChange >= 0 ? 'positive' : 'negative'}">
                    ${priceChange >= 0 ? '↗' : '↘'} $${Math.abs(priceChange).toFixed(2)} (${priceChangePercent.toFixed(2)}%)
                </span>
            `;
            
            document.getElementById('confidence').textContent = `${(avgConfidence * 100).toFixed(0)}%`;
            document.getElementById('confidenceLabel').innerHTML = '<span>Model Accuracy</span>';
            
            updateSentimentGauge(avgSentiment);
            updateSentimentFeed(sentiments);
            updateTradingSignals(avgSentiment, avgConfidence);
            updateChart(priceData);
            
            loadingIndicator.style.display = 'none';
        }

        document.addEventListener('DOMContentLoaded', function() {
            initChart();
            analyzeStock();
            
            setInterval(analyzeStock, 30000);
            
            document.getElementById('tickerInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    analyzeStock();
                }
            });
        });