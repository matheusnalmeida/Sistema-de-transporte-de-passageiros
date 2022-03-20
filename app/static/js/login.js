$(document).ready(function(){
    $("#login-form").submit(function(event) {
      event.preventDefault()
      event.stopPropagation()      
      
      var form = $(this);
      
      var actionUrl = form.attr('action');
      
      var userFilled = !!$("#user-input").val().trim()
      var passwordFilled = !!$("#password-input").val().trim()
      if (!userFilled || !passwordFilled) {          
        toastr.error('Por favor preencha todos os dados para seguir com o login!')
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
              window.location.href = data.url
              return;
            }
            toastr.error(mensagem)
          },
          error: function (data) {
            toastr.error('Ocorreu um erro ao tentar logar. Contate o administrador!')
        }
      });      
  });
});