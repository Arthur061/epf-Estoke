from bottle import request, redirect, template
from services.user_service import UserService

class PerfilController:
    def __init__(self, bottle_app):
        self.user_service = UserService()

        bottle_app.route('/perfil', method='GET', callback=self.pagina_perfil)
        bottle_app.route('/perfil', method='POST', callback=self.processa_perfil)
        
    def pagina_perfil(self):
        """
        Exibe a página de perfil com os dados do usuário.
        """
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')

        if not user_id:
            return redirect('/login')

        user = self.user_service.get_by_id(user_id)
        if not user:
            return redirect('/login')

        user_name = user.name.strip().split()[0]
        is_admin_user = (user.tipo == 'administrador')

        success_message = session.pop('message', None)

        return template('perfil_template',
                        user=user,
                        user_name=user_name,
                        is_admin=is_admin_user,
                        message=success_message,
                        session=session)

    def processa_perfil(self):
        """
        Processa o formulário de atualização de perfil.
        """
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')

        if not user_id:
            return redirect('/login')

        name = request.forms.get('name')
        email = request.forms.get('email')
        password = request.forms.get('password')
        birthdate = request.forms.get('birthdate')

        update_data = {'name': name, 'email': email, 'birthdate': birthdate}

        if password:
            update_data['password'] = password

        self.user_service.update_profile(user_id, update_data)

        session['message'] = 'Perfil atualizado com sucesso!'
        session.save()
        return redirect('/perfil')