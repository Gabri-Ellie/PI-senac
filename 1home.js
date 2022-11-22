const btnn = document.querySelector('.btnn');
    const containerr = document.querySelector('.containerr');
    btnn.onclick = function(){
        this.classList.toggle('active')
        containerr.classList.toggle('active')
    }