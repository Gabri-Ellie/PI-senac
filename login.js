function confereSenha() {
    const senha = document.getElementById('senha');
    const confirma = document.getElementById('confirma');

    if (confirma.value === senha.value){
        confirma.setCustomValidity('')
    }
    else{
        confirma.setCustomValidity('senhas não valem')
    }

    function senhaOK(){
        alert('deu certo')
    }
    }