const passwordInput = document.querySelector('#passwordInput');
const passwordGenerate = document.querySelector('#passwordGenerate');
const passwordToggle = document.querySelector('#passwordToggle');

const handleGenerate = (e) => {
    let passwordCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()';
    let passwordLength = 20;
    let passwordGenerated = '';
    for (let i = 0; i < passwordLength; i++) {
        let passwordRandChar = Math.floor(Math.random() * passwordCharacters.length);
        passwordGenerated += passwordCharacters.charAt(passwordRandChar);
    }
    passwordInput.value = passwordGenerated;
}

const handleToggle = (e) => {
    if (passwordToggle.textContent === 'SHOW') {
        passwordToggle.textContent = 'HIDE';
        passwordInput.setAttribute('type', 'text');
    } else {
        passwordToggle.textContent = 'SHOW';
        passwordInput.setAttribute('type', 'password');
    }
}

passwordGenerate.addEventListener('click', handleGenerate);
passwordToggle.addEventListener('click', handleToggle);