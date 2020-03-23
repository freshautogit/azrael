    const selectCity = document.querySelector('select[name=city]');
    const selectAddress = document.querySelector('select[name=addr]');
    const selectUnit = document.querySelector('select[name=unit]');
    const selectDepart = document.querySelector('select[name=depart]');
    const selectPosition = document.querySelector('select[name=position]');

    const divCities = document.querySelector('div[class=cities');
    const divAddresses = document.querySelector('div[class=addresses]');
    const divDeparts = document.querySelector('div[class=departs');
    const divPositions = document.querySelector('div[class=positions');
    const divUnits = document.querySelector('div[class=units]');

    // делаешь асинхронный хэндлер к селекту
    selectCity.addEventListener('change', async event => {
        // не дает форме обновиться (блокируешь стандартное поведение)
        event.preventDefault();
        // получаешь выбранный текст
        const selectedOption = event.target.value;
        let xhr = new XMLHttpRequest();
        let url = 'dropdown_request/?city=' + encodeURIComponent(selectedOption);
        xhr.open('GET', url, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let json = JSON.parse(xhr.response);
                if (selectAddress != null) {
                    while (selectAddress.firstChild) {
                        selectAddress.removeChild(selectAddress.firstChild);
                    }
                }

                if (json.response != 'None') {
                    for (let i = 0; i < json.response.length; i++) {

                        selectAddress.classList.remove('hidden');

                        let option = document.createElement('option');
                        option.value += json.response[i];
                        option.innerHTML += json.response[i];
                        selectAddress.appendChild(option);
                    }
                    if (divAddresses != null) {
                        divAddresses.classList.remove('hidden');
                        let addAddressOption = document.createElement('option');
                        addAddressOption.innerHTML = 'Добавить новый адрес';
                        addAddressOption.value = 'addNewAddress';
                        addAddressOption.style = 'color: black; background-color: lightgreen;';
                        selectAddress.appendChild(addAddressOption);
                        addingNewAddress();
                    }
                } else {
                    selectAddress.classList.add('hidden');
                    let option = document.createElement('option');
                    option.value = 'None';
                    option.innerHTML = 'Пусто';
                    selectAddress.appendChild(option);
                }
            }
        };
        xhr.send();
    });

    // делаешь асинхронный хэндлер к селекту
    selectUnit.addEventListener('change', async event => {
        // не дает форме обновиться (блокируешь стандартное поведение)
        event.preventDefault();
        // получаешь выбранный текст
        const selectedOption = event.target.value;
        let xhr = new XMLHttpRequest();
        let url = 'dropdown_request/?unit=' + encodeURIComponent(selectedOption);
        xhr.open('GET', url, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let json = JSON.parse(xhr.response);
                if (selectDepart != null) {
                    while (selectDepart.firstChild) {
                        selectDepart.removeChild(selectDepart.firstChild);
                    }
                };
                if (selectPosition != null) {
                    while (selectPosition.firstChild) {
                        selectPosition.removeChild(selectPosition.firstChild);
                    }
                };

                if (json.response != 'None') {
                for (let i = 0; i < json.response.length; i++) {
                    selectDepart.classList.remove('hidden');
                    if (selectPosition != null) {
                        selectPosition.classList.remove('hidden');
                    }
                    let option = document.createElement('option');
                    option.value += json.response[i];
                    option.innerHTML += json.response[i];
                    selectDepart.appendChild(option);
                    if (selectPosition != null) {
                        let option_position = document.createElement('option')
                        option_position.value += json.response_position[i];
                        option_position.innerHTML += json.response_position[i];
                        selectPosition.appendChild(option_position);
                    }
                    }
                } else {
                    selectDepart.classList.add('hidden');
                    let option = document.createElement('option');
                    option.value = 'None';
                    option.innerHTML = 'Пусто';
                    selectDepart.appendChild(option);

                }
            }
        };
        xhr.send();
    });


    // делаешь асинхронный хэндлер к селекту

    if (selectPosition != null) {
        selectDepart.addEventListener('change', async event => {
            // не дает форме обновиться (блокируешь стандартное поведение)
            event.preventDefault();
            // получаешь выбранный текст
            const selectedOption = event.target.value;
            let xhr = new XMLHttpRequest();
            let url = 'dropdown_request/?position=' + encodeURIComponent(selectedOption);
            xhr.open('GET', url, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    let json = JSON.parse(xhr.response);
                    if (selectPosition != null) {
                        while (selectPosition.firstChild) {
                            selectPosition.removeChild(selectPosition.firstChild);
                        }
                    }
                    if (json.response != 'None') {
                        for (let i = 0; i < json.response.length; i++) {
                            selectPosition.classList.remove('hidden');
                            let option = document.createElement('option');
                            option.value += json.response[i];
                            option.innerHTML += json.response[i];
                            selectPosition.appendChild(option);

                        }

                    } else {
                        selectDepart.classList.add('hidden');
                        let option = document.createElement('option');
                        option.value = 'None';
                        option.innerHTML = 'Пусто';
                        selectPosition.appendChild(option);
                    }
                }
            };
            xhr.send();
        });
    }
    // Добавление нового города
    if (document.querySelector('select[id=addCity]').options[1].value=='addNewCity' && document.querySelector('select[id=addCity]') != null) {
        console.log('success');
        selectCity.addEventListener('change', event => {
            event.preventDefault();
            const currentOption = event.target.value;
            console.log(currentOption);

            if (currentOption == 'addNewCity') {

            if (document.querySelector('input[name=newCity]') != null) {
                divCities.removeChild(divCities.lastChild);

            }

                let input = document.createElement('input');
                input.name = 'newCity';
                input.classList.add('contactInfo');
                input.placeholder = 'Введи название города';
                input.type = 'text';
                divCities.appendChild(input);
                divAddresses.removeChild(divAddresses.lastChild);
            }
        });
    } else {
        console.log('fail');
    }

    // Добавление нового адреса
    let addingNewAddress = function () {
    if (selectAddress != null) {
        console.log('success');
        selectAddress.addEventListener('change', event => {
            event.preventDefault();
            const currentOption = event.target.value;
            console.log(currentOption);

            if (currentOption == 'addNewAddress') {
                if (document.querySelector('input[name=newAddress]') != null) {
                divAddresses.removeChild(divAddresses.lastChild);
            }

                let input = document.createElement('input');
                input.name = 'newAddress';
                input.classList.add('contactInfo');
                input.placeholder = 'Введи новый адрес';
                input.type = 'text';
                divAddresses.appendChild(input);
                selectAddress.removeChild(selectAddress.lastChild);
            }
        });
    } else {
        console.log('fail address');
    }
    }
