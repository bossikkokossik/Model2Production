function startDataStreaming(form) {
    const formData = new FormData(form);
    const selectedSensor = formData.get('sensor');

    if (selectedSensor) {
        const url = `/check?sensor=${encodeURIComponent(selectedSensor)}`;
        const evtSourceLocal = new EventSource(url);

        evtSourceLocal.onmessage = function (event) {
            const data = JSON.parse(event.data);
            updateDataTable(data);
        };

        evtSourceLocal.onerror = function (err) {
            console.error('EventSource failed:', err);
            evtSourceLocal.close();
        };

        return evtSourceLocal;
    }
}

function updateDataTable(data) {
    const tableBody = document.querySelector('#data-table tbody');
    const newRow = tableBody.insertRow();

    newRow.insertCell(0).textContent = data.Temperature;
    newRow.insertCell(1).textContent = data.Humidity;
    newRow.insertCell(2).textContent = data.Loudness;
    newRow.insertCell(3).textContent = data.Label;

    if (data.Label === 'anomaly') {
        newRow.style.color = 'red';
    }

    newRow.scrollIntoView({ behavior: 'smooth' });
}
