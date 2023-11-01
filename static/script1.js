window.onload = function () {
    const form = document.querySelector('form');
    const messageBox = createMessageBox();
    let evtSource;

    document.body.appendChild(messageBox);

    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        const submitButton = form.querySelector('button[type="submit"]');

        if (submitButton.textContent === 'STOP') {
            evtSource.close();
            resetSubmitButton(submitButton);
            return;
        }

        indicateDataFetching(submitButton);

        evtSource = startDataStreaming(form);

        setTimeout(() => {
            setButtonToStop(submitButton);
        }, 1000);
    });

    handleUnavailableSensors(messageBox);
};

function createMessageBox() {
    const messageBox = document.createElement('span');
    messageBox.style.color = 'red';
    messageBox.style.backgroundColor = 'white';
    messageBox.style.border = '1px solid red';
    messageBox.style.borderRadius = '4px';
    messageBox.style.padding = '2px 5px';
    messageBox.style.position = 'absolute';
    messageBox.innerText = 'Currently unavailable';
    messageBox.style.display = 'none';
    return messageBox;
}

function resetSubmitButton(button) {
    button.textContent = 'CHECK';
    button.style.backgroundColor = '#4CAF50';
}

function indicateDataFetching(button) {
    button.textContent = 'Fetching the data...';
    button.disabled = true;
}

function setButtonToStop(button) {
    button.textContent = 'STOP';
    button.style.backgroundColor = 'red';
    button.disabled = false;
}

function handleUnavailableSensors(messageBox) {
    const unavailableSensors = document.querySelectorAll('input[type="radio"][disabled]');
    unavailableSensors.forEach(sensor => {
        sensor.parentElement.addEventListener('mouseover', function (event) {
            messageBox.style.display = 'block';
            messageBox.style.left = event.pageX + 'px';
            messageBox.style.top = event.pageY + 'px';
        });

        sensor.parentElement.addEventListener('mouseout', function () {
            messageBox.style.display = 'none';
        });
    });
}
