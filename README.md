# ESTOKE: Controle de Estoque Inteligente

ESTOKE é um projeto web educacional que demonstra a construção de uma aplicação de controle de inventário utilizando Programação Orientada a Objetos (POO) com Python e o microframework Bottle. O projeto foi pensado para ser uma base de estudos clara, didática e extensível, ideal para disciplinas de Engenharia de Software e afins.

## 💡 Objetivo

Fornecer uma base simples, extensível e didática para construção de aplicações web orientadas a objetos com aplicações WEB em Python, ideal para trabalhos finais ou exercícios práticos.

---

## 🗂 Estrutura de Pastas

```bash
poo-python-bottle-template/
├── app.py # Ponto de entrada do sistema / Inicialização da aplicação
├── config.py # Configurações e caminhos do projeto
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
├── controllers/ # Controladores e rotas
├── models/ # Definição das entidades 
├── services/ # Lógica de persistência 
├── views/ # Arquivos HTML (Bottle Templating)
├── static/ # CSS, JS e imagens
├── data/ # Arquivos JSON de dados
└── .vscode/ # Configurações opcionais do VS Code
```

---

## ✨ Funcionalidades Principais
Autenticação de Usuários: Sistema completo de registro e login com armazenamento seguro de senhas (hash).

Gestão de Produtos (CRUD): Cadastro, visualização, edição e remoção de produtos.

Gestão de Fornecedores (CRUD): Gerenciamento completo de fornecedores associados aos produtos.

Controle de Estoque: Registro de movimentações de entrada e saída, com atualização em tempo real do estoque.

Relatório de Reposição Inteligente: O sistema identifica e lista proativamente os produtos que atingiram o estoque mínimo, sugerindo a reposição.

Painel de Administrador: Área segura para gerenciamento de todos os usuários e administradores do sistema.

Interface Responsiva e Personalizável: Design moderno com um seletor de cores para personalizar a aparência dos formulários.

## 🛠️ Tecnologias Utilizadas

Backend: Python 3.9+

Bottle: Microframework web leve e rápido.

SQLite: Banco de dados relacional embarcado.

bcrypt: Para hashing seguro de senhas.

Frontend:

HTML5

CSS3 (com Flexbox e Variáveis CSS)

JavaScript (vanilla) para interatividade e validações no cliente.

## 📁 Descrição das Pastas

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação. Exemplos:
- `admin_controller.py`: rotas exclusivas para administradores, permitindo gerenciar usuários e outras contas de administrador, sempre com verificação de permissão.
- `auth_controller.py`: Gerencia todo o processo de autenticação. É responsável pelas rotas de login, registro de novos usuários e logout. Ele valida as credenciais, gerencia a sessão do usuário (criando-a no login e destruindo-a no logout) e controla o acesso a páginas restritas.
- `base_controller.py`: classe base com utilitários comuns.
- `fornecedor_controller.py`: Controla as operações de CRUD (Criar, Ler, Atualizar, Excluir) para os fornecedores. Garante que um usuário só possa gerenciar os fornecedores que ele mesmo cadastrou, validando a permissão em todas as rotas.
- `movimentacao_controller.py`: Orquestra o registro de entradas e saídas de produtos do estoque. Ele exibe o histórico de movimentações e, ao registrar uma nova, atualiza a quantidade do produto correspondente.
- `perfil_controller.py`: Permite que o usuário autenticado visualize e atualize suas próprias informações de perfil, como nome, e-mail e senha.
- `prdotuo_controller.py`: Gerencia o ciclo de vida completo dos produtos (CRUD). Permite listar, detalhar, adicionar, editar e excluir produtos, além de gerar um relatório para reposição de estoque.
- `redirect_controller`: Atua como um redirecionador de rotas, garantindo que os usuários que acessam URLs específicas sejam enviados para a página correta, dependendo do seu status de login.
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.

