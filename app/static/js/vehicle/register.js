// https://github.com/CodeSeven/toastr

$(document).ready(function(){

    $('#cpf-input').mask('000.000.000-00');
    $("#plate-input").mask('AAA-9999');
    
    $("#vehicle-user-form").submit(function(event) {
      event.preventDefault()
      event.stopPropagation()      

      var form = $(this);
      var actionUrl = form.attr('action');
      
      var typeFilled = !!$("#type-input").val().trim()
      var plateFilled = !!$("#plate-input").val().trim()
      var brandFilled = !!$("#brand-input").val().trim()
      var modelFilled = !!$("#model-input").val().trim()
      var cpfFilled = !!$("#cpf-input").val().trim()
      var yearFilled = !!$("#year-input").val().trim()
      var capacityFilled = !!$("#capacity-input").val().trim()

      if (!typeFilled || !plateFilled || !brandFilled || !modelFilled || !cpfFilled || !yearFilled || !capacityFilled) {          
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
            toastr.error('Ocorreu um erro ao tentar inserir um veiculo. Contate o administrador!')
        }
      });      
  });
});