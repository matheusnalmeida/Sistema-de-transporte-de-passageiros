$(document).ready(function () {
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