### `models/`
Define as classes que representam os dados da aplicação. Exemplo:
- `adm.py`: Define a classe Administrador (um tipo especial de User com permissões) e a classe AdministradorRepository, responsável por todas as operações de banco de dados (CRUD) relacionadas especificamente aos administradores.
- `fornecedor.py`: Define a classe Fornecedor e a classe FornecedorRepository, que lida com a lógica de banco de dados para adicionar, editar, buscar e remover fornecedores, sempre vinculando os registros a um usuário específico.
- `movimentacao.py`: Define a classe Movimentacao e a classe MovimentacaoRepository, responsáveis por registrar e consultar o histórico de entradas e saídas de produtos do estoque.
- `produto.py`:  Define a classe Produto e a classe ProdutoRepository, que gerencia o ciclo de vida completo (CRUD) dos produtos no banco de dados, incluindo uma consulta para identificar itens que precisam de reposição.
- `user.py`: Arquivo fundamental que define a classe User (o modelo base para qualquer usuário) e a classe UserRepository, que gerencia as operações de CRUD na tabela de usuários e a lógica de segurança de senhas.

### `services/`
Esta pasta contém as classes de serviço, que servem como uma camada intermediária entre os controllers e os models. Elas orquestram as operações e contêm a lógica de negócio da aplicação.
- `adm_service.py`: Contém a lógica de negócio para gerenciar administradores. Este serviço coordena as ações do AdminController com o AdministradorRepository, lidando com a criação, atualização, busca e remoção de administradores, incluindo a criptografia de senhas.
- `fornecedor_service.py`: Centraliza a lógica de negócio e as operações de banco de dados para os fornecedores. É responsável pelo CRUD dos fornecedores, garantindo que cada usuário só possa gerenciar seus próprios dados.
- `movimentacao_service.py`:  Orquestra a lógica de negócio para o controle de estoque. Ele fornece métodos para registrar entradas e saídas, criando os registros de movimentação e interagindo com a camada de dados.
- `produto_service.py`: Centraliza a lógica de negócio para os produtos. Atua como ponte entre o controlador e o repositório, validando dados e orquestrando as operações de CRUD e a consulta de produtos para reposição.
- `user_service.py`: Serviço essencial que lida com a lógica de negócio de usuários, incluindo autenticação, registro de novas contas com criptografia de senha e as operações básicas de CRUD.

### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
- `admin_administrator_form.tpl`: Template que gera um formulário dinâmico para criar ou editar administradores. Ele altera seu título e campos (como os de senha) com base na operação (adição ou edição) e usa JavaScript para validar a confirmação de senha no lado do cliente.
- `admin_administrator.tpl`: Template que exibe a página principal de gerenciamento de administradores. Ele renderiza uma tabela com a lista de todos os administradores e fornece botões de "Editar" e "Excluir" para cada um, além de um link para adicionar novos.
- `admin_user_form.tpl`: Template do formulário que o administrador usa para criar ou editar usuários. Sua principal característica é a capacidade de gerenciar o papel do usuário (Comum ou Administrador) através de um campo de seleção.
- `admin_users.tpl`: Apresenta a lista de todos os usuários do sistema para o administrador. Fornece opções de "Editar" e "Excluir" para cada usuário, com uma confirmação em JavaScript para evitar exclusões acidentais.
- `fornecedor-form.tpl`: Gera o formulário para adicionar um novo fornecedor ou editar um existente. Ele se adapta dinamicamente, alterando o título e preenchendo os dados conforme a operação.
- `fornecedores.tpl`: Gera a página principal de gerenciamento de fornecedores, exibindo uma lista de todos os fornecedores do usuário. Inclui botões de "Editar" e "Excluir" em cada linha, com uma confirmação via JavaScript para exclusões seguras.
- `home_template.tpl`: Gera a página de boas-vindas da aplicação. Seu foco é apresentar o projeto, explicando a arquitetura baseada em Orientação a Objetos e o fluxo de uso do sistema.
- `layout_login_page.tpl`: Um template autônomo que gera a página de login. Ele contém o formulário de login, um local para exibir mensagens de erro e um link para a página de registro.
- `layout.tpl`: O template mestre da aplicação. Ele define a estrutura HTML principal (cabeçalho, rodapé, menus) e usa {{!base}} como um marcador de posição onde o conteúdo de outras páginas é inserido. É responsável por manter a consistência visual e carregar os arquivos CSS e JS globais.
- `login.tpl`: Gera o formulário de login, que se integra ao layout principal. Apresenta os campos para autenticação, um local para exibir erros e o widget de personalização de cores.
- `movimentacoes.tpl`: Apresenta uma interface completa para controle de estoque, combinando um formulário para registrar novas entradas/saídas com uma tabela que exibe o histórico de todas as movimentações.
- `perfil_template.tpl`: Gera a página onde o usuário edita suas próprias informações de perfil. O formulário vem preenchido com os dados atuais e permite a alteração opcional da senha.
- `produto_detalhes.tpl`: Exibe uma página de detalhes para um único produto, mostrando todas as suas informações em um formato de lista. Contém botões de navegação para voltar ou editar o item.
- `produto_form.tpl`: Gera o formulário para adicionar um novo produto ou editar um existente. É um template reutilizável cujo título, URL de envio e valores dos campos são definidos dinamicamente pelo controlador.
- `produto_reposicao.tpl`: Gera uma página de relatório somente leitura que lista todos os produtos que precisam de reposição de estoque, comparando o estoque atual com o mínimo definido.
- `produtos.tpl`: Gera a página principal de gerenciamento de produtos do usuário. Exibe uma tabela com os produtos e fornece ações de "Editar" e "Excluir" para cada um, além de um link no nome do produto para uma página de detalhes.
- `register.tpl`: Gera a página de registro de novos usuários, com um formulário que inclui validação de senha e um botão para alternar a visibilidade da senha, melhorando a usabilidade.
- `user_form.tpl`: Um formulário genérico e reutilizável para criar ou editar um usuário, incluindo validação de senha via JavaScript.
- `users.tpl`: Gera uma página de gestão de usuários que exibe uma lista de todos os usuários em uma tabela, com botões de "Editar" e "Excluir" (com confirmação) para cada um.

