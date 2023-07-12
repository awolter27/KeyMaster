const passwordInput = document.querySelector('#passwordInput');
const passwordToggle = document.querySelector('.passwordToggle');

const handleToggleInput = (e) => {
    if (passwordToggle.textContent === 'SHOW') {
        passwordToggle.textContent='HIDE';
        passwordInput.setAttribute('type', 'text');
    } else {
        passwordToggle.textContent='SHOW';
        passwordInput.setAttribute('type', 'password');
    }
}

passwordToggle.addEventListener('click', handleToggleInput);

