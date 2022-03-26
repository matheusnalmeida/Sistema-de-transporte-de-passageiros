$(document).ready(function(){
    $("td[class*='cpf']").each(function(index, el){
        let cpf = $(el).text()
        $(el).text(cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4"))
    })

    $("td[class*='birth_date']").each(function(index, el){
        let date = new Date($(el).text()).toLocaleDateString()
        $(el).text(date)
    })

    $("#delete-motorista").click(function(event) {
        event.preventDefault();
        let actionUrl = $("#delete-motorista").attr('href')
        $.ajax({
            type: "GET",
            url: actionUrl,
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
              toastr.error('Ocorreu um erro ao tentar deletar o motorista. Contate o administrador!')
          }
        });  
    });
});