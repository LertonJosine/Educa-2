let nav_ancors = document.querySelectorAll('nav a');

nav_ancors.forEach(ancor => {
    if (ancor.innerText == 'Home'){
        ancor.classList.remove('active');
    }
    if (ancor.href == window.location.href) {
        ancor.classList.add('active');

    }
})