### `static/`
Arquivos estáticos como:
- `css/style.css`: É a folha de estilo principal da aplicação. Suas principais características são:

Tema Visual: Utiliza um fundo escuro com uma imagem de estoque e um efeito de desfoque. Os principais contêineres e formulários têm um fundo semitransparente e desfocado, criando uma aparência de "vidro". A paleta de cores é definida com variáveis CSS para fácil manutenção, com o azul como cor primária e um tom de amarelo/dourado como cor de destaque.

Layout: O layout é construído com Flexbox para garantir que a página ocupe toda a altura da tela e se adapte a diferentes tamanhos. A estrutura é dividida em um cabeçalho, conteúdo principal e rodapé.

Componentes Principais:

Cabeçalho e Navegação: O cabeçalho é fixo e semitransparente, contendo um menu "hambúrguer" para a navegação principal, o logo centralizado e um menu dropdown para o perfil do usuário.

Formulários: Possuem um design consistente, com campos de entrada escuros e botões com gradientes e efeitos de transição.

Tabelas: Estilizadas para exibir dados de forma clara em um tema escuro, com destaque para o cabeçalho e efeitos de hover nas linhas.

Interatividade: A folha de estilo inclui diversas transições e efeitos de :hover e :focus para botões, links e campos de formulário, proporcionando um feedback visual dinâmico ao usuário.


- `js/main.js`: O principal arquivo JavaScript da aplicação, responsável por toda a interatividade da interface. Ele gerencia os menus de navegação, a validação de formulários (como a confirmação de senha) e a funcionalidade do seletor de cores, que persiste a escolha do usuário entre as sessões.
- `img/estoque.png`: Imagem de fundo.

### `data/`
Contém os scripts e arquivos relacionados à manipulação e inicialização dos dados da aplicação.
- `init_db.py`: Script fundamental para a inicialização do banco de dados. Ele é responsável por criar o arquivo do banco de dados SQLite e definir o esquema de todas as tabelas necessárias (users, fornecedores, produtos, movimentacoes), garantindo que a estrutura de dados esteja pronta para uso.

---

## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python main.py
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)

---

## ✍️ Personalização
Para adicionar novos modelos (ex: Atividades):

1. Crie a classe no diretório **models/**.

2. Crie o service correspondente para manipulação do JSON.

3. Crie o controller com as rotas.

4. Crie as views .tpl associadas.

---

## 🧠 Autor e Licença
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
Você pode reutilizar, modificar e compartilhar livremente.
