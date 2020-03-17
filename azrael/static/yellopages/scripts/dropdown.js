    const select1 = document.querySelector('select[name=city]');
    const select2 = document.querySelector('select[name=addr]');
    const select3 = document.querySelector('select[name=office]');
    const select4 = document.querySelector('select[name=position]');

    // делаешь асинхронный хэндлер к селекту
    select1.addEventListener('change', async event => {
        // не дает форме обновиться (блокируешь стандартное поведение)
        event.preventDefault();
        // получаешь выбранный текст
        const selectedOption = event.target.value;
        console.log('Выбранный в селекте текст: ' + selectedOption);



        let xhr = new XMLHttpRequest();
        let url = "test/?city=" + encodeURIComponent(selectedOption);
        xhr.open("GET", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let json = JSON.parse(xhr.response);
                console.log(json);
                if (select2 != null) {
                    while (select2.firstChild) {
                        select2.removeChild(select2.firstChild);
                    }
                }

                if (json.response != "None") {
                    for (let i = 0; i < json.response.length; i++) {
                        console.log(json.response[i]);
                        select2.classList.remove("hidden");
                        let option = document.createElement('option');
                        option.value += json.response[i];
                        option.innerHTML += json.response[i];
                        select2.appendChild(option);
                    }
                } else {
                    select2.classList.add("hidden");
                    let option = document.createElement('option');
                    option.value = "None";
                    option.innerHTML = "Пусто";
                    select2.appendChild(option);
                }
            }
        };
        xhr.send();
    });

    // делаешь асинхронный хэндлер к селекту
    select3.addEventListener('change', async event => {
        // не дает форме обновиться (блокируешь стандартное поведение)
        event.preventDefault();
        // получаешь выбранный текст
        const selectedOption = event.target.value;
        console.log('Выбранный в селекте текст: ' + selectedOption);



        let xhr = new XMLHttpRequest();
        let url = "test/?unit=" + encodeURIComponent(selectedOption);
        xhr.open("GET", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let json = JSON.parse(xhr.response);
                console.log(json);
                if (select4 != null) {
                    while (select4.firstChild) {
                        select4.removeChild(select4.firstChild);
                    }
                }
                if (json.response != "None") {
                for (let i = 0; i < json.response.length; i++) {
                    console.log(json.response[i]);
                    select4.classList.remove("hidden");
                    let option = document.createElement('option');
                    console.log('1.  ' + json.response)
                    option.value += json.response[i];
                    option.innerHTML += json.response[i];
                    select4.appendChild(option);
                    }
                } else {
                    select4.classList.add("hidden");
                    let option = document.createElement('option');
                    option.value = "None";
                    option.innerHTML = "Пусто";
                    select4.appendChild(option);
                }
            }
        };
        xhr.send();
    });
