const BASE_URL = "https://frequency-emotion.onrender.com";
async function generateFrequency() {
    const mood = document.getElementById('moodInput').value.trim();
    if (!mood) {
        document.getElementById('result').innerHTML = 'Please enter a mood.';
        return;
    }
    const response = await fetch('/generate_frequency', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mood })
    });
    const data = await response.json();
    if (data.frequency) {
        document.getElementById('result').innerHTML = `
            ${data.message}<br>
            <a href="${data.link}" target="_blank">Play it here</a>
        `;
    } else {
        document.getElementById('result').innerHTML = data.message;
    }
}

async function feelTheFrequency() {
    const emotions = prompt('What emotions do you feel when tuning in? (Separate with commas)');
    const response = await fetch('/feel_the_frequency', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ emotions: emotions || '' })
    });
    const data = await response.json();
    document.getElementById('result').innerHTML = `
        Play frequency: ${data.frequency} via <a href="${data.link}" target="_blank">this link</a><br>
        Others also felt: ${data.overlapping_emotions}<br>
        You were the first to add: ${data.new_emotions}