/**
 * Script Principal para o Sistema ESTOKE
 *
 * Responsável por:
 * - Efeitos visuais da interface.
 * - Lógica do menu de navegação hambúrguer.
 * - Lógica do seletor de cores do formulário com persistência.
 * - Validação de formulários específicos (ex: confirmação de senha).
 *
 * Versão: 2.1
 * Data: 30/06/2025
 */

// PONTO DE ENTRADA PRINCIPAL: Executa tudo depois que a página carregou.
document.addEventListener('DOMContentLoaded', function() {
    console.log('Sistema ESTOKE: Scripts inicializados!');

    // --- INICIALIZADORES ---
    // Chama cada função principal para organizar o código.
    inicializarEfeitosVisuais();
    inicializarMenuHamburguer();
    inicializarSeletorDeCores();
    inicializarValidacaoDeSenha(); // <-- ADICIONADO AQUI

});

/* Efeitos visuais de fade-in */
function inicializarEfeitosVisuais() {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease-in-out';
        document.body.style.opacity = '1';
    }, 100); 
}

/* Lógica do menu hambúrguer */
function inicializarMenuHamburguer() {
    const navToggleBtn = document.getElementById('navToggleBtn');
    const navDropdown = document.getElementById('navDropdown');

    if (!navToggleBtn || !navDropdown) {
        return;
    }

    navToggleBtn.addEventListener('click', function(event) {
        event.stopPropagation();
        navDropdown.classList.toggle('show');
    });

    window.addEventListener('click', function() {
        if (navDropdown.classList.contains('show')) {
            navDropdown.classList.remove('show');
        }
    });
}

/* Lógica do seletor de cores */
function inicializarSeletorDeCores() {
    const colorOptions = document.querySelectorAll('.color-option');
    const formContainer = document.querySelector('.form-container');

    if (colorOptions.length === 0) {
        return; // Sai se não houver seletor de cor na página.
    }

    const aplicarCor = (color) => {
        if (formContainer) {
            formContainer.style.backgroundColor = color;
        }
        document.documentElement.style.setProperty('--form-bg-color', color);
    };
    
    const savedColor = localStorage.getItem('formBgColor');
    if (savedColor) {
        aplicarCor(savedColor);
    }

    colorOptions.forEach(option => {
        if (savedColor && option.style.backgroundColor === savedColor) {
            option.classList.add('active');
        }

        option.addEventListener('click', function() {
            const selectedColor = this.style.backgroundColor;
            aplicarCor(selectedColor);
            localStorage.setItem('formBgColor', selectedColor);
            colorOptions.forEach(opt => opt.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

/**
 * Valida o formulário de usuário, checando se as senhas coincidem.
 */
function inicializarValidacaoDeSenha() {
    const userForm = document.getElementById('userForm');
    
    // Se o formulário não existir nesta página, a função não faz nada.
    if (!userForm) {
        return;
    }

    userForm.addEventListener('submit', function(e) {
        const passwordInput = document.getElementById('password');
        
        // Só executa a validação se o campo de senha existir no formulário.
        if (passwordInput) {
            const password = passwordInput.value;
            const confirmPassword = document.getElementById('confirm_password').value;
            
            if (password !== confirmPassword) {
                alert('As senhas não coincidem!');
                e.preventDefault(); // Impede o envio do formulário.
            }
        }
    });
}