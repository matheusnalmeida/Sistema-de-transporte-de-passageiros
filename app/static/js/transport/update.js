// https://github.com/CodeSeven/toastr

$(document).ready(function(){

    $('#cpf-input').mask('000.000.000-00');
    $("#plate-input").mask('AAA-9999');
    $('transport-date-input').attr('onkeydown', 'return false')

    $("#transport-user-form").submit(function(event) {
      event.preventDefault()
      event.stopPropagation()      
  
      var form = $(this);
      var actionUrl = form.attr('action');
      
      var plateFilled = !!$("#plate-input").val().trim()
      var cpfFilled = !!$("#cpf-input").val().trim()
      var transportDateFilled = !!$("#transport-date-input").val().trim()
      var transportHourFilled = !!$("#transport-hour-input").val().trim()
      var kmQuantitylFilled = !!$("#km-quantitty-input").val().trim()
      var amountChargedFilled = !!$("#amount-charged-input").val().trim()

      if (!plateFilled || !cpfFilled || !transportDateFilled || !transportHourFilled || !kmQuantitylFilled || !amountChargedFilled) {          
        toastr.error('Por favor preencha todos os dados para seguir com a inserção!')
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
            toastr.error('Ocorreu um erro ao tentar atualizar o registro de transporte. Contate o administrador!')
        }
      });      
  });
  });