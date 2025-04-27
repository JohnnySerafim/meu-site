const menuHamburgue = document.querySelector('.menu-hamburgue')
    menuHamburgue.addEventListener('click',()=> {
    toggleMenu();
});

function toggleMenu() {
    const nav = document.querySelector('.nav-responsive');
    console.log(nav)
    menuHamburgue.classList.toggle('change');
    if (menuHamburgue.classList.contains('change')) {
        nav.style.display='block' ;
    }
    else{
        nav.style.display = 'none';
    }
}