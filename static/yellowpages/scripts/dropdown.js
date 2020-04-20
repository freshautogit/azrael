    const selectCity = document.querySelector('select[name=city]');
    const selectAddress = document.querySelector('select[name=addr]');
    const selectUnit = document.querySelector('select[name=unit]');
    const selectDepart = document.querySelector('select[name=depart]');
    const selectPosition = document.querySelector('select[name=position]');
    const notDublicate = document.querySelector('p').innerHTML;

    if (notDublicate == 'False') {
    alert('Такая запись уже есть в справочнике!');
    };

    let doXHr = function(currentSelect, selectedOption, nextSelect, thirdSelect) {
    let nullOption = document.createElement('option');
    nullOption.value = '';
    nullOption.innerHTML = 'Оставить пустым';
    let nullOption2 = document.createElement('option');
    nullOption2.value = '';
    nullOption2.innerHTML = 'Оставить пустым';

    let xhr = new XMLHttpRequest();
    let url = 'dropdown_request/?' + currentSelect.name + '=' + encodeURIComponent(selectedOption);
    xhr.open('GET', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let json = JSON.parse(xhr.response);
            if (nextSelect != null) {
                while (nextSelect.firstChild) {
                    nextSelect.removeChild(nextSelect.firstChild);
                }
            }
            if (thirdSelect != null) {
                while (thirdSelect.firstChild) {
                    thirdSelect.removeChild(thirdSelect.firstChild);
                }
                thirdSelect.appendChild(nullOption2);
            }
            if (json.response != 'None') {
                nextSelect.removeAttribute('disabled');
                nextSelect.appendChild(nullOption2);
                for (let i = 0; i < json.response.length; i++) {
                    let option = document.createElement('option');
                    option.value += json.response[i];
                    option.innerHTML += json.response[i];
                    nextSelect.appendChild(option);
                    if (thirdSelect != null) {
                        thirdSelect.removeAttribute('disabled');
                        thirdSelect.appendChild(nullOption);
                        let option_position = document.createElement('option')
                        option_position.value += json.response_position[i];
                        option_position.innerHTML += json.response_position[i];
                        thirdSelect.appendChild(option_position);
                    }
                }
            } else {
                nextSelect.appendChild(nullOption2);
                thirdSelect.appendChild(nullOption);
            }
        }
    }
    xhr.send();
    };

    selectCity.addEventListener('change', async event => {
    event.preventDefault();
    const selectedOption = event.target.value;
    doXHr(selectCity, selectedOption, selectAddress, null);
    });

    selectUnit.addEventListener('change', async event => {
    event.preventDefault();
    const selectedOption = event.target.value;
    doXHr(selectUnit, selectedOption, selectDepart, selectPosition);
    });

    selectDepart.addEventListener('change', async event => {
    event.preventDefault();
    const selectedOption = event.target.value;
    doXHr(selectDepart, selectedOption, selectPosition, null);
    });