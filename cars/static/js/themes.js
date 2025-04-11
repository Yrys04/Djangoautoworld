document.addEventListener('DOMContentLoaded', function() {
    const themeSwitch = document.getElementById('themeSwitch');
    const html = document.documentElement;
    const navbar = document.querySelector('.navbar');
    const footer = document.querySelector('footer');

    // Проверяем сохраненную тему
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
    themeSwitch.checked = savedTheme === 'dark';

    // Обработчик переключения
    themeSwitch.addEventListener('change', function() {
        const theme = this.checked ? 'dark' : 'light';
        localStorage.setItem('theme', theme);
        setTheme(theme);
    });

    function setTheme(theme) {
        html.setAttribute('data-bs-theme', theme);
        
        // Обновляем навбар и футер
        if (theme === 'dark') {
            navbar.classList.remove('bg-primary');
            navbar.classList.add('bg-dark');
            footer.classList.remove('bg-primary');
            footer.classList.add('bg-dark');
        } else {
            navbar.classList.remove('bg-dark');
            navbar.classList.add('bg-primary');
            footer.classList.remove('bg-dark');
            footer.classList.add('bg-primary');
        }
        
        // Обновляем кнопки
        document.querySelectorAll('.btn-outline-light').forEach(btn => {
            btn.classList.toggle('btn-outline-dark', theme === 'dark');
        });
    }
});