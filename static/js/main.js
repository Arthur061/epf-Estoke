/**
 * Script Principal para o Sistema ESTOKE
 *
 * Responsável por:
 * - Efeitos visuais da interface.
 * - Lógica do menu de navegação hambúrguer.
 * - Lógica do seletor de cores do formulário com persistência.
 *
 * Versão: 2.0
 * Data: 24/06/2025
 */

// PONTO DE ENTRADA PRINCIPAL: Executa tudo depois que a página carregou.
document.addEventListener('DOMContentLoaded', function() {
    console.log('Sistema ESTOKE: Scripts inicializados!');

    // --- INICIALIZADORES ---
    // Chama cada função principal para organizar o código.
    inicializarEfeitosVisuais();
    inicializarMenuHamburguer();
    inicializarSeletorDeCores();

});

/* efeitos visuais */
function inicializarEfeitosVisuais() {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease-in-out';
        document.body.style.opacity = '1';
    }, 100); 
}


/* menu hamburguer */
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



function inicializarSeletorDeCores() {
    const colorOptions = document.querySelectorAll('.color-option');
    const formContainer = document.querySelector('.form-container');

    if (colorOptions.length === 0) {
        return; // Sai se não houver seletor de cor na página.
    }

    // Função para aplicar a cor
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
        // Marca a bolinha da cor salva como ativa
        if (savedColor && option.style.backgroundColor === savedColor) {
            option.classList.add('active');
        }

        option.addEventListener('click', function() {
            const selectedColor = this.style.backgroundColor;

            aplicarCor(selectedColor);

            // salva cor
            localStorage.setItem('formBgColor', selectedColor);

            // att bolinha
            colorOptions.forEach(opt => opt.classList.remove('active'));
            this.classList.add('active');
        });
    });
}