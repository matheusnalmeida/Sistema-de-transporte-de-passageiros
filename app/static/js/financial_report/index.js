$(document).ready(function () {
  $("td[class*='cpf']").each(function(index, el){
    let cpf = $(el).text()
    $(el).text(cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4"))
  })
  
  $("td[class*='transport-date']").each(function(index, el){
    let date = new Date($(el).text()).toLocaleDateString()
    $(el).text(date)
  })

  $('#button-filter').click(function (event) {
    event.preventDefault();
    let actionUrl = $(this).attr('href')

    let beginDate = $('#transport-begindate-input').val()
    let endDate = $('#transport-enddate-input').val()

    $.ajax({
      type: "GET",
      url: actionUrl,
      data: {
        'transport-begin-date': beginDate,
        'transport-end-date': endDate
      },
      success: function (data) {
        mensagem = data.message
        if (data.success) {
          $("#report-content").html(data.data)
          return;
        }
        toastr.error(mensagem)
      },
      error: function (data) {
        toastr.error('Ocorreu um erro ao tentar carregar o relatório. Contate o administrador!')
      }
    });
  });
})