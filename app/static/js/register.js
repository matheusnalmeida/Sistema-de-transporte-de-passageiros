// https://github.com/CodeSeven/toastr

$(document).ready(function(){

    $('#cpf-input').mask('000.000.000-00');
    $('birthdate-input').attr('onkeydown', 'return false')

    $("#register-user-form").submit(function(event) {
      event.preventDefault()
      event.stopPropagation()      

      var form = $(this);
      var actionUrl = form.attr('action');
      
      var nameFilled = !!$("#name-input").val().trim()
      var loginFilled = !!$("#login-input").val().trim()
      var passwordFilled = !!$("#password-input").val().trim()
      var birthdateFilled = !!$("#birthdate-input").val().trim()
      var cpfFilled = !!$("#cpf-input").val().trim()

      if (!nameFilled || !loginFilled || !passwordFilled || !birthdateFilled || !cpfFilled) {          
        toastr.error('Por favor preencha todos os dados para seguir com o cadastro!')
        return;
      }

      $.ajax({
          type: "POST",
          url: actionUrl,
          data: form.serialize(),
          success: function(data)
          {
            mensagem = data.message
            if(data.success)
            {
              sessionStorage.setItem('sucessRegister', mensagem)
              window.location.href = data.url
              return;
            }
            toastr.error(mensagem)
          },
          error: function (data) {
            toastr.error('Ocorreu um erro ao tentar registrar um usuário. Contate o administrador!')
        }
      });      
  });
});