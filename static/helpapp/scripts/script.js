//Dsplay mode for lable(forusername) and input(username) in dependence of selected option in subject selct field
function Selected(a) {
    var input = a.value;
    if (input=='1CD') {
        document.getElementById("labelUserWrapper").style.display = 'none';
        document.getElementById("usernameWrapper").style.display = 'none';
    } else if (input=='1CP') {
        document.getElementById("labelUserWrapper").style.display = 'none';
        document.getElementById("usernameWrapper").style.display = 'none';
    } else if (input=='oter') {
        document.getElementById("labelUserWrapper").style.display = 'none';
        document.getElementById("usernameWrapper").style.display = 'none';
        
    } else if (input=='newAccount') {
        document.getElementById("labelUserWrapper").style.display = 'flex';
        document.getElementById("usernameWrapper").style.display = 'flex';
        document.getElementById("forusername").innerHTML = 'Имя нового сотрудника';
    } else if (input=='delAccount') {
        document.getElementById("labelUserWrapper").style.display = 'flex';
        document.getElementById("usernameWrapper").style.display = 'flex';
        document.getElementById("forusername").innerHTML = 'Имя уволенного сотрудника';
    }
    else if (input=='changeAccount') {
        document.getElementById("labelUserWrapper").style.display = 'flex';
        document.getElementById("usernameWrapper").style.display = 'flex';
        document.getElementById("forusername").innerHTML = 'Имя сотрудника для изменения';
}
}

const fakeInput = document.querySelector('.inputWrapper');
const fakeInputField = document.querySelector('.email');

fakeInputField.addEventListener('focus', function () {
  fakeInput.classList.add('inputWrapper--focused');
})

fakeInputField.addEventListener('blur', function () {
  fakeInput.classList.remove('inputWrapper--focused');
})

